from database import database
import importlib
from colorama import init , Fore

init(autoreset=True)

version='0.0.1.1'
p_session={}
sessions={}

"""
fonctions est un ensemble de fonctions et class pour faire resembler le plus ce programme à Metatsploit
"""
class use():
    """ La class use , permet de choisir un exploit (cve) """
    def __init__(self,exploit,**argv):
        exploit=str(exploit)
        trouve=0

        if 'CVE' not in exploit:
            exploit=exploit.lower()

        for (num, cve, name, auteur, vendeur, desc) in database.search_exloit(exploit):
            trouve = 1
            self.exploit = cve
            self.desc = desc
            self.name = name

        if trouve == 0:
            raise Exception(Fore.RED+"[+] Exploit Indisponible ! ")

        self.parametre={}
        self.module=importlib.import_module('exploits.'+self.exploit.replace('-', '_'),package='exploits')
        self.module.auto_args(self.parametre)

    def __str__(self):
        return 'Ceci est une instance de la class use ayant pour exploit {}'.format(self.exploit)

    def options(self):
        """ Affiche les options pour executé l'exploit """
        self.module.notice(self.parametre)

    def run(self):
        """ Execute l'exploit """
        try:
            #os.system('clear')
            self.session = self.module.exploit(self.parametre)
        except KeyboardInterrupt:
            print("Fin de la session")
            return self.session

    def info(self):
        print(self.name)
        print(self.desc)

# Fonction de recherche d'exploit
def search(exp:str,vendeur=None):
    # exp.replace("'",'\'') doit ajouter des protection cotre les injection sql

    """ 
        Fonction servant a chercher des exploits dans la base de donnée
        exp : expression
        vendeur : nom du vendeur
    """
    found=0

    x = database.mydb.cursor()

    if vendeur is None:
        x.execute("SELECT * FROM exploit WHERE CVE LIKE '%{0}%' OR num LIKE '%{0}%' OR desc LIKE '%{0}%' ;".format(exp))
    else:
        vendeur = str(vendeur).replace("'","\'")
        x.execute("SELECT * FROM exploit WHERE (CVE LIKE '%{0}%' OR num LIKE '%{0}%' OR desc LIKE '%{0}%') AND vendeur == {1} ;".format(exp,vendeur))

    for (num,cve, nom ,auteur, vendeurs,desc ) in x:
        print(
            f' num :{Fore.RED+str(num)}',
            f' cve :{Fore.GREEN+cve}',
            )
        found=1

    if found != 1:
        print(Fore.RED+'[+] Exploit Indisponible !')

