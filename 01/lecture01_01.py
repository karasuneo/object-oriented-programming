#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inspect import Attribute


def lecture01_01() -> None:
      
      #辞書型のオブジェクトhを宣言すること
      h={}
      
      #hに，キー（“ID”）に自身の学籍番号を代入すること．
      h["ID"] = 'k21116'
      
      #hに，キー（“attributes”）にタプル型で名前と年齢と性別(例：(“名前”，22，”男”))を代入すること．
      h["attributes"] = ('水谷祐生', 20, '男')
      
      # hをprint関数で出力せよ．
      print('h= ', h)
      
      #hのキー一覧をprint関数で出力せよ．
      print(h.keys())
      
      # hのキーの型をprint関数で出力せよ．
      print(type(h.keys()))
      
      #h[“attributes”]の型をprint関数で出力せよ．
      print(type(h['attributes']))
            
      #h[“attributes”]の各要素を１行づつprint関数で出力せよ．(for e in attr:)
      for x in h['attributes']:
            print(x) 
            
      # h[“attributes”]の各要素の型を１行づつprint関数で出力せよ．(for e in attr:)
      for x in h['attributes']:
            print(type(x)) 

if __name__ == '__main__':
      lecture01_01()
      
      
      