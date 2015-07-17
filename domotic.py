#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import wit
import json
import signal
import sys
import os
import xml.dom.minidom

from ClassDomotic import *

access_token = 'K3RY7CDERSUFT5KJTYJH6IVKKDBSI2WH' # Code Wit

#Fonction appelée quand vient l'heure de fermer notre programme
def fermer_programme(signal, frame):
    parole("Fermeture du programme. Au revoir a bientot")
    wit.close()
    db.close()
    sys.exit(0)

# Connexion du signal à notre fonction
signal.signal(signal.SIGINT, fermer_programme)

tree = xml.dom.minidom.parse("configSQL.xml")
valeurListe = tree.getElementsByTagName("SQL")
for valeur in valeurListe:
    print valeur.attributes['ip'].value
    print valeur.attributes['dbase'].value
    print valeur.attributes['login'].value
    print valeur.attributes['mdp'].value
    print ("-------------------------------")
    #connexion  à la base de données
    db = MySQLdb.connect(valeur.attributes['ip'].value, valeur.attributes['login'].value, valeur.attributes['mdp'].value, valeur.attributes['dbase'].value)
    dbSQL = db.cursor()

Domotic = {} #construction des objets.
tree = xml.dom.minidom.parse("config.xml")
valeurListe = tree.getElementsByTagName("WIT")
for valeur in valeurListe:
    print valeur.attributes['name'].value
    print valeur.attributes['ipurl'].value
    print valeur.attributes['nomled'].value
    print valeur.attributes['textvoixON'].value
    print valeur.attributes['textvoixOFF'].value
    print ("-------------------------------")
    Domotic[valeur.attributes['name'].value]= ClassDomotic(valeur.attributes['textvoixON'].value, valeur.attributes['textvoixOFF'].value, valeur.attributes['ipurl'].value, valeur.attributes['nomled'].value, db, dbSQL)

	
# Fonction lecture orale d'un texte
def parole(texte):
    cmd = 'espeak -v mb-fr1 \"%s\" -s 120'
    os.system(cmd % texte)

# Fonction Mise en route de l'écoute
def ecoute(passage): # Valeurs passage: 1 Mise en route, 2 Ecoute OK en attente, 3 Commande pas comprise, 4 pas de message 
    response = None
    if passage == 1:
	parole("Je suis a ton écoute")
    if passage == 2:
	parole("Je suis a l'écoute pour une autre commande")
    if passage == 3:
	parole("Merci de répéter la commande, je n'ai pas compris")
    
    while response == None:	
    	response = wit.voice_query_auto(access_token)

    texte_json(response)

#Fonction analyse retour écoute micro en JSON
def texte_json(response):
    js= json.loads(response)
    print(js['_text'])
    if js['_text'] == None:
        ecoute(4)
    else:
        analyse_texte(js)

#Fonction Analyse valeur texte
def analyse_texte(js):
    try:
	intent = js[u'outcomes'][0][u'intent']
    except NameError:
	ecoute(3)
		
    if intent == 'Jasper':
	parole('Je suis a ton service')
	ecoute(4)
    else:
	try:
		val_On_Off = js[u'outcomes'][0][u'entities'][u'on_off'][0][u'value']
	except NameError:
		ecoute(3)

	try:			
		Domotic[intent].commande(val_On_Off)
	except NameError:
		ecoute(3)
    ecoute(2)

parole("Je me prépare")	
wit.init() #Lancement de wit
# Mise en route et lancement de l'écoute	
ecoute(1)

