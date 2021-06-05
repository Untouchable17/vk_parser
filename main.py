import requests
from auto_reg import token
import os
import json


def get_wall_posts(group_name):
    url = f'https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={token}&v=5.130'
    response = requests.get(url)
    src = response.json()

    # Here we check, created directory or no
    if os.path.exists(f'{group_name}'):
        print(f'Директория с именем {group_name} уже существует')
    else:
        os.mkdir(group_name)

    # Save result JSON file
    with open(f'{group_name}/{group_name}.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    posts = src['response']['items']


def main():
    group_name = input('Введите название группы: ')
    get_wall_posts(group_name)


if __name__ == '__main__':
    main()



