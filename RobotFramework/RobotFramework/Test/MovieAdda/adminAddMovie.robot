*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
verify admin login and veiw movie
    Open Browser   http://127.0.0.1:5000/admin_login?admin_sign_in=  chrome
    Maximize Browser Window
    Input Text  //input[@name='user_name']  admin
    Input Password  //input[@name='user_password']  12345
    Press keys  //button[normalize-space()='Sign in']  [Return]
    Press Keys  //button[normalize-space()='Add Movie']  [Return]
    Input Text  Xpath://html/body/div/form/table/tbody/tr[4]/td[2]/textarea  Jab We Met
    Input Text  Xpath:/html/body/div/form/table/tbody/tr[8]/td[2]/input  Jab We Met (English: When We Met) is a 2007 Indian romantic comedy film.
    Input Text  //input[@name='duration']  2h48m
    Input Text  //input[@name='rating']  8.7
    Input Text  //input[@name='languages_available']  hindi
    Input Text  //input[@name='genre']  comedy,Drama
    Input Text  //input[@name='ticket_cost']  250
    Input Text  //input[@name='trailer']  https://www.youtube.com/watch?v=WiMIxwX4MjI
    Press Keys  //button[normalize-space()='Add movie']  [Return]
    Close Browser

*** Keywords ***
