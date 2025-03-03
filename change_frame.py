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

    def test_change_frame(self):
        # Wait for the "Login or Register" button in guest mode
        self.check_for_guest_mode()

	    # # Locate the notification pop up and click button 
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "permission_allow_button").click()
        
        # WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located(
        #         (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("اجازه دادن")'))
        # ).click()
        self.login()
        
        self.buy_frame()

        # Check for the presence of the pop-up
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "pantel_modal_close_btn"))
            ).click()
        except Exception as e:
            print(f"Type of exception: {type(e).__name__}")
            # If the pop-up is not found, proceed with the rest of the test
            print("No pop-up appeared.")
        
        self.change_frame()


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

    def buy_frame(self):
        session_id='a3197fe10e5c13dd59eb0efcf7de7464'

        transaction_url=f'https://api.pantel.me/a/get_user_transactions?$={session_id}&mode=product'

        transaction_list=requests.get(transaction_url).json().get("result",[])
        # print(transaction_list)    

        # check the specific target exists in user items
        trg_product_id=1678699828409169
        purchase_url= f'https://api.pantel.me/a/purchase?$={session_id}&product_id={trg_product_id}'

        frame1 = any( transaction.get("product_id") == trg_product_id for transaction in transaction_list)
        # print(frame1)
        if frame1 == False:
            #buy the frame
            requests.get(purchase_url)
            print("bought 'بهمن' frame.")
        else:
            print("the frame exists!")

    def change_frame(self):
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


        # click change frame 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "change_frame"))
        ).click()

        #choose the frame
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)'))
        ).click()

        # click save button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "save_frame"))
        ).click()

        # click close modal button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "close_modal_container"))
        ).click() 

        sleep(3)
        print("checkout frame update!")

        # click change frame 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "change_frame"))
        ).click()

        #choose delete frame
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "حذف قاب"))
        ).click()

        # click save button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "save_frame"))
        ).click()
        
        # click close modal button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "close_modal_container"))
        ).click()

        #click back button 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)'))#here
        ).click()
        sleep(4) 


if __name__ == '__main__':
    unittest.main()