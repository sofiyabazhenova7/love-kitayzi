a = input('Показывает: ')
b = input('Показывает: ')
s = 'Камень'
c = 'Ножницы'
p = 'Бумага'
def play(a, b, s, c, p):
    if a == b:
        print('Ничья')
    if a == s and b == c: #камень
        print('ВЫиграл игрок a')
    if a == s and b == p:
        print('ВЫиграл игрок b')
    if a == c and b == p: #ножницы
        print('ВЫиграл игрок a')
    if a == c and b == s:  
        print('ВЫиграл игрок b')
    if a == p and b == c: #бумага
        print('ВЫиграл игрок b')
    if a == p and b == s: #бумага
        print('ВЫиграл игрок a')
        
play(a, b, s, c, p)
    