#import requests
#from requests.auth import HTTPBasicAuth
from woocommerce import API

wcapi = API(
    url="https://drinkbomani.com/",
    #consumer_key="ck_8d47d8d1d6af1988093a6ec2db9597471120b08d",
    #consumer_secret="cs_c2064409bd4f8309e2defad029ea67ace9065659",
    version="wc/v3"
)

print(wcapi.get("products", params={"per_page": 20}).json())
print(wcapi.get("").json())






# WooCommerce store credentials

# base_url = "https://drinkbomani.com/shop/merch/"
# consumer_key = "ck_db1f448b703febe39887ad26e7c2b1562df7b819"
# consumer_secret = "cs_822f6635001c827e2b9a2f84944123b5d9cb1db5"

# # Fetch products from the API
# response = requests.get(
#     f"{base_url}products",
#     auth=HTTPBasicAuth(consumer_key, consumer_secret)
# )

# if response.status_code == 200:
#     try:
#         #products = response.json()  # Attempt to parse JSON
#         #print("Product Data:", products)
#         print(response.text)

#     except requests.exceptions.JSONDecodeError as e:
#         print("JSONDecodeError:", e)
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")
#     print(f"Response text: {response.text}")
