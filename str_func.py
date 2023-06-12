def make_capital_letters(word):
    '''Возвращает слова со всеми заглавными буквами'''
    return word.uppers()

def capitalize_first_letter(word):
    '''Возвращает слова с первой заглавной буквой'''
    capitalized_words = []
    for word in word.split():
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)

