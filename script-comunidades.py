from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#abrir chrome
driver = webdriver.Chrome()

#abrir dspace
driver.get('https://demo.dspace.org/home')

#click en boton iniciar sesion
driver.find_element(By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/div/ds-themed-header-navbar-wrapper/ds-header-navbar-wrapper/div/ds-themed-header/ds-header/header/nav/div[2]/ds-themed-auth-nav-menu/ds-auth-nav-menu/ul/li/a').click()

#poner correo
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/ds-themed-login-page/ds-login-page/div/div/div/ds-themed-log-in/ds-log-in/div/ds-log-in-container[1]/ds-log-in-password/form/input[1]').send_keys('dspacedemo+admin@gmail.com')

#poner contraseña
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/ds-themed-login-page/ds-login-page/div/div/div/ds-themed-log-in/ds-log-in/div/ds-log-in-container[1]/ds-log-in-password/form/input[2]').send_keys('dspace')

#iniciar sesion
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/ds-themed-login-page/ds-login-page/div/div/div/ds-themed-log-in/ds-log-in/div/ds-log-in-container[1]/ds-log-in-password/form/button').click()

#agregar nuevo
driver.find_element(By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/ds-themed-admin-sidebar/ds-admin-sidebar/nav/div[1]/ul/li[2]/ds-expandable-admin-sidebar-section/div/div').click()

#nueva comunidad
driver.find_element(By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/ds-themed-admin-sidebar/ds-admin-sidebar/nav/div[1]/ul/li[2]/ds-expandable-admin-sidebar-section/div/div/div[2]/ul/li[1]/ds-onclick-menu-item/a').click()

#buscar comunidad
driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/ds-themed-create-community-parent-selector/ds-create-community-parent-selector/div/div[2]/ds-dso-selector/div[1]/input').send_keys('comunidad 1')

#click en nuestra comunidad
driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/ds-themed-create-community-parent-selector/ds-create-community-parent-selector/div/div[2]/ds-dso-selector/div[3]/div/button[1]').click()

#poner nombre
driver.find_element(By.XPATH, '//*[@id="title"]').send_keys('Subcomunidad 2')

#guardar
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/ds-create-community/div/ds-community-form/ds-form/div/form/div/div/div/button[2]').click()

df = pd.read_csv('prueba.csv')
#df

#ciclo para ingresar todos los datos
for row, datos in df.iterrows():
    clave = datos['CLAVE']
    nombre = datos['NOMBRE']
    
    #nueva comunidad
    driver.find_element(By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/ds-themed-admin-sidebar/ds-admin-sidebar/nav/div[1]/ul/li[2]/ds-expandable-admin-sidebar-section/div/div/div[2]/ul/li[1]/ds-onclick-menu-item/a').click()
    time.sleep(2)
    
    #buscar comunidad
    driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/ds-themed-create-community-parent-selector/ds-create-community-parent-selector/div/div[2]/ds-dso-selector/div[1]/input').send_keys('comunidad 1')
    time.sleep(2)
    
    #click en nuestra comunidad
    driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/ds-themed-create-community-parent-selector/ds-create-community-parent-selector/div/div[2]/ds-dso-selector/div[3]/div/button[1]').click()
    time.sleep(3)
    
    #poner nombre a nuestra subcomnunidad
    driver.find_element(By.XPATH, '//*[@id="title"]').send_keys(nombre)
    time.sleep(2)
    
    #guardar
    driver.find_element(By.XPATH, '//*[@id="main-content"]/div/ds-create-community/div/ds-community-form/ds-form/div/form/div/div/div/button[2]').click()
    time.sleep(15)