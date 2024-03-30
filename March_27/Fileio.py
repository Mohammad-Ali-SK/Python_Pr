# Types of all files
# 1. Text Files : .txt, .docx, .log ect.
# 2. Binary Files : .mp4, .mov, .png, .jpeg ect.

# f = open('ytmanager.txt','rt')
# data = f.read()
# # f.close()
# print(data)

# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)

# How to works enumerate------------------------------- 1.0)

# x = ('A','B', 'C')
# c = enumerate(x)
# print(list(c))

# Files opening in python ----------------------------2.0)

# There are two types of file opening.

# file = open('text.txt','w')

# try:
#     file.write('How are you baby')
# finally:
    # file.close()

# Method two open file-----

# with open('text.txt','w') as file:
#     file.write('Helo fr lok')

# Project Youtube Manager -------------------------------3.0)

# import json


# def load_videos():
#     try:
#         with open('text.txt', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
    
# def save_data(videos):
#     with open('text.txt', 'w') as file:
#         json.dump(videos,file)

# def list_all_videos(videos):
#     print('*' * 70)
#     print('\n')
#     for index, vid in enumerate(videos,start=1):
#         print(f'{index}. Name_{vid['name']} Time__{vid['time']}')

# def add_video(videos):
#     name = input('Enter the video name__')
#     time = input('Enter the vid time ___')
#     videos.append({'name':name, 'time':time})
#     save_data(videos)


# def update_video(videos):
#     index = int(input('Enter the vid index to update__'))
#     if 1 <= index <= len(videos):
#         name = input('Enter the video name___')
#         time = input('Enter the video time___')
#         videos[index-1] = {'name':name, 'time':time}
#     save_data(videos)
# def delete_videos(videos):
#     index = int(input('Enter the vid index to delete__'))
#     if 1<=index <= len(videos):
#         del videos[index -1]
#         save_data(videos)




# def main():
#     videos = load_videos()
#     while True:
#         print(f'Youtube Manager || Chosen Option')
#         print('1. List all yt video.')
#         print('2. Add yt video.')
#         print('3. Update video.')
#         print('4. Delete Video.')
#         print('5. Exit the app.')
#         choice = input('Enter your option.__')
#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_video(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_videos(videos)
#             case '5':
#                 break
#             case _:
#                 print('Enter the right option___')
            
# if __name__ == '__main__':
#     main()

# import os
# # with open('ytmanager.txt','r') as file:
# os.remove('text.txt')


# with open('address.txt','r') as file:
#     data = file.read()
#     new_data = data.replace('babay','no')
#     print(new_data)


# word = "nooojo"
# with open('address.txt','r') as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print('Found')
#     else:
#         print('Not found')
