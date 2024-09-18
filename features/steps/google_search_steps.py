from screenpy import Actor
from behave import given, when, then
from screenplay.questions.is_element_visible import IsElementVisible
from screenplay.tasks.close_cookie_notice_google import CloseCookieNoticeGoogle
from screenplay.tasks.search_google import SearchGoogle
from screenplay.ui.google_home import GoogleHomePage

@given('the user is on the Google homepage')
def step_given_usuario_esta_en_google(context):
    context.driver.get(GoogleHomePage.URL)

@when('the user searches for "{query}"')
def step_when_usuario_busca(context, query):
    # context.actor.attempts_to(CloseCookieNoticeGoogle.close_cookie_notice())
    context.actor.attempts_to(SearchGoogle.for_term(query))

@then('the user should see search results')
def step_then_usuario_deberia_ver_resultados(context):
    assert IsElementVisible(GoogleHomePage.RESULTS).answered_by(context.actor)
