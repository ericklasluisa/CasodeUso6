import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la seccion vehiculo')
def entrar_seccion_vehiculo(context):
    try:
        context.driver.maximize_window()
        context.driver.get("C:\\Users\\erick\\Desktop\\ESPE\\QUINTO SEMESTRE\\REQUISITOS\\PRUEBAS-RF\\Vehiculo\\Vehiculo\\Vehiculo.html")
        take_screenshot(context, '1. Entra a la seccion vehiculo')
        print("Entered 'Vehiculo' section")
    except Exception as e:
        mark_step_as_failed(context, 'entra_seccion_vehiculo', e)

@when('Aplasta el botón editar')
def aplastar_boton_editar(context):
    try:
        editar_button = context.driver.find_element(By.XPATH, '//*[@id="editar-0"]')
        editar_button.click()
        take_screenshot(context, '2. Clickar el boton editar')
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_boton_editar', e)

@when('Actualizar el campo Marca {marca}')
def actualizar_marca(context, marca):
    try:
        marca_field = context.driver.find_element(By.XPATH, '//*[@id="editMarca"]')
        marca_field.clear()
        marca_field.send_keys(marca)
        take_screenshot(context, '3. Actualizar el campo Marca')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_marca', e)

@when('Actualizar el campo Modelo {modelo}')
def actualizar_modelo(context, modelo):
    try:
        modelo_field = context.driver.find_element(By.XPATH, '//*[@id="editModelo"]')
        modelo_field.clear()
        modelo_field.send_keys(modelo)
        take_screenshot(context, '4. Actualizar el campo Modelo')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_modelo', e)

@when('Actualizar el campo Kilometraje {kilometraje}')
def actualizar_kilometraje(context, kilometraje):
    try:
        kilometraje_field = context.driver.find_element(By.XPATH, '//*[@id="editKilometraje"]')
        kilometraje_field.clear()
        kilometraje_field.send_keys(kilometraje)
        take_screenshot(context, '7. Actualizar el campo Kilometraje')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_kilometraje', e)

@when('Seleccionar el tipo de combustible {combustible}')
def seleccionar_combustible(context, combustible):
    try:
        combustible_dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="editCombustible"]'))
        combustible_dropdown.select_by_visible_text(combustible)
        take_screenshot(context, '8. Seleccionar el tipo de combustible')
    except Exception as e:
        mark_step_as_failed(context, 'seleccionar_combustible', e)

@when('Actualizar el campo Peso {peso}')
def actualizar_peso(context, peso):
    try:
        peso_field = context.driver.find_element(By.XPATH, '//*[@id="editPeso"]')
        peso_field.clear()
        peso_field.send_keys(peso)
        take_screenshot(context, '9. Actualizar el campo Peso')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_peso', e)

@then('Aplastar el boton para editar')
def aplastar_editar_vehiculo(context):
    try:
        guardar_button = context.driver.find_element(By.XPATH, '//*[@id="editVehiculoForm"]/button')
        time.sleep(1)
        guardar_button.click()
        time.sleep(1)
        take_screenshot(context, '11. Aplastar el boton para editar')
        print("Vehicle edited")
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_guardar_vehiculo', e)

@then('Visualizar alerta confirmacion')
def verificarMensaje(context):
    try:
        # Esperar a que el modal de confirmación aparezca
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div'))
        )
        confirmation_message = context.driver.find_element(By.XPATH, '/html/body/div[8]/div')
        # Si el elemento se encuentra, el paso es exitoso
        time.sleep(1)
        take_screenshot(context, '5. Observar el mensaje de confirmacion')
        mark_step_as_passed(context, 'verificar_mensaje')
    except Exception as e:
        # Si ocurre una excepción, el paso falla
        mark_step_as_failed(context, 'verificar_mensaje', e)
