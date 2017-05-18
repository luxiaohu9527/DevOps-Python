#!/bin/bash

# author hanson
# date 2015/9/28
# 删除金额为0的收益计划，每4小时运行一次

mysql_path='/usr/local/mysql'
mysql_user='root'
mysql_pwd='+DZK;$Y2_1ct6B$erqT.'

curr_time=`date "+%Y%m%d%H%M%S"`
bak_name='/opt/db_backup/bug/need_bid_income_plan_'$curr_time'.sql'

records=`$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd p2p_db -e "select count(*) from need_bid_income_plan where principle = 0.00 and interest = 0.00 and delete_flag = 0 and state = 0;"|awk 'NR==2'`

#echo ${records}

if [ ${records} -gt 0 ]
then

$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd <<EOF

use p2p_db;
select * from need_bid_income_plan where principle = 0.00 and interest = 0.00 and delete_flag = 0 and state = 0 into outfile '$bak_name';
update need_bid_income_plan set delete_flag = 1 where principle = 0.00 and interest = 0.00 and delete_flag = 0 and state = 0;

EOF

fi
