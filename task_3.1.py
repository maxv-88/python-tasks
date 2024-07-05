'''
1. Выведите в консоль категории товаров, представленных на https://fakestoreapi.com.
Запросите у пользователя, товары какой категории он желает просмотреть.
Выведите информацию о соответствующих товарах в отформатированном для чтения виде в
консоль. Используйте API https://fakestoreapi.com/docs.
'''
import requests

url_main = 'https://fakestoreapi.com/products/categories'
response = requests.get(url_main).json()
print ('Категории товаров: ')
for i in range(len(response)):
       print (response[i])

category = input('Введите интересующую вас катеогрию: ')
print ('Выбраная категория:', category)
url = (f'https://fakestoreapi.com/products/category/{category}')

product = requests.get(url).json()
for k in range(len(product)):
    print(f' Название: {product[k]["title"]}\n Цена: {product[k]["price"]}\n Описание: {product[k]["description"]}\n Рейтинг: {product[k]["rating"]["rate"]} на основе {product[k]["rating"]["count"]} оценок\n =================================')
