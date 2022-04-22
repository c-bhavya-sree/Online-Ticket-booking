*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
verify theatre owner login
    Open Browser   http://127.0.0.1:5000/admin_login?admin_sign_in=  chrome
    Maximize Browser Window

    Input Text  //input[@name='user_email']  p@gmail.com
    Input Password  //input[@name='user_password']  asdf
    Press Keys  //button[normalize-space()='Sign in']  [Return]
    Press Keys  Xpath://html/body/div[2]/div[3]/div[1]/div/div[1]/div/div[2]/button[1]/a  [Return]

    Close Browser

*** Keywords ***