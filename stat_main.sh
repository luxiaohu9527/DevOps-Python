#!/bin/bash
#author: leo
#create: 2015/10/26
cd /usr/local/bin

## 每天记录一次当天的注册人数(从2016-02-20开始不用)
##./stat_report_business_shapshots.sh
## 每天统计前一天的互联网运营支出明细
./stat_report_online_cost.sh
## 每天统计投资、债转、注册人数、投资人数
./stat_report_invest_day.sh
## 每天将优选计划到期的用户退出自动投标
./stat_user_autobid_exit.sh
## 每天车必贷进件数据统计
./stat_report_jinjian.sh
## 每日运营报表统计
./stat_report_business_day.sh

