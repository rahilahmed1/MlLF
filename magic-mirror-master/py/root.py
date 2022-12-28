from selenium import webdriver
import weather as w

def initWeather():
    #Initialize weather widget
    weather = w.getCurrentWeather()
    setWeather(weather)

def setWeather(weather):
    weather_script = f"""
    $('#humidity')[0].innerHTML = {weather['humidity']};
    $("#pressure")[0].innerHTML = {weather['pressure']};
    $("#mintemp")[0].innerHTML = {round(weather['mintemp'])};
    $("#maxtemp")[0].innerHTML = {round(weather['maxtemp'])};
    $('#desc')[0].innerHTML = '{weather['description']}';
    $('#te')[0].innerHTML = '{round(weather['temp'])}';
    $("#image").attr("src",'img/{weather['icon']}.png');
    """
    driver.execute_script(weather_script)

def next():
    driver.find_element_by_class_name('next').click()
    pos+=1

def prev():
    driver.find_element_by_class_name('previous').click()
    pos-=1

driver = webdriver.Chrome()
driver.get("file:///C:/Users/mjk/Downloads/Magic_Mirror/web_page/prototype.html")
pos = 0
initWeather()
# Set home position
for i in range(2):
        driver.find_element_by_class_name('next').click()
