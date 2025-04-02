import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FingerprintAuthTestFramework(unittest.TestCase):
    
    def setUp(self):
        # Initialize WebDriver and navigate to the fingerprint authentication page
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/fingerprint-auth")  # Replace with actual URL
    
    def test_fingerprint_enrollment(self):
        """Test enrolling a new fingerprint."""
        driver = self.driver
        enroll_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "enroll")))
        enroll_button.click()
        
        scan_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "scan")))
        scan_button.click()
        
        # Validate success message
        success_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message"))).text
        print(f"Actual message received: {success_message}")
        self.assertEqual(success_message, "Fingerprint enrolled successfully")
    
    def test_successful_authentication(self):
        """Test authentication with a valid fingerprint."""
        driver = self.driver
        auth_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "authenticate")))
        auth_button.click()
        
        scan_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "scan")))
        scan_button.click()
        
        # Validate success message
        success_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message"))).text
        print(f"Actual message received: {success_message}")
        self.assertEqual(success_message, "Authentication successful")
    
    def test_failed_authentication(self):
        """Test authentication failure with an incorrect fingerprint."""
        driver = self.driver
        auth_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "authenticate")))
        auth_button.click()
        
        wrong_fingerprint_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "wrong_scan")))
        wrong_fingerprint_button.click()
        
        # Validate error message
        error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message"))).text
        print(f"Actual message received: {error_message}")
        self.assertEqual(error_message, "Authentication failed")
    
    def test_multiple_failed_attempts(self):
        """Test lockout mechanism after multiple failed attempts."""
        driver = self.driver
        auth_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "authenticate")))
        auth_button.click()
        
        for _ in range(5):
            wrong_fingerprint_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "wrong_scan")))
            wrong_fingerprint_button.click()
        
        # Validate lockout message
        lock_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message"))).text
        print(f"Actual message received: {lock_message}")
        self.assertEqual(lock_message, "Too many failed attempts. Please try again later.")
    
    def test_wet_fingerprint(self):
        """Test authentication failure with a wet fingerprint."""
        driver = self.driver
        auth_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "authenticate")))
        auth_button.click()
        
        wet_fingerprint_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "wet_scan")))
        wet_fingerprint_button.click()
        
        # Validate error message
        error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message"))).text
        print(f"Actual message received: {error_message}")
        self.assertIn("Fingerprint not recognized", error_message)
    
    def test_spoofing_detection(self):
        """Test spoofing detection with a fake fingerprint."""
        driver = self.driver
        auth_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "authenticate")))
        auth_button.click()
        
        fake_fingerprint_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "fake_scan")))
        fake_fingerprint_button.click()
        
        # Validate spoof attempt detection message
        spoof_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message"))).text
        print(f"Actual message received: {spoof_message}")
        self.assertEqual(spoof_message, "Spoof attempt detected. Access denied.")
    
    def test_performance_response_time(self):
        """Test the response time of authentication."""
        driver = self.driver
        auth_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "authenticate")))
        auth_button.click()
        
        start_time = time.time()
        scan_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "scan")))
        scan_button.click()
        
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message")))
        response_time = time.time() - start_time
        print(f"Response time: {response_time:.2f} seconds")
        self.assertLess(response_time, 2, "Authentication response took too long")
    
    def tearDown(self):
        """Close the browser after tests are complete."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
