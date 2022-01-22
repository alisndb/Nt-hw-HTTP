import requests


def get_most_int_hero(*args):
    if not args:
        return 'Ошибка: данные введены некорректно!'
    heroes = []
    for hero in args:
        resp = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
        if resp.status_code != 200 or resp.json()['response'] == 'error':
            return 'Ошибка: героя нет в базе данных либо сервер не отвечает!'
        int_lvl = resp.json()['results'][0]['powerstats']['intelligence']
        if int_lvl == 'null':
            heroes.append([hero, 0])
        else:
            heroes.append([hero, int(int_lvl)])
    heroes.sort(key=lambda i: i[1])
    best_int_lvl = heroes[-1][1]
    most_int_heroes = [[hero, int_lvl] for hero, int_lvl in heroes if int_lvl == best_int_lvl]
    if len(most_int_heroes) == 1:
        print(f'Наиболее умный супергерой: {most_int_heroes[0][0]}')
    else:
        print(f'Наиболее умные супергерои: {", ".join([i[0] for i in most_int_heroes])}')


get_most_int_hero('Hulk', 'Captain America', 'Thanos')
