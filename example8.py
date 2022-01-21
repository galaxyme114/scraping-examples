from selenium import webdriver
path = r'C:\\Users\\butterfly\\Downloads\\Chromedriver'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://tutorialspoint.com/')
screenshot = browser.save_screenshot('screenshot.png')
browser.quit