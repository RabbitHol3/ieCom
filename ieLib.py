import time
from win32com.client import Dispatch


class IE:
    def __init__(self, **kwargs):
        self.driver = Dispatch("InternetExplorer.Application")
        self.driver.Visible = kwargs.get('visible', 0)
        self.url = kwargs.get('url', '')

    def navigate(self, url, timeout=5):
        self.driver.Navigate(url)
        while self.driver.ReadyState != 4:
            time.sleep(0.05)
            if not timeout:
                return False
            timeout -= 0.05
        return True

    def get_element_by_id(self, id):
        return [elemento for elemento in ie.document.all if elemento.id == id]

    def find_elements_by_tag_name(self, name):
        return [elemento for elemento in ie.document.all if elemento.tag_name == name]
