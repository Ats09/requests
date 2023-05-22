import requests

status = 'available'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
data = {'name': 'smutov'}
data_change = {'name': 'NOTsmutov'}
base_url = f'https://petstore.swagger.io/v2/pet/'

res = requests.get(base_url + f'findByStatus?status={status}', headers=headers)
"""get"""
print(res.status_code)
print('Выводим питомца со статусом "available"')
print(res.text)
print("--------------------------------")

res = requests.post(base_url, headers=headers, json=data)
"""post"""
if res.status_code == 200:
    pet_id = res.json().get('id')
    print("Динамический ID питомца:", pet_id)
else:
    print("Ошибка при создании питомца:", res.status_code)

print(res.status_code)
print('Обновляем имя питомца на "Smutov"')
print(res.text)
print("--------------------------------")

res = requests.put(base_url, json=data_change)
"""put"""
print(res.status_code)
print('Обновляем имя питомца "Smutov" на "NOTsmutov"')
print(res.text)
print("--------------------------------")

res = requests.delete(base_url + f'{pet_id}')
"""delete"""

print(res.status_code)
print('Удаляем питомца "NOTsmutov"')
print(res.text)
print("--------------------------------")