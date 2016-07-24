
### 简单介绍

一个用命令行查询12306火车票信息的软件.

可以显示车次信息,座位等详细信息.

### 用法

命令行格式

Usage:
    python3 TicketsInfo.py [-gdtkz] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:
    python3 TicketInfo.py 南京 北京 2016-07-01
    python3 TicketInfo.py -dg 南京 北京 2016-07-01

一些查询结果的过滤功能暂时还没有实现,后续有待加强.

### 依赖的库

> pip3 install docopt

这是个命令行解释器,比 optParser 使用起来要方便一些.

> pip3 install requests

用于发起restful 请求到12306的网站

> pip3 install prettytable

用于格式化显示查询结果.

### 待优化

没有异常检验,对日期,地名等.包括日期格式,包括日期是否合理.
