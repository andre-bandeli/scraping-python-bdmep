from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://bdmep.inmet.gov.br/")

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "instrucoes_proximo.submit"))).click()

time.sleep(2)
email_field = driver.find_element(By.CLASS_NAME, "email")
email_field.send_keys("seu_email@example.com")
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit.form1_proximo"))).click()

time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='tipo_pontuacao' and @value='P']").click()
driver.find_element(By.XPATH, "//input[@name='tipo_dados' and @value='H']").click()
driver.find_element(By.XPATH, "//input[@name='tipo_estacao' and @value='T']").click()
driver.find_element(By.XPATH, "//input[@name='abrangencia' and @value='R']").click()

data_inicio = driver.find_element(By.ID, "datepickerInicio")
data_inicio.send_keys("dd/mm/aaaa")
data_fim = driver.find_element(By.ID, "datepickerFim")
data_fim.send_keys("dd/mm/aaaa")

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#div-regioes > div:nth-child(4) > div > label > span").click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#containerFullScreen > div.formulario_2 > section:nth-child(2) > div.box-variaveis > div > div > label > span").click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#estacoes-SU > div > div:nth-child(154) > div > label > span").click()

time.sleep(2)

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit.form2_proximo"))).click()

time.sleep(5)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#containerFullScreen > div.confirmacao > div:nth-child(2) > a.submit.confirmacao_confirmar"))).click()
time.sleep(5)
driver.quit()
