# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:30:28 2021

@author: jubis
"""

from kiteconnect import KiteConnect
from selenium import webdriver
import time
import os

print("Running ?")


def login():
    print("Running ??")
    token_path = "my_det.txt"
    key_secret = open(token_path,"r").read().split()
    kite = KiteConnect(api_key = key_secret[0])
    service = webdriver.chrome.service.Service("./chromedriver")
    service.start()
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, options)
    driver.get(kite.login_url())
    driver.implicitly_wait(10)
    username = driver.find_element_by_xpath('//*[@id="userid"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.send_keys(key_secret[2])
    password.send_keys(key_secret[3])
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/form/div[4]/button').click()
  
    pin = driver.find_element_by_xpath('//*[@id="pin"]')
    pin.send_keys(key_secret[4])
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/form/div[3]/button').click()
    time.sleep(10)
    token_text = "request_token"
    request_token=driver.current_url.split('&')
    print("request_token array",request_token)
    for x in request_token:
        tok = x.split("=")
        if(tok[0]== token_text):
            print("tok[0]",tok[0])
            print("tok[1]",tok[1])
            with open('request_token.txt', 'w') as the_file:
                the_file.write(tok[1])
            break
    driver.quit()
    
    
login()
    
#generating and storing access token - valid till 6 am the next day
request_token = open("request_token.txt",'r').read()
key_secret = open("my_det.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
data = kite.generate_session(request_token, api_secret=key_secret[1])
with open('access_token.txt', 'w') as file:
        file.write(data["access_token"])