import time,json,requests,random,datetime
from campus import CampusCard

def main():

    #sectets字段录入
    phone = input()
    password = input()
    areaStr = input()
    sckey = input()

    #提交打卡
    campus = CampusCard(phone, password)
    token = campus.user_info["sessionId"]
    userInfo = getUserInfo(token)
    response = checkIn(areaStr,userInfo,token,phone)
    strTime = getNowTime()
    if response.json()["msg"] == '成功':
        msg = strTime + "打卡成功"
    else:
        msg = strTime + "打卡异常"
    print(msg)
    print(response.json())
    print("-----------------------")
    ff = str(response.json()["data"])
    title = userInfo['username'] + msg + ff
    try:
        print('主用户开始微信推送...')
        wechatPush(title,sckey)
    except:
        print("微信推送出错！")

#时间函数
def getNowTime():
    utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    strTime = utcTime.strftime("%H时%M分%S秒")
    return strTime

#打卡参数配置函数
def getUserJson(areaStr,userInfo,token,phone):
    temperature = 36.4
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
                "propertyname": "isGoWarningAdress",
                "value": "低"
            }, 
            {
                "propertyname": "isis",
                "value": "无异动"
            },
            {
                "propertyname": "temperature",
                "value": "36.5"
            },
            {
                "propertyname": "symptom",
                "value": "无症状"
            },
            {
                "propertyname": "isIsolation",
                "value": "否"
            },
            {
                "propertyname": "isConfirmed",
                "value": "否"
            },
            {
                "propertyname": "isTransitArea",
                "value": "否"
            },
            {
                "propertyname": "cxjh",
                "value": "否"
            },
            {
                "propertyname": "isAlreadyInSchool",
                "value": "否"
            },
            {
                "propertyname": "ownPhone",
                "value": ""
            }
        ],
        "gpsType": 1,
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
def checkIn(areaStr,userInfo,token,phone):
    sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"
    jsons=getUserJson(areaStr,userInfo,token,phone)
    #提交打卡
    response = requests.post(sign_url, json=jsons)
    return response

#微信通知
def wechatPush(title,sckey):
    data = {
            "text":title,
            "desp":"详情见GitHub运行日志：https://github.com/"
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
