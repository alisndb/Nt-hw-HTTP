import requests
import datetime


def get_questions():
    current_date = datetime.date.today()
    from_date = current_date - datetime.timedelta(days=1)
    to_date = current_date + datetime.timedelta(days=1)
    from_date_ts = int(datetime.datetime(*[int(i) for i in str(from_date).split('-')]).timestamp())
    to_date_ts = int(datetime.datetime(*[int(i) for i in str(to_date).split('-')]).timestamp())
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={from_date_ts}'\
          f'&todate={to_date_ts}&order=desc&sort=activity&tagged=python&site=stackoverflow'
    resp = requests.get(url)
    if resp.status_code != 200:
        return 'Ошибка!'
    print("Список всех вопросов с тегом 'python' за последние два дня:\n")
    for item in resp.json()['items']:
        print(item['title'])


get_questions()
