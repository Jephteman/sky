from sky.database import database
from colorama import init , Fore
import importlib

init(autoreset=True)

class use():
    """ La class use , permet de choisir un exploit (cve) """
    def __init__(self,exploit,**argv):
        self.exploit = str(exploit).upper()
        trouve = 0

        for (num, cve, name, auteur, vendeur, desc) in database.search_exloit(exploit):
            trouve = 1
            self.exploit = cve
            self.desc = desc
            self.name = name

        if trouve == 0:
            raise Exception(Fore.RED+"[+] Exploit Indisponible ! ")

        self.parametre={}
        self.module=importlib.import_module('exploits.'+self.exploit.replace('-', '_'),package='sky')
        self.module.auto_args(self.parametre)

    def __str__(self):
        return 'Ceci est une instance de la class use ayant pour exploit {}'.format(self.exploit)

    def options(self):
        """ retourne les options pour executé l'exploit """

        return self.module.ARGS

    def run(self):
        """ Execute l'exploit """
        self.session = self.module.exploit(self.parametre)
        
    def info(self):
        return [self.name,self.desc]


        