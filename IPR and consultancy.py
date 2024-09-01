from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.vardhaman.org")
driver.maximize_window()

try:
    ipr=driver.find_element(By.LINK_TEXT,"IPR & CONSULTANCY")
    ipr.click()
    driver.implicitly_wait(5)
    cse=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/header/nav/ul/li[5]/ul/li[2]/a/span")
    cse.click()
    tit=driver.title
    print(tit)
    if tit=="Consultancy – Vardhaman":
        print("Yes")
    else:
        print("No")
except Exception as e:
    print(f" an error occured:{e}")
