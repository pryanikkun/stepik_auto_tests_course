from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.TAG_NAME, "img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    oprion1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    oprion1.click()
    oprion2 = browser.find_element(By.CSS_SELECTOR,"[id='robotCheckbox']")
    oprion2.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(10)
    
finally:
    time.sleep(10)
    browser.quit()

