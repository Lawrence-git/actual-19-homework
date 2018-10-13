#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : db.py
# @Author: ZhouGui
# @Date  : 2018/9/15
# @Description :数据库操作
import os
import pymysql
from utils import config


def connect():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    INIFILE = os.path.join(BASEDIR, 'conf.ini')
    try:
        dbinfo = config.ReadConfigFile(INIFILE, 'DB')
    except Exception as e:
        return 'mysql connect failed '
    return pymysql.connect(**dict(dbinfo))


def add_user(sql):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as  e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def del_user(sql):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        if cur.rowcount == 1:
            print("Delete successfully")
        else:
            print("Delete failed.")
    except Exception as  e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def update_user(sql):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        if cur.rowcount == 1:
            print("update successfully")
        else:
            print("update failed.")
    except Exception as  e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def select_user(sql):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        rows = cur.fetchall()
        return rows
    except Exception as  e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def list_user():
    users = []
    sql = 'select * from user;'
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        users_data = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    for info in users_data:
        user_dict = {}
        user_dict['id'] = info[0]
        user_dict['name'] = info[1]
        user_dict['age'] = info[2]
        user_dict['tel'] = info[3]
        user_dict['address'] = info[4]
        users.append(user_dict)

    return users
