from selenium import webdriver
# from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path= r'/usr/local/share/chromedriver_linux64/chromedriver')
driver.get('http://www.nba.com/players/')
html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')


print(soup.prettify())

# print(html)

driver.quit()
