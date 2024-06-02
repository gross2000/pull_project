def cap_lit(instring):

    """ функция для возвращения строки пользователя заглавными буквами """
    return instring.upper()

def first_cap(instring):

    """ функция для возврата строки пользователя с первой заглавной буквой, строка для конфликта """
    words = instring.split()
    cap_words = [word.capitalize() for word in words]
    return ''.join(cap_words)
