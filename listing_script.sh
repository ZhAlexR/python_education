#! /bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color
var_path=$(pwd)
cur_date_time=$(date +'%y/%m/%d - %H:%M')
echo -e "Current directory is ${RED}$var_path${NC}"
echo "$cur_date_time"
ls -tlr
