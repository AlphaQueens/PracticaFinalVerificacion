Feature: testing reset

  Scenario: Access initial page


      When I submit a valid public twitter account
      Then I am redirected to the initial page

      When I submit an invalid public twitter account
      Then I am redirected to initial page

      When I submit a valid private twitter account
      Then I am redirected to the principal page

      When I submit a valid public twitter account with no recent tweets
      Then I am redirected to the main page
