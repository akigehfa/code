import os

# while True:
    
#         os.system('clear')

        # print(' Welcome to The Club')
        # print('====================')
        # print('1. Input your name. ')
        # print('2. Exit.')
        # option = input('Input your options: ')
        
        # if option == '2':
        #     print('Thanks for coming!')
        #     break

        # name = input('Input: ')
        # print('\nHello, Mr.Mrs.', name + '\n')
        # print('=====================')
        
import requests

# Replace 'user' and 'pass' with your actual username and password
url = 'https://httpbin.org/basic-auth/user/pass'
response = requests.get(url, auth=('user', 'pass'))

# Check the HTTP status code
if response.status_code == 200:
    print("Request was successful.")
    print("Content-Type:", response.headers['content-type'])
    print("Encoding:", response.encoding)
    
    # Print the response text
    print(response.text)
    
    # Parse the JSON response
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
