# -*- coding:utf-8 -*-

import unittest

import nagisa

class TestNagisa(unittest.TestCase):
    def test_tagging(self):
        # test_1 
        text   = 'Pythonで簡単に使えるツールです'
        output = 'Python/名詞 で/助詞 簡単/形状詞 に/助動詞 使える/動詞 ツール/名詞 です/助動詞'
        words = nagisa.tagging(text)
        self.assertEqual(output, str(words))

        # test_2
        text   = 'ニューラルネットワークを使ってます。' 
        output = 'ニューラル/名詞 ネットワーク/名詞 を/助詞 使っ/動詞 て/助動詞 ます/助動詞 。/補助記号'
        self.assertEqual(output, str(nagisa.tagging(text)))

        
        # test_3
        tagger_nn = nagisa.Tagger(single_word_list=['ニューラルネットワーク'])
        output = 'ニューラルネットワーク/名詞 を/助詞 使っ/動詞 て/助動詞 ます/助動詞 。/補助記号'
        self.assertEqual(output, str(tagger_nn.tagging(text)))

        # test_4
        text   = '(人•ᴗ•♡)こんばんは♪'
        output = '(人•ᴗ•♡)/補助記号 こんばんは/感動詞 ♪/補助記号'
        words  = nagisa.tagging(text)
        self.assertEqual(output, str(words))

        # test_5
        url    = 'https://github.com/taishi-i/nagisaでコードを公開中(๑¯ω¯๑)'
        output = 'コード/名詞 公開/名詞 中/接尾辞'
        words   = nagisa.filter(url, filter_postags=['URL', '補助記号', '助詞'])
        self.assertEqual(output, str(words))


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestNagisa))
    return suite

if __name__ == '__main__':
    unittest.main()
