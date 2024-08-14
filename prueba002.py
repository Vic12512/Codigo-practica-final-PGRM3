from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Función para iniciar sesion
def test_login_usuario (driver, usern, passw):

    # URL del sitio web
    driver.get('https://mastodon.social/explore')

    # Ingresar al apartado de Sign Up
    login_button = driver.find_element(By.CLASS_NAME, 'button-tertiary')
    login_button.click()

    # Esperar a que carge el formulario
    email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user_email')))

    # Ingresar datos
    password_field = driver.find_element(By.ID, 'user_password')
    singUp_button = driver.find_element(By.CLASS_NAME, 'btn')

    email_field.send_keys(usern)
    password_field.send_keys(passw)
    singUp_button.click()
        
    WebDriverWait(driver, 20).until(
    EC.title_is(('Home - Mastodon')))
    time.sleep(5)

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU2 succes evi.png'
    driver.save_screenshot(screenshot_path1)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    Mail = 'manuel_pgrm@hotmail.com'
    password = 'Anitalahuerfanita'
    test_login_usuario(driver, Mail, password)
    driver.quit()