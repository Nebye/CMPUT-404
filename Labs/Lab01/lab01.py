"""
Cmput 404 - Lab 01
"""
import requests


def main():
    #  prints out the version of the requests library
    print("Version of requests library installed on the system is "+ requests.__version__)
    
    # GET the Google homepage
    numFive = requests.get("http://www.google.com/")
    print(numFive.status_code)
    
    # Downloads itself from GitHub and prints out its own source code from GitHub
    rawURL = "https://raw.githubusercontent.com/Nebye/Cmput404/main/Labs/Lab01/lab01.py"
    print(requests.get(rawURL).text)
    

main()