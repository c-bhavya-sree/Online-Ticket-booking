*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
this is a sample test case
    Open Browser   https://www.google.com/  chrome
    Maximize Browser Window

    Close Browser
*** Keywords ***
