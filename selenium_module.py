"""
It is an open source automated testing suite for web applications across
different browsers and platforms. It is not a single tool but a suite of
software. We have selenium bindings for Python, Java, C#, Ruby and JavaScript.
Selenium Python bindings provide a convenient API to access Selenium Web-
Drivers like Firefox, IE, Chrome, Remote etc.
"""
from selenium import webdriver
path = r'C:\\Users\\butterfly\\Downloads\\Chromedriver'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://authoraditiagarwal.com/leadershipmanagement')
#browser.find_element_by_xpath('/html/body/chromedriver_linux64.zip').click()
