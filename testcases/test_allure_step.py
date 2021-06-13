import allure
import pytest
from common.common_function import *

'''
流程性的用例，添加测试步骤，让用例更清晰
用例步骤：1.登陆， 2.浏览商品 3.添加购物车  4.生成订单  5.支付成功
作者：上海-悠悠 QQ交流群：779429633
'''


# print('读取yaml结果：', dbinfo)
@allure.feature("功能模块")
@allure.story("测试用例小模块-成功案例")
@allure.title("测试用例名称：流程性的用例，添加测试步骤")
def test_add_goods_and_buy(login_setup):
    '''
    用例描述：前置：登陆
    用例步骤：1.浏览商品 2.添加购物车  3.购买  4.支付成功
    '''
    with allure.step("step1：浏览商品"):
        open_goods()

    with allure.step("step2：添加购物车"):
        add_shopping_cart()

    with allure.step("step3：生成订单"):
        buy_goods()

    with allure.step("step4：支付"):
        pay_goods()

    with allure.step("断言"):
        assert 1 == 1
