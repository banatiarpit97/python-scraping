from selenium import webdriver
driver = webdriver.Chrome(executable_path= r'/usr/local/share/chromedriver_linux64/chromedriver')
driver.get('http://python.org')
html = driver.page_source

print(html)

driver.quit()
