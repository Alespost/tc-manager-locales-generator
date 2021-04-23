import json
import os
import requests
import sys


def load_messages():
    with open('messages.json') as json_file:
        messages = json.load(json_file)
        return messages


def base_messages(lang):
    messages = load_messages()

    result = {}
    for key in messages:
        result[key] = {'message': messages[key][lang]}
    return result


def get_list(list_type, list_data):
    result = {}
    for i in list_data:
        d = list_data[i]
        result[list_type + str(d['id'])] = {'message': d['name']}
        result[list_type + str(d['id']) + '_description'] = {'message': d['description']}
    return result


if len(sys.argv) == 2 and sys.argv[1] == 'all':
    langs = ['bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'eus', 'fi', 'fr', 'hr', 'hu', 'it', 'ja', 'lt',
             'lv', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'sr-Cyrl', 'sr-Latn', 'ru', 'sk', 'sl', 'sv', 'tr', 'zh']
else:
    langs = ['cs', 'en']

if not os.path.exists('_locales'):
    os.makedirs('_locales')

for lang in langs:
    if lang in ['cs', 'en']:
        data = base_messages(lang)
    else:
        data = {}

    if lang == 'en':
        url = 'https://vendor-list.consensu.org/v2/vendor-list.json'
    else:
        url = 'https://vendor-list.consensu.org/v2/purposes-' + lang + '.json'

    response = requests.get(url=url).json()

    purposes = response['purposes']
    p = get_list(list_type='purpose', list_data=purposes)
    data.update(p)

    specialFeatures = response['specialFeatures']
    sf = get_list(list_type='special_feature', list_data=specialFeatures)
    data.update(sf)

    if not os.path.exists('_locales/' + lang):
        os.makedirs(name='_locales/' + lang)

    with open(file='_locales/' + lang + '/messages.json', mode='w') as file:
        json.dump(obj=data, fp=file, indent=2)

print('Translations generated.')
exit()
