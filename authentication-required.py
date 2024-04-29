from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

instagram_id = os.environ.get('INSTAGRAM_ID')
instagram_pw = os.environ.get('INSTAGRAM_PW')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
login_url = "https://www.instagram.com/"
driver.get(login_url)

instagram_id_form = driver.find_element(By.TAG_NAME, "input")
instagram_id_form.send_keys(instagram_id)
time.sleep(1)

instagram_pw_form = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
instagram_pw_form.send_keys(instagram_pw)
time.sleep(1)

login_ok_button = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
login_ok_button.click()
time.sleep(5)
print("instagram login success")

feed_url = "https://www.instagram.com/p/C3ojsG1y2hJ"
driver.get(feed_url)
time.sleep(3)

html1 = driver.page_source

soup = BeautifulSoup(html1, 'html.parser')
span_tag = soup.find('span', class_='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')

print(span_tag.text.strip())
