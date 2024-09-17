from screenpy import Actor
from screenpy.pacing import beat
from selenium.webdriver.common.keys import Keys
from screenpy_selenium.actions import Enter, Wait, Click
from screenplay.ui.google_home import GoogleHomePage

class CloseCookieNoticeGoogle:
    """Tarea para cerrar el aviso de cookies en Google."""

    @staticmethod
    def close_cookie_notice():
        """Cerrar el aviso de cookies."""
        return CloseCookieNoticeGoogle()

    @beat('Cerrando el aviso de cookies...')
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to close the cookie notice."""
        the_actor.attempts_to(
            Wait.for_the(GoogleHomePage.ACCEPT_COOKIES),
            Click.on_the(GoogleHomePage.ACCEPT_COOKIES),
        )
