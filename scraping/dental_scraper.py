from operator import ge
from selenium import webdriver
import re




def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i
        result += decodedNumber
    return result

# 실습2
# AIA 생명 치아보험 견적 페이지에서 보장 내역과 보험료을 가져와서 출력을한다


def getAIAData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(
        'https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    if gender == 0:
        # 남자를 클릭하라
        man = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        man.click()

    else:
        # 여자 버튼을 클릭하라
        woman = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        woman.click()


    birthInput = driver.find_element_by_xpath('//*[@id="aia644363719"]')
    birthInput.send_keys(birth)

    calculate = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    calculate.click()

    driver.implicitly_wait(1)

    price = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]')
    print(f'{name}님의 AIA 보험료는 {price.text} 입니다.')


def getLinaData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(
        'https://direct.lina.co.kr/product/ess/dtc01/easy')
    if gender == 0:
        # 남자를 클릭하라
        man = driver.find_element_by_xpath('//*[@id="main_btn_male"]')
        man.click()

    else:
        # 여자 버튼을 클릭하라
        woman = driver.find_element_by_xpath('//*[@id="main_btn_female"]')
        woman.click()


    birthInput = driver.find_element_by_xpath('//*[@id="birthday"]')
    birthInput.send_keys(birth[2:])

    calculate = driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]')
    calculate.click()

    driver.implicitly_wait(1)

    price = driver.find_element_by_xpath('//*[@id="mo_amount_span"]')
    print(f'{name}님의 라이나생명 보험료는 {price.text}원 입니다.')



getAIAData("강수현", "19980123", 1)
getLinaData("강수현", "19980123", 1)