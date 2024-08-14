from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import test_login_usuario
import time
import os

name = 'manoloPGRM@gmail.com'
passw = 'anitalahuerfanita'
driver = webdriver.Chrome()

def test_de_cambio_de_tema(tema):

    # Abrir preferencias
    preferencias = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/settings/preferences']"))
    )
    preferencias.click()

    # Abrir selector de temas
    selector = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "user_settings_attributes_theme"))
    )
    selector.click()

    #seleccionar el tema
    options = selector.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.get_attribute('value') == tema:
            option.click()
            break

    # Guardar cambios
    guardar_boton = driver.find_element(By.XPATH, "//button[@type='submit']")
    guardar_boton.click()

    # Tomar captura
    time.sleep(3)
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU10 succes evi.png'
    driver.save_screenshot(screenshot_path1)

    # Cerrar el navegador
    driver.quit()


# Ejecutar la prueba
theme= "default"
test_login_usuario(driver, name, passw)
test_de_cambio_de_tema(theme)