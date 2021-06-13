# coding:utf-8
import pytest
import requests


city_ids = []
@pytest.mark.parametrize('cityID',['101200101', '101010100', '101200401','101210301'])
def test_tianqi(cityID):
    url = 'http://api.help.bj.cn/apis/weather?id='+ cityID

    headers ={
    'content-type': 'application/json',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    res = requests.get(url,headers=headers).json()
    # print(res.json())
    # return res.json()
    assert res['citycode']==cityID


if __name__ == '__main__':
    pytest.main(['-s'])

