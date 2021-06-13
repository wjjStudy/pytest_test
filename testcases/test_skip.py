import pytest

nums = [1, 2, 3, 4]
for num in nums:
    print("num的值：", num)

    @pytest.mark.skipif(num == 3, reason='跳过不执行')
    def test_skip():
        pass
