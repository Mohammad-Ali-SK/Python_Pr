import json
import requests

def free_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data['success'] and 'data' in data:
        user_data = data['data']
        user_name = user_data['login']['username']
        # user_id = user_data['id']
        user_email = user_data['email']
        
        return user_name,user_email
    else:
        raise Exception('Wrong API details.')

def load_data():
    try:
        with open('user.txt','r') as file:
            return json.load(file)
    except:
        return []
    
def save_data(user_details):
    with open('user.txt','w') as file:
        json.dump(user_details,file)
    
def list_all_user(user_details):
    print('*' * 70)
    print(f'\n')
    for index, user in enumerate(user_details, start=1):
        print(f'{index}. Name _{user['name']} and Email__{user['email']}')
def add_user(user_details,name,email):
    user_details.append({'name':name,'email':email})
    save_data(user_details)
def update_user_details(user_details,id,name,email):
    list_all_user(user_details)
    if 1 <= id <= len(user_details):
        user_details[id - 1] = {'name':name,'email':email}
    
    save_data(user_details)
    
def delete_user_details(user_details,id):
    list_all_user(user_details)
    if 1<=id <= len(user_details):
        del user_details[id -1]
        
    save_data(user_details)

def main():
    user_details = load_data()
    while True:
        print(f'\n Random User Details || Chosen Option.')
        print(f'1. List all user details.')
        print(f'2. Add a new user.')
        print('3. Update user_ details.')
        print('4. Delete user by id__')
        print('5. Exit the app.')
        name,email = free_api()
        choice = input('Enter your choic___')
        if choice == '1':
            list_all_user(user_details)
        elif choice == '2':
            add_user(user_details,name,email)
        elif choice == '3':
            name_2 = input('Enter the new name__')
            email = input('Enter the new email__')
            user_id = int(input('Enter the id to update__'))
            update_user_details(user_details,user_id,name_2,email)
        elif  choice == '4':
            id = int(input('Enter the user id to delete__'))
            delete_user_details(user_details,id)
        elif choice == '5':
            break
        else:
            print('Enter the right option....!!!')
            
if __name__ == '__main__':
    main()