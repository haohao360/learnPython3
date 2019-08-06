# -*- coding:utf8 -*-
'''
Created on 2019��8��2��
 
@author: Administrator
'''


import requests
import lxml.html
import re
from lxml import html
from urllib import parse
import json
from builtins import str

url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
r = requests.get(url)
r.encoding #获取res的编码格式
r.headers   #获取Content-Type内容
r.apparent_encoding   #获取网页正确的编码格式
html2 = r.text# 返回的结果是处理过的Unicode类型的数据
#print(r.encoding)#获得网页源码的格式 打印显示 ISO-8859-1
etree = html.etree
html =etree.HTML(html2)
a= html.xpath('//div[@class="list_num "]')
redli= html.xpath('//div[@class="list_num red"]')
#print(len(a)) #17
#print(len(redli))
i =0;
for item in a:
    i+=1;
#   print(a[i-1])


ul =html.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/child::*')
'''
print(len(ul)) #20 <li>
print(ul[0])
print(type(ul[0]))
print(ul[0].tag)#获取<li>标签名
print(ul[0][0].attrib)#  {'class': 'list_num red'}  获取标签的属性和class
print(ul[0][0].text)#获取<a>标签的文字部分
print(ul[1][0].text)

print(etree.tostring(ul[0])) #b'<li>&#13;\n    <div class="list_num red">1.</div>   &#13;\n    <div class="pic"><a href="http://product.dangdang.com/27883500.html" target="_blank"><img src="http://img3m0.ddimg.cn/51/4/27883500-1_l_6.jpg" alt="&#25105;&#20801;&#35768;&#20320;&#65292;&#22312;&#25105;&#24515;&#19978;&#34892;&#36208;&#65306;&#20840;&#19990;&#30028;&#26368;&#32654;&#30340;&#24773;&#20070;&#65288;&#20462;&#35746;&#29645;&#34255;&#29256;&#65289;" title="&#25105;&#20801;&#35768;&#20320;&#65292;&#22312;&#25105;&#24515;&#19978;&#34892;&#36208;&#65306;&#20840;&#19990;&#30028;&#26368;&#32654;&#30340;&#24773;&#20070;&#65288;&#20462;&#35746;&#29645;&#34255;&#29256;&#65289;" /></a></div>    &#13;\n    <div class="name"><a href="http://product.dangdang.com/27883500.html" target="_blank" title="&#25105;&#20801;&#35768;&#20320;&#65292;&#22312;&#25105;&#24515;&#19978;&#34892;&#36208;&#65306;&#20840;&#19990;&#30028;&#26368;&#32654;&#30340;&#24773;&#20070;&#65288;&#20462;&#35746;&#29645;&#34255;&#29256;&#65289;">&#25105;&#20801;&#35768;&#20320;&#65292;&#22312;&#25105;&#24515;&#19978;&#34892;&#36208;&#65306;&#20840;&#19990;&#30028;&#26368;&#32654;&#30340;&#24773;&#20070;&#65288;&#20462;&#35746;&#29645;&#34255;&#29256;&#65289;</a></div>    &#13;\n    <div class="star"><span class="level"><span style="width: 97.2%;"></span></span><a href="http://product.dangdang.com/27883500.html?point=comment_point" target="_blank">5234&#26465;&#35780;&#35770;</a><span class="tuijian">100%&#25512;&#33616;</span></div>    &#13;\n    <div class="publisher_info"><a href="http://search.dangdang.com/?key=&#24352;&#36827;&#27493;" title="&#24352;&#36827;&#27493; &#31243;&#30887;/&#20027;&#32534; &#26089;&#34299;/&#35793;" target="_blank">&#24352;&#36827;&#27493;</a> <a href="http://search.dangdang.com/?key=&#31243;&#30887;" title="&#24352;&#36827;&#27493; &#31243;&#30887;/&#20027;&#32534; &#26089;&#34299;/&#35793;" target="_blank">&#31243;&#30887;</a>/&#20027;&#32534; <a href="http://search.dangdang.com/?key=&#26089;&#34299;" title="&#24352;&#36827;&#27493; &#31243;&#30887;/&#20027;&#32534; &#26089;&#34299;/&#35793;" target="_blank">&#26089;&#34299;</a>/&#35793;</div>    &#13;\n    <div class="publisher_info"><span>2019-06-01</span>&#160;<a href="http://search.dangdang.com/?key=&#21271;&#26041;&#25991;&#33402;&#20986;&#29256;&#31038;" target="_blank">&#21271;&#26041;&#25991;&#33402;&#20986;&#29256;&#31038;</a></div>    &#13;\n&#13;\n            <div class="biaosheng">&#20116;&#26143;&#35780;&#20998;&#65306;<span>5044&#27425;</span></div>&#13;\n                      &#13;\n    &#13;\n    <div class="price">        &#13;\n        <p><span class="price_n">&#165;34.50</span>&#13;\n                        <span class="price_r">&#165;69.00</span>(<span class="price_s">5.0&#25240;</span>)&#13;\n                    </p>&#13;\n                    <p class="price_e"></p>&#13;\n                <div class="buy_button">&#13;\n                          <a ddname="&#21152;&#20837;&#36141;&#29289;&#36710;" name="" href="javascript:AddToShoppingCart(\'27883500\');" class="listbtn_buy" id="">&#21152;&#20837;&#36141;&#29289;&#36710;</a>&#13;\n                        &#13;\n                        <a ddname="&#21152;&#20837;&#25910;&#34255;" id="addto_favorlist_27883500" name="" href="javascript:showMsgBox(\'addto_favorlist_27883500\',encodeURIComponent(\'27883500&amp;platform=3\'), \'http://myhome.dangdang.com/addFavoritepop\');" class="listbtn_collect">&#25910;&#34255;</a>&#13;\n     &#13;\n        </div>&#13;\n&#13;\n    </div>&#13;\n  &#13;\n    </li>    &#13;\n    &#13;\n    '
'''
li1 = ul[0].xpath('//div[@class="name"]')
'''
print(type(li[0]))
print(li[0].tag)
print(li[0][0].text)
#print(li[0].xpath('div[]'))
'''
#print(type(ul))
#print(len(ul))
i=0
for li in ul:
    '''
    print('@@')
    print(len(li))
    print(li[0].tag)
    print(li[0].attrib)
    '''
    div1 = li.xpath('//div[@class="name"]')
    '''
    print(type(div1))
    print('##')
    print(div1[i].tag)
    print(div1[i].attrib)
    '''
    a1 = div1[i].xpath('./a/@title')
    '''
    print("!!!!!!!!!!!!!!!!")
    print(len(a1))
    print(type(a1))
    '''
    print(a1[0])
    i+=1
   
    
    

   


        