from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import Text

class IsElementVisible:
    """Pregunta si un elemento está visible en la página."""

    @staticmethod
    def answered_by(result):
        """Realizar una búsqueda con el término especificado."""
        return IsElementVisible(result)

    @beat("{} checks the results message...")
    def perform_as(self, the_actor: Actor) -> bool:
        # return the_actor.driver.find_element(*self.locator).is_displayed()
        return Text.of(self.result).answered_by(the_actor)
    
    def __init__(self, result) -> None:
        self.result = result

