from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.questions import List
from screenpy_selenium import Target

class ClickOnElementAtIndex:
    """Tarea para hacer clic en un elemento en un índice específico de una lista."""

    def __init__(self, target: Target, index: int) -> None:
        self.target = target
        self.index = index

    @beat("{} hace clic en el elemento en el índice {} de la lista {}")
    def perform_as(self, the_actor: Actor) -> None:
        elements = List.of(self.target).answered_by(the_actor)
        if self.index < 0 or self.index >= len(elements):
            raise IndexError(f"Índice {self.index} fuera de rango. Hay {len(elements)} elementos disponibles.")
        the_actor.attempts_to(
            Click.on(elements[self.index])
        )

    @staticmethod
    def on(target: Target, idx: int) -> "ClickOnElementAtIndex":
        return ClickOnElementAtIndex(target, idx)