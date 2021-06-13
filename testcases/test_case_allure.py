import allure
import pytest

@allure.step("测试步骤1:点xxx")
def step_1():
    print("111")

@allure.step("测试步骤2:点xxx")
def step_2():
    print("222")

@allure.feature("模块--编辑页面")
class TestEditPage():
    '''编辑页面'''
    # file = open('../data/test.jpg', 'rb').read()
    # @allure.attach.file(source =open('../data/test.jpg', 'rb'), attachment_type = allure.attachment_type.JPG)
    @allure.severity('blocker')
    @allure.story("这是一个xxx的用例标题")
    def test_1(self, login_setup):
        '''用例描述：先登录，再去执行xxx'''
        # allure.attach.file('../data/test.jpg', '我是附件截图的名字', attachment_type=allure.attachment_type.JPG)
        step_1()
        step_2()
        print("xxx")

    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.testlink.com")
    @allure.story("打开a页面的用例标题")
    def test_2(self, login_setup):
        '''用例描述：先登录，再去执行yyy'''
        print("yyy")

