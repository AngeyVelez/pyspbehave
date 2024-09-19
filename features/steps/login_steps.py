from behave import given, when, then
from screenplay.questions.current_url import CurrentURL
from screenplay.tasks.login import Login
from screenplay.ui.login import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user launch the login page')
def step_given_launch_login(context):
    context.driver.get(LoginPage.URL_LOGIN)

@when('enter valid credentials and submit form "{username}" "{password}"')
def step_when_enter_credentials(context, username, password):
    context.actor.attempts_to(Login.login(username, password))

@then('the user should see the user dashboard')
def step_then_should_see_dashboard(context):
    actual_url = CurrentURL.answered_by(context.actor)
    WebDriverWait(context.driver, 10).until(EC.url_contains(LoginPage.URL_EXPECTED))
    assert LoginPage.URL_EXPECTED in actual_url

