from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class RecruitmentPage:
    """Elementos del recruitment"""

    RECRUITMENT_OPT = Target.the("Sidebar option").located_by("//ul/li/a[contains(@href,'/recruitment/')]")
    URL_RECRUITMENT_MODULE = "/recruitment/viewCandidates"
    ADD_CANDIDATE_BTN = Target.the("Add candidate button").located_by("//button/i[contains(@class, 'bi-plus')]")
    URL_ADD_CANDIDATE = "/recruitment/addCandidate"
    SAVE_CANDIDATE_BTN = Target.the("Save candidate button").located_by("//button[@type='submit']")

    FULL_NAME_FIELD = Target.the("Full name field").located_by("//input[@name='firstName']")
    LAST_NAME_FIELD = Target.the("Lst Name field").located_by("//input[@name='lastName']")
    EMAIL_FIELD = Target.the("Email field").located_by("//label[text()='Email']/../following-sibling::div/input")
    VACANCY_SELECT = Target.the("Vacancy select").located_by("//div[contains(@class,'oxd-select-text-input')]")
    VACANCY_OPTIONS = Target.the("elements with role option").located_by((By.CSS_SELECTOR, '[role="option"]'))
    VACANCY_OPT = Target.the("Vacancy options").located_by("//div[contains(@class,'oxd-select-option')]")

    CONFIRMATION_MESSAGE = Target.the("confirmation message").located_by("//div[@class='alert alert-success']")

    SHORTLIST_BTN = Target.the("continue process button").located_by("//button[contains(@class, 'oxd-button--success')]")
    SHORTLIST_SAVE_BTN = Target.the("save shortlist button").located_by("//button[@type='submit']")

    