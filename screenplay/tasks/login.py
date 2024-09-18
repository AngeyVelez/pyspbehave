from screenpy import Actor
from screenpy.pacing import beat
from selenium.webdriver.common.keys import Keys
from screenpy_selenium.actions import Enter, Wait, Click
from screenplay.ui.login import LoginPage

class Login:
    """Taks to login"""

    @staticmethod
    def login(username, password):
        """Login with valid credentials"""
        return Login(username, password)

    @beat('{} login with "username", "password"')
    def perform_as(self, the_actor: Actor) -> None:
        """Login"""
        the_actor.attempts_to(
            Wait.for_the(LoginPage.USERNAME),
            Enter.the_text(self.username).into(LoginPage.USERNAME),
            Enter.the_text(self.password).into(LoginPage.PASSWORD),
            Click.on_the(LoginPage.LOGIN_BTN)
        )
    
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
