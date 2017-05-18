#!/bin/bash
IP="localhost"
DB_USER="root"
DB_PASS='+DZK;$Y2_1ct6B$erqT.'
BIN_DIR="/usr/local/mysql/bin"
DATABASE="p2p_db"
FILE=stat_log.txt
DATE_START=`date "+%F %T"`
echo "***************************" >> $FILE
echo "$DATE_START : call sp_user_autobid_exit" >> $FILE
if $BIN_DIR/mysql -u$DB_USER -h$IP -p$DB_PASS -D$DATABASE --default-character-set=utf8 -e " call sp_user_autobid_exit() "; then 
  echo  "`date "+%F %T"` : call success!" >> $FILE
else
  echo "`date "+%F %T"` : call fail!" >> $FILE
fi
