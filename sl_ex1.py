from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sauceclient import SauceClient
from threading import Thread

'''
desired_cap = {
        'platform': "Mac OS X 10.9",
        'browserName': "chrome",
        'version': "31",
}
desired_cap1 = {
        'platform': "Windows",
        'browserName': "Internet Explorer",
        'version': "10",
}
'''
def start_Browser_SL(os,browser,version):
    desired_cap = {
        'platform': os,
        'browserName': browser,
        'version': version,
    }   

    driver = webdriver.Remote(
        command_executor='http://shivashankarr1:2aa6bacd-689b-47c6-bb80-1c59e30fd785@ondemand.saucelabs.com:80/wd/hub', desired_capabilities=desired_cap)

    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    if not "Google" in driver.title:
     raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("Sauce Labs")
    elem.submit()
    # This is where you tell Sauce Labs to stop running tests on your behalf. 
    # It's important so that you aren't billed after your test finishes.
    driver.quit()

t1 = Thread(target=start_Browser_SL,args=["Windows 8","Internet Explorer","10"])
t1.start()
t2 = Thread(target=start_Browser_SL,args=["Windows 2003","Internet Explorer","8"])
t2.start()
t3 = Thread(target=start_Browser_SL,args=["Linux","Firefox","40"])
t3.start()

t1.join()
t2.join()
t3.join()
