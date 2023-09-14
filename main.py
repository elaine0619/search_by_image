from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import config
import logging


def main():

    # Config logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s ',
                        filename=config['LOG_NAME'],
                        filemode='w')

    driver = None
    # Choose browser
    if config['BROWSER'].lower() == 'chrome':
        driver = webdriver.Chrome()
    elif config['BROWSER'].lower() == 'firefox':
        driver = webdriver.Firefox()
    elif config['BROWSER'].lower() == 'ie':
        driver = webdriver.Ie()
    else:
        raise Exception("Browser info is wrong!")
    logging.info(f"Use {config['BROWSER']} browser!")

    if driver:
        driver.maximize_window()
        driver.get(config['SEARCH_ENGINE'])
        driver.implicitly_wait(10)
    else:
        raise Exception("Failed to boot browser!")
    logging.info(f"Opened search engine: {config['SEARCH_ENGINE']} !")

    try:
        # Choose to search by image
        search_by_image = driver.find_element(By.CLASS_NAME, 'soutu-btn')
        search_by_image.click()
        driver.implicitly_wait(10)

        # Upload picture file
        upload_pic = driver.find_element(By.CLASS_NAME, 'upload-pic')
        upload_pic.send_keys(config['PICTURE_PATH'])
        driver.implicitly_wait(10)
        logging.info(f"Searching by the graph: {config['PICTURE_PATH']} !")

        # Open from result
        results = driver.find_elements(By.CLASS_NAME, 'graph-same-item')
        result_num = len(results)
        if result_num > 0:
            if config['VISIT_RESULT'] > result_num:
                raise Exception(f"Beyond the return scope: [{config['VISIT_RESULT']}/{result_num}]!")
            n = config['VISIT_RESULT'] - 1
            r = results[n]
            r.click()
        else:
            raise Exception("No items returns!")
        logging.info("Opening selected result page!")

        # Switch to new page
        sleep(5)
        windows = driver.window_handles
        if len(windows) < 2:
            sleep(5)
            windows = driver.window_handles
            if len(windows) < 2:
                raise Exception("It seems that no new window is opened!")
        driver.switch_to.window(windows[-1])
        driver.implicitly_wait(10)
        logging.info("Switched to selected result page!")

        # Save the screenshot of the last page
        driver.save_screenshot(config['SCREENSHOT_PATH'])
        logging.info(f"Saved screenshot to: {config['SCREENSHOT_PATH']}!")

        # Validate result:
        validate = 'Not Related'
        page_content = driver.page_source
        for str in config['VALIDATE_STRINGS']:
            if page_content.find(str) > -1:
                logging.info(f"Mapped string: {str}!")
                validate = 'Related'
                break

        # Close browser
        driver.quit()
        logging.info(f"Closed browser and validate result is: {validate}!")
        print(f"validate result is: {validate}!")

    except Exception as e:
        if driver:
            driver.quit()
        logging.error(e)
        print(e)


if __name__ == '__main__':
    main()
