"""
    Entry favorileyen tüm suserler için otomatik olarak engelle ve 
    başlaklarını engelle istekleri gönderilir.
"""

# Todo: 
# error handling, 
# blockedSuserList() will return blocekd susers and total count
# headless will set to true 


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep


URL_LOGIN = 'https://eksisozluk.com/giris?'
URL_SUSER = 'https://eksisozluk.com/biri/'
URL_ENTRY = 'https://eksisozluk.com/entry/'
URL_BLOCAKED = 'https://eksisozluk.com/takip-engellenmis'

class eksi_engelle:
    
    def __init__(self):
        super().__init__()
        opts = Options()
        #todo: headles true ?
        opts.headless = True
        self.browser = Firefox(options = opts)

        
    def login(self,USERNAME,PASSWORD):
        #todo login:

        self.browser.get(URL_LOGIN)
        self.browser.find_element(By.ID,value='username').send_keys(USERNAME)  # login
        self.browser.find_element(By.ID,value='password').send_keys(PASSWORD)  # password
        self.browser.find_element(By.CSS_SELECTOR, value='button.btn.btn-primary.btn-lg.btn-block').click()
        try :
            self.browser.find_element(By.CSS_SELECTOR, value='#login-form-container')
        except NoSuchElementException :  
            return True
        else:
            return False

    def popupClick(self):
        # pop up menu
        self.browser.find_element(By.CSS_SELECTOR, value='#options-dropdown > a:nth-child(1)').click()


    def logout(self):
        #todo logout
        # pop up menu
        self.popupClick()
        # terk button
        self.browser.find_element(By.CSS_SELECTOR, value='li.separated:nth-child(6) > a:nth-child(1)').click()
    
    def close(self):
        #close browser
        self.browser.close()

    def quit(self):
        #quit terminates webdriver session
        self.browser.quit()

    def byEntry(self,value):
        # entry main page
        self.browser.get(URL_ENTRY + value)
        self.browser.implicitly_wait(10)
        suserList = self.collectFavs()
        #return print(suserList)
        self.runEngelleToCollectedUsers(suserList)


    def bySuser(self,suser):
        #suser main page
        self.browser.get(URL_SUSER + suser)
        self.browser.implicitly_wait(10)
        sleep(5)
        self.engelle()
        sleep(5)
        self.bEngelle()     


    def collectFavs(self):
        ##suser fav page

        #
        ##selenium.common.exceptions.ElementClickInterceptedException: 
        # Message: Element <a class="favorite-count toggles"> 
        # is not clickable at point (491,684) 
        # because another element <div class="toast-bottom-content"> obscures it
        # Fix WebDriverWait added
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.toggles:nth-child(2)'))).click()
        #self.browser.find_element_by_css_selector('a.toggles:nth-child(2)').click()
        
        #Caylak susers collecyion
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#show-caylak-favs-link'))).click()

        #faved suser list 
        collection = self.browser.find_element(By.CSS_SELECTOR, value='div.toggles-menu:nth-child(3)')

        susers = collection.text[0:(collection.text.find('\n.'))].replace(' ', '-').replace('@','').split()
        
        return susers

    def engelle(self):
        #engelle butonu click
        sleep(5)
        try:

            self.browser.find_element(By.XPATH, value='//*[@id="blocked-link"]').click()
            self.browser.implicitly_wait(10)

        except NoSuchElementException:

            return 'NoSuchElementException'
        else :

            return 'Blocked'
        
    def bEngelle(self):
        #baslıklarını engelle click
        sleep(5)
        try:

            self.browser.find_element(By.ID, value='blocked-index-title-link').click()
            self.browser.implicitly_wait(10)
        except  NoSuchElementException:

            return 'NoSuchElementException'
        else:
            return 'B-Blocked'

    def runEngelleToCollectedUsers(self,suserCollection):
        """Gets Suser list, opens each susers page in new tab and performs 
        blocking actions.

            Parameters
            ----------
            suserCollection : []
                list of the susers.
        """
        for suser in suserCollection:
            # open susers page in new tab
            new_url = URL_SUSER + suser
            new_tab = "window.open('" + new_url + "\',  \'new tab\')"
            self.browser.execute_script(new_tab)

            # change tab
            self.browser.switch_to.window(self.browser.window_handles[1])

            # engelle 
            self.engelle()
            self.browser.implicitly_wait(10)

            # baskıları engelle 
            self.bEngelle()
            self.browser.implicitly_wait(10)

            # close susers tab
            self.close()            

            # return to main tab
            self.browser.switch_to.window(self.browser.window_handles[0])


    def blockedSuserList(self):
        # Blocked susers 

        # pop up menu
        self.popupClick()

        # takip/engellenmis button
        self.browser.find_element(By.CSS_SELECTOR, value='.open > li:nth-child(5) > a:nth-child(1)').click()

        #Return Blocked Count
        #WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#show-caylak-favs-link'))).click()
        self.browser.implicitly_wait(10)
        return self.browser.find_element(By.CSS_SELECTOR, value='div.relation-block:nth-child(4) > p:nth-child(2)').text
      
    