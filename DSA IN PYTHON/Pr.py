# import requests
# from pymongo import MongoClient

# def freeApi():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     data = response.json()
    
#     if data['success'] and 'data' in data:
#         user_data = data['data']
#         usert_name = user_data['login']['username']
#         user_id = user_data['id']
#         user_email = user_data['email']
#         return usert_name,user_id,user_email
#     else:
#         raise Exception('Invaid url')
    
    
# client = MongoClient('mongodb+srv://mohammadpy:mohammadpy@machinelearning.hbo9rte.mongodb.net/')
# db = client['ytmanager']
# collection = db['April 9']


# def list_all_user():
#     all_user = collection.find()
#     for i in all_user:
#         print(f'Id : {i['_id']} Name : {i['name']} and Email : {i['email']}')
        
# def add_new_user(user_id,user_name,user_email):
#     collection.insert_one({'_id':user_id, 'name' : user_name, 'email' : user_email})
 
# def update_user_details(user_id,user_name,user_email):
#     collection.update_one(
#         {'_id' : user_id},
#         {"$set" :{'name' : user_name, 'email' : user_email}}
#     )

# def delete_user_data(user_id):
#     collection.delete_one({'_id' : user_id})


# while True:
#     print('\n Youtube manager ||  chosen option.')
#     print('1. List all user details.')
#     print('2. Add new user.')
#     print('3. Update user details.')
#     print('4. Delete user.')
#     print('5. Exit the app..')
#     choice = input('Enter your choice...')
#     a,b,c = freeApi()
    
#     if choice == '1':
#         list_all_user()
#     elif choice == '2':
#         add_new_user(b,a,c)
#     elif choice == '3':
#         user_id = int(input('Enter the user id to update.....'))
#         name = input('Enter a new name..')
#         email = input('Enter the new email add.....')
#         update_user_details(user_id,name,email)
#     elif choice == '4':
#         user_id_1 = int(input('Enter user id to delete'))
#         delete_user_data(user_id_1)
#     elif choice == '5':
#         break
#     else:
#         print('Enter the valid choice....')
    
    
