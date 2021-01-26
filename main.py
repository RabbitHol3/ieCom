import random
import time

from win32com.client import Dispatch

ie = Dispatch("InternetExplorer.Application")
ie.visible = 1

ie.navigate('http://www.thecrims.com')

ie.document.getElementsByTagName('input')


# document.getElementsByTagName('input')[6].value

def find_element_by_tag_name(tag_name):
    return [elemento for elemento in ie.document.all if
            elemento.className == 'front-input' and elemento.name == 'username']
    pass


while (ie.ReadyState != 4):
    time.sleep(0.05)

hrefs = ie.document.getElementsByTagName("A")
href = hrefs[random.randrange(hrefs.length)]
# How to click this one?


from ieLib import IE

url = 'http://www.thecrims.com/'

ie = IE(url=url, visible=True)

dic = {
    'lg': 'nONoGame',
    'pw': '14a86fbc0091',
}

# tydpczedpczcrepfoi@mhzayt.online
# tc = crims(dic['lg'],dic['pw'])

# tc.browser.find_elements_by_xpath('')
