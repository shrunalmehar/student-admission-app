from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Open website
driver.get("https://shrunalmehar.github.io/student-admission-app/")

time.sleep(3)  # wait before starting

# Fill Name
driver.find_element(By.ID, "name").send_keys("Shrunal Mehar")
time.sleep(2)

# Fill Email
driver.find_element(By.ID, "email").send_keys("test@gmail.com")
time.sleep(2)

# Fill Password
driver.find_element(By.ID, "password").send_keys("123456")
time.sleep(2)

# Wait before submit (TAKE SCREENSHOT HERE 📸)
time.sleep(4)

# Click submit
driver.find_element(By.ID, "submitBtn").click()

# Wait after submit (TAKE SCREENSHOT HERE 📸)
time.sleep(5)

# Close browser
driver.quit()