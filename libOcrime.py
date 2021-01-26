from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time, os, shutil, requests, zipfile


class crims():

    def __init__(self, login, password):

        option = webdriver.ChromeOptions()
        # Removes navigator.webdriver flag
        # For older ChromeDriver under version 79.0.3945.16
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")

        # For ChromeDriver version 79.0.3945.16 or over
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.473")

        self.login = login
        self.password = password
        self.browser = webdriver.Chrome(
            executable_path=os.path.dirname(os.path.realpath(__file__)) + '\\downloads\\webdriver\\chromedriver.exe',
            options=options)
        self.browser.implicitly_wait(5)
        self.browser.get("http://www.youtube.com/")
        self.rob_power = 10
        self.number = 6
        self.counter = None

    def down_chromium(self, vers='87.0.4280.88'):
        """
        Funcao para certificar que haja o webdriver
        """
        diretorio = os.path.dirname(os.path.realpath(__file__)) + '\\downloads\\webdriver\\chromedriver.exe'
        if not (os.path.isfile(diretorio)):
            try:
                if not os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + "\\downloads\\webdriver\\"):
                    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "\\downloads\\")
                    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + "\\downloads\\webdriver\\")

            except FileExistsError:
                pass

            url = f"https://chromedriver.storage.googleapis.com/{vers}/chromedriver_win32.zip"
            local_filename = url.split('/')[-1]
            # NOTE the stream=True parameter below
            with requests.get(url, stream=True) as r:
                print(r.raise_for_status())
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        # If you have chunk encoded response uncomment if
                        # and set chunk_size parameter to None.
                        # if chunk:
                        f.write(chunk)

            with zipfile.ZipFile(local_filename, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(os.path.realpath(__file__)) + "\\downloads\\webdriver\\")
            os.remove(local_filename)
            return local_filename
        return str(diretorio)

    def wait_element(self, driver, method, element, timeout=60):
        """
            Aguarda Elemento existir
        """
        myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((eval(method), element)))

    def log_in(self):
        log = self.browser.find_element_by_xpath('//*[@id="loginform"]/input[1]')
        pas = self.browser.find_element_by_xpath('//*[@id="loginform"]/input[2]')
        logged = None
        if log:
            try:
                log.send_keys(f'{self.login}')
            except:
                print("Problema com o Login")
        if pas:
            try:
                pas.send_keys(f'{self.password}')
            except:
                print("Problema com a Senha")
        if log.get_attribute("value") == f'{self.login}' and pas.get_attribute("value") == f'{self.password}':
            try:
                self.browser.find_element_by_xpath('//*[@id="loginform"]/button').click()
            except Exception as e:
                print(str(e))
