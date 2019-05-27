from behave import Given, When, Then

@When('I submit a valid public twitter account')
def text_reset_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("realdonaldtrump")

    reset_button = box.find_elements_by_xpath("//input[@class = 'btn btn-danger' and @type = 'button' and @value = 'Reset']")[0]
    reset_button.click()

@then('I am redirected to the initial page')
def text_reset_button(context):
    firefox_browser = context.firefox_browser

    # Check success
    # Checkeamos que la página ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text != "realdonaldtrump"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text == "Word counter"

@when('I submit an invalid public twitter account')
def text_reset_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("awdasraweadsads")

    reset_button = box.find_elements_by_xpath("//input[@class = 'btn btn-danger' and @type = 'button' and @value = 'Reset']")[0]
    reset_button.click()

@then('I am redirected to initial page')
def text_reset_button(context):
    firefox_browser = context.firefox_browser

    # Check success
    # Checkeamos que la página ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text != "awdasraweadsads"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text == "Word counter"

@when ('I submit a valid private twitter account')
def text_reset_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("iloretobr")

    reset_button = box.find_elements_by_xpath("//input[@class = 'btn btn-danger' and @type = 'button' and @value = 'Reset']")[0]
    reset_button.click()

@then('I am redirected to the principal page')
def text_reset_button(context):
    firefox_browser = context.firefox_browser

    # Check success
    # Checkeamos que la página ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text != "iloretobr"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text == "Word counter"

@When('I submit a valid public twitter account with no recent tweets')
def text_reset_button(context):
    firefox_browser = context.browser
    firefox_browser.get(context.server_url)
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]')

    firefox_browser.find_element_by_id("id_name").send_keys("testing")

    reset_button = box.find_elements_by_xpath("//input[@class = 'btn btn-danger' and @type = 'button' and @value = 'Reset']")[0]
    reset_button.click()

@then('I am redirected to the main page')
def text_reset_button(context):
    firefox_browser = context.firefox_browser

    # Check success
    # Checkeamos que la página ha funcionado mirando
    # el input box
    # En caso de haber fallado el input box estaría vacío

    assert firefox_browser.find_element_by_id("id_name").text != "testing"
    assert firefox_browser.find_element_by_xpath('//*[@title=Word counter"]').text == "Word counter"
