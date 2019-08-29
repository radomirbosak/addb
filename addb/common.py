# -*- coding: utf-8 -*-

import datetime


def get_now_utc():
    nowdate = datetime.datetime.utcnow()
    return nowdate.replace(tzinfo=datetime.timezone.utc)

def get_min_utc():
    mindate = datetime.datetime.min
    return mindate.replace(tzinfo=datetime.timezone.utc)

def get_max_utc():
    mindate = datetime.datetime.max
    return mindate.replace(tzinfo=datetime.timezone.utc)
