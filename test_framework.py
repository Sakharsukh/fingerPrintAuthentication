# Import required modules
import unittest  # Built-in Python testing framework
from selenium import webdriver  # WebDriver for browser automation
from test_case import FingerprintAuthTests  # Import test cases from another file

class FingerprintAuthTestFramework(unittest.TestCase):
    """
    This framework runs multiple test cases related to fingerprint authentication.
    It initializes a web browser, executes test cases, and then closes the browser.
    """

    def setUp(self):
        """
        Step 1: Set up the test environment.
        - Launches a web browser (Chrome in this case).
        - Opens the web page for fingerprint authentication testing.
        """
        self.driver = webdriver.Chrome()  # Initialize WebDriver for Chrome browser
        
        # Navigate to the fingerprint authentication web page.
        # Make sure this URL is correct before running the tests.
        self.driver.get("http://localhost:8080/index.html")  

    def test_fingerprint_enrollment(self):
        """
        Step 2: Test fingerprint enrollment functionality.
        - Calls the test case to simulate enrolling a fingerprint.
        - Checks if the system correctly registers the fingerprint.
        """
        FingerprintAuthTests.test_fingerprint_enrollment(self.driver)

    def test_successful_authentication(self):
        """
        Step 3: Test successful authentication.
        - Simulates a valid fingerprint authentication attempt.
        - Ensures that the system grants access as expected.
        """
        FingerprintAuthTests.test_successful_authentication(self.driver)

    def test_failed_authentication(self):
        """
        Step 4: Test authentication failure.
        - Simulates an unregistered fingerprint attempting authentication.
        - Ensures the system correctly denies access.
        """
        FingerprintAuthTests.test_failed_authentication(self.driver)

    def test_multiple_failed_attempts(self):
        """
        Step 5: Test account lockout after multiple failed authentication attempts.
        - Tries multiple incorrect fingerprints to trigger the security mechanism.
        - Ensures that the system locks the account after repeated failures.
        """
        FingerprintAuthTests.test_multiple_failed_attempts(self.driver)

    def test_wet_fingerprint(self):
        """
        Step 6: Test system behavior with wet/damp fingerprints.
        - Simulates a scenario where a fingerprint is scanned with wet fingers.
        - Ensures that the system either rejects or correctly processes the scan.
        """
        FingerprintAuthTests.test_wet_fingerprint(self.driver)

    def test_spoofing_detection(self):
        """
        Step 7: Test anti-spoofing detection.
        - Simulates an attempt to log in using a fake fingerprint (e.g., a printed image).
        - Ensures the system detects and prevents unauthorized access.
        """
        FingerprintAuthTests.test_spoofing_detection(self.driver)

    def tearDown(self):
        """
        Step 8: Clean up after each test.
        - Closes the browser session to free up resources.
        - Ensures each test starts with a fresh browser session.
        """
        self.driver.quit()

# Run the tests when this script is executed directly.
if __name__ == "__main__":
    unittest.main(verbosity=2)  # Runs all tests with detailed output
