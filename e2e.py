# test url with selenium
# url = http://0.0.0.0:8777/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def test_scores_service():

    drive = webdriver.Chrome(executable_path="/home/boss/Downloads/drivers/chromedriver")
    url = input('Please ENTER url: http://0.0.0.0:8777/')
    drive.get(url)
    print(drive.title)
    element = int(drive.find_element_by_id("score").text)
    print(element)
    drive.quit()
    return element <= 1000

def main_function():
    try:
        if test_scores_service():
            return 0
        else:
            return -1
    except:
        print("Try again")

main_function()
