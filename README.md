# 济南大学图书馆座位预约系统API
_UJN Library Seat API for Python_
# 说明
Python 版在 libapi 目录下
支持 Python 2 3 蛋疼的编码问题建议 Python 3

本人未参与任何金钱(PY)交易，项目仅供学习交流使用
这是个还不错的 Python 爬虫 HTTP RESTful（RESTful 其实也不正规）学习项目

### 用例
``` Python
正在更新...
```

# API
| API                                           | 功能                           |
|-----------------------------------------------|--------------------------------|
| getToken()                                    | 获取 token                     |
| reservations()                                | 查看预约                       |
| user()                                        | 用户信息                       |
| filters()                                     | 图书馆信息                     |
| roomStats(building_id)                        | 楼层信息                       |
| seatStartTime(seat_id, date)                  | 座位开始时间                   |
| seatEndTime(seat_id, date, start_time)        | 根据座位开始时间得到的结束时间 |
| freeBook(start_time, end_time, seat_id, date) | 预约座位                       |
| layoutByDate(room_id, date)                   | 查看阅览室信息                 |
| checkIn()                                     | 签到                           |
| history(page=1, count=10)                     | 查看预约历史                   |
| cancelRes(res_id)                             | 取消预约                       |
正在更新...
