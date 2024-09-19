import time
from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium import Wait
from screenpy_selenium.actions import Click
from screenplay.tasks.click_on_element import ClickOnElement
from screenplay.ui.recruitment import RecruitmentPage

class ShorlistCandidate:
    """Taks to shortlist candidate"""

    @staticmethod
    def shortlist_candidate():
        return ShorlistCandidate()

    @beat('{}shortlist candidate')
    def perform_as(self, the_actor: Actor) -> None:
        """Shortlist candidate"""
        the_actor.attempts_to(
            # Wait.for_the(RecruitmentPage.SHORTLIST_BTN).to_appear(),
            # Click.on_the(RecruitmentPage.SHORTLIST_BTN)
            ClickOnElement.click_on_element(RecruitmentPage.SHORTLIST_BTN)
        )

    

