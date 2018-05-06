#!/bin/bash

PID_FILE="pid"
LOG_FILE="`date +%Y-%m-%d`.log"
start()
{
     if [ -f ${PID_FILE} ];then
            SPID=`cat ${PID_FILE}`
            if [ "$SPID" != "" ];then
               echo "stop it first"
               exit
            fi
     fi

    echo "Starting"
    nohup python application.py >$LOG_FILE 2>&1 & my_pid=$!
    echo "$my_pid" > $PID_FILE
    echo "Started"
}

stop()
{

     if [ -f ${PID_FILE} ];then
            SPID=`cat ${PID_FILE}`
            if [ "$SPID" != "" ];then
               kill -9  $SPID
               echo  > $PID_FILE
               echo "stop success"
            fi
     fi
}
stop
start