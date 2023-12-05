from SeleniumLibrary.keywords import element
from selenium import webdriver
from selenium.webdriver.chrome.service import service
import pytest
from selenium.webdriver.common.by import By

driver = None


@pytest.fixture(scope='module')
def init_browser():
    global driver
    driver = webdriver.Edge(executable_path=r"D:\Selenium drivers\msedgedriver.exe")
    driver.maximize_window()


def test_launch_url(init_browser):
    driver.get("http://webdriveruniversity.com/index.html")
    print("driver")

def test_teardown(init_browser):
    driver.quit()
    print("close driver")

def test_pageLocators(init_browser):

    #Clicking on dropdown link
    driver.find_element(By.XPATH, "//a[@id='dropdown-checkboxes-radiobuttons']").click()

    #Selecting drop down
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH,'//select[@id="dropdowm-menu-1"]').click()
    driver.find_element(By.XPATH, '//select[@id="dropdowm-menu-1"]//option[@value="sql"]').click()
    text = driver.find_element(By.XPATH,'//select[@id="dropdowm-menu-1"]').text
    print("Dropdown text ",text)

    elements = driver.find_elements_by_xpath('//div[@id="checkboxes"]//input')
    elements[0].click()
    driver.find_elements_by_xpath('//div[@id="checkboxes"]//input')[2].click()

    checkedbox_count = len(driver.find_elements_by_xpath('//div[@id="checkboxes"]//input[@checked]'))
    print(checkedbox_count)
    assert checkedbox_count == 1

    #selecting radio button
    driver.find_element(By.XPATH, '//form[@id="radio-buttons"]//input[@value="yellow"]').click()


