#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


class Md5Util(object):
    @staticmethod
    def getMd5(raw):
        return hashlib.md5(raw.encode()).hexdigest()


if __name__ == '__main__':
    print(Md5Util.getMd5('jun'))
