from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_checkbox_counts(driver):
    """
    Returns checked and unchecked checkbox counts
    """
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    checked_count = 0
    unchecked_count = 0

    for checkbox in checkboxes:
        if checkbox.is_selected():
            checked_count += 1
        else:
            unchecked_count += 1

    return checked_count, unchecked_count, len(checkboxes)


def run_test_case(driver, expected_unchecked, test_name):
    print(f"\n{'='*60}")
    print(f"TEST CASE: {test_name}")

    checked, unchecked, total = get_checkbox_counts(driver)

    print(f"Total Checkboxes: {total}")
    print(f"Checked: {checked}")
    print(f"Unchecked: {unchecked}")
    print(f"Expected Unchecked: {expected_unchecked}")

    if unchecked == expected_unchecked:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL (Mismatch detected)")

    print(f"{'='*60}")


def main():
    driver = webdriver.Chrome()

    try:
        driver.get("file:///D:/Study/College/T.Y.B.Tech/Software%20Testing/index.html")
        time.sleep(2)

        run_test_case(
            driver,
            expected_unchecked=2,
            test_name="Unchecked Checkbox Count - Wrong Expected Value"
        )

        checked, unchecked, total = get_checkbox_counts(driver)

        run_test_case(
            driver,
            expected_unchecked=unchecked,
            test_name="Unchecked Checkbox Count - Correct Expected Value"
        )

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()