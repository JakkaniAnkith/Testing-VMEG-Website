from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.vardhaman.org")
driver.maximize_window()

try:
    inc = driver.find_element(By.LINK_TEXT,"INCUBATION")
    inc.click()
    driver.implicitly_wait(5)
    entr = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/header/nav/ul/li[7]/ul/li[1]/a/span/span")
    entr.click()
    tit = driver.title
    print(tit)
    if tit == "Centre for Innovation and Entrepreneurship – Vardhaman":
        print("Yes")
    else:
        print("No")
except Exception as e:
    print(f"an error occured:{e}")
