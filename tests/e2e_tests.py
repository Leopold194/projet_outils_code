import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_and_create_task():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://localhost:3000/login")

        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        email_input.send_keys("admin@test.com")
        password_input.send_keys("password")
        password_input.send_keys(Keys.RETURN)

        time.sleep(2)

        driver.get("http://localhost:3000/dashboard")
        
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Nouvelle Tâche']")))
        button.click()
        
        title_input = driver.find_element(By.ID, "title")
        description_input = driver.find_element(By.ID, "description")
        submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Créer']")

        title_input.send_keys("Nouvelle tâche E2E")
        description_input.send_keys("Créée via un test end-to-end Selenium")
        submit_button.click()

        time.sleep(2)

        driver.get("http://localhost:3000/dashboard")

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Nouvelle tâche E2E')]")))

    finally:
        driver.quit()
