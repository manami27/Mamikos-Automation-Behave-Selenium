Feature: Mamikos Booking Room with Login Previously

  Scenario: Login to Mamikos Website with valid parameters
    Given launch chrome browser
    When open Mamikos homepage
    And click on Masuk button
    And click on Pencari Kos button
    And Enter nohp "085100733977" and password "mamikos12345"
    And click on Login button
    And open room detail page
    And select mulai kos and cara bayar
    And click on Ajukan Sewa button
    And next to booking summary page
    Then booking success confirmation