from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

# Navigatinh to the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
sleep(2)

# Entering the Details(username & password)
username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username_input.send_keys("asahoo264200@gmail.com")
sleep(2)

# Finding the user
password_input = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password_input.send_keys("test_account")
sleep(2)



login_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
login_box.click()

not_now = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
not_now.click()

not_now1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
not_now1.click()

search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div').click()

sleep(2)
search_user = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
search_user.send_keys("unk264_os")

sleep(2)
user_found = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[1]/div/div/object/a')
user_found.click()

sleep(2)
user_msg = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div')
user_msg.click()

# Sending the automated message
sleep(6)
msg = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
msg.send_keys("Automated Message using Selenium")
sleep(3)
msg.send_keys(Keys.ENTER)
sleep(10)
print("Automation closed")
