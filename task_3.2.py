'''
2. Выведите информацию о всех корзинах пользователей (Cart),
представленных на https://fakestoreapi.com. Проанализируйте данные и устно
ответьте на вопрос, что из себя представляют эти корзины и какая информация в
них находится - что означает каждое поле в полученном json.
* По желанию доработайте программу: запросите у пользователя его имя
(или идентификатор), в соответствии с этим выведите содержание всех корзин
этого пользователя в отформатированном для чтения виде в консоль.
Используйте API https://fakestoreapi.com/docs.
'''
import requests

url = 'https://fakestoreapi.com/carts'
response = requests.get(url).json()
carts = requests.get(url).json()
for k in range(len(carts)):
    print(f' Id корзины: {carts[k]["id"]}\n Id покупателя: {carts[k]["userId"]}\n Дата покупки: {carts[k]["date"]}\n Товары в корзине:')
    for h in range(len(carts[k]["products"])):
        print(f' Id товара {carts[k]["products"][h]["productId"]}, {carts[k]["products"][h]["quantity"]} шт')
    print('=================================')


#user_id = input('Введите вш id')
#if user_id == carts[k]["userId"]:
