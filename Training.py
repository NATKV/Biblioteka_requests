import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_file, to_file, from_lang, to_lang="ru"):
    original_file = open(from_file, "r", encoding = "utf-16")
    reading_original_text = original_file.read()
    original_file.close()

    params = {
        'key': API_KEY,
        'text': reading_original_text,
        'lang': '{}-{}'.format(from_lang, to_lang),

    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    translation = ''.join(json_['text'])
    new_file = open(to_file, "w", encoding = "utf-16")
    # print(translation)
    new_file.write(translation)
    new_file.close()
    return translation


def send_to_disk(file_name):
    with open(file_name, encoding='utf-16', mode='r') as file:
        reading_file = file.read().encode('utf-16')

    auto = {"Authorization": "AgAAAAA5Ml4xAADLW6oFwNGya0w7t-OlVEonii8"}

    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'  # сервис, который дает / не дает разрение на загрузку файла

    path = "path=" + file_name
    overwrite = "overwrite=true"
    fields = "fields=name"

    request_url = URL + "?" + path + "&" + overwrite + "&" + fields
    response = requests.get(request_url, headers=auto)
    response = requests.put(response.json()["href"], reading_file)


if __name__ == '__main__':
    print(translate_it('requestsDE.txt', "DE_RU.txt", 'de'))
    print(translate_it('requestsES.txt', "ES_RU.txt", 'es'))
    print(translate_it('requestsFR.txt', "FR_RU.txt", 'fr'))
    send_to_disk("DE_RU.txt")
    send_to_disk("ES_RU.txt")
    send_to_disk("FR_RU.txt")





