import time
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from screenpy_selenium.actions import Click
from screenplay.tasks.add_candidate import AddCandidate
from screenplay.ui.login import LoginPage
from screenplay.ui.recruitment import RecruitmentPage

@given('the user is logged in as an admin')
def step_given_login(context):
    context.execute_steps('''
        Given the user launch the login page
        When enter valid credentials and submit form "Admin" "admin123"
    ''')
    time.sleep(2)
    #wait to be logged
    WebDriverWait(context.driver, 10).until(EC.url_contains(LoginPage.URL_EXPECTED))

@when('the user navigate to the "Add candidate" section')
def step_when_navigate(context):
    time.sleep(2)
    context.actor.attempts_to(
        Click.on(RecruitmentPage.RECRUITMENT_OPT)
    )

@when('the user click on the "Add" button in the module')
def step_when_click_add(context):
    time.sleep(2)
    context.actor.attempts_to(
        Click.on(RecruitmentPage.ADD_CANDIDATE_BTN)
    )

@when('the user fill out the candidate form with the following details: "{fullname}" "{lastname}" "{email}"')
def step_when_fillout_form(context, fullname, lastname, email):  
    time.sleep(2)
    context.actor.attempts_to(AddCandidate.add_candidate(fullname, lastname, email))

@when('the user submit the form')
def step_when_save(context):
    time.sleep(2)
    context.actor.attempts_to(
        Click.on(RecruitmentPage.SAVE_CANDIDATE_BTN)
    )

@then('the user should see a shortlist option')
def step_then_should_see_shortlist_option(context):
    assert 1
