from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from secrets import pw


class IGBot:
    def __init__(self, username, pw, target):
        self.base_url = "https://instagram.com"
        self.username = username
        self.target = target
        self.target_url = self.base_url + "/" + self.target
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        sleep (1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
        sleep(4)

    def follow_followers(self):
        self.driver.get(self.target_url)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        counter = 0

        while(counter<50):

            try:
                follow = self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
                counter += 1
                print("Cantidad de seguidos: " + str(counter))
            except NoSuchElementException:
                self.scroll_down()
            


    def scroll_down(self):
        last_element = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[last()]")
        self.driver.execute_script('arguments[0].scrollIntoView()', last_element)
    
        

my_bot = IGBot('bautirueda', pw, "rufinas_swimwear")
my_bot.follow_followers()


