import pytest
from utils.browser_setup import start_browser
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.result_page import ResultPage


def capture_screenshot(driver, case_id):
    driver.save_screenshot(f"screenshots/FAIL_{case_id}.png")


def run_case(driver, input_text, expected_output, case_id):
    home = HomePage(driver)
    home.enter_input(input_text)
    home.click_submit()

    result = ResultPage(driver)
    actual = result.fetch_output()

    try:
        assert actual == expected_output
    except AssertionError:
        capture_screenshot(driver, case_id)
        raise

    result.go_back_home()


def test_AUTO_F_001_repeating_pattern():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "abcabcbb", "3", "AUTO_F_001")
    driver.quit()


def test_AUTO_F_002_all_repeat():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "kkkkk", "1", "AUTO_F_002")
    driver.quit()


def test_AUTO_F_003_unique_string():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "abcdef", "6", "AUTO_F_003")
    driver.quit()


def test_AUTO_F_004_single_character():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "p", "1", "AUTO_F_004")
    driver.quit()


def test_AUTO_F_005_blank_validation():
    driver = start_browser()
    driver.get(BASE_URL)

    home = HomePage(driver)
    home.enter_input("")
    home.click_submit()

    try:
        assert "Please enter" in home.get_error_message()
    except AssertionError:
        capture_screenshot(driver, "AUTO_F_005")
        raise

    driver.quit()


def test_AUTO_F_006_numeric_string():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "1123456", "6", "AUTO_F_006")
    driver.quit()


def test_AUTO_F_007_symbols():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "@#@abc", "4", "AUTO_F_007")
    driver.quit()


def test_AUTO_F_008_mixed_alphanumeric():
    driver = start_browser()
    driver.get(BASE_URL)
    run_case(driver, "ab12ab34", "6", "AUTO_F_008")
    driver.quit()


def test_AUTO_F_009_back_navigation():
    driver = start_browser()
    driver.get(BASE_URL)

    home = HomePage(driver)
    home.enter_input("abcabcbb")
    home.click_submit()

    result = ResultPage(driver)
    result.go_back_home()

    try:
        assert "input" in driver.current_url
    except AssertionError:
        capture_screenshot(driver, "AUTO_F_009")
        raise

    driver.quit()
