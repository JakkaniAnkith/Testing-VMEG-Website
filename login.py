from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Open the website
website_url = "https://www.vardhaman.org"
driver.get(website_url)
driver.maximize_window()

try:
    login = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div/span/span")
    login.click()
    driver.implicitly_wait(5)
    Fac_Profile = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/ul/li[4]/a/span/span")
    Fac_Profile.click()
    print(driver.title)
    exp_tit = driver.title
    if exp_tit == 'VCE':
        print("Yes")
    else:
        print("No")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
