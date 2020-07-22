#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:52:44 2020

@author: andynystrom
"""


import requests
import csv

url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/case-hosp-death.csv'
response = requests.get(url)

wrapper = csv.reader(response.text.strip().split('\n'))

for record in wrapper:
    date = (record[0])
    case_count = (record[1])
    hospitalizes_count = (record[2])
    death_count = (record[3]) 

print("Date: " + date)
print("New cases: " + case_count)
print("New hospitalizations: " + hospitalizes_count) 
print("Deaths yesterday: " + death_count)


