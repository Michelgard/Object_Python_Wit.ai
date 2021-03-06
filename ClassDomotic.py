#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib

class ClassDomotic:
	"""Cette class va créer des commandes vocales, envoyer une commande sur une URL et
		modifier la valeur de la base de données suivant les ordres de Wit.Ai.
	
Les arguments:
textON = le texte de la voix au passage de la commande ON.
textOFF = le texte de la voix au passage de la commande OFF.
IPVal =  la valeur de l'IP pour l'URL
Led = sur quel lampe va la commande.
dbSQL = connexion base SQL

ComVal = la valeur de la commande ON ou OFF.

"""

	def __init__(self, textON, textOFF, IPVal, Led):
		"""Constructeur de la classe. Chaque attribut va être instancié
			avec une valeur"""
		self._textON = textON
		self._textOFF = textOFF
		self._IPVal = IPVal
		self._Led = Led
		
	def _parole(self, textClass):
		""" Fonction qui donne la voix suivant le texte passé.
			Le texte peut être dépendant de l'objet créé par l'argument text de INIT
			ou un texte d'erreur contenu dans la class"""

		cmd = '/home/pi/Object_Python_Wit.ai/speech.sh \"%s\"'
		os.system(cmd % textClass)
		
	def _sendURL(self, IPVal, Led, ComVal): 
		"""envoie la commande On ou OFF sur la bonne led """
		url = "http://" + IPVal + '/?' +  Led + '=' + ComVal
		try:
			resultat = urllib.urlopen(url)
		except:
			return False
		return True	

	def _sendSQL(self, db, dbSQL, Led, ComVal):
		""" Modification de la valeur dans la base de donnée suite à la commande"""
		sql = "UPDATE Position_prise SET  Valeur_Prise ='" + ComVal + "' WHERE  N_Prise = '" + Led + "'"
		try:
			dbSQL.execute(sql)
			db.commit()			
		except:
			return False		
		return True
	
	def _lectureSQL(self, dbSQL,  Led):
		"""Lecture de la valeur de la base sql pour vérifier la concordance de la commande """
		sql = "select Valeur_Prise from Position_prise where N_Prise ='" + Led + "'"
		print(sql)	
		try:
			dbSQL.execute(sql)
			results = dbSQL.fetchall()
			for row in results:
  				fname = row[0]
				print(fname)
		except OperationalError as e:
			reconnect()
			return False
		return fname
	
	def commande(self, ComVal, db, dbSQL):
		""" Fonction de la class qui fait la commande ou pas si il n'est pas pertinant"""
		ComVal = ComVal.upper()
		if (ComVal == "ON" or ComVal == "OFF"):
			valeurSQL = self._lectureSQL(dbSQL, self._Led)
			if (valeurSQL == False):
				self._parole("Il y a une erreur de chemin sur la base de donner")
			else:
				if (valeurSQL == ComVal):
					self._parole("Attention la commande a deja etais valider")
				else:
					requestURL = self._sendURL(self._IPVal, self._Led, ComVal)
					if (requestURL):
						requestSQL = self._sendSQL(db, dbSQL, self._Led, ComVal)
						if (requestSQL):
							if (ComVal == 'ON'):
								self._parole(self._textON)
							else:
								self._parole(self._textOFF)
						else:
							self._parole("Une erreur s'est produite, merci de redire la commande")
					else:
						self._parole("Une erreur s'est produite. Merci de refaire la commande")
		else :
			self._parole("La commande n'est pas valide")
