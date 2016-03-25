#!/usr/bin/python
# -*- coding:utf8 -*-
__author__ = 'huangpeng03@baidu.com'

import getopt
import sys
import urllib2
from xml.dom import minidom
from collections import namedtuple
from termcolor import colored

'''
Shell内置插件，用于翻译
'''

KEY = 'E0F0D336AF47D3797C68372A869BDBC5'
URL = 'http://dict-co.iciba.com/api/dictionary.php'

TAG = namedtuple('TAG', 'value color')
TAG_DICT = {
    'orig': TAG('ex. %s', 'green'),
    'trans': TAG('    %s', 'cyan'),
    'acceptation': TAG('%s', 'yellow')
}


def getXMLresponse(words):
    response = urllib2.urlopen(URL + '?key=' + KEY + '&w=' + words)
    return response


def readXml(res):
    dom = minidom.parse(res)
    return dom.documentElement


def show(node):
    if not node.hasChildNodes():
        if node.nodeType == node.TEXT_NODE and node.data != '\n':
            tag_name = node.parentNode.tagName
            content = node.data.replace('\n', '')
            if tag_name in TAG_DICT.keys():
                tag = TAG_DICT[tag_name]
                print colored(tag.value % content, tag.color)
    else:
        for e in node.childNodes:
            show(e)


def main():
    if len(sys.argv) > 1:
        options, args = getopt.getopt(sys.argv[1:], [])
        if args:
            worlds = '_'.join(args)
            res = getXMLresponse(worlds)
            root = readXml(res)
            show(root)


if __name__ == '__main__':
    main()
