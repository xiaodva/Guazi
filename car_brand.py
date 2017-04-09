import requests
from bs4 import BeautifulSoup

main_url="http://www.guazi.com/www/buy/"
def get_brand_urls(main_url):
    webdata=requests.get(main_url)
    soup=BeautifulSoup(webdata.text,'lxml')
    car_name_list=soup.select('ul.o-b-list > li > div > a')
    count=0
    for car_name in car_name_list:
        count+=1
        print(count)
        print('http://www.guazi.com'+car_name.get('href'))
        #print(car_name.get('title'),'http://www.guazi.com'+car_name.get('href'))

get_brand_urls(main_url)

all_car_name='''
                http://www.guazi.com/www/audi/
                http://www.guazi.com/www/astonmartin/
                http://www.guazi.com/www/anchi/
                http://www.guazi.com/www/alpina/
                http://www.guazi.com/www/ac-schnitzer/
                http://www.guazi.com/www/alfaromeo/
                http://www.guazi.com/www/buick/
                http://www.guazi.com/www/bmw/
                http://www.guazi.com/www/honda/
                http://www.guazi.com/www/byd/
                http://www.guazi.com/www/benz/
                http://www.guazi.com/www/biaozhi/
                http://www.guazi.com/www/benteng/
                http://www.guazi.com/www/baojun/
                http://www.guazi.com/www/porsche/
                http://www.guazi.com/www/shenbao/
                http://www.guazi.com/www/beijingqiche/
                http://www.guazi.com/www/huansu/
                http://www.guazi.com/www/beiqi/
                http://www.guazi.com/www/bentley/
                http://www.guazi.com/www/baowo/
                http://www.guazi.com/www/babosi/
                http://www.guazi.com/www/bisu/
                http://www.guazi.com/www/bujiadi/
                http://www.guazi.com/www/baolong/
                http://www.guazi.com/www/baofeili/
                http://www.guazi.com/www/changan/
                http://www.guazi.com/www/changanshangyong/
                http://www.guazi.com/www/changcheng/
                http://www.guazi.com/www/chuanqi1/
                http://www.guazi.com/www/changhe/
                http://www.guazi.com/www/chuanqiyema/
                http://www.guazi.com/www/chenggong/
                http://www.guazi.com/www/dazhong/
                http://www.guazi.com/www/fengxing/
                http://www.guazi.com/www/dongfengxiaokang/
                http://www.guazi.com/www/dongnan/
                http://www.guazi.com/www/dongfengfengshen/
                http://www.guazi.com/www/dongfengfengdu/
                http://www.guazi.com/www/daoqi/
                http://www.guazi.com/www/ds/
                http://www.guazi.com/www/dongfeng/
                http://www.guazi.com/www/jilindafa/
                http://www.guazi.com/www/dayu/
                http://www.guazi.com/www/ford/
                http://www.guazi.com/www/toyota/
                http://www.guazi.com/www/fiat/
                http://www.guazi.com/www/futian/
                http://www.guazi.com/www/fudi/
                http://www.guazi.com/www/fuqiqiteng/
                http://www.guazi.com/www/huaxiangfuqi/
                http://www.guazi.com/www/ferrari/
                http://www.guazi.com/www/jiao/
                http://www.guazi.com/www/gmc/
                http://www.guazi.com/www/guanzhi/
                http://www.guazi.com/www/galue/
                http://www.guazi.com/www/hafu/
                http://www.guazi.com/www/haima/
                http://www.guazi.com/www/huatai/
                http://www.guazi.com/www/hafei/
                http://www.guazi.com/www/huanghai/
                http://www.guazi.com/www/hongqi/
                http://www.guazi.com/www/huapu/
                http://www.guazi.com/www/haige/
                http://www.guazi.com/www/sh-huizhong/
                http://www.guazi.com/www/hanma/
                http://www.guazi.com/www/huasong/
                http://www.guazi.com/www/hengtian/
                http://www.guazi.com/www/hanteng/
                http://www.guazi.com/www/zhongke-huabei/
                http://www.guazi.com/www/huayang/
                http://www.guazi.com/www/fusangheibao/
                http://www.guazi.com/www/jili/
                http://www.guazi.com/www/jianghuai/
                http://www.guazi.com/www/jeep/
                http://www.guazi.com/www/huachen/
                http://www.guazi.com/www/jiebao/
                http://www.guazi.com/www/jiangling/
                http://www.guazi.com/www/jlshwuche/
                http://www.guazi.com/www/jinlv/
                http://www.guazi.com/www/jinlong/
                http://www.guazi.com/www/jiangnan/
                http://www.guazi.com/www/jincheng/
                http://www.guazi.com/www/yiqijiefang/
                http://www.guazi.com/www/cadillac/
                http://www.guazi.com/www/krui/
                http://www.guazi.com/www/chrysler/
                http://www.guazi.com/www/kaiyi/
                http://www.guazi.com/www/kawei/
                http://www.guazi.com/www/kenisaige/
                http://www.guazi.com/www/kaersen/
                http://www.guazi.com/www/suzuki/
                http://www.guazi.com/www/landrover/
                http://www.guazi.com/www/lifan/
                http://www.guazi.com/www/lexus/
                http://www.guazi.com/www/lufeng/
                http://www.guazi.com/www/renault/
                http://www.guazi.com/www/liebao/
                http://www.guazi.com/www/linian/
                http://www.guazi.com/www/lincoln/
                http://www.guazi.com/www/lamborghini/
                http://www.guazi.com/www/lotuscars/
                http://www.guazi.com/www/rolls-royce/
                http://www.guazi.com/www/laolunshi/
                http://www.guazi.com/www/rover/
                http://www.guazi.com/www/mazda/
                http://www.guazi.com/www/mg1/
                http://www.guazi.com/www/mini/
                http://www.guazi.com/www/maserati/
                http://www.guazi.com/www/meiya/
                http://www.guazi.com/www/maybach/
                http://www.guazi.com/www/maikailun/
                http://www.guazi.com/www/dongfengyulongnazhijie/
                http://www.guazi.com/www/njjinlong/
                http://www.guazi.com/www/opel/
                http://www.guazi.com/www/acura/
                http://www.guazi.com/www/oulang/
                http://www.guazi.com/www/kia/
                http://www.guazi.com/www/chery/
                http://www.guazi.com/www/qichen/
                http://www.guazi.com/www/lotus/
                http://www.guazi.com/www/qingling/
                http://www.guazi.com/www/richan/
                http://www.guazi.com/www/rongwei/
                http://www.guazi.com/www/ruilin/
                http://www.guazi.com/www/skoda/
                http://www.guazi.com/www/mitsubishi/
                http://www.guazi.com/www/smart/
                http://www.guazi.com/www/subaru/
                http://www.guazi.com/www/datong/
                http://www.guazi.com/www/shuanglong/
                http://www.guazi.com/www/siming/
                http://www.guazi.com/www/shuanghuan/
                http://www.guazi.com/www/xiaqitongjia/
                http://www.guazi.com/www/siwei/
                http://www.guazi.com/www/saab/
                http://www.guazi.com/www/springo/
                http://www.guazi.com/www/scion/
                http://www.guazi.com/www/saibao1/
                http://www.guazi.com/www/sailin/
                http://www.guazi.com/www/shijue/
                http://www.guazi.com/www/tesila/
                http://www.guazi.com/www/tengshi/
                http://www.guazi.com/www/yiqitongyong/
                http://www.guazi.com/www/tianma/
                http://www.guazi.com/www/tongtian/
                http://www.guazi.com/www/wuling/
                http://www.guazi.com/www/volvo/
                http://www.guazi.com/www/weiwang/
                http://www.guazi.com/www/weilin/
                http://www.guazi.com/www/wushiling/
                http://www.guazi.com/www/weiziman/
                http://www.guazi.com/www/wanfeng/
                http://www.guazi.com/www/hyundai/
                http://www.guazi.com/www/chevrolet/
                http://www.guazi.com/www/citroen/
                http://www.guazi.com/www/brand-xiali/
                http://www.guazi.com/www/xiyate/
                http://www.guazi.com/www/xinkai/
                http://www.guazi.com/www/tj-yiqi/
                http://www.guazi.com/www/infiniti/
                http://www.guazi.com/www/nj-iveco/
                http://www.guazi.com/www/yongyuanqiche/
                http://www.guazi.com/www/yingzhi/
                http://www.guazi.com/www/cf-yangzi/
                http://www.guazi.com/www/zhongtai/
                http://www.guazi.com/www/huachen-zhonghua/
                http://www.guazi.com/www/zhidou/
                http://www.guazi.com/www/zhongxing/
                http://www.guazi.com/www/zhongou/
                http://www.guazi.com/www/zhongshun/
                '''