from selenium import webdriver
# SELECT 엘리먼트를 위한 라이브러리 로드
from selenium.webdriver.support.ui import Select

# work1 : 전라남도 고흥군 고흥읍 남계리 본번 45 부번 1 지역에 공시지가를 출력하세요

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.eum.go.kr/web/am/amMain.jsp")

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="selSido"]'))
sidoSelect.select_by_visible_text('전라남도')

driver.implicitly_wait(1)

SggSelect = Select(driver.find_element_by_xpath('//*[@id="selSgg"]'))
SggSelect.select_by_visible_text('고흥군')

driver.implicitly_wait(1)

UmdSelect = Select(driver.find_element_by_xpath('//*[@id="selUmd"]'))
UmdSelect.select_by_visible_text('고흥읍')

driver.implicitly_wait(1)

RiSelect = Select(driver.find_element_by_xpath('//*[@id="selRi"]'))
RiSelect.select_by_visible_text('남계리')

driver.implicitly_wait(1)

bonbun = driver.find_element_by_xpath('//*[@id="bobn"]')
bonbun.send_keys('45')

driver.implicitly_wait(1)

bonbun = driver.find_element_by_xpath('//*[@id="bubn"]')
bonbun.send_keys('1')

driver.implicitly_wait(1)


searchButton = driver.find_element_by_xpath('//*[@id="frm"]/fieldset/div[3]/p/span/a')
searchButton.click()

driver.implicitly_wait(1)


location = driver.find_element_by_xpath('//*[@id="appoint"]/div[2]/table/tbody/tr[1]/td')
name = driver.find_element_by_xpath('//*[@id="appoint"]/div[2]/table/tbody/tr[3]/th')
gongsi = driver.find_element_by_xpath('//*[@id="appoint"]/div[2]/table/tbody/tr[3]/td')
gongsi = gongsi.text.split('(')[0]

print(f'{location.text}의 {name.text}는 {gongsi}입니다.')