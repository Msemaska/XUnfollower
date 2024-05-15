import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
user_data_path = r'C:\Users\marty\AppData\Local\Google\Chrome\User Data'
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_path}")
chrome_options.add_argument("profile-directory=Default")

# Setup WebDriver
driver_path = r'C:\Users\marty\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the site
driver.get('https://twitter.com/HexdMedia/following')

try:
    while True:
        # Wait for the buttons to be clickable and interactable
        following_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/button/div/div[2]/div[1]/div[2]/button//span[contains(text(), 'Following')]"))
        )

        if not following_buttons:
            print("No 'Following' buttons found, ending script.")
            break

        for button in following_buttons:
            print("Attempting to click 'Following' button")
            try:
                # Random delay before clicking the 'Following' button
                time_before_click = random.randint(1, 7)
                print(f"Waiting for {time_before_click} seconds before clicking.")
                time.sleep(time_before_click)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button)).click()
                time.sleep(1)  # Fixed short wait for the popup to appear

                # Handle the confirmation popup
                print("Attempting to confirm unfollow")
                time_before_confirm = random.randint(1, 3)
                print(f"Waiting for {time_before_confirm} seconds before confirming.")
                time.sleep(time_before_confirm)

                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]"))
                )
                confirm_button.click()
                time.sleep(1)  # Fixed short wait for the action to be processed

            except Exception as click_ex:
                print(f"Failed to click due to: {click_ex}")
                continue  # Skip this iteration and try the next button

        # Scroll down to load more buttons
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
