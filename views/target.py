from sky.backend import (vuln, info)
from rich.console import Console
from rich.table import Table

console = Console()
table = Table()

def view_vuln(ip:str):
    """
    liste le vulnerabilité decouverte par shodan
    """
    x=vuln(ip)

    table.add_column("Type", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    table.add_row('hostnames',x['hostnames'])
    table.add_row('ports',x['ports'])
    table.add_row('vulns',x['vulns'])
    console.print(table)

def view_info(ip:str,**argx):
    """
    DOnne les information sur une addresse IP
    """
    x = info(ip)
    
    table.add_column("Type", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row('ip',x['ip_str'])

    if 'asn' in x.keys():
    	table.add_row('asn',x['asn'])
    if 'ports' in x.keys():
    	table.add_row('ports',str(x['ports']))
    if 'vulns' in x.keys():
    	table.add_row('vuls',x['vulns'])
    table.add_row('os',x['os'])

    if 'domains' in x.keys():
    	table.add_row('domains',str(x['domains']))
    if 'org' in x.keys():
    	table.add_row('org',x['org'])
    if 'hostnames' in x.keys():
    	table.add_row('hostnames',x['hostnames'])
    if 'location' in x.keys():
    	table.add_row('country_name',x['location']['country_name'])
    	table.add_row('city',x['location']['city'])
    	table.add_row('longitude',x['location']['longitude'])
    	table.add_row('latitude',x['location']['latitude'])
    if 'data' in x.keys():
        table.add_column('Data',x['data'])
    console.print(table)

