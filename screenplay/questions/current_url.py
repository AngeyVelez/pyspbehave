from screenpy import Actor
from screenpy_selenium.questions import BrowserURL

class CurrentURL:
    """Ask to get current url."""

    @staticmethod
    def answered_by(actor: Actor) -> str:
        return BrowserURL().answered_by(actor)


