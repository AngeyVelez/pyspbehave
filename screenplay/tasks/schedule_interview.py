import time
from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait
from screenplay.tasks.click_on_element_at_index import ClickOnElementAtIndex
from screenplay.ui.schedule_interview import SceduleInterviewPage

class ScheduleInterview:
    """class Schedule Interview:"""

    @staticmethod
    def schedule_interview(title, interviewer, date):
        """Schedule interview with valid data"""
        return ScheduleInterview(title, interviewer, date)

    @beat('{} create a scedule interview with "title", "interviwer", "date"')
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Wait.for_the(SceduleInterviewPage.TITLE_FIELD),
            Enter.the_text(self.title).into(SceduleInterviewPage.TITLE_FIELD),
            Enter.the_text(self.date).into(SceduleInterviewPage.DATE_FIELD),
            Enter.the_text(self.interviewer).into(SceduleInterviewPage.INTERVIEWER_FIELD),
            Wait.for_the(SceduleInterviewPage.INTERVIEWER_OPTIONS).to_appear(),
            ClickOnElementAtIndex.on(SceduleInterviewPage.INTERVIEWER_OPTIONS, 1)
        )
        time.sleep(2)

    def __init__(self, title: str, interviewer: str, date: str) -> None:
        self.title = title
        self.interviewer = interviewer
        self.date = date


