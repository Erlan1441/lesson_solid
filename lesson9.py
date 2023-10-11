# Исключение 
# try:
#     num = int(input('Введите число : '))
#     res = 10 / num
#     print(res)

# except(ValueError,ZeroDivisionError):
#     print('erorr')

# except ValueError:
#     print('ошибка значения')
# except ZeroDivisionError:
#     print('на ноль, не надо')

# try:
#     num=int(input('vvedi; '))
#     res = 10 / num
#     print(res)
# except ValueError as ve:
#     print('ошибка значений {0} '.format(ve))
# except ZeroDivisionError as ze:
#     print('не надо, на ноль {0}'.format(ze))
# finally:
#     print('finish')

# try:
#     num = int(input('vvedi: '))
#     res = 10 / num
#     print(res)

# except Exception as ex:
#     print('ERRoR')




# print('ok')
# задание 1
# num = int(input('Vedite '))

# if num % 2 == 0:
#     print ('h')
# else:
#     print ('neh')
# задание 2 
# num1 = int(input('pervoe chi: '))
# oper = input('ведите оператов : ' ) 
# num2 = int(input('vtoroe chi : '))

# if oper == '+':
#     result = num1 + num2

# elif oper == '-':
#     result = num1 - num2
# elif oper == '*':
#     result == num1 * num2
# elif oper == '/':
#     if num2 != 0 :
#         result = num1 / num2

# else:
#     print('Oshibka')


# print (f'resultat : {result}')
# задание 4
# word = str(input('ведите слово:'))
# result = word[:: -1]

# print(result)


# def Cazar (text,shift):
#     result = ''
#     alphabet_lower = 'abcdefghikjolmnpqrstuwxyz'
#     # alphabet_upper= 'ABCDEFGHIKJOLMNPQRSTUWXYZ'

#     for i in text:
#         is_upper = str(i).upper()
#         if str(i).isalpha():
#             i_index = alphabet_lower.index(str(i).lower())
#             i_shift = alphabet_lower[(i_index + shift)] % 26 
#             result += i_shift if not is_upper else i_shift.upper()
#         else:
#             result += i

# inp_text = 'abc xyz'
# shift_v = 3
# enc_text = Cazar(inp_text,shift=shift_v)
# print(enc_text)

# def caesar_cipher(text, shift):
#     result = ""

#     for char in text:
#         if char.isalpha():
#             ascii_offset = ord('a') if char.islower() else ord('A')
#             shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
#             result += shifted_char
#         else:
#             result += char

#     return result

# try:
#     text = input("Введите строку для шифрования: ")
#     shift = int(input("Введите сдвиг: "))

#     encrypted_text = caesar_cipher(text, shift)

#     print(f"Зашифрованная строка: {encrypted_text}")
# except ValueError:
#     print("Ошибка! Введите целое число для сдвига.")
