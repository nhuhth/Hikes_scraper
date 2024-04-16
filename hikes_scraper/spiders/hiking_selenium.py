import scrapy
import selenium
from bs4 import BeautifulSoup
import time
import re
import numpy as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class HikingSeleniumSpider(scrapy.Spider):
    name = "hiking_selenium"
    allowed_domains = ["www.komoot.com"]
    start_urls = ["https://www.komoot.com/discover/Poland/@52.2159330,19.1344220/tours?sport=hike&map=true&regionId=2486&max_distance=4.82"]

#
    def __init__(self):
        options_chrome = webdriver.ChromeOptions()
        options_list = ["--incognito","--no-sandbox","--disable-notifications","--disable-infobars","--disable-extensions","--disable-web-security"]
        for i in options_list:
            options_chrome.add_argument(i)
        service_chrome = webdriver.chrome.service.Service(ChromeDriverManager().install()) 
        self.driver = webdriver.Chrome(service=service_chrome, options=options_chrome) 
        self.item = {'Name': [], 'Level': [], 'Rating': [], 'Duration': [], 'Distance': [], 'Height': []}

        
    def parse(self, response):
        self.driver.get(response.url)
        
        # Turn off banner
        self.turn_off_banner()
        
        #loggin to explore more data
        self.login()

        time.sleep(np.random.chisquare(1)+3)
        self.data() 
    
        for i in range(1,5):
                if i == 1:
                    WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]")))
                    self.driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]").click()
           
                else:
                    WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/button[2]")))
                    self.driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/button[2]").click() 

                self.data() 
        
    
    def data(self):
    
            time.sleep(np.random.chisquare(1) + 3)  # More natural-looking delays

            # Use Selenium for dynamic content, BeautifulSoup for parsing
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
           
            # Function lambda
            append_data = lambda elements, key: [self.item[key].append(element.text) for element in elements]

            # Extracting and appending data
            #names
            names = soup.find_all('strong')
            append_data(names, "Name")

            # levels
            levels = soup.find_all('div', {'class': 'css-elu0ie'})
            append_data(levels, "Level")

            # durations
            durations = soup.find_all('span', attrs={'data-test-id': 't_duration_value'})
            append_data(durations, "Duration")

            #rating
            ratings = soup.find_all('div', {'class': 'css-xlo6ik'})
            for element in ratings:
                match = re.search(r'css-1rt9qp4', str(element)) # use regex
                if match:
                    self.item["Rating"].append(float(element.find('p', {'class': 'css-1rt9qp4'}).text))
                else:
                    self.item["Rating"].append(0)

            #distance
            distances = soup.find_all('span', attrs={'data-test-id': 't_distance_value'})
            for element in distances:
                self.item["Distance"].append(float(re.search(r'[\d.]+', element.text).group()))

            #uphill
            uphills = soup.find_all('span', attrs={'data-test-id': 't_elevation_up_value'})
            for element in uphills:
                self.item["Height"].append(re.search(r'([\d,]+(?:\.\d+)?)', element.text).group()) 

    def turn_off_banner(self):
        # Cookies consent
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '''//*[@data-testid="gdpr-banner-accept"]''')))
        time.sleep(np.random.chisquare(1) + 3)
        self.driver.find_element("xpath", '''//*[@data-testid="gdpr-banner-accept"]''').click()
    
    def login(self):
        # Login
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sign up or log in')]")))
        time.sleep(np.random.chisquare(1)+3)
        self.driver.find_element("xpath", "//a[contains(text(),'Sign up or log in')]").click()

        time.sleep(1)

        #login by email
        login = self.driver.find_element("xpath", "//input[@id='email']") 
        login.send_keys("mailracbalan@gmail.com")

        WebDriverWait(self.driver, 30).until(
             EC.visibility_of_element_located((By.XPATH, "//body/div[@id='pageMountNode']/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[4]/button[1]")))
        
        self.driver.find_element("xpath", "//body/div[@id='pageMountNode']/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[4]/button[1]").click()

        time.sleep(1)
        #for password
        password = self.driver.find_element("xpath", "//input[@id='password']")
        password.send_keys("webds123")

        time.sleep(np.random.chisquare(1)+3)

        self.driver.find_element("xpath", "//button[contains(text(),'Log In')]").click()

    def save_data(self):
        data = pd.DataFrame(self.item)
        data['Height'] = data['Height'].apply(lambda x: x.replace(',', ''))
        data['Duration'] = data['Duration'].apply(lambda x: round((int(x.split(':')[0]) + int(x.split(':')[1])/60), 2))
        data.to_csv("recommend_web/komoot1.csv", encoding="utf-8", index=False)
         
    def closed(self, reason):
        self.save_data()
        self.driver.quit()
