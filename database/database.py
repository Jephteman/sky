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


