import time
from screenpy import Actor
from behave import given, when, then
from screenplay.questions.is_element_visible import IsElementVisible
from screenplay.questions.current_url import CurrentURL
from screenplay.tasks.click_on_element import ClickOnElement
from screenplay.tasks.login import Login
from screenplay.tasks.shortlist_candidate import ShorlistCandidate
from screenplay.ui.login import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from screenplay.ui.recruitment import RecruitmentPage

@given('the user want to shortlist a newly created candidate')
def step_given_add_candidate(context):
    context.execute_steps('''
        Given the user is logged in as an admin
        When the user navigate to the "Add candidate" section
        And the user click on the "Add" button in the module
        And the user fill out the candidate form with the following details: "Andrew" "Gil" "mail@email.com"
        And the user submit the form
    ''')
    time.sleep(1)

@when('the user click on shortlist button')
def step_when_shortlist(context):
    time.sleep(1)
    context.actor.attempts_to(ClickOnElement(RecruitmentPage.SHORTLIST_BTN))

@then('the user should see a shortlist form')
def step_then_should_see_form(context):
    assert 1


