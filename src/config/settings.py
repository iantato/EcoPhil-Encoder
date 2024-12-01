from datetime import date
from pathlib import Path
import os

from selenium import webdriver
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Get environment variables.
INTERCOMMERCE_USERNAME = os.getenv('INTERCOMMERCE_USERNAME')
INTERCOMMERCE_PASSWORD = os.getenv('INTERCOMMERCE_PASSWORD')

VBS_USERNAME = os.getenv('VBS_USERNAME')
VBS_PASSWORD = os.getenv('VBS_PASSWORD')

# Directories for data.
DATA_DIR = Path(__file__).parent.parent / 'data'
DOWNLOAD_DIR = DATA_DIR / 'download'
SHEETS_DIR = DATA_DIR / 'sheets'
SAVES_DIR = DATA_DIR / 'saves'
FORMATS_DIR = dict({
    'liquidation': DATA_DIR / 'formats' / 'liquidation.xlsx',
    'summary': DATA_DIR / 'formats' / 'summary.xlsx',
})

# Webdriver Chrome options.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--enable-chrome-browser-cloud-management')
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': str(DOWNLOAD_DIR),
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True,
    'safebrowsing.enabled': True
})

# Dates for the VBS system.
DATE_RANGES = {
    'start': date(0, 0, 0), # Year, Month, Day
    'end': date(0, 0, 0) # Year, Month, Day
}

# URLs for the Intercommerce website.
BASE_URL = 'https://www.intercommerce.com.ph/WebCWS/'
URLS = {
    'main': BASE_URL + os.getenv('MAIN_BRANCH'),
    'fcie': BASE_URL + os.getenv('FCIE_BRANCH'),
}