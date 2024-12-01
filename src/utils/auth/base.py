from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginHandler(ABC):
    def __init__(self, driver: webdriver.Chrome, timeout: int = 120, retries = 3) -> None:
        self.driver = driver
        self.timeout = timeout
        self.retries = retries

    @abstractmethod
    def login(self) -> bool:
        pass

    @classmethod
    def wait_for_element(self, by: By, value: str) -> WebDriverWait:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )