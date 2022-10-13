from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome() #aqui faz a linkagem com o navegador
navegador.get('https://www.walissonsilva.com/cursos')

elemento = navegador.find_element(By.TAG_NAME, "input")
elemento.send_keys("data")