from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Inicialización del WebDriver
driver = webdriver.Chrome()

# URL del sitio web
driver.get('https://mastodon.social/explore')

Usuario = 'Huerfano003'
Mail = 'manuel_pgrm@hotmail.com'
password = 'Anitalahuerfanita'

# Función para registrar un nuevo usuario
def test_registro_usuario():

   # Ingresar al apartado de Sign Up
    signUp_button = driver.find_element(By.CLASS_NAME, 'button')
    signUp_button.click()
    time.sleep(5)


    # Acceptar las reglas
    accept_button = driver.find_element(By.CLASS_NAME, 'button')
    accept_button.click()

    # Esperar a que carge el formulario
    name_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user_account_attributes_username')))

    # Ingresar datos
    email_field = driver.find_element(By.ID, 'user_email')
    password_field = driver.find_element(By.ID, 'user_password')
    passwordConf_field = driver.find_element(By.ID, 'user_password_confirmation')
    verification_box = driver.find_element(By.ID, 'user_agreement')
    singUp_button = driver.find_element(By.CLASS_NAME, 'btn')

    name_field.send_keys (Usuario)
    time.sleep(3)
    email_field.send_keys(Mail)
    time.sleep(3)
    password_field.send_keys(password)
    time.sleep(3)
    passwordConf_field.send_keys(password)
    time.sleep(3)
    verification_box.send_keys(Keys.SPACE)
    singUp_button.click()
    time.sleep(5) 

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU1 succes evi1.png'
    driver.save_screenshot(screenshot_path1)
    
    WebDriverWait(driver, 70).until(
    EC.title_is(('Home - Mastodon')))

    screenshot_path2 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU1 succes evi3.png'
    driver.save_screenshot(screenshot_path2)
# Ejecutar la prueba
test_registro_usuario()

# Cerrar el navegador
driver.quit()
