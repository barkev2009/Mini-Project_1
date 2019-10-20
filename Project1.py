from datetime import date

# Printing the heading
print('''"Вояджер-1" был запущен 5 сентября 1977 года.
 Предлагаем узнать примерное расстояние от зонда до Солнца на выбранную Вами дату,
 предполагая, что зонд движется по прямой, с постоянной скоростью.''')

# Setting the velocity
velocity = 38241  # miles/hour
lag_vel = 299792458  # meters/sec

# Recording the current date
input_date = input('\nВведите дату в формате дд.мм.гггг: ')
print('')
now_date = list(input_date)
now_day = int(now_date[0] + now_date[1])
now_mon = int(now_date[3] + now_date[4])
now_year = int(now_date[6] + now_date[7] + now_date[8] + now_date[9])
now_date1 = date(now_year, now_mon, now_day)

# Setting the constant dates
date_init = date(1977, 9, 5)

# Calculating the parameters
days = (now_date1 - date_init).days
miles = velocity * days * 24
kms = miles * 1.609
aster_uns = kms / 149598100

i = 0
while True:
    i += 1
    if i >= 4:
        print('Если хотите закончить программу, нажмите q.')
    choice = input('В каком измерении хотите получить расстояние (км/мили/ае)? ')

    if days < 0:
        print('\nВы ввели дату более раннюю, чем дата запуска "Вояджера".')
    else:
        if choice == 'км':
            print('\nНа {} '.format(input_date) +
                  'зонд прошел расстояние в {:,.0f} километров.'.format(kms).replace(',', ' '))
            break
        elif choice == 'мили':
            print('\nНа {} '.format(input_date) +
                  'зонд прошел расстояние в {:,.0f} миль.'.format(miles).replace(',', ' '))
            break
        elif choice == 'ае':
            print('\nНа {} '.format(input_date) +
                  'зонд прошел расстояние в {:,.0f} астрономических единиц.'.format(aster_uns).replace(',', ' '))
            break
        elif choice == 'q' or choice == 'й':
            break
        else:
            print('\nВы ввели неправильное измерение.')
