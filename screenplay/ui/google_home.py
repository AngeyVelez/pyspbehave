from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class GoogleHomePage:
    """Elementos de la página principal de Google."""
    
    SEARCH_BAR = Target.the("Google search bar").located_by((By.NAME, "q"))
    RESULTS = Target.the("Google search results").located_by((By.ID, "search"))
    ACCEPT_COOKIES = Target.the("Accept cookies button").located_by((By.ID, "L2AGLb"))
    URL = "https://www.google.com"