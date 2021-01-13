## 🌈HTU_autoCheck

**完美校园健康打卡**

- 随机温度(36.2℃-36.7℃)🌡
- 基于GitHub Actions，完全解放你的设备和服务器✔
- 打卡时间5点40分左右
- 项目仅供学习研究，为了疫情防控，大家还是要早起打卡哦

## 研究方法

#### 1、点击右上角fork，fork到自己的GitHub上

#### 2、设置Secrets，输入项目运行的数据

- 先找到自己fork的库，点击Settings->Secrets->New sceret

- 字段名要大写，下面的值则填写自己的值(不要加其他标点之类的,直接填写就可)，共6个

- 要认真填哦，这关系你之后能否成功运行代码

- ```
  # 设置如下secret字段，直接填入值即可，不要加引号之类的东西
  """
  PHONE       (完美校园账号)       大概率是你的手机号
  PASSWORD    (完美校园密码)
  PPHONE      (紧急联系人名字)
  PNAME       (紧急联系人电话)
  SCKEY       (Server酱微信推送)   例：https://sc.ftqq.com/【SENDKEY_Server酱的密匙】.send
  AREASTR     (打卡地址)           例：{"streetNumber":"","street":"","district":"","city":"郑州市","province":"河南省","town":"","pois":"xxxx","lng":经度,"lat":纬度,"address":"新郑市双湖大道居易·国际城北区","text":"河南省-郑州市","code":""}
  # 打卡地址说明
  # street    -街道名                eg.开元大道（有则写，没有则不用写）
  # district  -县级市或县            eg.新郑市或xx县
  # city      -地级市                eg.郑州市
  # town      -可空
  # pois      -打卡定位时附近的地点   eg.xxxx小区 或 xxxx商铺（不加县级市或者县）
  # 经纬度可去 -https://jingweidu.bmcx.com/ 网站查询
  # address   -同pois但是要加上县级市和街道名，附近没有街道名就不用写街道了  eg.新郑市双湖大道居易·国际城北区
  # code      -可空
  # 地点可参照完美校园中的打卡地点填写，如果不成功可抓包尝试
  
  """
  ```

#### 3、开启Actions

- 找到自己fork的库，点击Settings->Action->I understand...

- 回到项目主页，任意添加修改README.md并保存即可触发Actions（开始运行）

#### 4、查看结果

- 通过Update README.md -- > bot  或者手机微信推送查看
- 成功之后则开启了自动化部署（每天早上六点自动打卡）
- 如果失败，则在Actions -- > Update README.md -- > bot中查看报错情况，解决不了可提交Issues



## Q&A

**1、fork之后，修改README.md并没有触发actions**？

到 Actions中开启workflow，-- > Enable workflow

**2、想修改脚本自动运行时间怎么办？**

在 .github/workflows/run.yml 修改时间

```python
  schedule:
    - cron: 0 22 * * *
"""
cron就是脚本运行时间，22对应的时间是世界标准时UTC，在时刻上尽量接近于格林威治标准时间，22对应北京时间早上六点
详细对应关系可查看：http://timebie.com/cn/universalbeijing.php
"""
```

**3、当发现报错显示密码错误，还有 * 次后冻结，请立马修改 secrets 的密码再尝试运行**



## 代码参考及详细教程

https://github.com/ReaJason/17wanxiaoCheckin-Actions

https://github.com/YooKing/HAUT_autoCheck/
