from selenium import webdriver
from selenium.webdriver.common.by import By
PATH = "C:\Andy\Chromedriver\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('http://flashbynight.com/drench/')
browser.save_screenshot("screenshot.png")

def get_moves(browser):
    webElement = browser.find_element_class_name("moveNum");
    return int(webElement.text);

def click_button(browser, color):
    browser.find_element_by_id(color).click();

click_button(browser)