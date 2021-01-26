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