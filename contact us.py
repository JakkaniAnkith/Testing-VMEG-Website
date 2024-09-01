from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.vardhaman.org")
driver.maximize_window()

try:
    cu = driver.find_element(By.LINK_TEXT,"CONTACT US")
    cu.click()
    tit=driver.title
    print(tit)
    if tit=="Contact Us – Vardhaman":
        print("Yes")
    else:
        print("No")
except Exception as e:
    print(f"an error occured:{e}")

