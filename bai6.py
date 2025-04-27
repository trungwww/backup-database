import requests # pip install requests
import pandas as pd # pip install pandas

def get_data_motel():
    url = "https://gateway.chotot.com/v1/public/ad-listing?limit=10&protection_entitlement=true&cg=1050&region_v2=3017&st=u,h&key_param_included=true"
    payload = {}
    headers = {}
    response = requests.request("GET",url, headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
        return response.json().get("ads")
    return

phong_tro_datas = get_data_motel()
if phong_tro_datas:
    data_alls = []
    for i_data in phong_tro_datas:
        name = i_data.get("subject")
        price = i_data.get("subject")
        size = i_data.get("size")
        street_name = i_data.get("street_name")
        body = i_data.get("body")
        owner = i_data.get("account_name")
        item = [name, price, size, street_name, body, owner]
        data_alls.append(item)

    df1 = pd.DataFrame(data_alls, columns=["Tiêu đề", "Giá", "Diện tích", "Địa chỉ", "Mô tả", "Chủ sở hữu"])
    df1.to_excel("output_cho_tot.xlsx")