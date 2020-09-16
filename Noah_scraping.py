from selenium import webdriver

import time


driver = webdriver.Chrome('/mnt/c/users/ashwi/chromedriver.exe')


driver.get("http://casesearch.courts.state.md.us/casesearch/inquiry-index.jsp")

time.sleep(1)

driver.find_element_by_name("disclaimer").click()
driver.find_element_by_name("action").click()

time.sleep(1)

driver.find_element_by_name("lastName").send_keys("Rueger")
driver.find_element_by_name("firstName").send_keys("T")
driver.find_element_by_name("action").click()

time.sleep(1)


driver.find_element_by_xpath( ".//*[contains(text(), '0D00354417')]").click()

time.sleep(1)
des = driver.find_elements_by_xpath( ".//*[contains(text(), 'Description:')]")
for el in des:
    #print(/following-sibling::span)
    print(el.find_element_by_xpath( "following-sibling::span").text)

dis = driver.find_elements_by_xpath( ".//*[contains(text(), 'Disposition:')]")
#print(dis)
for el in dis:
    #print(/following-sibling::span)
    if el.text == "Disposition:":
        print(el.find_element_by_xpath( "//following-sibling::tr[1]").text)

#des2 = driver.find_element_by_xpath( ".//*[contains(text(), 'Description:')]/following-sibling::span/following-sibling::span/following-sibling::span").text

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     print(elem.get_attribute("href"))



#driver.quit()
