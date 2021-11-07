import requests

url="http://127.0.0.1:8000/api/users_list/"
ur="http://127.0.0.1:8000/api/auth/"
d={'username':'bhavs','password':'codechef'}
#response=requests.post(ur,d)
#print(response.json())
def get_token():
    response=requests.post(ur,d)
    return response.json()

def get_data():
    header={'Authorization':f'Token {get_token()}'}
    response=requests.get(url,headers=header)
    #print(response.json())
    emp=response.json()
    for e in emp:
        print(e)


def create_new():
    header={'Authorization':f'Token {get_token()}'}
    data={
    "employee_id":"12",
    "name":"TBG",
    "ranking":5,
    "age":10
    }
    response=requests.post(url,data=data ,headers=header)
    print(response.text)


def edit_data(employee_id):
	u=url+"{employee_id}/"
    header={'Authorization':f'Token {get_token()}'}
    data={
    "employee_id":"12",
    "name":"TBG",
    "ranking":5,
    "age":10
    }
    response=requests.put(u,data=data ,headers=header)
    print(response.text)


def delete(employee_id):
	u=url+"{employee_id}/"
    header={'Authorization':f'Token {get_token()}'}
    response=requests.delete(u,headers=header)
    print(response.status_code)