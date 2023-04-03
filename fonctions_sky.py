from colorama import init, Fore
from rich.console import Console
from rich.table import Table
from shodan.client import Shodan
import subprocess
import requests

init(autoreset=True)
console = Console()


Instance = ''


def init(key):
	global Instance 
	Instance = Shodan(key)

def verif_key():
	i = subprocess.getstatusoutput('cat ~/.config/shodan/api_key')
	if i[0] == 0:
		return i[1]
	else:
		return False

def banner_1():
	print("""
	 ________________________________________________________________
	/                                                                \
	|  Welcom to sky , a simple promgram to hack the world machine , |
	\                                                                /
	 ----------------------------------------------------------------\
	    \
	     \
	         .--.
	        |o_o |
	        |:_/ |
	       //   \ \
	      (|     | )
	     /'\_   _/`\
	     \___)=(___/

		""")

def vuln(ip:str):
	"""
		show vuln of ip
	"""
	x = requests.get(f"https://internetdb.shodan.io/{ip}").json()
	if x['detail'] == 'No information available':
		print('Information indisponible')
		return
	
	return x

def info(ip:str,**argv):
	"""
		Gie information about ip
	"""
	try:
		x = Instance.host(ip)
	except shodan.exception.APIError:
		print(Fore.RED + '[+] Aucunne Information sur cette adresse IP ')
		return
	return x
	
def filters(resultat,**argv):
	if len(argv.keys()) == 0:
		return resultat

	condition = 'ret = True if '
	n = 0
	for i in argv.keys():
		if n == 1:
			condition +=  "'{resultat}['{i}']' == '{argv}['{i}']' ".format(i=i)
			n=1
		else:
			condition +=  "and '{resultat}['{i}']' == '{argv}['{i}']' ".format(i=i)
	
	condition += 'else True'

	for i in resultat['matches']:
		exec(condition.format(argv=argv,resultat=i))
		if ret:
			y.append(i)

def seach_service(kind,**argv):
	support_kinds = {'adb':'Android Debug Bridge','vnc':'vnc',\
	'vmware':'vmware','docker':'docker','couchdb':'couchdb',\
	'screenshot':'has_screenshot:true','ganglia':'product:"Ganglia XML Grid Monitor"',\
	'bitcoin':'satoshi','chromecast':'chromecast','cloud': ['Amazon cloud','cloud Azure','cloud Google'],\
	'cockroachdb':'cockroachdb','dns':['dns-tcp','dns-udp recursion enabled','dns-udp recursion enabled'],\
	'ftp':['ftp','ftp 220']}

	if kind not in support_kinds.keys():
		print(f'{kind} is not supported')
		return 

	x = Instance.search(kind)
	return filters(x,argv)




	


	

	





