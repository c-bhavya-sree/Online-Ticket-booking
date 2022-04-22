*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
verify admin_login
    Open Browser  http://127.0.0.1:5000/admin_login?admin_sign_in=  chrome
    Maximize Browser Window
    Input text  //input[@name='user_name']  admin
    Input password  //input[@name='user_password']  12345
    Press keys  //button[normalize-space()='Sign in']  [Return]
    Sleep  02

    Close Browser

*** keywords ***
