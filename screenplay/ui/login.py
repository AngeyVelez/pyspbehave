from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class LoginPage:
    """Elementos del login de OrangeHRM."""
    
    USERNAME = Target.the("Username input").located_by((By.NAME, "username"))
    PASSWORD = Target.the("Password input").located_by((By.NAME, "password"))
    LOGIN_BTN = Target.the("Login button").located_by("//button[contains(@class,'orangehrm-login-button')]")
    URL_LOGIN = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    URL_EXPECTED = "/dashboard/index"