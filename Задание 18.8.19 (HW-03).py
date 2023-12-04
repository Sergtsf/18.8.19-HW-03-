### Запрос ввода кол-во билетов, если 0 то вывод ошибки на экран;
ticket = int(input('Введите колличество билетов: '))
if ticket <= 0:
    print('Ошибка!!! Не указано колличество билетов!')

### Добавление переменной, условной корзины покупок;
total_price = 0

### Запрос ввода возраста для каждого билета;
ticket_for_age = [i for i in range(1, ticket+1)]
for ticket in ticket_for_age:
    age = int(input(f'Введите возраст для {ticket}-го билета: '))

### Цена билета для каждой возрастной категории;
    if age < 18:
        total_price += 0
    elif 18 <= age <= 25:
        total_price += 990
    else:
        total_price += 1390

### Скидка 10% при покупке от 3-х билетов.
if ticket > 3:
    discount = (total_price / 100) * 10
    print(f'Сумма к оплате cо скидкой: {total_price - discount} руб.')
else:
    print(f'Сумма к оплате: {total_price} руб.')