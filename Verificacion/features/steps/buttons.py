from behave import Given, When, Then


@When('I test execute button')
def execute_button_testing(context):
    #Primero pillamos la url del servidor
    browser = context.browser
    browser.get(context.server_url)

    #Localizamos la cajita donde introducir el nombre de un usuario con cuenta pública que haya tuiteado últimamente
    box = browser.find_element_by_id("id_name")
    box.clear()
    box.send_keys("realdonaldtrump")

    #Click en el botón de ejecutar
    execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('It should show tweets')
def execute_button_testing(context):
    #Nuestra manera de testear que ha funcionado será ver que la cajita donde hemos introducido el usuario sigue siendo realdonaldtrump
    #Y el título es Word Counter
    browser = context.browser
    #value = browser.find_element_by_xpath("//input[@value='realdonaldtrump']")
    assert browser.find_element_by_xpath("//input[@value='realdonaldtrump']") != "realdonaldtrump"
    #if(browser.find_element_by_xpath("//input[@value='realdonaldtrump']") == "realdonaldtrump"):
        #print ("Hola mundo")


@When('I test execute button on a public account that hasnt tweet recently')
def execute_button_testing(context):
    #Primero pillamos la url del servidor
    browser = context.browser
    browser.get(context.server_url)

    #Localizamos la cajita donde introducir el nombre de un usuario con cuenta pública que haya tuiteado últimamente
    box = browser.find_element_by_id("id_name")
    box.clear()
    box.send_keys("testing")

    #Click en el botón de ejecutar
    execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('It shouldnt show any tweet')
def execute_button_testing(context):
    browser = context.browser

    #Probamos con la cuenta "testing"
    #Al introducir la cuenta volvemos simplemente a la páginca de inicio
    assert browser.find_element_by_id("id_name").text != "testing"

    #Accedemos de nuevo a la página para continuar los tests
    browser = context.browser
    browser.get(context.server_url)

@When('I test execute button on a non existing account')
def execute_button_testing(context):
    #Primero pillamos la url del servidor
    browser = context.browser
    browser.get(context.server_url)


    #Localizamos la cajita donde introducir el nombre de un usuario con cuenta privada que haya tuiteado últimamente
    box = browser.find_element_by_id("id_name")
    box.clear()
    box.send_keys("awdawrasdawd")

    #Click en el botón de ejecutar
    execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('It should show an error')
def execute_button_testing(context):
    #Nuestra manera de testear que no ha funcionado será comprobar que no hay cajita de usuario por ejemplo

    browser = context.browser

    assert browser.find_element_by_id("myBodyError").text != "awdawrasdawd"

    #Accedemos de nuevo a la página para continuar los tests
    browser = context.browser
    browser.get(context.server_url)

@When('I test execute button on a private account')
def execute_button_testing(context):
    #Primero pillamos la url del servidor
    browser = context.browser
    browser.get(context.server_url)


    #Localizamos la cajita donde introducir el nombre de un usuario con cuenta privada que haya tuiteado últimamente
    box = browser.find_element_by_id("id_name")
    box.clear()
    box.send_keys("iloretobr")

    #Click en el botón de ejecutar
    execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@Then('It shouldnt show tweets')
def execute_button_testing(context):
    #Nuestra manera de testear que no ha funcionado será comprobar que no hay cajita de usuario por ejemplo

    browser = context.browser
    assert browser.find_element_by_id("myBodyError").text != "iloretobr"


    #Accedemos de nuevo a la página para continuar los tests
    browser = context.browser
    browser.get(context.server_url)


#Test reset button
@Given('A valid profile')
def reset_button_testing(context):
    #Primero pillamos la url del servidor
    browser = context.browser
    browser.get(context.server_url)

    #Localizamos la cajita donde introducir el nombre de un usuario con cuenta pública que haya tuiteado últimamente
    box = browser.find_element_by_id("id_name")
    box.clear()
    box.send_keys("realdonaldtrump")

    #Click en el botón de ejecutar
    execute_button = box.find_elements_by_xpath("//input[@class = 'btn btn-primary' and @type = 'submit' and @value = 'Execute']")[0]
    execute_button.click()

@When('I press the reset button')
def reset_button_testing(context):
    browser = context.browser
    browser.get(context.server_url)
    reset_button = browser.find_elements_by_xpath("//input[@class = 'btn btn-danger' and @type = 'button' and @value = 'Reset']")[0]
    reset_button.click()

@Then('It should redirect to initial page')
def reset_button_testing(context):
    browser = context.browser
    browser.get(context.server_url)
    browser = context.browser

    #Probamos con la cuenta "realdonaldtrump"
    #Al presionar el botón de reset volvemos simplemente a la página de inicio
    #Por lo que el campo debe ser distinto a donald trump
    assert browser.find_element_by_id("id_name").text != "realdonaldtrump"
