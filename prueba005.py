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

def test_publicaciones(postContent):

    # Click al boton de new post
    nuevo_post_boton = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='ui__header__links']/a[@href='/publish']"))
    )
    nuevo_post_boton.click()

    # Buscar elementos de pagina de post
    contenido_del_post = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "autosuggest-textarea__textarea"))
    )
    postear_boton = driver.find_element(By.XPATH, "//button[@type='submit']")

    #Escribir y enviar post
    contenido_del_post.send_keys(postContent)
    postear_boton.click()
    time.sleep(5)

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU5 succes evi.png'
    driver.save_screenshot(screenshot_path1)

    # Cerrar el navegador
    driver.quit()


# Ejecutar la prueba
post = 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,'
test_login_usuario(driver, name, passw)
test_publicaciones(post)
