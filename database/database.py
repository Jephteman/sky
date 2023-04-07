import sqlite3

#   ma base de donneé
exploit_db = sqlite3.Connection('exploit.db')
target_db = sqlite3.Connection('target.db')

def search_exloit(exploit:str):
    """
    exploit : CVE of vulnerability or number in db
    """
    sql = exploit_db.cursor()
    sql.execute("SELECT * FROM exploit WHERE CVE == '{0}' OR NUM == '{0}';".format(exploit))
    return sql


