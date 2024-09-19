# pyspbehave
This project is an automated testing suite using [Behave](https://behave.readthedocs.io/en/latest/) and [ScreenPy](https://screenpy-docs.readthedocs.io/en/latest/). The goal is to automate tests for different functionalities of a web application.

## Project Structure


├── .gitignore
├── env/
│   ├── Lib/
│   ├── Scripts/
│   ├── pyvenv.cfg
├── example.log
├── features/
│   ├── add_candidate.feature
│   ├── environment.py
│   ├── google_search.feature
│   ├── login.feature
│   ├── shortlist_candidate.feature
│   ├── steps/
│   │   ├── __init__.py
│   │   ├── ...
├── README.md
├── requirements.txt
├── screenplay/
│   ├── questions/
│   ├── tasks/
│   ├── ui/

## Installation

1. Clone the repository:
  sh
  git clone <REPOSITORY_URL>
  cd <REPOSITORY_NAME>
  

2. Create and activate a virtual environment:
  sh
  python -m venv env
  source env/Scripts/activate  # On Windows
  source env/bin/activate      # On Unix or MacOS
  

3. Install the dependencies:
  sh
  pip install -r requirements.txt
  

## Directory Structure

- [features/]: Contains the .feature files that describe the test scenarios in Gherkin language.
  - add_candidate.feature: Tests related to adding candidates.
  - google_search.feature: Tests related to Google search.
  - login.feature: Tests related to login.
  - shortlist_candidate.feature: Tests related to shortlisting candidates.
  - steps/: Contains the Python files that implement the steps defined in the .feature files.

- [screenplay/]: Contains the implementation of the Screenplay pattern.
  - questions/: Contains the questions that actors can ask about the state of the application.
  - tasks/: Contains the tasks that actors can perform.
  - ui/: Contains the user interface selectors.

## Running Tests

To run the tests, use the following command:

sh
behave

