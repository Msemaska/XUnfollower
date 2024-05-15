import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"--user-data-dir=C:\Users\marty\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"--profile-directory=Profile 4")

# Set up Chromedriver path
chromedriver_path = r"C:\Users\marty\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Initialize the Chrome browser
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Define the base website
base_website = "https://twitter.com/HexdMedia/following"

# Function to perform random mouse movements
def perform_random_mouse_movements():
    actions = ActionChains(driver)
    for _ in range(random.randint(5, 10)):
        x_offset = random.randint(-50, 50)
        y_offset = random.randint(-50, 50)
        actions.move_by_offset(x_offset, y_offset)
        actions.perform()
        time.sleep(0.5)

# Function to find and click buttons with "Following" span
def click_following_buttons():
    following_buttons = driver.find_elements(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/button[./div/div[2]/div[1]/div[2]/button/span[text()='Following']]")
    for button in following_buttons:
        # Scroll to the button
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        # Perform random mouse movements
        perform_random_mouse_movements()
        # Click the button
        button.click()
        time.sleep(random.uniform(0.5, 1))
        # Click the confirmation button
        confirmation_button = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]")
        confirmation_button.click()
        time.sleep(random.uniform(0.5, 1))

# Function to scroll down a full screen height
def scroll_down():
    driver.execute_script("window.scrollTo(0, window.scrollY + window.innerHeight);")
    time.sleep(2)

# Main script
driver.get(base_website)
time.sleep(2)

while True:
    click_following_buttons()
    scroll_down()
