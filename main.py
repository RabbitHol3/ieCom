from ieLib import IE
from libOcrime import crims
from datetime import date
import json, time


with open('../auth/tc_auth.txt') as f:
    auth = json.loads(f.read())

with IE(visible=True) as ieObj:
    teste = 'x'

cliente = crims(login=auth['username'], password=auth['password'], url=auth['url'], visible=True)

cliente.log_in()
cliente.roubo()




elm = cliente.ie.get_elements_by_class_name('modal-footer')[0]
elm.innerText = ""
cliente.ie.execute(code)
x =1

#14a86fbc0091
