import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_browser(driver, url):
    driver.get(url)
    driver.maximize_window()

def login(driver, wait = 30):
    driver.find_element(By.ID, 'email').send_keys('testeautomacao12345654321@teste.com')
    driver.implicitly_wait(wait)
    driver.find_element(By.ID, 'password').send_keys('testeautomacao12345654321')
    driver.implicitly_wait(wait)
    driver.find_element(By.ID, 'pgtpy-botao').click()
    driver.implicitly_wait(wait)

def cadastro_produtos(driver, ids, sheet, wait = 30):
    for i in sheet.index:
        for j, k in enumerate(sheet.columns):
            if str(sheet[k][i]) == 'nan':
                pass
            else:
                driver.find_element(By.ID, ids[j]).send_keys(str(sheet[k][i]))
                driver.implicitly_wait(wait)
        driver.find_element(By.ID, 'pgtpy-botao').click()
        driver.implicitly_wait(wait)

def main():
    url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    driver = webdriver.Chrome()
    csv = pd.read_csv('./produtos.csv')
    ids = ['codigo', 'marca', 'tipo', 'categoria', 'preco_unitario', 'custo', 'obs']
    
    open_browser(driver, url)
    login(driver)
    cadastro_produtos(driver, ids, csv)

if __name__ == "__main__":
    main()