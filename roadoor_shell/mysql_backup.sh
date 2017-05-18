#!/bin/bash

# author hanson
# date 2015/7/13
# mysql db backup
# add by leo,date 2015/08/12

mysql_path=/usr/local/mysql
mysql_user='root'
mysql_pwd=''
#routeip='172.16.10.14'
#routepath='/data/db_bak/172.16.10.22/'

bak_path=/data/db_bak/local

# delete expire backupsets
find $bak_path -daystart -ctime +30 | xargs rm -rf

today=`date +%Y%m%d`

if [ ! -d $bak_path/$today ]; then
        mkdir -p $bak_path/$today
fi

full_scritps_path=$bak_path/$today/'roadoor_init_script.sql'
full_data_path=$bak_path/$today/'roadoor_data.sql.gz'

#$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd -e "stop slave;"
#$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd -e "show slave status\G;" > $bak_path/$today/slave_status.txt
$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd -e "show master status\G;" > $bak_path/$today/master_status.txt

$mysql_path/bin/mysqldump -u$mysql_user -p$mysql_pwd -A -d -R -E > $full_scritps_path && $mysql_path/bin/mysqldump -u$mysql_user -p$mysql_pwd -A | gzip > $full_data_path

#sleep 30
$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd -e "flush logs;"
#$mysql_path/bin/mysql -u$mysql_user -p$mysql_pwd -e "start slave;"

cp /etc/my.cnf $bak_path/$today/
#sudo -u webuser scp -r $bak_path/$today  webuser@$routeip:$routepath

exit 0
# delete expire backupsets
#find $bak_path -daystart -ctime +1 | xargs rm -rf

# scp route backup mechine
#user='root'
#password='roadoor.com'
#routeip='172.16.10.14'
#routepath='/data/db_bak/172.16.10.32/'

#push_db_bak_data() {
#expect -c "
#set timeout 3600;
#spawn scp -r $bak_path/$today $user@$routeip:$routepath
#expect {
#        \"*yes/no*\" {send \"yes\r\";exp_continue}
#        \"*password*\" {send \"$password\r\";}
#        }
#expect eof;"
#}
#push_db_bak_data

# delete expire backupsets
#find $bak_path -daystart -ctime +3 | xargs rm -rf


