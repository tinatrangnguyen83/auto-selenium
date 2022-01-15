# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
# dri.find_elements('input').send_keys("javatpoint") ;
# dri.find_elements('input').send_keys(Keys.ENTER)
element = driver.find_element(By.NAME, "q")
element.send_keys("typing")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
