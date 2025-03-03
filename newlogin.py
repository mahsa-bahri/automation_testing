# login.py
from appium_helpers import AppiumHelpers
from appium.webdriver.common.appiumby import AppiumBy
class Login:
    def __init__(self, appium_helper):
        """Initialize the Login class with an instance of AppiumHelpers."""
        self.appium_helper = appium_helper

    def perform_login(self):
        """Perform the login process."""
        # Step 1: Check for guest mode
        
       
        self.appium_helper.check_for_guest_mode()
        self.appium_helper.click_element_if_present_else_click_another(
            element_to_check=(AppiumBy.ACCESSIBILITY_ID, "رد کردن"),
            element_to_click_if_present=(AppiumBy.ACCESSIBILITY_ID, "element_to_click_if_present"),
            element_to_click_if_not_present=(AppiumBy.ACCESSIBILITY_ID, "phone_number_input")
        )


        # Step 2: Enter phone number
        self.appium_helper.enter_text("phone_number_input", "8888886438")

        # Step 3: Click the 'Next' button
        self.appium_helper.click_element("login_next_btn")

        # Step 4: Click the 'Login with code' button
        self.appium_helper.click_element("login_with_code")

        # Step 5: Enter OTP
        self.appium_helper.enter_otp("36438")

        # Step 6: Handle pop-ups
        self.appium_helper.handle_popup("pantel_modal_close_btn")
        self.appium_helper.handle_popup("deny_incoming_call_permission")

        # Log success
        print("Login process completed successfully.")

    def login_guest(self):
        self.appium_helper.click_element("رد کردن")
        self.appium_helper.click_element("ورود به عنوان مهمان")
        self.appium_helper.handle_popup("pantel_modal_close_btn")
        self.appium_helper.click_element("ساخت جمع ")
        self.appium_helper.enter_text("phone_number_input", "8888886438")

        # Step 3: Click the 'Next' button
        self.appium_helper.click_element("login_next_btn")

        # Step 4: Click the 'Login with code' button
        self.appium_helper.click_element("login_with_code")

        # Step 5: Enter OTP
        self.appium_helper.enter_otp("36438")

        # Step 6: Handle pop-ups
        self.appium_helper.handle_popup("pantel_modal_close_btn")
        self.appium_helper.handle_popup("deny_incoming_call_permission")
        print("Login process completed successfully.")
        

    def login(self):
        # Step 2: Enter phone number
        self.appium_helper.enter_text("phone_number_input", "8888886438")

        # Step 3: Click the 'Next' button
        self.appium_helper.click_element("login_next_btn")

        # Step 4: Click the 'Login with code' button
        self.appium_helper.click_element("login_with_code")

        # Step 5: Enter OTP
        self.appium_helper.enter_otp("36438")

        # Step 6: Handle pop-ups
        self.appium_helper.handle_popup("pantel_modal_close_btn")
        self.appium_helper.handle_popup("deny_incoming_call_permission")

        # Log success
        print("Login process completed successfully.")
        
        
        # Add your regular login logic here
        # Example:
        # self.appium_helper.enter_text("username_input", "testuser")
        # self.appium_helper.enter_text("password_input", "password123")
        # self.appium_helper.click_element("login_button")