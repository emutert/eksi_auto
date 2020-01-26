"""
 Entry favorileyen tüm suserler için otomatik olarak engelle ve başlaklarını engelle 
 istekleri gönderilir.
"""

# Todo: 
# error handling, 
# command prompt parameter read, 



from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# TODO: imput from command line



URL_LOGIN = 'https://eksisozluk.com/giris?'
URL_SUSER = 'https://eksisozluk.com/biri/'
URL_ENTRY = 'https://eksisozluk.com/entry/'
URL_BLOCAKED = 'https://eksisozluk.com/takip-engellenmis'

class eksi_engelle:
    
    def __init__(self):
        super().__init__()
        opts = Options()
        #todo: headles true ?
        opts.headless = False
        self.browser = Firefox(options = opts)
        # todo first parameter of run command
        
    def login(self,USERNAME,PASSWORD):
        #todo login:

        self.browser.get(URL_LOGIN)
        self.browser.find_element_by_id('username').send_keys(USERNAME)  # login
        self.browser.find_element_by_id('password').send_keys(PASSWORD)  # password
        self.browser.find_element_by_css_selector('button.btn.btn-primary.btn-lg.btn-block').click()
        try :
            self.browser.find_element_by_css_selector('#login-form-container')
        except NoSuchElementException :
            
            return True
        else:
            return False

    def logout(self):
        #todo logout
        # pop up menu
        self.browser.find_element_by_css_selector('#options-dropdown > a:nth-child(1)').click()
        # terk link
        self.browser.find_element_by_css_selector('li.separated:nth-child(6) > a:nth-child(1)').click()
    
    def close(self):
        #close browser
        self.browser.close()

    def byEntry(self,value):
        # entry main page
        self.browser.get(URL_ENTRY + value)
        self.browser.implicitly_wait(10)
        suserList = self.collectFavs()
        #return print(suserList)
        self.runEngelleToCollectedUsers(suserList)


    def bySuser(self,suser):
        #suser main page
        #self.browser.get('https://eksisozluk.com/biri/marlon-brandonun-kedisi')
        self.browser.get(URL_SUSER + self.target_suser)
        self.browser.implicitly_wait(10)
        self.bEngelle()
        sleep(5)
        self.engelle()


    def collectFavs(self):
        ##suser fav page
        ##self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/section/div[3]/ul/li[2]/a').click()
        #fav icon click
        self.browser.find_element_by_css_selector('a.toggles:nth-child(2)').click()
        #faved suser list 
        collection = self.browser.find_element_by_css_selector('div.toggles-menu:nth-child(3)')

        susers = collection.text[0:(collection.text.find('\n.'))].replace(' ', '-').replace('@','').split()
        return susers

    def engelle(self):
        #engelle butonu click
        self.browser.find_element_by_xpath('//*[@id="blocked-link"]').click()
        self.browser.implicitly_wait(10)
        
    def bEngelle(self):
        #baslıklarını engelle click
        self.browser.find_element_by_id('blocked-index-title-link').click()
        self.browser.implicitly_wait(10)

    def runEngelleToCollectedUsers(self,suserCollection):
        for suser in suserCollection:
            # open susers page in new tab
            new_url = URL_SUSER + suser
            new_tab = "window.open('" + new_url + "\',  \'new tab\')"
            self.browser.execute_script(new_tab)

            # change tab
            self.browser.switch_to.window(self.browser.window_handles[1])
            
            # engelle 
            #engelle = browser.find_element_by_id('blocked-link')
            #self.engelle(engelle)
            self.engelle()
            self.browser.implicitly_wait(10)

            #baslikEngelle = browser.find_element_by_id('blocked-index-title-link')
            #self.bEngelle(baslikEngelle)
            self.bEngelle()
            self.browser.implicitly_wait(10)

            # return to main tab
            self.browser.switch_to.window(self.browser.window_handles[0])

        # log out 
        #self.logout()
        # close susers tab
        #self.close()

    def blockedSuserList():
        pass
