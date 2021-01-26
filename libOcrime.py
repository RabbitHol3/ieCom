import time, os, shutil, requests, zipfile
from ieLib import IE
from classLib import criminoso, botStats

class crims:

    def __init__(self, login, password, url, visible):
        self.login = login
        self.password = password
        self.url = url
        self.bot = botStats()
        self.ie = IE(visible=visible)
        self.ie.activate()
        self.player_status = None


    def log_in(self):
        self.ie.navigate(self.url)
        if not self.bot.logged:
            self.ie.get_elements_by_name('username')[1].value = self.login
            self.ie.get_elements_by_name('password')[0].value = self.password
            self.ie.get_elements_by_class_name('btn btn-large btn-inverse btn-block')[0].click()
            self.ie.wait_its_ready()
            self.player_status = criminoso(self.ie)
            self.bot.logged = True
        return True

