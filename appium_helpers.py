# appium_helpers.py
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AppiumHelpers:
    def __init__(self, appium_server_url, capabilities):
        """Initialize the Appium driver and start the session."""
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        logger.info("Appium session started.")

    def tearDown(self):
        """Quit the Appium session."""
        if self.driver:
            self.driver.quit()
            logger.info("Appium session ended.")

    def click_element(self, accessibility_id, timeout=20):

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            ).click()
            logger.info(f"Clicked element with accessibility ID: {accessibility_id}")
        except NoSuchElementException:
            logger.warning(f"Element with accessibility ID '{accessibility_id}' not found. Proceeding to the next step.")
        except Exception as e:
            logger.error(f"Failed to click element with accessibility ID: {accessibility_id}. Error: {str(e)}")
            raise

    def click_element_by_uiselector(self, uiselector_query, timeout=20):
    
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, uiselector_query))
            ).click()
            logger.info(f"Clicked element using UiSelector query: {uiselector_query}")
        except NoSuchElementException:
            logger.warning(f"Element with UiSelector query '{uiselector_query}' not found. Proceeding to the next step.")
        except Exception as e:
            logger.error(f"Failed to click element with UiSelector query: {uiselector_query}. Error: {str(e)}")
            raise
    def enter_text(self, accessibility_id, text, timeout=20):
        """Enter text into an input field using its accessibility ID."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            )
            element.clear()
            element.send_keys(text)
            logger.info(f"Entered text '{text}' into element with accessibility ID: {accessibility_id}")
        except Exception as e:
            logger.error(f"Failed to enter text into element with accessibility ID: {accessibility_id}. Error: {str(e)}")
            raise

    def enter_otp(self, otp_code, timeout=20):
        """Enter OTP into the input fields."""
        try:
            for i in range(5):
                self.enter_text(f"input_{i + 1}", otp_code[i], timeout)
            logger.info(f"Entered OTP: {otp_code}")
        except Exception as e:
            logger.error(f"Failed to enter OTP. Error: {str(e)}")
            raise

    def handle_popup(self, accessibility_id, timeout=20):
        """Handle a pop-up by clicking its close button."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            ).click()
            logger.info(f"Handled pop-up with accessibility ID: {accessibility_id}")
        except Exception as e:
            logger.warning(f"Pop-up with accessibility ID {accessibility_id} not found. Proceeding without handling it.")

    def scroll_to_element_and_click(self, element_description, scrollable_container_id=None, timeout=20):
    
        try:
        # Construct the UiScrollable command
            if scrollable_container_id:
            # Scroll within a specific container
                scroll_command = (
                f'new UiScrollable(new UiSelector().resourceId("{scrollable_container_id}"))'
                f'.scrollIntoView(new UiSelector().description("{element_description}"));'
            )
            else:
            # Scroll the entire screen
                scroll_command = (
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().description("{element_description}"));'
            )

        # Execute the scroll command and wait for the element to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, scroll_command))
                ).click()
            logger.info(f"Scrolled to and clicked element with description: {element_description}")

        except Exception as e:
            logger.error(f"Failed to scroll to or click element with description: {element_description}. Error: {str(e)}")
        raise
    def enter_text_with_wait(self, accessibility_id, text, timeout=10):
        """
        Wait for an element to be present and send text to it.

        Args:
            accessibility_id (str): The accessibility ID of the element.
            text (str): The text to send to the element.
            timeout (int): Maximum time to wait for the element. Default is 10 seconds.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            ).send_keys(text)
            logger.info(f"Entered text '{text}' into element with accessibility ID: {accessibility_id}")
            print(f"First mission, channel created, completed!")
        except Exception as e:
            logger.error(f"Failed to enter text into element with accessibility ID: {accessibility_id}. Error: {str(e)}")
            raise
    def click_element_by_id(self, resource_id, timeout=20):
    
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.ID, resource_id))
        ).click()
            logger.info(f"Clicked element with resource ID: {resource_id}")
        except Exception as e:
            logger.error(f"Failed to click element with resource ID: {resource_id}. Error: {str(e)}")
        raise
    def check_for_guest_mode(self, timeout=20):
        """Check if the app is in guest mode and proceed to login."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "login_with_code"))
            ).click()
            logger.info("Proceeding with login as guest mode is not active.")
        except Exception as e:
            logger.warning("Guest mode check failed. Proceeding with login...")
    
    def click_element_if_present_else_click_another(self, element_to_check, element_to_click_if_present, element_to_click_if_not_present, timeout=20):
    
        try:
            # Check if the first element is present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(element_to_check)
            )
            logger.info(f"Element to check is present: {element_to_check}")

            # Click the first element
            self.driver.find_element(*element_to_check).click()
            logger.info(f"Clicked element: {element_to_check}")
        except Exception:
            # If the first element is not found, click the alternative element
            logger.warning(f"Element to check is not present: {element_to_check}")

            try:
                # Click the alternative element
                self.driver.find_element(*element_to_click_if_not_present).click()
                logger.info(f"Clicked alternative element: {element_to_click_if_not_present}")
            except Exception as e:
                logger.error(f"Failed to click alternative element: {element_to_click_if_not_present}. Error: {str(e)}")
                raise

    def check_element_and_run_functions(self, element_to_check, function_if_present, function_if_not_present, timeout=20):
    
        try:
            # Check if the element is present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(element_to_check)
            )
            logger.info(f"Element to check is present: {element_to_check}")

            # Run the function if the element is present
            function_if_present()
        except Exception:
            # If the element is not found, run the alternative function
            logger.warning(f"Element to check is not present: {element_to_check}")

            # Run the function if the element is not present
            function_if_not_present()