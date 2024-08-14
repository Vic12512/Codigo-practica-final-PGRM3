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

def test_editar_publicaciones(postContent):
    driver.set_window_size(1366, 768)
    
   # Click al post
    post = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/@manoloPGRM/112959960835879159']"))
    )
    post.click()   

    # Desplegar menu
    menu = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//button[@title='More']"))
    )
    menu.click()

    # Leer menu
    lista = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "dropdown-menu__item"))
    )

    # Seleccionar editar
    editar = lista[5].find_element(By.XPATH, "//a[@data-index = '8']")
    editar.click()
    time.sleep(3)

    # Esperar carga del area texto de post
    area_de_texto = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "autosuggest-textarea__textarea"))
    )
    actualizar_boton = driver.find_element(By.XPATH, "//button[@type='submit']")

    #editar post
    area_de_texto.send_keys(postContent)
    time.sleep(3)

    #Actualizar post
    actualizar_boton.click()
    time.sleep(3)

    # Boton de volver
    volver_boton = driver.find_element(By.XPATH, "//div[@class='navigation-panel']/a[@title='Home']")
    volver_boton.click()
    time.sleep(10)

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU6 succes evi.png'
    driver.save_screenshot(screenshot_path1)

    # Cerrar el navegador
    driver.quit()


# Ejecutar la prueba
post = ' Soy Manolo'
test_login_usuario(driver, name, passw)
test_editar_publicaciones(post)