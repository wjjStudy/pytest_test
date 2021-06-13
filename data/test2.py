# 1. 导入包
import requests
import json

# 2. 组装请求
def test_add_normal():
    # url  字符串格式
    # url = base_url + "/add/"
    url = base_url + "/api/sub/"
    # headers = {"Content-Type": "application/json"}
    # data {} 字典格式
    data = {"a": "3", "b": "2"}
    # print('转换前',type(data))
    # data = json.dumps(data)  #将请求数据转化为字符串（将 Python 对象编码成 JSON 字符串）
    # print('转换后',type(data))
    # 3. 发送请求,获取响应对象
    # response = requests.post(url, data)
    response = requests.post(url=url, json=data)
    print('response类型', type(response))
    # 4. 解析响应
    # 5. 断言结果

    assert response.json().get("code") == '100000'
    assert response.json().get("msg") == "成功"
    print(response.json().get("data"))
    assert response.json().get("data") == "1.0"



if __name__ == '__main__':
    base_url = "http://127.0.0.1:5000"
    test_add_normal()

