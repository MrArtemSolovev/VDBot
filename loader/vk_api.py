import requests
import vk_auth
from time import sleep
from tqdm import tqdm
import datetime
import database_loader as sql


def vk_api_loader():
    data_frame = []
    index = 0
    for index in tqdm(range(len(vk_auth.group_id))):
        sleep(1)
        r = requests.get('https://api.vk.com/method/wall.get', params={'owner_id': vk_auth.group_id[index],
                                                                       'count': vk_auth.count,
                                                                       'offset': vk_auth.offset,
                                                                       'access_token': vk_auth.token,
                                                                       'v': vk_auth.v})
        n = 0
        for r.json()['response']['items'][n] in tqdm(r.json()['response']['items']):
            if 'attachments' in r.json()['response']['items'][n] \
                    and len(r.json()['response']['items'][n]['attachments']) == 1 \
                    and r.json()['response']['items'][n]['attachments'][0]['type'] == 'photo' \
                    and r.json()['response']['items'][n]['marked_as_ads'] == 0 \
                    and r.json()['response']['items'][n]['post_type'] == 'post':
                data_list = (r.json()['response']['items'][n]['id'],
                             datetime.datetime.fromtimestamp(r.json()['response']['items'][n]['date']).strftime('%Y-%m-%d %H:%M:%S'),
                             r.json()['response']['items'][n]['text'],
                             r.json()['response']['items'][n]['attachments'][0]['photo']['sizes'][-1]['url'],
                             'https://vk.com/wall'+str(r.json()['response']['items'][n]['from_id'])+'_'+str(r.json()['response']['items'][n]['id']))
                data_frame.append(data_list)
            n += 1

    return data_frame


def main():
    data_frame = vk_api_loader()
    sql.truncate_stg_loader()
    sql.sql_insert_stg_intel(data_frame)


if __name__ == '__main__':
    main()
