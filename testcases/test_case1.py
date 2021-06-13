# coding:utf-8

import pytest
from utils_tools import database_tools
from utils_tools import read_yaml

dbinfo = read_yaml.readYaml()
print('读取yaml结果：', dbinfo)
@pytest.mark.parametrize('my_fixture', dbinfo['DB'],indirect=True)
def test_1(my_fixture):
    FND_CODE = 'ATA001'
    sql = "SELECT * FROM `found`.found_yld WHERE FND_CODE = '%s'" % FND_CODE
    conn = my_fixture
    results = database_tools.fetch_all(conn, sql)
    print(results)

if __name__ == '__main__':
    pytest.main(["-s"])
    # pytest.main(['-s','test_01.py')

