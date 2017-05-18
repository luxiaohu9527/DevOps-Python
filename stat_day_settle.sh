#!/bin/bash

# author : hanson
# date   : 2015/11/26
# 活期标日结主过程调用，每天凌晨1点执行

/usr/local/mysql/bin/mysql -uroot -p'+DZK;$Y2_1ct6B$erqT.' <<EOF

use scjr;
call sp_stat_main();
call sp_rep_user_analysis_product();

EOF
