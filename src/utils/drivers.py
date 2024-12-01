from contextlib import contextmanager
from typing import Generator

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import chrome_options

class DriverManager:
    """
    A context manager for the Selenium WebDriver.

    Provides a context manager for browser sessions and handles the driver's instance.

    Attributes:
        delay_preset (str): A preset string ('short', 'medium', 'long') to determine the range of the delay.
        timeout (int): The maximum time to wait for an element to appear in seconds.
        _driver (webdriver.Chrome): The Chrome WebDriver instance.
        _wait (WebDriverWait): The WebDriverWait instance.

    Example:
        >>> manager = DriverManager()
        >>> with manager.session() as driver:
        ...     driver.get('https://www.example.com')
    """

    def __init__(self, delay_preset: str = 'short', timeout: int = 120) -> None:
        """
        Initializes the DriverManager with configurable delay preset and timeout.

        Args:
            delay_preset (str): A preset string ('short', 'medium', 'long') to determine the range of the delay.
            timeout (int): The maximum time to wait for an element to appear in seconds
        """

        self.delay_preset = delay_preset
        self.timeout = timeout
        self._driver = None
        self._wait = None

    @property
    def driver(self) -> webdriver.Chrome:
        """
        Create a Chrome Webdriver instance.

        Returns:
            webdriver.Chrome: The Chrome WebDriver instance.

        Raises:
            WebDriverException: If the WebDriver instance is not available.
        """

        if not self._driver:
            self._driver = webdriver.Chrome(options=chrome_options)
        return self._driver

    @property
    def wait(self) -> WebDriverWait:
        """
        Create a WebDriverWait instance.

        Returns:
            WebDriverWait: The WebDriverWait instance.
        """

        if not self._wait:
            self._wait = WebDriverWait(self.driver, self.timeout)
        return self._wait

    @contextmanager
    def session(self) -> Generator[webdriver.Chrome, None, None]:
        """
        Context manager for the WebDriver session.

        Yields:
            webdriver.Chrome: The Chrome WebDriver instance.

        Example:
            >>> manager = DriverManager()
            >>> with manager.session() as driver:
            ...     driver.get('https://www.example.com')
        """

        try:
            yield self.driver
        finally:
            if self._driver:
                self._driver.quit()
                self._driver = None
                self._wait = None