# Import necessary Selenium modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
# Ensure the 'openpyxl' library is installed before running this script.
# You can install it using the following command in your terminal:
# pip install openpyxl

class FingerprintAuthTests:
    
    @staticmethod
    def test_fingerprint_enrollment(driver):
        """Test fingerprint enrollment - basic functionality."""
        try:
            # Explanation: This test simulates a user enrolling their fingerprint in the system.
            # The steps include clicking the "Enroll" button, scanning the fingerprint, 
            # and verifying the success message.

            # Step 1: Wait for the "Enroll" button to be clickable and then click it.
            # This ensures that the page has loaded and the button is interactive.
            enroll_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "enroll"))
            )
            enroll_button.click()

            # Step 2: Wait for the "Scan Fingerprint" button to be clickable and then click it.
            # This simulates the user placing their finger on the scanner.
            scan_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "scan"))
            )
            scan_button.click()

            # Step 3: Wait for the success message to appear after fingerprint enrollment.
            # This confirms that the fingerprint was stored successfully.
            success_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "message"))
            ).text

            # Step 4: Verify if the success message is correct.
            # If the expected message does not match, the test will fail.
            assert success_message == "Fingerprint enrolled successfully", f"Enrollment failed: {success_message}"
        
        except Exception as e:
            # If an error occurs at any step, print the error message and fail the test.
            print(f"Error in test_fingerprint_enrollment: {e}")
            raise

    @staticmethod
    def test_failed_authentication(driver):
        """Test authentication failure with an unregistered fingerprint."""
        try:
            # Explanation: This test checks if the system correctly denies access when 
            # an unregistered fingerprint is used.
            # The steps include clicking the "Authenticate" button, attempting an invalid scan, 
            # and verifying the error message.

            # Step 1: Wait for the "Authenticate" button to be clickable and then click it.
            # This simulates a user trying to log in using their fingerprint.
            auth_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "authenticate"))
            )
            auth_button.click()

            # Step 2: Wait for the "Invalid Scan" button to be clickable and then click it.
            # This simulates a user placing an unregistered or incorrect fingerprint.
            invalid_scan_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "invalid_scan"))
            )
            invalid_scan_button.click()

            # Step 3: Wait for the error message to appear after an invalid fingerprint attempt.
            # This confirms that the system correctly rejects unauthorized users.
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "error_message"))
            ).text

            # Step 4: Verify if the error message is correct.
            # If the expected message does not match, the test will fail.
            assert error_message == "Authentication failed", f"Unexpected error message: {error_message}"

        except Exception as e:
            # If an error occurs at any step, print the error message and fail the test.
            print(f"Error in test_failed_authentication: {e}")
            raise
#-----------------------------------------------------------------------------------------------------------------------

def generate_test_cases_excel(file_path):
    # Create a new workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Fingerprint Auth Test Cases"

    # Define the headers for the test cases
    headers = [
        "Test Case ID", "Test Case Description", "Preconditions", 
        "Test Steps", "Expected Result", "Actual Result", "Status"
    ]
    sheet.append(headers)

    # Define the test cases
    test_cases = [
        # Valid Test Cases
        {
            "id": "TC001",
            "description": "Enroll fingerprint successfully",
            "preconditions": "User is on the fingerprint enrollment page",
            "steps": "1. Click 'Enroll' button\n2. Click 'Scan Fingerprint' button\n3. Verify success message",
            "expected_result": "Fingerprint enrolled successfully",
        },
        {
            "id": "TC002",
            "description": "Authenticate successfully with registered fingerprint",
            "preconditions": "User has enrolled a fingerprint",
            "steps": "1. Click 'Authenticate' button\n2. Place registered fingerprint\n3. Verify success message",
            "expected_result": "Authentication successful",
        },
        # Invalid Test Cases
        {
            "id": "TC003",
            "description": "Fail authentication with unregistered fingerprint",
            "preconditions": "User has not enrolled the fingerprint being used",
            "steps": "1. Click 'Authenticate' button\n2. Place unregistered fingerprint\n3. Verify error message",
            "expected_result": "Authentication failed",
        },
        {
            "id": "TC004",
            "description": "Fail enrollment with no fingerprint scan",
            "preconditions": "User is on the fingerprint enrollment page",
            "steps": "1. Click 'Enroll' button\n2. Do not scan fingerprint\n3. Verify error message",
            "expected_result": "Enrollment failed: No fingerprint detected",
        },
        # Edge Cases
        {
            "id": "TC005",
            "description": "Handle multiple rapid clicks on 'Enroll' button",
            "preconditions": "User is on the fingerprint enrollment page",
            "steps": "1. Rapidly click 'Enroll' button multiple times\n2. Verify system handles it gracefully",
            "expected_result": "System should process only one enrollment request",
        },
        {
            "id": "TC006",
            "description": "Handle multiple rapid clicks on 'Authenticate' button",
            "preconditions": "User has enrolled a fingerprint",
            "steps": "1. Rapidly click 'Authenticate' button multiple times\n2. Verify system handles it gracefully",
            "expected_result": "System should process only one authentication request",
        },
    ]

    # Add the test cases to the sheet
    for case in test_cases:
        sheet.append([
            case["id"], case["description"], case["preconditions"], 
            case["steps"], case["expected_result"], "", "Not Executed"
        ])

    # Save the workbook to the specified file path
    file_path = r"E:\fingerPrintAuthentication\fingerprint_auth_test_cases.xlsx"
    workbook.save(file_path)
    print(f"Test cases saved to {file_path}")

# Generate the test cases Excel file
generate_test_cases_excel("fingerprint_auth_test_cases.xlsx")
