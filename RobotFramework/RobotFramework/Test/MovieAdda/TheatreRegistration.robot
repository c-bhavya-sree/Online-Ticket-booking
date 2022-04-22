*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
Verify theatre registration
    Open Browser  http://127.0.0.1:5000/admin_login?admin_sign_in=  chrome
    Maximize Browser Window
    Click Link  Xpath://html/body/div[2]/form/table/tbody/tr[5]/td[1]/a
    Input Text  //input[@name='owner_name']  Rahul
    Input Password  //input[@name='theater_password']   1234
    Input Text  //input[@name='theater_name']  Rahul Cinema
    Input Text  //input[@name='place']  bahadurgarh
    Input Text  //input[@name='timing']  Morning, Afternoon , Evening
    Input Text  //input[@name='number_of_screen']  5
    Register  //button[normalize-space()='Register']  [Return]
    Close Browser

*** Keywords ***
