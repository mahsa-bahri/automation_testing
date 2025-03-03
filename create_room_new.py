# new_test_script.py
import unittest
from appium_helpers import AppiumHelpers  # AppiumHelpers is used in the Login class
from newlogin import Login
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define desired capabilities and Appium server URL
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='DUM0219722005759',
    app='/home/panco/testnew/panco.apk',
    appPackage='me.panco.app',
    appActivity='.MainActivity',
    adbExecTimeout=100000,  # Timeout is set to 60 seconds
)

appium_server_url = 'http://192.168.1.79:4723'


class NewAppiumTest(unittest.TestCase):
    def setUp(self):
        """Initialize the AppiumHelpers and Login classes."""
        # AppiumHelpers is used here to initialize the Login class
        self.appium_helper = AppiumHelpers(appium_server_url, capabilities)
        self.login = Login(self.appium_helper)

    def tearDown(self):
        """Quit the Appium session."""
        self.appium_helper.tearDown()

    def test_new_feature(self):
        """Test a new feature after performing login."""
        self.appium_helper.check_element_and_run_functions(
            element_to_check=(AppiumBy.ACCESSIBILITY_ID, "رد کردن"),
            function_if_present=self.login.login_guest,
            function_if_not_present=self.login.login
        )

        # Perform login using the Login class
        #self.login.perform_login()

        # Add additional test steps here
        # Example: Open side menu and logout
        self.appium_helper.click_element("ساخت جمع ")
        self.appium_helper.click_element("ساخت ")

        # Enter text into the new club name field
        self.appium_helper.enter_text_with_wait("new_club_name", "adsd")

        # Click the "new_chat_room_ساخت _false" button
        self.appium_helper.click_element("new_chat_room_ساخت _false")

        # Wait for and click the "تم جمع کمپ" button using UiSelector
        try:
            WebDriverWait(self.appium_helper.driver, 20).until(
                EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("تم جمع کمپ")'))
            ).click()
            logger.info("Clicked element with text: تم جمع کمپ")
        except Exception as e:
            logger.error(f"Failed to click element with text: تم جمع کمپ. Error: {str(e)}")
            raise

        # Click the "use_asset_ساخت _false" button
        #self.appium_helper.click_element("asset_preview_خرید_false")
        #self.appium_helper.click_element("تم جمع کمپ")
        self.appium_helper.click_element("use_asset_ساخت _false")
        self.appium_helper.click_element("باشه")
        try:
            self.appium_helper.click_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            logger.info("Permission dialog handled successfully.")
        except Exception as e:
            logger.warning(f"Permission dialog not found. Error: {str(e)}")
        try:
            self.appium_helper.click_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        except Exception as e:
            logger.warning(f"Permission dialog not found. Error: {str(e)}")
        self.appium_helper.click_element("room_footer_text_input")
        self.appium_helper.enter_text_with_wait("room_footer_text_input", "test")
        self.appium_helper.click_element("room_footer_bottom_send_btn")
        self.appium_helper.click_element("room_container_subscribers_box")
        self.appium_helper.click_element("room_footer_bottom_gem_btn_container")
        self.appium_helper.click_element("استیکر صوتی")
        self.appium_helper.click_element_by_uiselector('new UiSelector().text("استیکرهای خریداری شده")')
        self.appium_helper.click_element_by_uiselector('new UiSelector().className("android.widget.ImageView").instance(1)')
        self.appium_helper.click_element("room_footer_bottom_gem_btn_container")
        

        




if __name__ == '__main__':
    unittest.main()