# coding=utf-8

import pytest
import logging

log = logging.getLogger(__name__)


class Test_Pytest():
    def test_one(self):
        # log = logging.getLogger('test_one')
        log.info("\n----start------")
        # pytest.xfail(reason='该功能尚未完成')
        log.debug("test_one方法执行" )
        assert 1==1

    def test_two(self):
        # log = logging.getLogger('test_two')
        log.info("test_two方法执行" )
        assert "o" in "love"
        assert 3 == 1+2

    # @pytest.mark.xfail()
    def test_three(self):
        print("test_three方法执行" )
        assert 3-2==1

if __name__=="__main__":
    pytest.main(['-s','-r','test_case4.py'])
