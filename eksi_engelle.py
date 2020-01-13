/**
 Entry favorileyen tüm suserler için otomatik olarak engelle ve başlaklarını engelle 
 istekleri gönderilir.
**/

# Todo: 
# error handling, 
# command prompt parameter read, 
# login configuration file,

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# TODO: imput from command line
URL_SUSER = 'https://eksisozluk.com/biri/'

class eksi_engelle():
    
    def __init__(self):
        super().__init__()
        opts = Options()
        #todo: headles true ?
        opts.headless = False
        self.browser = Firefox(options = opts)
        self.browser.get(URL_USER + '') # todo first parameter of run command
        self.suser = []
        
    def log_in(self):
        #todo login
        self.browser.find_element_by_id('username').send_keys("xxxxxx")  # login
        self.browser.find_element_by_id('password').send_keys("xxxxxx")  # password
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/div/form/fieldset/div[4]/button').click()

    def log_out(self):
        #todo logout
        # pop up menu
        self.browser.find_element_by_xpath('/html/body/header/div/nav[1]/ul/li[9]/a').click()
        # terk link
        self.browser.find_element_by_xpath('/html/body/header/div/nav[1]/ul/li[9]/ul/li[6]/a').click()

    def collectFavs(self):
        #self.browser.find_element_by_xpath() # todo second parameter of run command
        #suser main page
        self.browser.get('https://eksisozluk.com/biri/marlon-brandonun-kedisi')
        #suser fav page
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/div[3]/ul/li[2]/a').click()
        #suser faved entrys favs
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/div[3]/div/div/div[1]/ul/li/footer/div[1]/span[3]/a[2]').click()
        #faved suser list 
        self.collection = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/div[3]/div/div/div[1]/ul/li/footer/div[1]/span[3]/div/div/ul')

        susers = collection.text[0:(collection.text.find('\n.'))].replace(' ', '-').replace('@','').split()

    def engelle(engelle):
        #engelle butonu click
        engelle.click()
        
    def bEngelle(baslikEngelle):
        #baslıklarını engelle click
        baslikEngelle.click()

    def runEngelleToCollectedUsers(self):
        while suser in suserCollection:
            # open susers page in new tab
            new_url = 'https://eksisozluk.com/biri/' + suser
            new_tab = "window.open('" + new_url + "\',  \'new tab\')"
            self.browser.execute_script(new_tab)

            # change tab
            self.browser.switch_to.window(browser.window_handles[1])
            
            # engelle 
            engelle = browser.find_element_by_id('blocked-link')
            self.engelle(engelle)
            self.browser.implicitly_wait(10)

            baslikEngelle = browser.find_element_by_id('blocked-index-title-link')
            self.bEngelle(baslikEngelle)
            self.browser.implicitly_wait(10)

            # return to main tab
            self.browser.switch_to.window(browser.window_handles[0])

        # log out 
        self.log_out()
        # close susers tab
        browser.close()
