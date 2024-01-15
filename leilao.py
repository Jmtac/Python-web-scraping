import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

site_url = 'https://www.freitasleiloeiro.com.br/Leiloes/Pesquisar?query=&categoria=1'

options = webdriver.ChromeOptions()
options.headless = False

driver = webdriver.Chrome(options=options)
driver.get(site_url)

button = driver.find_element(By.ID, 'btnListarLotes')
for i in range(0, 100):
    try:
        button.click()
        sleep(1.5)
    except Exception as e:
        if e:
            continue
    print(i)

nomes = driver.find_elements(By.XPATH, "//div[@class='cardLote-descVeic']")
precos = driver.find_elements(By.XPATH, "//div[@class='cardLote-vlr']")

workbook = openpyxl.Workbook()

workbook.create_sheet('lotes')

pag = workbook['lotes']

pag['A1'].value = 'veículo'
pag['B1'].value = 'preço'

for nome, preco in zip(nomes, precos):
    pag.append([nome.text, preco.text])
workbook.save('leilao.xlsx')
