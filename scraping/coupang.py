from selenium import webdriver

# 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩
driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.coupang.com/np/categories/176522')

button = driver.find_element_by_xpath('//*[@id="5726960662"]/a/dl/dt/img')
button.click()