from lxml import etree
text = '''
<div>
    <ul>.
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

text1 = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

text2 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
text3 = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
#print(result.decode('utf-8'))


html = etree.parse('./test.html', etree.HTMLParser())
# 选取所有节点
result = html.xpath('//*')

# 选取所有li节点
result = html.xpath('//li')

# 选取所有li节点下的所有a子节点
result = html.xpath('//li/a')

# 选取ul节点下的所有子孙a节点
result = html.xpath('//ul//a')

# 选中href是link4.html的a节点，然后再获取其父节点，然后再获取其classss属性
result = html.xpath('//a[@href="link4.html"]/../@class')

# 通过parent::来获取父节点实现上述功能
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')

# 通过text()方法获取文本，获取一下上文 li 节点中的文本
result = html.xpath('//li/a/text()')

#  获取所有li节点下的所有a节点的href属性
result = html.xpath('//li/a/@href')


# 属性多值匹配
html1 = etree.HTML(text1)
result = html1.xpath('//li[contains(@class,"li")]/a/text()')

# 多属性匹配
html2 = etree.HTML(text2)
result = html2.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')

# 按序选择
html3 = etree.HTML(text3)
result = html3.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
