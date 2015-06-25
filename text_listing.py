# -*- coding: utf-8 -*-

import MeCab
import json
import os

"""
in : '関数型言語では関数を第一級オブジェクトとして扱う。'
out: ['関数', '型', '言語', '関数', '一', '級', 'オブジェクト']
"""
def make_noun_list(text) :
    tagger = MeCab.Tagger("mecabrc")
    noun_list = filter(lambda n : ("名詞" in n and ("一般" in n or "固有名詞" in n)), tagger.parse(text.encode("utf-8")).split("\n"))
    return map(lambda n : n.split("\t")[0], noun_list)

def make_text_list(directory) :
    return map(lambda n : open(os.path.join(directory, n)).read(), os.listdir(directory))

def text_list_from_json(jsonfile, key) :
    return map(lambda n : n[key], json.load(open(jsonfile, 'r')))
