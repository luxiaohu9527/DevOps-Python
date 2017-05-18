#!/bin/bash

# author hanson
# date 2015/12/28
# 每天统计前一天车贷进件等相关数据

export LANG=en_US.UTF-8

mysql_path='/usr/local/mysql'
mysql_user='root'
mysql_pwd='+DZK;$Y2_1ct6B$erqT.'

yesterday=`date -d yesterday +%Y%m%d`
#yesterday=`date -d "2 days ago" +%Y%m%d`
report_path='/opt/report/'$yesterday
filename=$report_path'/stat_report_jinjian_'$yesterday'.xls'
filetmp=$report_path'/stat_report_jinjian_'$yesterday'.tmp'
file_chs_name=$report_path'/每日车必贷进件数据统计_'$yesterday'.xls'

if [ ! -d $report_path ]; then
	mkdir -p $report_path
	chown -R mysql.root $report_path
fi

$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd <<EOF

use rda;
call sp_stat_jinjian();
SELECT '日期' AS tday,'进件数' AS jinjianshu,'过件数' AS guojianshu,'上标数' AS shangbiaoshu,'放款笔数' AS fangkuanbishu,'放款总金额' AS fangkuanzongjine
UNION ALL
SELECT rj_day,rj_jinjian,rj_guojian,rj_shangbiao,rj_fangkuanshu,rj_fangkuanjine
FROM rda_report_jinjian
WHERE rj_day = $yesterday INTO OUTFILE '$filetmp';

EOF

# 转码
iconv -f utf8 -t gb18030 -o $filename $filetmp
rm -f $filetmp

#转成中文名称
mv $filename $file_chs_name

# 复制到远程机器，系统发邮件给指定人员
user='hanson'
password='han1qaz@WSX'
routeip='172.16.11.254'
routepath='/mail/chebidai/'

push_new_bid_data() {
expect -c "
set timeout 3600;
spawn scp $file_chs_name $user@$routeip:$routepath
expect {
        \"*yes/no*\" {send \"yes\r\";exp_continue}
        \"*password*\" {send \"$password\r\";}
        }
expect eof;"
}
push_new_bid_data
