import pytest


@pytest.mark.run(order=1)
def test_login():
    '''登录'''
    # if user == 'wjj' and password == 'wjj@123456':
    #     # assert True
    print("登录成功")


@pytest.mark.run(order=2)
def test_open_goods():
    '''浏览商品'''
    print("浏览商品")


@pytest.mark.run(order=3)
def test_add_shopping_cart(goods_id="10086"):
    '''添加购物车'''
    print("添加购物车")


@pytest.mark.run(order=5)
def test_pay_goods():
    '''支付'''
    print("支付")


@pytest.mark.run(order=4)
def test_buy_goods():
    '''生成订单'''
    print("生成订单")


if __name__ == "__main__":
    pytest.main(['-s', '-r', 'test_order.py'])
