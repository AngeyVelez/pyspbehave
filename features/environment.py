from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, filename="example.log")

# Hook that runs before each scenario
def before_scenario(context, scenario):
    logging.info(f"Starting scenario: {scenario.name}")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.actor = Actor.named("Usuario").who_can(BrowseTheWeb.using(context.driver))

# Hook that runs after each scenario
def after_scenario(context, scenario):
    logging.info(f"Ending scenario: {scenario.name}")
    if context.driver:
        context.driver.quit()
