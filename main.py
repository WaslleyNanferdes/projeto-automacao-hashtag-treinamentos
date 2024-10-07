from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def open_browser(driver, url : str):
    driver.get(url)
    driver.maximize_window()

def login(driver, wait = 30):
    driver.find_element(By.ID, 'email').send_keys('testeautomacao12345654321@teste.com')
    driver.implicitly_wait(wait)
    sleep(randint(1, 3))
    driver.find_element(By.ID, 'password').send_keys('testeautomacao12345654321')
    driver.implicitly_wait(wait)
    sleep(randint(1, 3))
    driver.find_element(By.ID, 'pgtpy-botao').click()
    driver.implicitly_wait(wait)

def main():
    url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    driver = webdriver.Chrome()
    
    open_browser(driver, url)
    login(driver)

if __name__ == "__main__":
    main()