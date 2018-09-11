#!/usr/bin/env python
# encoding: utf-8

import json

class LoginException(BaseException):
    def __init__(self, account, password, message):
        err = '登录异常:账号:%s 密码:%s %s' % (account, password, message)
        BaseException.__init__(self, err)
        self.err = err
        self.account = account
        self.password = password
        self.message = message

class ParseJsonException(BaseException):
    def __init__(self, s):
        err = "parse str into json dict error, {} is not json".format(s)
        BaseException.__init__(self, err)


class JsonDict(dict):
    """general json object that allows attributes to be bound to and also behaves like a dict"""

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


def parse_json(json_str):
    """parse str into JsonDict"""

    def _obj_hook(pairs):
        """convert json object to python object"""
        o = JsonDict()
        for k, v in pairs.items():
            o[str(k)] = v
        return o
    try:
        return json.loads(json_str, object_hook=_obj_hook)
    except:
        raise ParseJsonException(json_str)