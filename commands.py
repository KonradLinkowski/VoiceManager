from selenium import webdriver
from os import system

driver_path = './chromedriver'

def web_click(video_name, site):
    print(f'Opening {site + video_name}')
    ff = webdriver.Chrome(executable_path=driver_path)
    ff.get(site + video_name)
    element = ff.find_element_by_id("video-title")
    element.click()

def web(query_name, site):
    print(f'Opening {site + query_name}')
    ff = webdriver.Chrome(executable_path=driver_path)
    ff.get(site + query_name)

def run(name):
    print(f'Running {name}')
    system(name)

def run_path(path):
    print(f'Running {path}')
    system(path)

def run_command(command):
    print(f'Running command {command}')
    system(command)
