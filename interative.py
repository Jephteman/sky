from colorama import init , Fore
from fonctions import (
    search ,
    version,
    use as use_,
    p_session
)

init(autoreset=True)
mysession = ''

def session(name):
    """ Change a sesion """
    if name in p_sessions.keys():
        try:
            global mysession
            mysession = name
            p_session[name].session()
        except KeyboardInterrupt:
            print(Fore.GREEN+f'[+] Session {name} en arrière plan!')
    else:
        print(Fore.RED+'[+] La sesion {} n\'existe pas !'.format(name))


def set(arg:dict):
    """ attribue la ou les valeur """
    if type(arg) == type(dict()):
        try:
            for mysession in arg.keys():
                p_session[0].parametre[mysession.upper()]=arg[mysession]
                print(mysession.upper(),'==> ',arg[mysession])
        except IndexError:
            pass
    else:
        print(Fore.RED+'[+] Entré un format valide')
        print("ex : set({'user':'admin','rhosts':'10.10.0.1'})")


def use(cve):
    global mysession
    last = len(p_session.keys()) + 1
    p_session[last]=use_(cve)
    mysession = last


def info(*argv):
    """ Fonction servant a trouver des informations sur un exploit (cve) """
    try:
        if type(argv[0]) == type(str()) or type(argv[0]) == type(int()):
            x=mydb.cursor()
            x.execute("select nom,desc from exploit where cve == '{0}' or num == {0};".format(argv[0]))
            for name ,desc in x:
                print(name)
                print(desc)
    except IndexError:
        if len(p_session) != 0 :
            p_session[0].info()
        else:
            print(Fore.GREEN+"""
                eXpy est un programme Open-Source codé par Mr me

                """)


def back():
    """ Retour en arriere """
    global mysession
    mysession = ''


def show_options():
    """ Affiche les options """
    if mysession != "":
        p_session[mysession].options()
    else:
        print(Fore.GREEN+"Veillez d'abord choisir un exploit")


options = show_options


def run():
    """ execute l'exploit """
    try:
        if mysession in p_session.keys():
            p_session[mysession].run()
        else:
            print(Fore.GREEN + '[+] Veillez choisir un exploit et completer les arguments')
    except KeyboardInterrupt:
        print(Fore.GREEN + f'[+] session {mysession} en arriere plan')


exploit = run


def sessions():
    """ s'occupe d'affichier les sessions """
    if len(p_session) != 0:
        print('\n')
        for i in p_session.keys():
            print('id : \t{0} \t{1}:{2} \t{3}'.format(i,p_session[i].parametre['RHOSTS'],p_session[i].parametre['RPORTS'],p_session[i].exploit))

