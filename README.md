# Object_Python_Wit.ai
Connexion avec wit.ai avec un objet en python
Une class ClassDomotic permet de créer un objet par Intents du site de wit.ai.

Pour initialiser l'objet on lui passe URL de l'arduino Ethernet, le texte de la voix pour le ON et pour le OFF, l'objet de connexion SQL et le nom du contact à allumer et éteindre.

Les objets sont créés au démarrage du programme avec les données d'un fichier config.xml.

Quand une commande est reçue de wit.ai on passe la commande à l'objet concerné avec ON ou OFF. ex domotic[intents].commande('on').

Il faut coupler cela avec un arduino, une carte internet et un émetteur en 433 Mhz. Une base de données permet de connaitre la position du contact On ou OFF pour une utilisation sur plusieurs système soit par la voix ou une page web. Je vous met le code de l'arduino sur github.




