from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class SceduleInterviewPage:
    """Schedule interview items"""

    TITLE_FIELD = Target.the("title input").located_by("//input[not(@placeholder) and not(@readonly)]")
    DATE_FIELD = Target.the("date input").located_by("//div[contains(@class, 'oxd-date-input')]//input")
    INTERVIEWER_FIELD = Target.the("interviewer input").located_by("//input[@include-employees]")
    INTERVIEWER_OPTIONS = Target.the("elements with role option").located_by((By.CSS_SELECTOR, '[role="option"]'))
    