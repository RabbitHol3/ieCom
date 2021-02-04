from bs4 import BeautifulSoup
import json


class criminoso:
    def __init__(self, driver):
        self.driver = driver
        self.xHTML = None

    def parse_right_content(self):
        return [x.strip() for x in BeautifulSoup(self.driver.get_element_by_id('content_right')[0].outerHtml, 'lxml').findAll(text=True) if not len(x) == 1 or x.isdigit()]

    def parse_user_info_html(self):
        return BeautifulSoup(self.driver.get_element_by_id('user-profile-info')[0].outerHtml, 'lxml')

    def parse_user_stats1_html(self):
        return BeautifulSoup(self.driver.get_elements_by_class_name('user_profile_stats pull-left text-center')[0].outerHtml, 'lxml')

    def parse_user_stats2_html(self):
        return BeautifulSoup(self.driver.get_elements_by_class_name('user_profile_stats pull-right text-center')[0].outerHtml, 'lxml')

    #User Info

    def name(self):
        return self.parse_user_info_html().findAll(text=True)[0]

    def moral(self):
        return self.parse_user_info_html().findAll(text=True)[9]

    def url(self):
        return next((x.href for x in self.driver.get_elements_by_tag_name('A') if 'user' in x.href), None)

    def respect(self):
        return self.parse_user_info_html().findAll(text=True)[13]

    def tickets(self):
        return self.parse_user_info_html().findAll(text=True)[17]

    # Stats

    #tab1
    def inteligencia(self):
        return self.parse_user_stats1_html().findAll(text=True)[1]

    def carisma(self):
        return self.parse_user_stats1_html().findAll(text=True)[4]

    #tab2
    def forca(self):
        return self.parse_user_stats2_html().findAll(text=True)[1]

    def resistencia(self):
        return self.parse_user_stats2_html().findAll(text=True)[3]



    def estamina(self):
        return int(self.parse_right_content()[10].split(' ')[1].split('%')[0])

    def addiction(self):
        return int(self.parse_right_content()[12].split(' ')[1].split('%')[0])


    def hp(self):
        return self.parse_right_content()[11].split('HP: ')[1].split(' / ')

    def money(self):
        return float(self.parse_right_content()[22].split('$')[1].replace(',', '.'))

    def pwr_solo(self):
        return int(self.parse_right_content()[24])

    def pwr_gg(self):
        return int(self.parse_right_content()[26])

    def pwr_fight(self):
        return int(self.parse_right_content()[28])

    def creditos(self):
        return int(self.parse_right_content()[29].split(': ')[1])



class botStats:
    def __init__(self):
        self.running = None
        self.logged = None

class novoSats:
    def __init__(self, driver):
        self.driver = driver
        self.code = "document.getElementsByClassName('modal-footer')[0].innerText = JSON.stringify(userState)"
        self.userState = self.updateStats()

    def updateStats(self):
        try:
            elm = self.driver.get_elements_by_class_name('modal-footer')[0]
            elm.innerText = ""
            self.driver.execute(self.code)
            self.userState = json.loads(elm.innerText)
            return json.loads(elm.innerText)
        except TypeError:
            return False
        
    def __enter__(self):  
        return self.userState      

    def __exit__(self):
        pass