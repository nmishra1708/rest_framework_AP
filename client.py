import requests  


url = "http://127.0.0.1:8000/api/user_list"
response = requests.get(url)
print(response.json())














# def get_token():
#     url = "http://127.0.0.1:8000/api/auth/"
#     response = requests.post(url, data={'username':'admin', 'password':'admin@123'})
#     print(response.json())

# def get_data():
#     url = "http://127.0.0.1:8000/api/user_list/"
#     header = {'Authorization':f'Token{get_token()}'}
#     response = requests.get(url, headers=header)
#     emp_data = response.json()
#     for e in emp_data:
#         print(e)


# get_token()
