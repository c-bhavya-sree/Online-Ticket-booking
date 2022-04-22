*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
verify user login
    Open Browser   http://127.0.0.1:5000/user_login?user_sign_in=  chrome
    Maximize Browser Window

    Input Text  //input[@name='user_email']  p@gmail.com
    Input Password  //input[@name='user_password']  asdf
    Press Keys  //button[normalize-space()='Sign in']  [Return]
    Close Browser

*** Keywords ***
