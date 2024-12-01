from utils.auth.base import LoginHandler

from utils.wait import uniform_delay

class IntercommerceLogin(LoginHandler):
    def login(self) -> bool:
        try:
            self.driver.get('https://www.intercommerce.com.ph/login')
            self.driver.implicitly_wait(uniform_delay('short'))


        except Exception as e:
            raise e