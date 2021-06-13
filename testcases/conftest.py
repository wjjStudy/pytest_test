import pytest
import pymysql
from common.common_function import *
from utils_tools import read_yaml


@pytest.fixture(scope="session")
def login_setup():
    userinfo = read_yaml.readYaml()['userInfo']
    login(userinfo['user'], userinfo['password'] )


@pytest.fixture()
def my_fixture(request):
    dbinfo = request.param
    print("=====dbinfo:=======", dbinfo)
    host = dbinfo['host']
    port = dbinfo['port']
    db = dbinfo['db']
    user = dbinfo['user']
    password = dbinfo['password']
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    def close_connection():
        conn.close()
    request.addfinalizer(close_connection)
    return conn
