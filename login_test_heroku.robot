*** Settings ***
Documentation    viết test case trang login
Library    seleniumLibrary

*** Variables ***
${URl}    https://the-internet.herokuapp.com/login
${URl}    tomsmith
${URl}    SuperScretPassword!

*** Test Cases ***
Invalid Login
    # 1.Mở trình duyệt
    Mở trình duyệt
    # 2.Đăng nhập
    đăng nhập
    # 3.Kiểm tra đăng nhập thành công
    kiểm tra đăng nhập thành công
    # 4.Đóng trình duyệt

*** Keywords ***
Mở trình duyệt
    Open Brower    ${URl}    chrome
    Maximize Brower Window

đăng nhập
    Input Text    id=usernaem    ${USENAME}
    Input Text    id=usernaem    ${PASSWORD}

kiểm tra đăng nhập thành công
    Page Should Contain