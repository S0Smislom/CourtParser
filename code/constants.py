from pathlib import Path
from selenium.webdriver.chrome.options import Options


BASE_DIR = Path(__file__).resolve().parent

BASE_URL = 'https://mos-gorsud.ru/search?formType=shortForm&courtAlias=mgs&uid=&instance=1&processType=1&category=&letterNumber=&caseNumber=&participant='
BASE_FILTER = '123 - Об установлении рыночной стоимости земельных участков и отдельных объектов недвижимости'
TARGET_CLASS_NAME = 'custom_table'
OUTPUT_PATH = 'output'
DATA_SHEET_NAME = 'Data'
DEFAULT_THREADS = 4
DEFAULT_PAGES = 10

driver_options = Options()
driver_options.add_argument('--headless')

driver_path = Path(BASE_DIR / 'drivers' / 'chromedriver.exe')
