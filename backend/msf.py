from sky.database import database
import importlib
from colorama import init , Fore

init(autoreset=True)

p_session = {}

class use():
    """ La class use , permet de choisir un exploit (cve) """
    def __init__(self,exploit,**argv):
        exploit = str(exploit).upper()
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
        """ Affiche les options pour executé l'exploit """
        print('Les options et leurs valeurs \n')
        for i in self.module.ARGS:
            try:
                print(f'\t {i} ==> {self.parametre[i]}')
            except:
                print(f'\t {i} ==> ')

    def run(self):
        """ Execute l'exploit """
        self.session = self.module.exploit(self.parametre)
        
    def info(self):
        print(self.name)
        print(self.desc)

def set(session:int,param:dict):
    """
        Pose les parametres d'exploitation
    """
    global p_session
    for i in param.keys():
        p_session[session].parametre[i] = param[i]

def show_options(session = None):
    if session is None:
        l = len(p_session)
        print(p_session[l].options())
    else:
        print(p_session[session].options())




