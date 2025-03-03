import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import datetime

# Setup desired capabilities and start Appium session
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='bfc520780121',
    app='/home/farzad/Downloads/myket.apk',
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

    def test_create_room(self):
        # Wait for the "Login or Register" button in guest mode
        self.check_for_guest_mode()

	    # # Locate the notification pop up and click button 
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "permission_allow_button").click()
        
        # WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located(
        #         (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اجازه دادن")'))
        # ).click()
        self.login()

        # Check for the presence of the pop-up
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "pantel_modal_close_btn"))
            ).click()
        except Exception as e:
            print(f"Type of exception: {type(e).__name__}")
            # If the pop-up is not found, proceed with the rest of the test
            print("No pop-up appeared.")

        self.create_room()

         
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

    def create_room(self):
        sleep(2)
        # Select create room
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "ساخت جمع "))
        ).click()

        # click create room
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "ساخت "))
        ).click()
        
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "new_club_name"))
        ).click()
        
        #define room name
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "new_club_name"))
        ).send_keys("test")

        #click create room
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "new_chat_room_ساخت _false"))
        ).click()

        #click create button
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "use_asset_ساخت _false"))
        ).click()

        #give permission modal
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "باشه"))
        ).click()

        #click the mic access permission
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
        ).click()

        #click the gps access permission
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        ).click()
        print("mission of giving permission, check:) ")
        sleep(3)
        print("room created successfully!")


    
if __name__ == '__main__':
    unittest.main()