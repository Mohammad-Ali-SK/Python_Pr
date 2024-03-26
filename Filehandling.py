import json
import requests
from pymongo import MongoClient


def free_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(data)
    
    
    if data['success'] and "data" in data:
        user_data = data['data']
        user_name = user_data['login']['username']
        user_id = user_data['id']
        user_email = user_data['email']
        
        return user_name, user_id, user_email
    else:
        raise Exception('Falid to fetch API.')


client = MongoClient('mongodb://localhost:27017/')
db = client['March_26']
colection = db['ytManager']


def list_users():
    all_user = colection.find()
    for i in all_user:
        print(f'ID :{i['_id']} Name : {i['name']} Email : {i['email']}')

def add_user(vid_id,vid_name,email):
    # print(a)
    colection.insert_one({'_id': vid_id, 'name' : vid_name, 'email' : email})


def update_user(vid_id,vid_name,vid_time):
    colection.update_one(
        {'_id':vid_id},
        {"$set" : {'name':vid_name, 'email': vid_time}}
    )

def delete_user(vid_id):
    colection.delete_one({'_id':vid_id})





def main():
    
    # a,b,c = free_api()
    
    while True:
        print(f'\n YOutube manager | Chosen Option')
        print('1. List all user details.')
        print('2. Add a new user_.')
        print('3. Update user details.')
        print('4. Delete user details.')
        print('5. Exit the app.')
        choice = input('Enter your choice..')
        
        user_name,user_id,user_email = free_api()
       
        match choice:
           case '1':
               list_users()
           case '2':
                add_user(user_id, user_name, user_email)
           case '3':
               user_id_2 =  int(input('Enter user id to update details___'))
               user_name = input('Enter the new user name__')
               user_email = input('Enter the new user email___')
               update_user(user_id_2,user_name,user_email)
           case '4':
               user_id_3 = int(input('Enter user id to delete details__'))
               delete_user(user_id_3)
           case '5':
                break
           case _:
                print('Enter the valid num__')
   
   
   
   
   

if __name__ == '__main__':
    main()