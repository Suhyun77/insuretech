from selenium import webdriver

# 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩
driver = webdriver.Chrome('./chromedriver')

driver.get('https://kr.leagueoflegends.com/ko-kr/')
loginButton = driver.find_element_by_xpath('//*[@id="riotbar-right-content"]/div[3]/div[1]/a')
loginButton.click()

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys('test')
password.send_keys('test')