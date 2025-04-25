from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://mms.baa.at/")

input("Bitte logge dich manuell ein und öffne eine Übung. Drücke dann Enter...")

try:
    # Warten, bis der Text sichtbar ist
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ex_displ .content-display"))
    )
    text_element = driver.find_element(By.CSS_SELECTOR, ".ex_displ .content-display")
    text_to_type = text_element.text
    print("Text zum Tippen:", text_to_type)

    # Eingabefeld holen und sicher fokussieren
    input_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ex_write .content-display"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(input_field).click().perform()

    time.sleep(1)  # kurze Wartezeit zur Sicherheit

    # Tipp-Schleife mit echter Tasteneingabe
    for index, char in enumerate(text_to_type):
        try:
            input_field.send_keys(char)
            print(f"[{index}] Getippt: '{char}'")
            time.sleep(0.8)
        except Exception as char_error:
            print(f"Fehler beim Tippen von '{char}':", char_error)

    print("Fertig getippt!")
    input("Drücke Enter, wenn du speichern willst...")

except Exception as e:
    print("Fehler beim Ausführen:", e)
