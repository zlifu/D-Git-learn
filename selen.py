from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.page_source)