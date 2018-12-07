''' How many words from Slavic languages can you understand without Google? '''

from ru_local import *
print(BEGIN)
print(BEGIN1)
key = ['ковер', 'киндер-сюрприз', 'носки', 'привидение', 'салон красоты',
       'арбуз', 'цвет', 'красота']
count = 0
answer = []

''' Questions '''

firs_q = input('DYWAN (польск.): ')
if firs_q in key:
    count += 1
    answer.append(firs_q)
    print(TRUE)
else:
    print(FALSE, 'ковер')

second_q = input('ЯЙКО-СПОДIВАЙКО (укр.): ')
if second_q in key:
    count += 1
    answer.append(second_q)
    print(TRUE)
else:
    print(FALSE, 'киндер-сюрприз')

third_q = input('ШКАРПЕТКИ (укр.): ')
if third_q in key:
    count += 1
    answer.append(third_q)
    print(TRUE)
else:
    print(FALSE, 'носки')

fourth_q = input('Strašidlo [страшидло] (чеш.): ')
if fourth_q in key:
    count += 1
    answer.append(fourth_q)
    print(TRUE)
else:
    print(FALSE, 'привидение')

fifth_q = input('SALON URODY (польск.): ')
if fifth_q in key:
    count += 1
    answer.append(fifth_q)
    print(TRUE)
else:
    print(FALSE, 'салон красоты')

sixth_q = input('КОЛИР (укр.): ')
if sixth_q in key:
    count += 1
    answer.append(sixth_q)
    print(TRUE)
else:
    print(FALSE, 'цвет')

seventh_q = input('URODA (польс.): ')
if seventh_q in key:
    count += 1
    answer.append(seventh_q)
    print(TRUE)
else:
    print(FALSE, 'красота')

eighth_q = input('ДИНЯ (болг.): ')
if eighth_q in key:
    count += 1
    answer.append(eighth_q)
    print(TRUE)
else:
    print(FALSE, 'арбуз')

''' Results '''

if count >= 6:
    print(GREAT)
if 6 > count >= 4:
    print(OKEY)
if count < 4:
    print(BAD)
print(ANSWER, ', '.join(answer) )