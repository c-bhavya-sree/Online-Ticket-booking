*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
verify new user registration
    Open Browser   http://127.0.0.1:5000/user_register  chrome
    Maximize Browser Window
    Input Text  //input[@name='user_name']  kapil
    Input Password  //input[@name='user_password']  1234
    Input Text  //input[@name='user_mobile']  9856321475
    Input Text  //input[@name='user_mail']  K@gmail.com
    Input Text  //input[@name='user_place']  Faridabad
    Press Keys  //button[normalize-space()='Sign up']  [Return]
    Close Browser

*** keywords ***
