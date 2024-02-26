from browser import Browser


class LoginPage(Browser):

    def navigate_to_login_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')


