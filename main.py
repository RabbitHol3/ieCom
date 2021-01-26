from ieLib import IE
from libOcrime import crims
import json
with open('../tc_auth.txt') as f:
    auth = json.loads(f.read())

cliente = crims(login=auth['username'], password=auth['password'], url=auth['url'], visible=True)

cliente.log_in()
ie = IE(visible=True)
ie.navigate('http://www.thecrims.com')


#14a86fbc0091
