*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
verify admin login and veiw movie
    Open Browser   http://127.0.0.1:5000/admin_login?admin_sign_in=  chrome
    Maximize Browser Window
    Input Text  //input[@name='user_name']  admin
    Input Password  //input[@name='user_password']  12345
    Press Keys  Xpath://html/body/div[2]/form/table/tbody/tr[5]/td[2]/button  [Return]
    Press Keys  Xpath://html/body/div[2]/table/tbody/tr[2]/td/button  [Return]

    Close Browser

*** Keywords ***
