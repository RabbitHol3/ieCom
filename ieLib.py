import time
from win32com.client import Dispatch


class IE:
    def __init__(self, **kwargs):
        self.driver = Dispatch("InternetExplorer.Application")
        self.driver.Visible = kwargs.get('visible', 0)
        self.url = kwargs.get('url', '')

    def navigate(self, url, timeout=5):
        self.driver.Navigate(url)
        while (self.driver.ReadyState != 4):

            time.sleep(0.05)
            if not timeout:
                return False
            timeout -= 0.05

    def get_element_by_id(self):
        pass
