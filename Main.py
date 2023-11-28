from selenium import webdriver
import pandas as pd
import time

# Lê o valor de usuário e de senha do arquivo .csv
tabela = pd.read_csv('arquivo.csv', sep=',')
usuario = tabela.iat[2, 0]
senha = tabela.iat[1, 1]
nome = tabela.iat[1, 2]
sobrenome = tabela.iat[0, 3]
zipcode = tabela.iat[1, 4]

# Entra no navegador e coloca as informações de usuário e senha, e entra no site
navegador = webdriver.Chrome()
navegador.get('https://www.saucedemo.com/')
navegador.find_element('xpath', '//*[@id="user-name"]').send_keys(usuario)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(senha)
navegador.find_element('xpath', '//*[@id="login-button"]').click()

# Adiciona os produtos no carrinho
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-onesie"]').click()

# Verifica o carrinho com os produtos e faz o checkout
navegador.find_element('xpath', '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
navegador.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
navegador.find_element('xpath', '//*[@id="checkout"]').click()

# Adiciona as informações de checkout, continua e finaliza a compra
navegador.find_element('xpath', '//*[@id="first-name"]').send_keys(nome)
navegador.find_element('xpath', '//*[@id="postal-code"]').send_keys(str(zipcode))

#Usando o javascrip para definir o valor do campo
Sobrenome = navegador.find_element('xpath', '//*[@id="last-name"]')
navegador.execute_script('arguments[0].value = arguments[1];', Sobrenome, sobrenome)
navegador.find_element('xpath', '//*[@id="continue"]').click()
navegador.find_element('xpath', '//*[@id="finish"]').click()

# Retorna a página de compras
navegador.find_element('xpath', '//*[@id="back-to-products"]')
time.sleep(100)
