import requests, time, json

userId = '******'
password = '******'

params = (
    ('method', 'login'),
)

data = {
  'userId': userId,
  'password': password,
  'service': '',
  'queryString': 'wlanuserip%3D287324d7096b55dfa970b6a32e180d90%26wlanacname%3Df43d705bb44eb56d54f2c8d6500609b4%26ssid%3D%26nasip%3D4eea2cd266564f25c9e41f29ed4b9a83%26snmpagentip%3D%26mac%3Ddfe38b8bfa7cc6c920cf99046fdede2f%26t%3Dwireless-v2%26url%3D1af7de55847f1c8549f5ec14818707e848cc09cec606ed94%26apmac%3D%26nasid%3Df43d705bb44eb56d54f2c8d6500609b4%26vid%3D87b1ac4e088d4cf3%26port%3D1a1a7210b78236d6%26nasportid%3D6e542cb8cfadb3517435ab7861235634ad9b55c45edd91fefdd7df4852012789',
  'operatorPwd': '',
  'operatorUserId': '',
  'validcode': '',
  'passwordEncrypt': 'false'
}

while True:
    try:
        response = requests.post('http://202.118.253.94:8080/eportal/InterFace.do', params=params, data=data)
        if response.status_code == 200:
            response.encoding = 'UTF-8'
            result = json.loads(response.text)
            if 'success' in result['result']:
                print("校园网登入成功！响应为：", response.text)
                break
            elif '密码错误' in result['message']:
                print("密码错误！请重新尝试")
                break
            elif '用户不存在' in result['message']:
                print("用户不存在！请重新尝试")
                break
            else:
                print("失败", response.text)
                time.sleep(3)
        else:
            print("提交请求失败！")
            time.sleep(3)
    except Exception as e:
        print("正在尝试重连......", e)
        time.sleep(3)

