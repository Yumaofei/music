import configparser
import requests
import json
import read_config as cf
import sql

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',}


def get_cookie():
    url = cf.get('Login','url')
    data = {'phone':cf.get('Login','phone'),
            'md5_password':cf.get('Login','md5_password')}
    cookie_jar = requests.session().post(url=url,data=data,headers=headers).cookies
    cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
    headers['cookie']=cookie_t
    print(headers)
    return cookie_t

def get_recommend_playlist():
    r = requests.get(url='https://api.mtnhao.com/personalized?limit=10')
    json_t = r.text
    result = json.loads(json_t)
    playlist_len = len(result['result'])
    max_playlist = result['result'][playlist_len - 1]

    id = max_playlist['id']
    type = max_playlist['type']
    name = max_playlist['name']
    copywriter = max_playlist['copywriter']
    picUrl = max_playlist['picUrl']
    canDislike = max_playlist['canDislike']
    trackNumberUpdateTime = max_playlist['trackNumberUpdateTime']
    playCount = max_playlist['playCount']
    trackCount = max_playlist['trackCount']
    highQuality = max_playlist['highQuality']
    alg = max_playlist['alg']
    sql.insert_playlist(id,type,name,copywriter,picUrl,canDislike,trackNumberUpdateTime,playCount,trackCount,highQuality,alg)

def recommend_playlist():
    url = cf.get('Login', 'url')
    requests.Session().get(url=url, headers=headers)
    response = requests.Session().get(url=url)
    return  response.content


get_recommend_playlist()

