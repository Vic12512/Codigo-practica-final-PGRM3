from selenium import webdriver
from login import test_login_usuario
import time
import os

name = 'manoloPGRM@gmail.com'
passw = 'anitalahuerfanita'
driver = webdriver.Chrome()

def test_ver_publicaciones():
    driver.set_window_size(1366, 768)
    time.sleep(2)

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU8 succes evi.png'
    driver.save_screenshot(screenshot_path1)

    # Cerrar el navegador
    driver.quit()


# Ejecutar la prueba
post = ' Soy Manolo'
test_login_usuario(driver, name, passw)
test_ver_publicaciones()