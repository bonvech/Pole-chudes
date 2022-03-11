print('Здравствуйте, вы долны вводить по одной маленькой букве, чтобы отгодать слово. Или угадать слово сразу. Введите #сдаться чтобы сдаться. И #help чтобы узнать правтла и команды.')
sl = {'кот', 'котенок', 'лошадь', 'собака', 'осел', 'мышь'}
napom = 'Напоминаем вам нужно ввести одну маленькую букву русского алфавита, которую вы еще не вводили е = ё. Или угадать слово. Введите #сдаться чтобы сдаться. И #help чтобы узнать правтла и команды.'
zanovo = 'Попрубуйте ввести заново.'
b = sl.pop()
a = len(b)
for i in range(a):
    print('*', end=(''))
h = 1
x = 0
e = ''
d = 0
v = int(input('Введите число попыток.'))
for i in range(v):
    o1 = input()
    if len(o1) == 1 and ord(o1) > (ord('а') - 1) and ord(o1) < (ord('я') + 1):
        if o1 in b:
            for s in range(a):
                if x > a or x == a:
                    x = a -1
                else:
                    if o1 == b[x]:
                        m = b[x]
                    else:
                        m = '*'
                    e += m
                    x += 1
            print(e, end=('\n'))
            x = 0
            if e == b:
                print('Ура вы победили! Вам пондобилось', h, 'попыток.')
                break
            else:
                if m != '*':
                    e += m
                else:
                    e = ''
                m = ''
        else:
            print(zanovo , napom)
    elif len(o1) == len(b) and '#' not in o1:
        if o1 == b:
            print('Ура вы победили! Вам понадобилось', h, 'попыток.')
        else:
            print(zanovo, napom)
    elif '#help' in o1:
        print(napom)
    elif '#сдаться' in o1:
        print('Увы вы проиграли(((')
        break
    else:
        print(zanovo, napom)
    h += 1
