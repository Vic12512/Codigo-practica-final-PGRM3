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

def test_de_actualizacion_de_perfil(nom, bio, foto):

    # Abrir preferencias
    preferencias = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/settings/preferences']"))
    )
    preferencias.click()

    # Abrir editor de perfil
    perfil = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//li[@id='profile']/a[@href='/settings/profile']"))
    )
    perfil.click()

    # Buscar los campos a editar
    nombre = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "account_display_name"))
    )
    biografia = driver.find_element(By.ID, "account_note")
    foto_de_perfil = driver.find_element(By.ID, "account_avatar")
    guardar_boton = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Llenar los campos
    nombre.send_keys(nom)
    biografia.send_keys(bio)
    foto_de_perfil.send_keys(foto)
    guardar_boton.click()
    time.sleep(7)

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU4 succes evi.png'
    driver.save_screenshot(screenshot_path1)

    # Cerrar el navegador
    driver.quit()


# Ejecutar la prueba
n = 'Perro Salchicha'
b = 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,'
f = 'C:/Users/Titiri Mundati/Desktop/6to Cuatrimestre/Programación 3/Proyecto final/fotos/imagenes.PNG'
test_login_usuario(driver, name, passw)
test_de_actualizacion_de_perfil(n, b, f)
