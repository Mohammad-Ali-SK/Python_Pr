# import requests
# from pymongo import MongoClient


# def free_api():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     data = response.json()
    
    
#     if data['success'] and 'data' in data:
#         user_data = data['data']
#         user_name = user_data['login']['username']
#         user_id = user_data['id']
#         user_email = user_data['email']
#         return user_id,user_name,user_email
#     raise Exception('Invalid Url')

# client = MongoClient('mongodb+srv://mohammadpy:mohammadpy@machinelearning.hbo9rte.mongodb.net/')
# db = client['ytmanager']
# colection = db['user_details']


# def list_all_user():
#     print(f'*' * 70)
#     print(f'\n')
#     all_data = colection.find()
#     for i in all_data:
#         print(f'Name - {i['name']} Id - {i['_id']} and Email - {i['email']}')

# def add_new_user(id,name,email):
#     colection.insert_one({'_id':id,'name':name,'email':email})

# def update_user(id,name,email):
#     colection.update_one(
#         {'_id' :id},
#         {"$set" : {'name':name, 'email':email}}
#     )

# def delete_user(id):
#     colection.delete_one({'_id' : id})



# def main():
#      user_id,user_name,user_email = free_api()
     
#      while True:
        
#         print(f'\n Yt user details__ || Chosen Option.')
#         print(f'1. List all User data.')
#         print('2. Add user.')
#         print('3. Update user data.')
#         print('4. Delete user data.')
#         print('5. Exit the app.')
#         choice = input('Enter your choice____.')
        
        
#         if choice == '1':
#             list_all_user()
#         if choice == '2':
#             add_new_user(user_id,user_name,user_email)
#         if choice == '3':
#             user_id_1 = int(input('Enter user id to update__'))
#             user_name_1 = input('Enter new user name___')
#             user_email_1 = input('Enter new email___')
#             update_user(user_id_1,user_name_1,user_email_1)
#         if choice == '4':
#             user_id = int(input('Enter user id to delete...'))
#             delete_user(user_id)
#         if choice == '5':
#             break
#         else:
#             print('Invalid option___')


# if __name__ == '__main__':
#     main()
# import json

# def load_video():
#     try:
#         with open('text.txt', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
    
# def save_data(videos):
#     with open('text.txt','w') as file:
#         json.dump(videos,file)

# def list_all_videos(videos):
#     print('*' * 70)
#     print('\n')
#     for index,vid in enumerate(videos,start=1):
#         print(f'{index}, {vid['name']}, Duration : {vid['time']}')

# def add_video(videos):
#     name = input('Enter the video name__')
#     time = input('Enter the video time.__')
#     videos.append({'name':name, 'time':time})
#     save_data(videos)

# def update_video(videos):
#     index = int(input('Enter the video id to update__'))
#     if 1 <= index <= len(videos):
#         name = input('Enter the name__')
#         time = input('Enter the new vid tme__')
#         videos[index-1] = {'name':name, 'time':time}
#         save_data(videos)
#     else:
#         print('Enter the thik input__')
# def delete_video(videos):
#    index = int(input('Enter the video id to update__'))
#    if 1 <= index <= len(videos):
#        del videos[index -1]
#        save_data(videos)
#    else:
#        print('Wrong input__')


# def main():
#     videos = load_video()
#     while True:
#         print('\n Youtube Manage || Chosen Option.')
#         print('1. List all youtube video.')
#         print('2. Add video.')
#         print('3. Update video.')
#         print('4. Delete video.')
#         print('5. Exit the app')
#         choice = input('Enter your choice__')
        
#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_video(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             case _:
#                 print('Enter vaild option !!')

# if __name__ == '__main__':
#     main()
