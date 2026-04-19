from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_total_objects(driver):
    """
    Returns total number of DOM objects on the page
    """
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "*"))
    )

    all_elements = driver.find_elements(By.TAG_NAME, "*")
    return len(all_elements)


def run_test_case(driver, expected_count, test_name):
    print(f"\n{'='*60}")
    print(f"TEST CASE: {test_name}")

    actual_count = get_total_objects(driver)

    print(f"Expected Objects: {expected_count}")
    print(f"Actual Objects: {actual_count}")

    if actual_count == expected_count:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL (Mismatch detected)")

    print(f"{'='*60}")


def print_object_breakdown(driver):
    print("\n--- Objects Count by Type ---")

    object_types = ["div", "p", "span", "img", "a", "button", "input", "form"]

    for obj_type in object_types:
        elements = driver.find_elements(By.TAG_NAME, obj_type)
        count = len(elements)
        if count > 0:
            print(f"{obj_type.upper()}: {count}")


def main():
    driver = webdriver.Chrome()

    try:
        driver.get("file:///D:/Study/College/T.Y.B.Tech/Software%20Testing/index.html")

        run_test_case(
            driver,
        expected_count=5, 
            test_name="DOM Object Count - Negative Test Case"
        )

        actual = get_total_objects(driver)

        run_test_case(
            driver,
            expected_count=actual, 
            test_name="DOM Object Count - Positive Test Case"
        )

        print_object_breakdown(driver)

        time.sleep(2)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()