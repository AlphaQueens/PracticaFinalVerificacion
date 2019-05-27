Feature: testing buttons

  Scenario: Test execute button

        When I test execute button
        Then It should show tweets

        When I test execute button on a public account that hasnt tweet recently
        Then It shouldnt show any tweet

        

        When I test execute button on a non existing account
        Then It should show an error

  Scenario: Test reset button

        Given A valid profile
        When I press the reset button
        Then It should redirect to initial page
