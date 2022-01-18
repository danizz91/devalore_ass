# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import instance as instance
import instanceof as instanceof
import requests
import json
import pytest
from pip._vendor.requests import RequestException


def exchangeratesapi(env):
    # Checking the env
    if env == 'Prod':
        # sending request to API with method 'GET'
        print('Sending request to API..')
        try:
            req = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=2911001d41881e8b35d9df0332612890')
            return json.loads(req.text)
        except requests.exceptions.RequestException as e:
            print('Failed to send request to API')
            raise SystemExit(e)
    elif env == 'Dev':
        # reading from mock
        print('Reading from mock..')
        try:
            f = open('mock.json')
            data = json.load(f)
            return data
        except IOError:
            print("Error: File does not appear to exist.")
            exit(1)
    else:
        print('Wrong environments variable');
        exit()



def checkRateLowerThan(rates):
    filterList = []
    # Iterating all rates to check if the value is lower than 10
    for key in rates:
        if rates[key] < 10:
            filterList.append(key)
    return filterList


#Checking the success status that comes from the API
def test_checkIfRequestSuccess():
    assert exchangeratesapi('Prod')['success'] == True

#Check if the function checkRateLowerThan returns list
def test_jsonStructure():
    obj = exchangeratesapi('Prod');
    assert type(checkRateLowerThan(obj['rates'])) == list




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   obj = exchangeratesapi('Prod');
   print(checkRateLowerThan(obj['rates']));

