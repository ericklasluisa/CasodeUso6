Feature: Actualizar vehículo

  Scenario: Actualizar un vehiculo
    Given Se inicia el navegador actualizar vehiculo
    When Entra a la seccion actualizar vehiculo
    And Aplasta el icono para editar vehiculo
    And Actualizar en vehiculo el campo Marca Chevrolet
    And Actualizar en vehiculo el campo Modelo Montana
    And Actualizar en vehiculo el campo Kilometraje 10800
    And Seleccionar en vehiculo el tipo de combustible Electrico
    And Actualizar en vehiculo el campo Peso 120
    Then Aplastar el boton para editar vehiculo
    And Visualizar alerta confirmacion actualizacion vehiculo

  Scenario: Ingresar una marca incorrecta
    Given Se inicia el navegador actualizar vehiculo
    When Entra a la seccion actualizar vehiculo
    And Aplasta el icono para editar vehiculo
    And Actualizar en vehiculo el campo Marca 123
    Then Aplastar el boton para editar vehiculo
    And Visualizar alerta confirmacion actualizacion vehiculo

  Scenario: Ingresar un modelo incorrecto
    Given Se inicia el navegador actualizar vehiculo
    When Entra a la seccion actualizar vehiculo
    And Aplasta el icono para editar vehiculo
    And Actualizar en vehiculo el campo Modelo 123
    Then Aplastar el boton para editar vehiculo
    And Visualizar alerta confirmacion actualizacion vehiculo

  Scenario: Ingresar un kilometraje incorrecto
    Given Se inicia el navegador actualizar vehiculo
    When Entra a la seccion actualizar vehiculo
    And Aplasta el icono para editar vehiculo
    And Actualizar en vehiculo el campo Kilometraje mil
    Then Aplastar el boton para editar vehiculo
    And Visualizar alerta confirmacion actualizacion vehiculo

  Scenario: Ingresar un peso incorrecto
    Given Se inicia el navegador actualizar vehiculo
    When Entra a la seccion actualizar vehiculo
    And Aplasta el icono para editar vehiculo
    And Actualizar en vehiculo el campo Peso cien
    Then Aplastar el boton para editar vehiculo
    And Visualizar alerta confirmacion actualizacion vehiculo

  
