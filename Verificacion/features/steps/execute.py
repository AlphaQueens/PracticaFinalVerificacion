from behave import Given, When, Then



@when('I submit a valid public twitter account ')
def test_execute_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("realdonaldtrump")

    execute_button = firefox_browser.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@then('I am redirected to the tweets page ')
def test_execute_button(context):
    firefox_browser = context.firefox_browser

    # Check success
    # Checkeamos que la página ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text == "realdonaldtrump"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text == "Word counter"

@When('I submit an invalid public twitter account ')
def test_execute_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("awdasraweadsads")

    execute_button = firefox_browser.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('I am redirected to the error page ')
def test_execute_button(context):
    firefox_browser = context.firefox_browser

    # Check fail
    # Checkeamos que la página no ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text != "awdasraweadsads"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text != "Word counter"


@When('I submit a valid private twitter account in box')
def test_execute_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("iloretobr")

    execute_button = firefox_browser.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('I am redirected to error page')
def test_execute_button(context):
    firefox_browser = context.firefox_browser

    # Check fail
    # Checkeamos que la página no ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text != "iloretobr"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text != "Word counter"

@When('I submit a valid public twitter account with no tweets')
def test_execute_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("testing")

    execute_button = firefox_browser.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('I am redirected to the start page')
def test_execute_button(context):
    firefox_browser = context.firefox_browser

    # Checkeamos de la siguiente manera
    # El input box estará vacío así que no tendrá "testing"
    # Pero esta vez sí que tendrá título "Word counter"
    # Distinto a si fallase

    assert firefox_browser.find_element_by_id("id_name").text != "testing"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text == "Word counter"
