from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import List
from screenpy_selenium import Target

class ClickOnElementAtIndex:
    """Task to click on an item in a specific index of a list."""

    def __init__(self, target: Target, index: int) -> None:
        self.target = target
        self.index = index

    @beat("{} clicks on the item in the 'index' of 'target'")
    def perform_as(self, the_actor: Actor) -> None:
        elements = self.target.all_found_by(the_actor)
        if self.index < 0 or self.index >= len(elements):
            raise IndexError(f"Index {self.index} out of range. There are {len(elements)} available items.")
        elements[self.index].click()

    @staticmethod
    def on(target: Target, idx: int) -> "ClickOnElementAtIndex":
        return ClickOnElementAtIndex(target, idx)