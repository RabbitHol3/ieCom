class criminoso:
    def __init__(self, driver):
        self.driver = driver
        self.nome = None
        self.profile_url = driver.find_element_by_xpath('//*[@id="content_right"]/div/div[1]/a').get_attribute('href')
        self.spirit = None
        self.respeito = None

    def get_name(self):
        pass

    def get_respect(self):
        pass

    def get_tickets(self):
        pass

    def get_staminia(self):
        pass

    def get_hp(self):
        pass

    def get_addiction(self):
        pass

    def get_intelligence(self):
        pass

    def
