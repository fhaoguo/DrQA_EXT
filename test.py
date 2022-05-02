# -*- coding: utf-8 -*-
# @FileName   :test.py
# @Time       :2022/5/2 16:38
# @Author     :fenghaoguo

import drqa
from drqa.tokenizers import CoreNLPTokenizer
import drqa.reader


def hello():
    drqa.tokenizers.set_default('corenlp_classpath', 'data/corenlp/*')
    tok = CoreNLPTokenizer()
    print(tok.tokenize('hello world').words())


def test_model():
    drqa.reader.set_default('model', 'data/reader/single.mdl')
    reader = drqa.reader.Predictor()
    print(reader)


if __name__ == '__main__':
    test_model()