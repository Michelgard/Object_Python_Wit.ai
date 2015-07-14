#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.dom.minidom 
from ClassDomotic import *

import MySQLdb


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


objet = {}

tree = xml.dom.minidom.parse("config.xml")
valeurListe = tree.getElementsByTagName("WIT")

for valeur in valeurListe:
    print valeur.attributes['name'].value
    print valeur.attributes['ipurl'].value
    print valeur.attributes['nomled'].value
    print valeur.attributes['textevoix'].value
    print ("-------------------------------")
    
    objet[valeur.attributes['name'].value]= ClassDomotic(valeur.attributes['textevoix'].value, valeur.attributes['ipurl'].value, valeur.attributes['nomled'].value, dbSQL)

"""objet["lampe_chambre"].commande('om')
objet["lustre_chambre"].commande('on')"""

