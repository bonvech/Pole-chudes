print('Здравствуйте, вы долны вводить по одной маленькой букве, чтобы отгодать слово. Или угадать слово сразу. Введите #сдаться чтобы сдаться. И #help чтобы узнать правтла и команды.')
sl = {'кот', 'котенок', 'лошадь', 'собака', 'осел', 'мышь'}
napom = 'Напоминаем вам нужно ввести одну маленькую букву русского алфавита, которую вы еще не вводили е = ё. Или угадать слово. Введите #сдаться чтобы сдаться. И #help чтобы узнать правила и команды.'
zanovo = 'Попрубуйте ввести заново.'
vibr_sl = sl.pop()
len_vibr_sl = len(vibr_sl)
for i in range(len_vibr_sl):
    print('*', end=(''))
popit = 1
zero_index = 0
index = 0
ugad_sl = ''
chislo_popit = int(input('Введите число попыток.'))
for i in range(chislo_popit):
    vvod = input()
    if len(vvod) == 1 and ord(vvod) > (ord('а') - 1) and ord(vvod) < (ord('я') + 1):
        if vvod in vibr_sl:
            for s in range(len_vibr_sl):
                if zero_index > len_vibr_sl or zero_index == len_vibr_sl:
                    zero_index = len_vibr_sl -1
                else:
                    if vvod == vibr_sl[x]:
                        tek_sim = vibr_sl[x]
                    else:
                        tek_sim = '*'
                    ugad_sl += tek_sim
                    zero_index += 1
            print(ugad_sl, end=('\n'))
            zero_index = 0
            if ugad_sl == vibr_sl:
                print('Ура вы победили! Вам пондобилось', popit, 'попыток.')
                break
            else:
                if tek_sim != '*':
                    ugad_sl += tek_sim
                else:
                    ugad_sl = ''
                tek_sim = ''
        else:
            print(zanovo , napom)
    elif len(vvod) == len_vibr_sl and '#' not in vvod:
        if vvod == vibr_sl:
            print('Ура вы победили! Вам понадобилось', popit, 'попыток.')
        else:
            print(zanovo, napom)
    elif '#help' in vvod:
        print(napom)
    elif '#сдаться' in vvod:
        print('Увы вы проиграли(((')
        break
    else:
        print(zanovo, napom)
    popit += 1
