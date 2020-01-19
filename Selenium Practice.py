from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Chrome Driver\chromedriver.exe")

print(driver.current_url)

if "data" in driver.current_url:
    print(True)
