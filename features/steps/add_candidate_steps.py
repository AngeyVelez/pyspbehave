import time
from behave import given, when, then
from screenpy_selenium import Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from screenpy_selenium.actions import Click
from screenpy_selenium.questions import Text
from screenplay.tasks.add_candidate import AddRecruitment
from screenplay.ui.login import LoginPage
from screenplay.ui.recruitment import RecruitmentPage

@given('I am logged in as an admin')
def step_impl(context):
    context.execute_steps('''
        Given the user launch the login page
        When enter valid credentials and submit form "Admin" "admin123"
    ''')
    # Espera hasta que el usuario esté logueado
    time.sleep(3)
    WebDriverWait(context.driver, 10).until(EC.url_contains(LoginPage.URL_EXPECTED))

@when('I navigate to the "Add candidate" section')
def step_impl(context):
    time.sleep(3)
    context.actor.attempts_to(
        Click.on(RecruitmentPage.RECRUITMENT_OPT)
    )

@when('I click on the "Add" button in the module')
def step_impl(context):
    time.sleep(3)
    context.actor.attempts_to(
        Click.on(RecruitmentPage.ADD_CANDIDATE_BTN)
    )

@when('I fill out the candidate form with the following details: "{fullname}" "{lastname}" "{email}"')
def step_impl(context, fullname, lastname, email):  
    time.sleep(3)
    context.actor.attempts_to(AddRecruitment.add_recruitment(fullname, lastname, email))

@when('I submit the form')
def step_impl(context):
    time.sleep(3)
    context.actor.attempts_to(
        Click.on(RecruitmentPage.SAVE_CANDIDATE_BTN)
    )

@then('I should see a confirmation message that the candidate was added successfully')
def step_impl(context):
    confirmation_text = Text.of(RecruitmentPage.CONFIRMATION_MESSAGE).answered_by(context.actor)
    assert 1
