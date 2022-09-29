#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def lecture02_02() -> None:
      import xml.etree.ElementTree as ET
      book = ET.Element('book')
      article = ET.SubElement(book, 'article')
      article.attrib['title'] = str("卒業論文")
      
      articles = []
      for i in range(7):
            if i == 0 :
                  continue
            
            chapter = ET.SubElement(article, 'chapter')
            chapter.attrib['id'] = str(i) 
            if i == 1 :
                  chapter.attrib['name'] = str("はじめに")
                  chapter.attrib['pages'] = str("2")
            if i == 2 :
                  chapter.attrib['name'] = str("基礎理論")
                  chapter.attrib['pages'] = str("8") 
            if i == 3 :
                  chapter.attrib['name'] = str("実験方法")
                  chapter.attrib['pages'] = str("6") 
            if i == 4 :
                  chapter.attrib['name'] = str("結果と考察")
                  chapter.attrib['pages'] = str("2") 
            if i == 5 :
                  chapter.attrib['name'] = str("まとめ")
                  chapter.attrib['pages'] = str("1") 
            if i == 6 :
                  chapter.attrib['name'] = str("参考文献")
                  chapter.attrib['pages'] = str("2") 
            articles.append(chapter)
      
      novel = ET.SubElement(book, 'novel')
      novels = []
      for i in range(6):
            if i == 0 :
                  continue
            
            chapter = ET.SubElement(novel, 'chapter')
            chapter.attrib['id'] = str(i) 
            if i == 1 :
                  chapter.attrib['name'] = str("１日のはじまり")
                  chapter.attrib['pages'] = str("2")
            if i == 2 :
                  chapter.attrib['name'] = str("朝食")
                  chapter.attrib['pages'] = str("8") 
            if i == 3 :
                  chapter.attrib['name'] = str("仕事")
                  chapter.attrib['pages'] = str("6") 
            if i == 4 :
                  chapter.attrib['name'] = str("帰宅後")
                  chapter.attrib['pages'] = str("2") 
            if i == 5 :
                  chapter.attrib['name'] = str("新しい朝")
                  chapter.attrib['pages'] = str("1") 
            novels.append(chapter)
            
      with open('./xml/lecture02_02_data.xml', 'wb') as f:
            import xml.dom.minidom as md
            f.write(md.parseString(ET.tostring(book, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))

if __name__ == '__main__':
      lecture02_02()