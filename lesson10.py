alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghikjlmnopqrstuvwxyz'

alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхчшщъыьэюя'

lang = input('Выберите язык RU/EU: ').upper()

smeshnie = int(input('Шаг шифровки: '))

message = input ('Сообщение для шифровки: ')

itog = ' '

if lang == 'RU':
    for i in message:
         mesto = alfavit_RU.find(i)
         new_mesto = mesto + smeshnie
         if i in alfavit_RU:
              itog += alfavit_RU[new_mesto]
         else:
                itog += i
else:
       for i in message:
             mesto = alfavit_EU.find(i)
             new_mesto = mesto + smeshnie
             if i in alfavit_EU:
                 itog += alfavit_EU[new_mesto]
             else:
                    itog += i
print(itog)
#Код сделан одной из однокурсниц, даже я не смог, так что уважение  
