Feature: testing execute

  Scenario: Access tweets page


      When I submit a valid public twitter account
      Then I am redirected to the tweets page

      When I submit an invalid public twitter account
      Then I am redirected to the error page

      When I submit a valid private twitter account in box
      Then I am redirected to error page

      When I submit a valid public twitter account with no tweets
      Then I am redirected to the start page
