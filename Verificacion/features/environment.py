from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox(executable_path= r'C:\Django projects\Prueba\Verificacion\geckodriver\geckodriver.exe')
    context.browser.implicitly_wait(1)
    context.server_url = 'http://127.0.0.1:8000/'

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass
