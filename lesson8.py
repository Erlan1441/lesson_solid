#  файлы чтение и запись


# file = open('text.txt','r')

# content = file.read()
# print (content)

# file.close()

# with open('text.txt','r',encoding='utf-8') as file:
#     content = file.read()
#     print(content) это чтение файла 

# with open ('text.txt', 'a' , encoding='utf-8') as file:
#     content = file.write('\n Привееет')
#     print(content) это запись файла без очисти его внутри

#  with open ('text.txt', 'w' , encoding='utf-8') as file:
#     content = file.write('\n Привееет')
#     print(content)  это очитска файла и новая запись 

# with open ('text.txt', 'a' , encoding='utf-8') as file:
#     lines = ['Строка 1',' Строка 2 ']
#     content = file.writelines(lines)
#     print(content) 


# with open ('text.txt', 'w' , encoding='utf-8') as file:
#      n = 5 * 5
#      content = file.write(str (n))
#      print(content) 

# with open ('text.txt', 'w' , encoding='utf-8') as file:
#      user = str(input())
#      content = file.write(user)
#      print(content) 


# with open ('text.txt', 'r' , encoding='utf-8') as file:
#     for l in file:
#         print(l)

# with open('text.txt' ,'r' , encoding = 'utf- 8') as file:
#     with open('copy.txt','w' , encoding = 'utf - 8') as copy_file:
#         copy_file.write(file.read())

# with open ('text.txt','r', encoding = 'utf - 8') as file:
#     for l in file:
#         if 'cat' in l:
#           print('we have ')

# with open ('text.txt', 'r' , encoding='utf-8') as file:
#      with open('readtext.txt' , 'a', encoding = ' utf - 8') as readtext:
#         readtext.write(file.read())

# with open ('text.txt','r', encoding = 'utf - 8') as file:
#     user = str(input('ключивое слово'))
#     for user in file:
#         if user in user:
#             print(user)
#             break
# with open ('text.txt','r', encoding = 'utf - 8') as file:
#     with open('vin.txt','w' ,encoding = 'utf-8' ) as file:
#         user = str(input('слово для замены'))
#         user.write(user.read())
        
# with open('text.txt' ,'r' , encoding = 'utf- 8') as file:
#     with open('text.txt','w' , encoding = 'utf - 8') as file:
#         file.write(file.read())

# def create_country_files():
#     countries = ['France', 'Germany', 'Italy']

#     for country in countries:
#         with open(f'{country}.txt', 'w', encoding='utf- 8') as file:
#             pass

# def choose_country():
#     print("Выберите страну (1 - France, 2 - Germany, 3 - Italy): ")
#     choice = input()

#     if choice == '1':
#         return 'France'
#     elif choice == '2':
#         return 'Germany'
#     elif choice == '3':
#         return 'Italy'
#     else:
#         print("Неверный выбор. Пожалуйста, введите число от 1 до 3.")
#         return choose_country()

# def write_words(country):
#     print(f"Введите пару слов о {country}: ")
#     words = input()

#     with open(f'{country}.txt', 'a',encoding='utf - 8') as file:
#         file.write(words)

# create_country_files()
# chosen_country = choose_country()
# write_words(chosen_country)


    

# countries = ['France', 'Germany', 'Italy']

# for country in countries:
#     with open(f'{country}.txt', 'w',encoding='utf - 8') as file:
#         pass


# print("Выберите страну (1 - France, 2 - Germany, 3 - Italy): ")
# choice = input()

# if choice == '1':
#     chosen_country = 'France'
# elif choice == '2':
#     chosen_country = 'Germany'
# elif choice == '3':
#     chosen_country = 'Italy'
# else:
#     print("Неверный выбор. Пожалуйста, введите число от 1 до 3.")
    


# print(f"Введите пару слов о {chosen_country}: ")
# words = input()

# with open(f'{chosen_country}.txt', 'a', encoding='utf - 8') as file:
#     file.write(words)

with open ('text.txt','r', encoding = 'utf-8') as file:
    content = file.read()

new_content = content.replace('cat','dog')

with open ('text.txt','w',encoding = 'utf=8') as new_file:
    new_file.write(new_content)
    

        
