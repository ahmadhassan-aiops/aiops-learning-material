from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path=Service(r"C:\Users\PMLS\PycharmProjects\pythonProject1\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.imdb.com/")
