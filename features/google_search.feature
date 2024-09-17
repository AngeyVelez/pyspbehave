Feature: Búsqueda en Google
  Como usuario
  Quiero buscar en Google
  Para poder obtener resultados de búsqueda

  Scenario: Realizar una búsqueda en Google
    Given que el usuario está en la página principal de Google
    When el usuario busca "Screenplay Pattern"
    Then el usuario debería ver resultados de búsqueda
