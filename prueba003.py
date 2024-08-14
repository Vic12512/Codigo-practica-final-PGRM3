from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import test_login_usuario
import time
import os


driver = webdriver.Chrome()
name = 'manoloPGRM@gmail.com'
passw = 'anitalahuerfanita'

# Función para iniciar sesion
def test_mantener_sesion_iniciada():

    # Abrir nueva pestaña
    driver.execute_script("window.open('https://www.google.com/search?q=mastodon&rlz=1C1ALOY_esHT1037DO1037&oq=mastodon&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGIAEGIoFMgcIARAuGIAEMgwIAhAAGEMYgAQYigUyBwgDEC4YgAQyBwgEEAAYgAQyBwgFEC4YgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQgyNTI4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8', '_blank');")

    driver.close()
    # Cambiar pestaña
    driver.switch_to.window(driver.window_handles[-1])
   
    # Espera hasta que el enlace "Mastodon: Explore" esté presente en la página
    mastodon_link = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='https://mastodon.social/']//h3[contains(text(), 'Mastodon: Explore')]"))
    )

    # Hacer clic en el enlace
    mastodon_link.click()
    WebDriverWait(driver, 10).until(
    EC.title_is(('Home - Mastodon')))

    # Tomar captura
    screenshot_path1 = 'C:/Users/Titiri Mundati/Desktop/evidencias/HU3 succes evi.png'
    driver.save_screenshot(screenshot_path1)
    
    # Cerrar el navegador
    driver.quit()

# Ejecutar la prueba & Iniciamos sesion
test_login_usuario(driver, name, passw)
test_mantener_sesion_iniciada()

