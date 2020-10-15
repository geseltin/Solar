from selenium import webdriver



class WebDriverInstance():


    def getWebDriverInstance(self):
        basePage = "http://10.201.48.146:8080/inrights/app/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(basePage)
        return driver





# cc = WebDriverInstance()
# cc.getWebDriverInstance()