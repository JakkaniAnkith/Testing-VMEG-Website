from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.vardhaman.org")
driver.maximize_window()

try:
    research=driver.find_element(By.LINK_TEXT,"RESEARCH")
    research.click()
    driver.implicitly_wait(5)
    obj=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/header/nav/ul/li[4]/ul/li[1]/a/span/span")
    obj.click()
    tit=driver.title
    if tit =="Research Objectives – Vardhaman":
        print("Yes")
    else:
        print("No")
    print(tit)
except Exception as e:
    print(f"an error occured:{e}")
