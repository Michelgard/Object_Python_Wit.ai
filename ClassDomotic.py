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

	def __init__(self, textON, textOFF, IPVal, Led, dbSQL):
		"""Constructeur de la classe. Chaque attribut va être instancié
			avec une valeur"""
		self._textON = textON
		self._textOFF = textOFF
		self._IPVal = IPVal
		self._Led = Led
		self._dbSQL = dbSQL
		
	def _parole(self, textClass):
		""" Fonction qui donne la voix suivant le texte passé.
			Le texte peut être dépendant de l'objet créé par l'argument text de INIT
			ou un texte d'erreur contenu dans la class"""
		cmd = "espeak -x -v mb/mb-fr1 \"%s\" | mbrola -e -C \"n n2\" /opt/mbrola/fr1/fr1 - -.au | paplay"
		os.system(cmd % textClass)
		print (textClass)
		
	def _sendURL(self, IPVal, Led, ComVal): 
		"""envoie la commande On ou OFF sur la bonne led """
		url = IPVal + '/?' + 'LED' + Led + '=' + ComVal
		return True #urllib.urlopen(url)
		
	def _sendSQL(self, ipSQL, Led, ComVal):
		""" Modification de la valeur dans la base de donnée suite à la commande"""
		
		return True #reponseSQL
	
	def _lectureSQL(self, ipSQL,  Led):
		"""Lecture de la valeur de la base sql pour vérifier la concordance de la commande """

		return "ON"
	
	def commande(self, ComVal):
		""" Fonction de la class qui fait la commande ou pas si il n'est pas pertinant"""
		ComVal = ComVal.upper()
		print (ComVal)
		if (ComVal == "ON" or ComVal == "OFF"):
			valeurSQL = self._lectureSQL(self._dbSQL, self._Led)
			if (valeurSQL == ComVal):
				self._parole("Attention la commande a déjà été validé !")
			else:
				requestURL = self._sendURL(self._IPVal, self._Led, ComVal)
				if (requestURL):
					requestSQL = self._sendSQL(self._dbSQL, self._Led, ComVal)
					if (requestSQL):
						if (ComVal == 'ON'):
							self._parole(self._textON)
						else:
							self._parole(self._textOFF)
					else:
						self._parole("Une erreur s'est produite, merci de redire la commande")
		else :
			self._parole("La commande n'est pas valide !")
