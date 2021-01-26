from win32com.client import Dispatch


class IE:
    def __init__(self, **kwargs):
        self.driver = Dispatch("InternetExplorer.Application")
        self.driver.Visible = kwargs.get('visible', 0)
        self.url = kwargs.get('url', '')

    def navigate(self, url):
        self.driver.Navigate(url)

    def get_element_by_
        https: // gist.github.com / f78be1494a5f5e27ff388877059d0001