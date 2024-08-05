Feature: Actualizar vehículo

  Scenario: Actualizar un vehiculo
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón editar
    And Actualizar el campo Marca Chevrolet
    And Actualizar el campo Modelo Montana
    And Actualizar el campo Kilometraje 10800
    And Seleccionar el tipo de combustible Electrico
    And Actualizar el campo Peso 120
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar una marca incorrecta
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón editar
    And Actualizar el campo Marca 123
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un modelo incorrecto
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón editar
    And Actualizar el campo Modelo 123
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un kilometraje incorrecto
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón editar
    And Actualizar el campo Kilometraje mil
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un peso incorrecto
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón editar
    And Actualizar el campo Peso cien
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  
