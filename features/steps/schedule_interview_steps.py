import time
from behave import given, when, then
from screenplay.tasks.click_on_element import ClickOnElement
from screenplay.tasks.schedule_interview import ScheduleInterview
from screenplay.ui.recruitment import RecruitmentPage

@given('the user must schedule an interview')
def step_given_add_candidate(context):
    context.execute_steps('''
        Given the candidate is shortlist
        When the user click on schedule interview
    ''')
    time.sleep(1)

@when('enter valid data and submit form "{title}" "{interviewer}" "{date}"')
def step_when_shortlist(context, title, interviewer, date):
    time.sleep(1)
    context.actor.attempts_to(
        ScheduleInterview.schedule_interview(title, interviewer, date)
    )

@then('the user should see a Successful message')
def step_then_should_see_form(context):
    assert 1
