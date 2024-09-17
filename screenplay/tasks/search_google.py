from screenpy import Actor
from screenpy.pacing import beat
from selenium.webdriver.common.keys import Keys
from screenpy_selenium.actions import Enter, Wait
from screenplay.ui.google_home import GoogleHomePage

class SearchGoogle:
    """Tarea para realizar una búsqueda en Google."""

    @staticmethod
    def for_term(search_query):
        """Realizar una búsqueda con el término especificado."""
        return SearchGoogle(search_query)

    @beat('{} searches Google for "{search_query}"')
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to search github for the given term."""
        the_actor.attempts_to(
            Enter.the_text(self.search_query).into(GoogleHomePage.SEARCH_BAR).then_hit(Keys.ENTER),
            Wait.for_the(GoogleHomePage.RESULTS),
        )
    
    def __init__(self, search_query: str) -> None:
        self.search_query = search_query
