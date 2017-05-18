#!/bin/bash

# author hanson
# date 2016/3/18
# 每月1号零点统计上一月的成交量

export LANG=en_US.UTF-8

mysql_path='/usr/local/mysql'
mysql_user='root'
mysql_pwd='+DZK;$Y2_1ct6B$erqT.'


$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd <<EOF

use p2p_db;
call sp_stat_trade_amount();

EOF

