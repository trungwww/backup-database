*** Settings ***
Documentation hàm dựng sẵn cho keywords
Documentation
Library    SeleniumLibrary


*** Variables ***
${x}    10
${y}    10


*** Test Cases ***
So sánh hai bien
#so sánh
    Should Be Equal    ${x}    ${y}
#điều kiện
    IF    ${x} == ${y}
        Log To Console    hai biến bằng nhau
    ELSE
        Log To Console    hai biến không bằng nhau
    END

vòng lặp
    # for i in range
    FOR To Console    ${i}    IN RANGE 10
        Log    ${1}
    END
xử lí lỗi
    TRY
        Click Elenment    id=btn-login
    EXCEPT
        Log To Console    không tìm thấy btn login
    END
    