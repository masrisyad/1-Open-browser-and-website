from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get('http://rebrand.ly/masrisyad')
