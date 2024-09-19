import time
from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click
from screenplay.tasks.click_on_element_at_index import ClickOnElementAtIndex
from screenplay.ui.recruitment import RecruitmentPage

class AddCandidate:
    """Tasks to add candidate"""

    @staticmethod
    def add_candidate(fullname, lastname, email):
        """Add candidate with valid data"""
        return AddCandidate(fullname, lastname, email)

    @beat('{} add candidate with "fullname", "lastname", "email"')
    def perform_as(self, the_actor: Actor) -> None:
        """Add candidate"""
        the_actor.attempts_to(
            Wait.for_the(RecruitmentPage.FULL_NAME_FIELD),
            Enter.the_text(self.fullname).into(RecruitmentPage.FULL_NAME_FIELD),
            Enter.the_text(self.lastname).into(RecruitmentPage.LAST_NAME_FIELD),
            Enter.the_text(self.email).into(RecruitmentPage.EMAIL_FIELD),
            Click.on(RecruitmentPage.VACANCY_SELECT),
            Wait.for_the(RecruitmentPage.VACANCY_OPTIONS).to_appear(),
            ClickOnElementAtIndex.on(RecruitmentPage.VACANCY_OPTIONS, 2),
            Click.on_the(RecruitmentPage.SAVE_CANDIDATE_BTN)
        )

    def __init__(self, fullname: str, lastname: str, email: str) -> None:
        self.fullname = fullname
        self.lastname = lastname
        self.email = email


