def start():
    name = input('Введите название грузика: ')

    znach_perv = float(input("Введите первое значение из столбца: "))
    znach_perv_voda = float(input("Введите первое значение в воде из столбца: "))

    znach_vt = float(input("Введите второе значение из столбца: "))
    znach_vt_voda = float(input("Введите второе значение в воде из столбца: "))

    znach_tr = float(input("Введите третье значение из столбца: "))
    znach_tr_voda = float(input("Введите третье значение в воде из столбца: "))

    f1 = (znach_tr + znach_vt + znach_perv) / 3
    f2 = (znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3

    formula(f1, f2, name, znach_tr, znach_vt, znach_perv, znach_tr_voda, znach_vt_voda, znach_perv_voda)


def formula(f1, f2, name, znach_tr, znach_vt, znach_perv, znach_tr_voda, znach_vt_voda, znach_perv_voda):

    m_kr = 0.00010197
    p_water = 999.9
    g = 9.80665

    massa_tela = (f1 / g) - m_kr

    print('')
    print(f'Для грузика под именем "{name}" соответствует масса тела = {massa_tela}')

    p = (-1 * massa_tela * p_water * g) / (f2 - (massa_tela * g))

    print('')
    print(f'Формула для расчета:  p(тела) = (-1 * {massa_tela} * {p_water} * {g}) / ({f2} - ({massa_tela} * {g}))')

    print('')
    print(f'Для грузика под именем "{name}" соответствует плотность тела = {p}')
    print('')

    sub_pogr = 0.001

    P1 = (sub_pogr / znach_perv) * p
    pogr1 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_perv) ** 2 + P1 ** 2)

    P2 = (sub_pogr / znach_vt) * p
    pogr2 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_vt) ** 2 + P2 ** 2)

    P3 = (sub_pogr / znach_tr) * p
    pogr3 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_tr) ** 2 + P3 ** 2)

    final_pogr = 0.5 ** (pogr1 ** 2 + pogr2 ** 2 + pogr3 ** 2)

    print(f'Погрешность для грузика = {final_pogr / 1000}')
    print('')

    print(f'Плотность для грузика с погр. = {(znach_tr + znach_vt + znach_perv) / 3} +- {final_pogr / 1000}')
    print('')

    P4 = (sub_pogr / znach_perv_voda) * p
    pogr4 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_perv_voda) ** 2 + P4 ** 2)

    P5 = (sub_pogr / znach_vt_voda) * p
    pogr5 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_vt_voda) ** 2 + P5 ** 2)

    P6 = (sub_pogr / znach_tr_voda) * p
    pogr6 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_tr_voda) ** 2 + P6 ** 2)

    final_pogr_vd = 0.5 ** (pogr4 ** 2 + pogr5 ** 2 + pogr6 ** 2)

    print(f'Погрешность для грузика в воде = {final_pogr_vd / 1000}')
    print('')

    print(f'Плотность для грузика с погр. в воде = {(znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3} +- {final_pogr_vd / 1000}')
    print('')

    pogr_chisl = 0.5 ** (final_pogr ** 2 + 0.001 ** 2)
    print(f'Погрешность числителя: {pogr_chisl}')

    pogr_znam = 0.5 ** (final_pogr ** 2 + 0.001 ** 2 + final_pogr_vd ** 2 + 0.001 ** 2)
    print(f'Погрешность знаменателя: {pogr_znam}')

    pogr_chisl_ot = pogr_chisl / (((znach_tr + znach_vt + znach_perv) / 3) - 0.021)
    print(f'Относительная погрешность числителя: {pogr_chisl_ot}')

    pogr_znam_ot = pogr_znam / (((znach_tr + znach_vt + znach_perv) / 3) - ((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - 0.021 + 0.016)
    print(f'Относительная погрешность знаменателя: {pogr_znam_ot}')

    last_pogr = 0.5 ** (pogr_znam_ot ** 2 + pogr_chisl_ot ** 2)

    print(f'Финальная погрешность = {last_pogr}')

    print(f'Ответ = {p} +- {last_pogr}')
    print('')


def der_gruz():
    name = input('Введите название грузика: ')

    znach_perv = float(input("Введите первое значение из столбца: "))
    znach_perv_voda = float(input("Введите первое значение в воде из столбца: "))

    znach_vt = float(input("Введите второе значение из столбца: "))
    znach_vt_voda = float(input("Введите второе значение в воде из столбца: "))

    znach_tr = float(input("Введите третье значение из столбца: "))
    znach_tr_voda = float(input("Введите третье значение в воде из столбца: "))

    final_pogr_dop, final_pogr_vd_dop, H, H_vd = dop_gruz()

    p = float(input('Введите полученную плотность деревянного грузика: '))

    print(f'Для грузика под именем "{name}" соответствует плотность тела = {p}')
    print('')

    sub_pogr = 0.001

    P1 = (sub_pogr / znach_perv) * p
    pogr1 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_perv) ** 2 + P1 ** 2)

    P2 = (sub_pogr / znach_vt) * p
    pogr2 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_vt) ** 2 + P2 ** 2)

    P3 = (sub_pogr / znach_tr) * p
    pogr3 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_tr) ** 2 + P3 ** 2)

    final_pogr = 0.5 ** (pogr1 ** 2 + pogr2 ** 2 + pogr3 ** 2)

    print(f'Погрешность для грузика = {final_pogr / 1000}')
    print('')

    print(f'Плотность для грузика с погр. = {(znach_tr + znach_vt + znach_perv) / 3} +- {final_pogr / 1000}')
    print('')

    P4 = (sub_pogr / znach_perv_voda) * p
    pogr4 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_perv_voda) ** 2 + P4 ** 2)

    P5 = (sub_pogr / znach_vt_voda) * p
    pogr5 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_vt_voda) ** 2 + P5 ** 2)

    P6 = (sub_pogr / znach_tr_voda) * p
    pogr6 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_tr_voda) ** 2 + P6 ** 2)

    final_pogr_vd = 0.5 ** (pogr4 ** 2 + pogr5 ** 2 + pogr6 ** 2)

    print(f'Погрешность для грузика в воде = {final_pogr_vd / 1000}')
    print('')

    print(f'Плотность для грузика с погр. в воде = {(znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3} +- {final_pogr_vd / 1000}')
    print('')

    pogr_chisl = 0.5 ** (final_pogr ** 2 + 0.001 ** 2)
    print(f'Погрешность числителя: {pogr_chisl}')

    pogr_znam = 0.5 ** (final_pogr ** 2 + 0.001 ** 2 + final_pogr_vd ** 2 + 0.001 ** 2 + final_pogr_vd_dop ** 2 + final_pogr_dop ** 2)
    print(f'Погрешность знаменателя: {pogr_znam}')

    pogr_chisl_ot = pogr_chisl / (((znach_tr + znach_vt + znach_perv) / 3) - 0.021)
    print(f'Относительная погрешность числителя: {pogr_chisl_ot}')

    pogr_znam_ot = pogr_znam / (((znach_tr + znach_vt + znach_perv) / 3) - (
                (znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - 0.021 + 0.016 + final_pogr_dop - final_pogr_vd_dop)
    print(f'Относительная погрешность знаменателя: {pogr_znam_ot}')

    last_pogr = 0.5 ** (pogr_znam_ot ** 2 + pogr_chisl_ot ** 2)

    print(f'Финальная погрешность = {last_pogr}')

    print(f'Ответ = {p} +- {last_pogr}')


def dop_gruz():
    print('')
    print('ЗНАЧЕНИЯ ДЛЯ ДОП ГРУЗА К ДЕР.')
    print('')
    znach_perv = float(input("Введите первое значение из столбца: "))
    znach_perv_voda = float(input("Введите первое значение в воде из столбца: "))

    znach_vt = float(input("Введите второе значение из столбца: "))
    znach_vt_voda = float(input("Введите второе значение в воде из столбца: "))

    znach_tr = float(input("Введите третье значение из столбца: "))
    znach_tr_voda = float(input("Введите третье значение в воде из столбца: "))

    p = float(input('Введите плотность доп груза:'))

    sub_pogr = 0.001

    P1 = (sub_pogr / znach_perv) * p
    pogr1 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_perv) ** 2 + P1 ** 2)

    P2 = (sub_pogr / znach_vt) * p
    pogr2 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_vt) ** 2 + P2 ** 2)

    P3 = (sub_pogr / znach_tr) * p
    pogr3 = 0.5 ** ((((znach_tr + znach_vt + znach_perv) / 3) - znach_tr) ** 2 + P3 ** 2)

    final_pogr = 0.5 ** (pogr1 ** 2 + pogr2 ** 2 + pogr3 ** 2)

    P4 = (sub_pogr / znach_perv_voda) * p
    pogr4 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_perv_voda) ** 2 + P4 ** 2)

    P5 = (sub_pogr / znach_vt_voda) * p
    pogr5 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_vt_voda) ** 2 + P5 ** 2)

    P6 = (sub_pogr / znach_tr_voda) * p
    pogr6 = 0.5 ** ((((znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3) - znach_tr_voda) ** 2 + P6 ** 2)

    final_pogr_vd = 0.5 ** (pogr4 ** 2 + pogr5 ** 2 + pogr6 ** 2)

    H_vd = (znach_tr_voda + znach_vt_voda + znach_perv_voda) / 3
    H = (znach_tr + znach_vt + znach_perv) / 3

    return [final_pogr, final_pogr_vd, H, H_vd]




print('')
print("Дальнейшие функции работают на вычисления для НЕ ДЕРЕВЯННЫХ грузиков")
print('')
#for i in range(3):
#   start()
print('')
print("ДАЛЬШЕ ИСКЛЮЧИТЕЛЬНО ДЛЯ ДЕРЕВЯННОГО ГРУЗИКА, НО СНАЧАЛА ПОСЧИТАЙТЕ ПЛОТНОСТЬ")
print('')
der_gruz()