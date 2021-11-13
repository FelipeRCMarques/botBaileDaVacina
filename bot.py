import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class bot():
    def __init__(self):
        self.drive = webdriver.Chrome(executable_path=r'.\chromedriver.exe')

    def preencherForms(self):
        drive = self.drive
        drive.get('https://docs.google.com/forms/d/e/1FAIpQLSefTvayqYrQTVmRR_rAfE6hewP5ihmosiVTCkz5sNa88ACMdg/viewform')

        # abacaxi
        drive.find_element(By.XPATH, '//*[@id="i8"]').click()

        # caso o chrome crashe
        # time.sleep(0.5)

        drive.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span').click()

bot = bot()
while(True):
    bot.preencherForms()