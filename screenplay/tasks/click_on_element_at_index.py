import time
from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import List
from screenpy_selenium import Target

class ClickOnElementAtIndex:
    """Task to click on an item in a specific index of a list."""

    @staticmethod
    def on(target: Target, idx: int) -> "ClickOnElementAtIndex":
        return ClickOnElementAtIndex(target, idx)

    @beat("{} hace clic en el elemento en el índice 'index' de 'target'")
    def perform_as(self, the_actor: Actor) -> None:
        elements = self.target.all_found_by(the_actor)
        # print(f"Elementos: {elements}")
        if self.index < 0 or self.index >= len(elements):
            raise IndexError(f"Index {self.index} out of range. There are {len(elements)} available items.")
        # print(f"Elemento: {elements[self.index].text}")
        elements[self.index].click()
        time.sleep(3)

    def __init__(self, target: Target, index: int) -> None:
        self.target = target
        self.index = index
