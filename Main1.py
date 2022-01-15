from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("file:///C:/Users/vanng/PycharmProjects/LearnPythonSelenium/n.html")

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

#assert len(driver.window_handles) == 1

# Click the link which opens in a new window
# driver.find_element(By.LINK_TEXT, "new window").click()
element = driver.find_element(By.ID, "clickme")


    .click()
# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Wait for the new tab to finish loading content
wait.until(EC.title_is("SeleniumHQ Browser Automation"))