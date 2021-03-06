#!/urs/bin/env python3
import os
from sys import exit
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from colorama import init, Fore


def screenshot(path):
    opts = Options()
    opts.headless = True
    driver = Chrome(options=opts)
    files = os.listdir(f'{path}/hydra_report/response_body/')
    for file in files:
        try:
            driver.get(f'file://{path}/hydra_report/response_body/{file}')
            driver.get_screenshot_as_file(f'{path}/hydra_report/screenshots/{file.split(".html")[0]}.png')
            print(f'{Fore.BLUE} | screenshot {file} ok')

        except Exception as e:
            print(f'{Fore.RED}Runtime Error:\n{e}')
        except KeyboardInterrupt:
            exit('Bye!')

    driver.quit()
