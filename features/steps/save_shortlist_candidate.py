import time
from screenpy import Actor
from behave import given, when, then
from screenplay.tasks.click_on_element import ClickOnElement
from screenplay.ui.recruitment import RecruitmentPage

@given('the user want to shortlist a newly created candidate and click on shortlist')
def step_given_add_candidate(context):
    context.execute_steps('''
         Given the user want to shortlist a newly created candidate
        When the user click on shortlist button
    ''')

@when('the user click on save shortlist button')
def step_when_shortlist(context):
    time.sleep(1)
    context.actor.attempts_to(ClickOnElement(RecruitmentPage.SUCCESS_BTN))

@then('the user should see x')
def step_then_should_see_form(context):
    assert 1


