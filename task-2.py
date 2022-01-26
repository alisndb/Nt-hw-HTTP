import requests
import os
from pprint import pprint


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        resp = requests.get(files_url, headers=self.get_headers())
        return resp.json()

    def _get_upload_link(self, disk_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': disk_path, 'overwrite': 'true'}
        resp = requests.get(upload_url, headers=self.get_headers(), params=params)
        return resp.json()

    def upload_file_to_disk(self, disk_path, path):
        href = self._get_upload_link(disk_path).get('href', '')
        resp = requests.put(href, data=open(path, 'rb'))
        if resp.status_code == 201:
            print('Файл успешно загружен!')
        else:
            print(f'Ошибка: {resp.status_code}')


disk = YandexDisk('')  # Строка для токена.

disk.upload_file_to_disk('file.txt', os.path.join(os.getcwd(), 'file.txt'))
pprint(disk.get_files_list())
