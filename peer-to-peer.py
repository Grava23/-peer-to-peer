password = input('Введите пароль: ')

password_length = len(password)

try:
    result = 1 / password_length
    result = int(password)
    print('Ваш пароль состоит только из цифр.')
except ZeroDivisionError:  
    print('Вы ввели пустой пароль.')
except:
    print =('Требования к паролю соблюдены')
        

