import sqlite3
from colorama import init, Fore

init(autoreset=True)

#   ma base de donneé
mydb = sqlite3.Connection('database/exploit.db')

def search_exloit(exploit:str):
    """
    exploit : CVE of vulnerability or number in db
    """
    sql = mydb.cursor()
    sql.execute("SELECT * FROM exploit WHERE CVE == '{0}' OR NUM == '{0}';".format(exploit))
    return sql

# Fonction de recherche d'exploit
def search(exp:str,vendeur=None):
    exp.replace("'",'\'')

    """ Fonction servant a chercher des exploits dans la base de donnée"""
    # exp : expression
    # vendeur : nom du vendeur

    x=mydb.cursor()
    found=0

    if vendeur is None:
        x.execute("SELECT * FROM exploit WHERE CVE LIKE '%{0}%' OR num LIKE '%{0}%' OR desc LIKE '%{0}%' ;".format(exp))
    else:
        vender=str(vendeur).replace("'","\'")
        x.execute("SELECT * FROM exploit WHERE (CVE LIKE '%{0}%' OR num LIKE '%{0}%' OR desc LIKE '%{0}%') AND vendeur == {1} ;".format(exp,vendeur))

    for (num,cve, nom ,auteur, vendeurs,desc ) in x:
        print(
            Fore.RED+str(num),
            Fore.GREEN+cve
            )
        found=1

    if found != 1:
        print(Fore.RED+'[+] Exploit Indisponible !')
