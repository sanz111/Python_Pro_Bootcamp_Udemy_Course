from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "/Users/dongwei/JoeyDong/development_files/ChromeDriver/chromedriver"
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "08046419568"
PASSWORD = "mjdw15209458256"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")  # 打开 ins 登陆页
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)  # 输入用户名
        password.send_keys(PASSWORD)  # 输入密码

        time.sleep(2)
        password.send_keys(Keys.ENTER)  # 按回车

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")  # 进入 要查找的账号页面

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')  # 获取 粉丝数 元素
        followers.click()  # 点击

        time.sleep(2)
        # 获取 modal 框
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
