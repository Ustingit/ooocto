def func(x):
    return x + 1


def test_answer():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    #'https://developer.mobileconnect.io/'
    driver = webdriver.Chrome('./resources/webdrivers/chromedriver.exe')
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

    assert func(3) == 4
