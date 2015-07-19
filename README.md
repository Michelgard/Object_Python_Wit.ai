# Object_Python_Wit.ai
Connexion avec wit.ai avec un objet en python
Une class ClassDomotic permet de créer un objet par Intents du site de wit.ai.

Pour initialiser l'objet on lui passe URL de l'arduino Ethernet, le texte de la voix pour le ON et pour le OFF, l'objet de connexion SQL et le nom du contact à allumer et éteindre.

Les objets sont créés au démarrage du programme avec les données d'un fichier config.xml.

Quand une commande est reçue de wit.ai on passe la commande à l'objet concerné avec ON ou OFF. ex domotic[intents].commande('on').

Il faut coupler cela avec un arduino, une carte internet et un émetteur en 433 Mhz. Une base de données permet de connaitre la position du contact On ou OFF pour une utilisation sur plusieurs système soit par la voix ou une page web. Je vous met le code de l'arduino sur github.

INTALLATION SUR UN RASPBERRY PI TOUT NEUF
Changer port SSH : 
sudo nano /etc/ssh/sshd_config
sudo service ssh restart

Installer micro USB :
sudo modprobe snd_bcm2835
sudo nano /etc/modprobe.d/alsa-base.conf et changer :
options snd-usb-audio index=0  (à la place de -2) plus reboot

Intallation wit :
sudo apt-get install libsox-dev
sudo apt-get install python-pip
sudo apt-get install python-dev
pip install wit

Copier configGit.xml en config.xml avec vos données

Copier configSQLGit.xml en configSQL.xml avec vos données de connexion SQL

sudo apt-get install python-mysqldb  pour la base de donnée

sudo apt-get install mpg123 pour la parole




