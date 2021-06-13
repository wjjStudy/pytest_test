# -*- coding: utf-8 -*-

import allure
import pytest


@allure.feature('这里是一级标签feature')
class TestAllure():

    @allure.title("用例标题0-title")
    @allure.story("这里是第一个二级标签story")
    @pytest.mark.parametrize('param', ['青铜', '白银', '黄金'])
    def test_0(self, param):
        allure.attach('附件内容是： '+param, '我是附件名', allure.attachment_type.TEXT)

    @allure.title("用例标题1-title")
    @allure.story("这里是第二个二级标签story")
    def test_1(self):
        allure.attach.file('../data/test.jpg', '我是附件截图的名字', attachment_type=allure.attachment_type.JPG)

    @allure.title("用例标题2-title")
    @allure.story("这里是第三个二级标签story")
    @allure.severity(allure.severity_level.NORMAL)
    def test_2(self):
        pass
