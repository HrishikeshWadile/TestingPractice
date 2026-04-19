from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_dropdown_count(driver, dropdown_id):
    """
    Returns number of options in a dropdown
    """
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, dropdown_id))
    )
    select = Select(dropdown)
    return len(select.options)


def run_test_case(driver, dropdown_id, expected_count, test_name):
    print(f"\n{'='*60}")
    print(f"TEST CASE: {test_name}")

    actual_count = get_dropdown_count(driver, dropdown_id)

    print(f"Dropdown ID: {dropdown_id}")
    print(f"Expected Count: {expected_count}")
    print(f"Actual Count: {actual_count}")

    if actual_count == expected_count:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL (Mismatch detected)")

    print(f"{'='*60}")


def main():
    driver = webdriver.Chrome()

    try:
        driver.get("file:///D:/Study/College/T.Y.B.Tech/Software%20Testing/index.html")

        run_test_case(
            driver,
            dropdown_id="dropdown-pass",
            expected_count=2,
            test_name="PASS Dropdown Validation (Correct Expectation)"
        )

        run_test_case(
            driver,
            dropdown_id="dropdown-fail",
            expected_count=1,  
            test_name="FAIL Dropdown Validation (Intentional Mismatch)"
        )

        time.sleep(2)

    except Exception as e:
        print(f"Test Execution Failed: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()