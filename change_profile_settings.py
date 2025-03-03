import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import random

# Setup desired capabilities and start Appium session
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='bfc520780121',
    app='/home/farzad/Downloads/panco3.apk',
    appPackage='me.panco.app',
    appActivity='.MainActivity',
    adbExecTimeout=100000,  # Timeout is set to 60 seconds
)

appium_server_url = 'http://192.168.1.228:4723'


class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_change_profile_settings(self):
        # Wait for the "Login or Register" button in guest mode
        self.check_for_guest_mode()

	    # # Locate the notification pop up and click button 
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "permission_allow_button").click()
        
        # WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located(
        #         (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اجازه دادن")'))
        # ).click()

        self.login()

        user_id='1636288351910575'
        #get profile api
        api_url=f"https://api.pantel.me/a/get_profile_pic?$=a3197fe10e5c13dd59eb0efcf7de7464&user_id={user_id}"


        # Check for the presence of the pop-up
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "pantel_modal_close_btn"))
            ).click()
        except Exception as e:
            print(f"Type of exception: {type(e).__name__}")
            # If the pop-up is not found, proceed with the rest of the test
            print("No pop-up appeared.")

        # Select header side menu
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "header_side_menu"))
        ).click()

        # Check for the presence of the pop-up for incoming call permission
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "deny_incoming_call_permission"))
            ).click()
        except Exception as e:
            # If the pop-up is not found, proceed with the rest of the test
            print("No pop-up appeared.")

        sleep(2)
        # Select profile setting menu
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "ویرایش پروفایل"))
        ).click()

        self.change_userid()

        self.change_familyname()

        

    # helper method
    def check_for_guest_mode(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ورود یا ثبت‌نام")'))
            ).click()
        except Exception as e:
            print("Error checking guest mode; proceeding with login ...")

    def login(self):
        user_id='1636288351910575'
        
        # Locate the test phone number input field using accessibility ID
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "phone_number_input"))
        ).send_keys("8888886444")

        # Locate the 'Next' button and click it
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_next_btn").click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, 'login_with_code'))
        ).click()

        # Wait for OPT input field to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "input_1"))
        )
        # Fill the OTP input field
        otp_code = "36444"
        for i in range(5):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"input_{i + 1}").send_keys(otp_code[i])

    def change_userid(self):
        #click user id field and go to change user id page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "profile_username_box"))
        ).click()

        #click change user id field
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "textInput"))
        ).click()

        #change user id 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "textInput"))
        ).send_keys("u64444")

        #change user id 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "تأیید"))
        ).click()

        #click back button 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)'))#here
        ).click()

        print("user id changed succesfully")

        #change user id for second time so that the difference in second run be recognizable
        #click user id field and go to change user id page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "profile_username_box"))
        ).click()

        #click change user id field
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "textInput"))
        ).click()

        #change user id 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "textInput"))
        ).send_keys("uuuuuu")

        #change user id 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "تأیید"))
        ).click()

        #click back button 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)'))#here
        ).click()

    def change_familyname(self):
        #choose family name field
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(22)'))
        ).click()

        number = random.randint(10,99)
        strnum = f"{number}"
        print(strnum)
        familyElem = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="textInput" and @text="chocolate"]'))
        )
        familyElem.send_keys(strnum)
        familyElem.clear()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("نام خانوادگی")'))
        ).click()

        #click save button 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "save_profile_btn_true"))
        ).click()
        print("family name successfully changed.")
        sleep(3)

        #choose family name field
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(22)'))
        ).click()
        
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="textInput" and @text="نام خانوادگی"]'))
        ).send_keys("chocolate")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("نام خانوادگی")'))
        ).click()

        #click save button 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "save_profile_btn_true"))
        ).click()
        sleep(3)
        
        #click back button 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)'))#here
        ).click()

if __name__ == '__main__':
    unittest.main()