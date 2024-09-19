import time
from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium import Target, Wait
from screenpy_selenium.actions import Click
from screenplay.ui.recruitment import RecruitmentPage

class ClickOnElement:
    """xxx"""

    @staticmethod
    def click_on_element(element: Target):
        return ClickOnElement(element)

    @beat('{}xxxx')
    def perform_as(self, the_actor: Actor) -> None:
        """xxxx"""
        the_actor.attempts_to(
            Wait.for_the(self.element).to_appear(),
            Click.on_the(self.element)
        )

    def __init__(self, element: Target):
        self.element = element

    

