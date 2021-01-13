import time,json,requests,random,datetime
from campus import CampusCard

def main():

    #sectets字段录入
    phone = input()
    password = input()
    phone2 = input()
    name = input()
    areaStr = input()
    sckey = input()

    #提交打卡
    campus = CampusCard(phone, password)
    token = campus.user_info["sessionId"]
    userInfo = getUserInfo(token)
    response = checkIn(areaStr,userInfo,token,phone,phone2,name)
    strTime = getNowTime()
    if response.json()["msg"] == '成功':
        msg = strTime + "打卡成功"
    else:
        msg = strTime + "打卡异常"
    result = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    print(msg + result)
    print("-----------------------")
    title = userInfo['username'] + msg
    try:
        print('主用户开始微信推送...')
        wechatPush(title,sckey,result)
    except:
        print("微信推送出错！")

#时间函数
def getNowTime():
    utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    strTime = utcTime.strftime("%H时%M分%S秒")
    return strTime

#打卡参数配置函数
def getUserJson(areaStr,userInfo,token,phone,phone2,name):
    #随机温度(36.2~36.7)
    a=random.uniform(36.2,36.7)
    temperature = round(a, 1)
    json = {
        "businessType": "epmpics",
        "method": "submitUpInfo",
        "jsonData": {
        "deptStr": {
            "deptid": userInfo['classId'],
            "text": userInfo['classDescription']
        },
        "areaStr": areaStr,
        "reportdate": round(time.time() * 1000),
        "customerid": userInfo['customerId'],
        "deptid": userInfo['classId'],
        "source": "app",
        "templateid": "pneumonia",
        "stuNo": userInfo['stuNo'],
        "username": userInfo['username'],
        "phonenum": phone,
        "userid": userInfo['userId'],
        "updatainfo": [
            {
                "propertyname": "temperature",
                "value": temperature
            },
            {
                "propertyname": "symptom",
                "value": "无症状"
            },
            {
                "propertyname": "isConfirmed",
                "value": "否"
            },
            {
                "propertyname": "isdefinde",
                "value": "否.未隔离"
            },
            {
                "propertyname": "isTouch",
                "value": "否"
            },
            {
                "propertyname": "isTransitArea",
                "value": "否"
            },
            {
                "propertyname": "是否途径或逗留过疫情中，高风险地区？",
                "value": "否"
            },
            {
                "propertyname": "isFFHasSymptom",
                "value": "没有"
            },
            {
                "propertyname": "isContactFriendIn14",
                "value": "没有"
            },
            {
                "propertyname": "xinqing",
                "value": "健康"
            },
            {
                "propertyname": "bodyzk",
                "value": "是"
            },
            {
                "propertyname": "cxjh",
                "value": "否"
            },
            {
                "propertyname": "isleaveaddress",
                "value": "否"
            },
            {
                "propertyname": "isAlreadyInSchool",
                "value": "没有"
            },
            {
                "propertyname": "ownPhone",
                "value": phone
            },
            {
                "propertyname": "emergencyContact",
                "value": name
            },
            {
                "propertyname": "mergencyPeoplePhone",
                "value": phone2
            },
            {
                "propertyname": "assistRemark",
                "value": "无"
            }
        ],
        "customerAppTypeRuleId": 146,
        "clockState": 0,
        "token": token
        },
    }
    return json
#信息获取函数
def getUserInfo(token):
    token={'token':token}
    sign_url = "https://reportedh5.17wanxiao.com/api/clock/school/getUserInfo"
    #获取用户信息
    response = requests.post(sign_url, data=token)
    return response.json()['userInfo']

#打卡提交函数
def checkIn(areaStr,userInfo,token,phone,phone2,name):
    sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"
    jsons=getUserJson(areaStr,userInfo,token,phone,phone2,name)
    #提交打卡
    response = requests.post(sign_url, json=jsons)
    return response

#微信通知
def wechatPush(title,sckey):
    data = {
            "text":title,
            "desp":"详情见运行日志：https://github.com/"
    }
    try:
        req = requests.post(sckey,data)
        if req.json()["errmsg"] == 'success':
            print("Server酱推送服务成功")
        else:
            print("Server酱推送服务失败")
    except:
        print("微信推送参数错误")

if __name__ == '__main__':
    main()
