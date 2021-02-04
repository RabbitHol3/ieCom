import time, psutil
from datetime import datetime
from win32com.client import Dispatch
from functools import  wraps


def retry(function):
    @wraps(function)
    def _retry(*args, **kwargs):
        trys = 6
        while trys:
            try:
                retorno = function(*args, **kwargs)
                if type(retorno) is list and len(retorno) == 0:
                    raise IndexError
                return retorno
            except:
                time.sleep(0.5)
                trys -= 1
                print ("_retry: another error")
    return _retry

class IE:

    def __enter__(self):
        PROCNAME = "iexplore.exe"
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()

    def __init__(self, **kwargs):
        self.driver = Dispatch("InternetExplorer.Application")
        self.driver.Visible = kwargs.get('visible', 0)
        self.url = kwargs.get('url', '')
        self.timeout = kwargs.get('timeout', 5)
        self.oShell = Dispatch('WScript.Shell')
        

    

    def __exit__(self, *args, **kwargs):
        try:
            self.driver.quit()
        except Exception:
            pass
    
    def activate(self):
        self.oShell.Appactivate('Internet Explorer')
        return True

    def maxmize(self):
        self.activate()
        self.oShell.SendKeys('% x')
        return True

    def minimize(self):
        self.activate()
        self.oShell.SendKeys('% n')

    def wait_its_ready(self):
        timeout = self.timeout
        while self.driver.ReadyState != 4:
            time.sleep(0.05)
            if not timeout:
                raise TimeoutError
            timeout -= 0.05

    def navigate(self, url, timeout=5):
        self.driver.Navigate(url)
        self.wait_its_ready()
        return True

    @retry
    def get_element_by_id(self, id):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.id == id:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno
    
    @retry
    def get_elements_by_tag_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.tagName == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    @retry
    def get_elements_by_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.name == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    @retry
    def get_elements_by_class_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.className == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    def execute(self, code):
        self.driver.document.parentWindow.execScript(code)    
        return True




class waitElement:
    def __init__(self, driver, **kwargs):
        self.driver = driver
        self.timeout = kwargs.get('timeout', 5)


    def by_id(self, id):
        retorno = []
        timeout = self.timeout
        while not retorno or timeout:
            for elemento in self.driver.document.all:
                try:
                    if elemento.id == id:
                        retorno.append(elemento)
                except AttributeError:
                    continue
            time.sleep(0.050)
            timeout -= 0.050
        return True if retorno else False

    def by_tag_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.tagName == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    def by_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.name == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    def by_class_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.className == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno
