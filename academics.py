from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open the website
website_url = "https://www.vardhaman.org"
driver.get(website_url)
driver.maximize_window()

try:
    aca = driver.find_element(By.LINK_TEXT,"ACADEMICS")
    aca.click()
    tit = driver.title
    print(tit)
    if tit=="Academics – Vardhaman":
        print("Yes")
    else:
        print("No")

except Exception as e:
    print(f"an error occured: {e}")
