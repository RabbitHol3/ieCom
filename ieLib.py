import time
from win32com.client import Dispatch


class IE:
    def __init__(self, **kwargs):
        self.driver = Dispatch("InternetExplorer.Application")
        self.driver.Visible = kwargs.get('visible', 0)
        self.url = kwargs.get('url', '')
        self.timeout = kwargs.get('timeout', 5)

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

    def get_element_by_id(self, id):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.id == id:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    def get_elements_by_tag_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.tagName == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    def get_elements_by_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.name == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno

    def get_elements_by_class_name(self, name):
        retorno = []
        for elemento in self.driver.document.all:
            try:
                if elemento.className == name:
                    retorno.append(elemento)
            except AttributeError:
                continue
        return retorno