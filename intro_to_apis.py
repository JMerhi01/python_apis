import requests

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_codes_req.status_code)
# # print(post_codes_req.headers)
# print(post_codes_req.content)
# print(post_codes_req.json()) # this .json function is from the requests library
# print(type(post_codes_req.json())) # it's a python dictionary in the format of .json


# post request to postcodes.io
import json

json_body = json.dumps({"postcodes": ["PR3 OSG]", "M45 6GN", "EX165BL"]}) # This is the body.
headers = {"Content-Type": "application/json"} # This is the header

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())