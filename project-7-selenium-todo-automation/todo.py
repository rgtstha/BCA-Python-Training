from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains
import time


try:
    driver = webdriver.Chrome()
    driver.get("https://example.cypress.io/todo#/completed")
    time.sleep(1)
    
    todo = driver.find_element(By.CLASS_NAME,"new-todo")
    todos = ["Learn python", "Create a project", "Master the python full stack"]
    for todo in todos:
        ActionChains(driver).send_keys(todo).perform()
        time.sleep(1)
        ActionChains(driver).key_down(Keys.ENTER).perform()
        time.sleep(1)
         
    time.sleep(1)
    
    all_link = driver.find_element(By.XPATH, '//a[text()="All"]')
    all_link.click()
    time.sleep(1)
    
    destroy_buttons = driver.find_elements(By.CLASS_NAME, "toggle")
    third_destroy_button = destroy_buttons[2]
    third_destroy_button.click()
    time.sleep(1)
    
    fourth_destroy_button = destroy_buttons[3]
    fourth_destroy_button.click()
    time.sleep(1)
    
    five_destroy_button = destroy_buttons[4]
    five_destroy_button.click()
    time.sleep(1)
      
    
    clear_completed_button = driver.find_element(By.CLASS_NAME, "clear-completed")
    clear_completed_button.click()
    time.sleep(1)

    
except Exception as e:
    print(e)
    
finally:
    driver.quit()
    
    
    
