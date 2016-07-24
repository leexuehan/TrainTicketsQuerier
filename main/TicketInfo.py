#! /usr/bin/env python
# coding=utf-8

"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
"""

from docopt import docopt
from stations import stations
import requests
from prettytable import PrettyTable


def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_staion = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    # 构建URL
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
            date, from_staion, to_station)

    r = requests.get(url, verify=False)
    rows = r.json()['data']['datas']

    headers = '车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 软座 硬座 无座'.split()
    pt = PrettyTable()
    pt._set_field_names(headers)
    for row in rows:
        # 从row中根据headers过滤信息, 然后调用pt.add_row()添加到表中
        pt.add_row([row.get('station_train_code'), ['始发站:' + row.get('from_station_name'), '终点站:' + row.get('to_station_name')],
                    ['发车时间:' + row.get('start_time'), '到达时间:' + row.get('arrive_time')],
                    row.get('lishi'), row.get('swz_num'), '', '', row.get('rw_num'), row.get('yw_num'),
                    row.get('rz_num'), row.get('yz_num'), row.get('wz_num')])

    print(pt)


if __name__ == '__main__':
    cli()
