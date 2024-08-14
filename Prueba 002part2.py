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

Mail = 'manuel_pgrm@hotmail.com'
password = 'PizzaFamiliar'

# Función para iniciar sesion
def test_login_usuario_fallido():

   # Ingresar al apartado de Sign Up
    login_button = driver.find_element(By.CLASS_NAME, 'button-tertiary')
    login_button.click()

    # Esperar a que carge el formulario
    email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user_email')))

    # Ingresar datos
    password_field = driver.find_element(By.ID, 'user_password')
    singUp_button = driver.find_element(By.CLASS_NAME, 'btn')

    email_field.send_keys(Mail)
    password_field.send_keys(password)
    singUp_button.click()
    time.sleep(7)

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU2 fail evi.png'
    driver.save_screenshot(screenshot_path1)


# Ejecutar la prueba
test_login_usuario_fallido()

# Cerrar el navegador
driver.quit()