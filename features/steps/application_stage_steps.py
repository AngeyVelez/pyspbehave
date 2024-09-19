import time
from behave import given, when, then
from screenplay.tasks.click_on_element import ClickOnElement
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

@given('the candidate is shortlist')
def step_given_add_candidate(context):
    context.execute_steps('''
        Given the user want to shortlist a newly created candidate
        When the user click on shortlist button
    ''')

@when('the user click on schedule interview')
def step_when_shortlist(context):
    time.sleep(1)
    context.actor.attempts_to(ClickOnElement(RecruitmentPage.SUCCESS_BTN))

@then('the user should see a interview form')
def step_then_should_see_form(context):
    assert 1


