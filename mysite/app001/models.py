from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# class Customer(models.Model):
#     field1 = models.CharField(max_length=200)
#     field2 = models.CharField(max_length=200)
#     field3 = models.CharField(max_length=200)
#     field4 = models.CharField(max_length=200)
#     field5 = models.CharField(max_length=200)
#     def __str__(self):
#         return self.field1

class Spec(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200,verbose_name="規格說明")
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2
class Cust(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2


class Item000(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    field6 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.field1

class Item001(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="幾號機")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")
 
 
#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")

#--- code1 for model.py (end) -----

  
    def __str__(self):
        return self.field1
# 客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%	客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				

class Item003v2(models.Model):
    CHOICE01 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('無法修復','無法修復'),
    )
    CHOICE02 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('裂縫','裂縫'),
        ('磨損、裂縫','磨損、裂縫'),
    )
    CHOICE03 = (
        ('---','---'),
        ('正常','正常'),
        ('平面變型','平面變型'),
        ('無法修復','無法修復'),
    )
    CHOICE04 = (
        ('---','---'),
        ('正常','正常'),
        ('平面變型','平面變型'),
        ('無法修復','無法修復'),
    )
    CHOICE05 = (
        ('---','---'),
        ('正常','正常'),
        ('合模缸漏油','合模缸漏油'),
        ('合模缸螺旋斷裂','合模缸螺旋斷裂'),
        ('合模活塞磨損','合模活塞磨損'),
        ('無法修復','無法修復'),
    )
    CHOICE06 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('無法修復','無法修復'),
    )
    CHOICE07 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('斷裂','斷裂'),
        ('無法修復','無法修復'),
    )
    CHOICE08 = (
        ('---','---'),
        ('正常','正常'),
        ('開關損壞','開關損壞'),
        ('線路不通','線路不通'),
        ('無法修復','無法修復'),
    )
    CHOICE09 = (
        ('---','---'),
        ('正常','正常'),
        ('無壓力','無壓力'),
        ('線路不通','線路不通'),
        ('壓射缸漏油','壓射缸漏油'),
        ('射杆彎曲','射杆彎曲'),
    )
    CHOICE10 = (
        ('---','---'),
        ('正常','正常'),
        ('斷線','斷線'),
        ('短路','短路'),
        ('鏈條斷','鏈條斷'),
        ('編碼器異常','編碼器異常'),
        ('銅套磨損','銅套磨損'),
    )
    CHOICE11 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('斷裂','斷裂'),
        ('接頭滑絲','接頭滑絲'),
    )
    CHOICE12 = (
        ('---','---'),
        ('正常','正常'),
        ('破損','破損'),
        ('堵塞','堵塞'),
    )
    CHOICE13 = (
        ('---','---'),
        ('正常','正常'),
        ('油品變質','油品變質'),
    )
    CHOICE14 = (
        ('---','---'),
        ('正常','正常'),
        ('磨損','磨損'),
        ('軸心斷裂','軸心斷裂'),
    )
    CHOICE15 = (
        ('---','---'),
        ('正常','正常'),
        ('線路不通','線路不通'),
        ('閥心斷裂','閥心斷裂'),
    )
    CHOICE16 = (
        ('---','---'),
        ('正常','正常'),
        ('管道不通','管道不通'),
        ('管道斷裂','管道斷裂'),
        ('泵心磨損','泵心磨損'),
    )
    CHOICE17 = (
        ('---','---'),
        ('正常','正常'),
        ('鋼瓶裂縫','鋼瓶裂縫'),
        ('壓力過高','壓力過高'),
        ('壓力過低','壓力過低'),
    )
    CHOICE18 = (
        ('---','---'),
        ('正常','正常'),
        ('線路不通','線路不通'),
        ('短路','短路'),
    )
    CHOICE19 = (
        ('---','---'),
        ('正常','正常'),
        ('霧化器損壞','霧化器損壞'),
        ('線路不通','線路不通'),
        ('緩衝彈簧斷裂','緩衝彈簧斷裂'),
    )
    CHOICE20 = (
        ('---','---'),
        ('正常','正常'),
        ('開關損壞','開關損壞'),
        ('軸承磨損','軸承磨損'),
        ('緩衝器斷裂','緩衝器斷裂'),
        ('線路不通','線路不通'),
        ('編碼器異常','編碼器異常'),
    )
    CHOICE21 = (
        ('---','---'),
        ('正常','正常'),
        ('尺寸NG','尺寸NG'),
        ('模崩','模崩'),
        ('模芯斷','模芯斷'),
        ('重覆修模','重覆修模'),
        ('待修模','待修模'),
    )
# generated by make-code-item003.py
    headera = models.CharField(default=".",max_length=99,verbose_name="幾號機")
    headerb = models.CharField(default=".",max_length=99,verbose_name="噸位")
    headerc = models.CharField(default=".",max_length=99,verbose_name="人員")
    headerd = models.DateField(verbose_name="日期")
    data01a = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    data01b = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    data01c = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    data01d = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    data01e = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明", choices=CHOICE01)
    data02a = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    data02b = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    data02c = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    data02d = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    data02e = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明", choices=CHOICE02)
    data03a = models.CharField(default=".",max_length=99,verbose_name="模板(定)-零件")
    data03b = models.CharField(default=".",max_length=99,verbose_name="模板(定)-進度一")
    data03c = models.CharField(default=".",max_length=99,verbose_name="模板(定)-進度二")
    data03d = models.CharField(default=".",max_length=99,verbose_name="模板(定)-進度三")
    data03e = models.CharField(default=".",max_length=99,verbose_name="模板(定)-備註說明", choices=CHOICE03)
    data04a = models.CharField(default=".",max_length=99,verbose_name="模板(動)-零件")
    data04b = models.CharField(default=".",max_length=99,verbose_name="模板(動)-進度一")
    data04c = models.CharField(default=".",max_length=99,verbose_name="模板(動)-進度二")
    data04d = models.CharField(default=".",max_length=99,verbose_name="模板(動)-進度三")
    data04e = models.CharField(default=".",max_length=99,verbose_name="模板(動)-備註說明", choices=CHOICE04)
    data05a = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    data05b = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    data05c = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    data05d = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    data05e = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明", choices=CHOICE05)
    data06a = models.CharField(default=".",max_length=99,verbose_name="曲軸-零件")
    data06b = models.CharField(default=".",max_length=99,verbose_name="曲軸-進度一")
    data06c = models.CharField(default=".",max_length=99,verbose_name="曲軸-進度二")
    data06d = models.CharField(default=".",max_length=99,verbose_name="曲軸-進度三")
    data06e = models.CharField(default=".",max_length=99,verbose_name="曲軸-備註說明", choices=CHOICE06)
    data07a = models.CharField(default=".",max_length=99,verbose_name="鋼帶-零件")
    data07b = models.CharField(default=".",max_length=99,verbose_name="鋼帶-進度一")
    data07c = models.CharField(default=".",max_length=99,verbose_name="鋼帶-進度二")
    data07d = models.CharField(default=".",max_length=99,verbose_name="鋼帶-進度三")
    data07e = models.CharField(default=".",max_length=99,verbose_name="鋼帶-備註說明", choices=CHOICE07)
    data08a = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    data08b = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    data08c = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    data08d = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    data08e = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明", choices=CHOICE08)
    data09a = models.CharField(default=".",max_length=99,verbose_name="壓射系統-零件")
    data09b = models.CharField(default=".",max_length=99,verbose_name="壓射系統-進度一")
    data09c = models.CharField(default=".",max_length=99,verbose_name="壓射系統-進度二")
    data09d = models.CharField(default=".",max_length=99,verbose_name="壓射系統-進度三")
    data09e = models.CharField(default=".",max_length=99,verbose_name="壓射系統-備註說明", choices=CHOICE09)
    data10a = models.CharField(default=".",max_length=99,verbose_name="澆注系統-零件")
    data10b = models.CharField(default=".",max_length=99,verbose_name="澆注系統-進度一")
    data10c = models.CharField(default=".",max_length=99,verbose_name="澆注系統-進度二")
    data10d = models.CharField(default=".",max_length=99,verbose_name="澆注系統-進度三")
    data10e = models.CharField(default=".",max_length=99,verbose_name="澆注系統-備註說明", choices=CHOICE10)
    data11a = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    data11b = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    data11c = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    data11d = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    data11e = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明", choices=CHOICE11)
    data12a = models.CharField(default=".",max_length=99,verbose_name="過濾網-零件")
    data12b = models.CharField(default=".",max_length=99,verbose_name="過濾網-進度一")
    data12c = models.CharField(default=".",max_length=99,verbose_name="過濾網-進度二")
    data12d = models.CharField(default=".",max_length=99,verbose_name="過濾網-進度三")
    data12e = models.CharField(default=".",max_length=99,verbose_name="過濾網-備註說明", choices=CHOICE12)
    data13a = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    data13b = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    data13c = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    data13d = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    data13e = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明", choices=CHOICE13)
    data14a = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    data14b = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    data14c = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    data14d = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    data14e = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明", choices=CHOICE14)
    data15a = models.CharField(default=".",max_length=99,verbose_name="電磁閥-零件")
    data15b = models.CharField(default=".",max_length=99,verbose_name="電磁閥-進度一")
    data15c = models.CharField(default=".",max_length=99,verbose_name="電磁閥-進度二")
    data15d = models.CharField(default=".",max_length=99,verbose_name="電磁閥-進度三")
    data15e = models.CharField(default=".",max_length=99,verbose_name="電磁閥-備註說明", choices=CHOICE15)
    data16a = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-零件")
    data16b = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-進度一")
    data16c = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-進度二")
    data16d = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-進度三")
    data16e = models.CharField(default=".",max_length=99,verbose_name="潤滑系統-備註說明", choices=CHOICE16)
    data17a = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    data17b = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    data17c = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    data17d = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    data17e = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明", choices=CHOICE17)
    data18a = models.CharField(default=".",max_length=99,verbose_name="電路控制-零件")
    data18b = models.CharField(default=".",max_length=99,verbose_name="電路控制-進度一")
    data18c = models.CharField(default=".",max_length=99,verbose_name="電路控制-進度二")
    data18d = models.CharField(default=".",max_length=99,verbose_name="電路控制-進度三")
    data18e = models.CharField(default=".",max_length=99,verbose_name="電路控制-備註說明", choices=CHOICE18)
    data19a = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    data19b = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    data19c = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    data19d = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    data19e = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明", choices=CHOICE19)
    data20a = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    data20b = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    data20c = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    data20d = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    data20e = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明", choices=CHOICE20)
    data21a = models.CharField(default=".",max_length=99,verbose_name="模具-零件")
    data21b = models.CharField(default=".",max_length=99,verbose_name="模具-進度一")
    data21c = models.CharField(default=".",max_length=99,verbose_name="模具-進度二")
    data21d = models.CharField(default=".",max_length=99,verbose_name="模具-進度三")
    data21e = models.CharField(default=".",max_length=99,verbose_name="模具-備註說明", choices=CHOICE21)
    def __str__(self):
        return self.headera

class Item003(models.Model):
    field1 = models.CharField(primary_key=True,max_length=200,verbose_name="壓鑄機編號")
    field1a = models.CharField(default=".",max_length=200,verbose_name="噸位")
    r01c6 = models.CharField(default=".",max_length=99,verbose_name="人員")
    r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")
 
 
#--- code1 for model.py (start) -----

    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
    r04c3 = models.CharField(default=".",max_length=99,verbose_name="機架底座-零件")
    r04c4 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度一")
    r04c5 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度二")
    r04c6 = models.CharField(default=".",max_length=99,verbose_name="機架底座-進度三")
    r04c7 = models.CharField(default=".",max_length=99,verbose_name="機架底座-備註說明")
    r05c3 = models.CharField(default=".",max_length=99,verbose_name="模板-零件")
    r05c4 = models.CharField(default=".",max_length=99,verbose_name="模板-進度一")
    r05c5 = models.CharField(default=".",max_length=99,verbose_name="模板-進度二")
    r05c6 = models.CharField(default=".",max_length=99,verbose_name="模板-進度三")
    r05c7 = models.CharField(default=".",max_length=99,verbose_name="模板-備註說明")
    r06c3 = models.CharField(default=".",max_length=99,verbose_name="合模-零件")
    r06c4 = models.CharField(default=".",max_length=99,verbose_name="合模-進度一")
    r06c5 = models.CharField(default=".",max_length=99,verbose_name="合模-進度二")
    r06c6 = models.CharField(default=".",max_length=99,verbose_name="合模-進度三")
    r06c7 = models.CharField(default=".",max_length=99,verbose_name="合模-備註說明")
    r07c3 = models.CharField(default=".",max_length=99,verbose_name="間隙-零件")
    r07c4 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度一")
    r07c5 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度二")
    r07c6 = models.CharField(default=".",max_length=99,verbose_name="間隙-進度三")
    r07c7 = models.CharField(default=".",max_length=99,verbose_name="間隙-備註說明")
    r08c3 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-零件")
    r08c4 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度一")
    r08c5 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度二")
    r08c6 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-進度三")
    r08c7 = models.CharField(default=".",max_length=99,verbose_name="膜厚調節-備註說明")
    r10c3 = models.CharField(default=".",max_length=99,verbose_name="油管-零件")
    r10c4 = models.CharField(default=".",max_length=99,verbose_name="油管-進度一")
    r10c5 = models.CharField(default=".",max_length=99,verbose_name="油管-進度二")
    r10c6 = models.CharField(default=".",max_length=99,verbose_name="油管-進度三")
    r10c7 = models.CharField(default=".",max_length=99,verbose_name="油管-備註說明")
    r11c3 = models.CharField(default=".",max_length=99,verbose_name="過濾-零件")
    r11c4 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度一")
    r11c5 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度二")
    r11c6 = models.CharField(default=".",max_length=99,verbose_name="過濾-進度三")
    r11c7 = models.CharField(default=".",max_length=99,verbose_name="過濾-備註說明")
    r12c3 = models.CharField(default=".",max_length=99,verbose_name="油箱-零件")
    r12c4 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度一")
    r12c5 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度二")
    r12c6 = models.CharField(default=".",max_length=99,verbose_name="油箱-進度三")
    r12c7 = models.CharField(default=".",max_length=99,verbose_name="油箱-備註說明")
    r13c3 = models.CharField(default=".",max_length=99,verbose_name="馬達-零件")
    r13c4 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度一")
    r13c5 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度二")
    r13c6 = models.CharField(default=".",max_length=99,verbose_name="馬達-進度三")
    r13c7 = models.CharField(default=".",max_length=99,verbose_name="馬達-備註說明")
    r15c3 = models.CharField(default=".",max_length=99,verbose_name="潤滑-零件")
    r15c4 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度一")
    r15c5 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度二")
    r15c6 = models.CharField(default=".",max_length=99,verbose_name="潤滑-進度三")
    r15c7 = models.CharField(default=".",max_length=99,verbose_name="潤滑-備註說明")
    r16c3 = models.CharField(default=".",max_length=99,verbose_name="氮氣-零件")
    r16c4 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度一")
    r16c5 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度二")
    r16c6 = models.CharField(default=".",max_length=99,verbose_name="氮氣-進度三")
    r16c7 = models.CharField(default=".",max_length=99,verbose_name="氮氣-備註說明")
    r17c3 = models.CharField(default=".",max_length=99,verbose_name="電控-零件")
    r17c4 = models.CharField(default=".",max_length=99,verbose_name="電控-進度一")
    r17c5 = models.CharField(default=".",max_length=99,verbose_name="電控-進度二")
    r17c6 = models.CharField(default=".",max_length=99,verbose_name="電控-進度三")
    r17c7 = models.CharField(default=".",max_length=99,verbose_name="電控-備註說明")
    r18c3 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-零件")
    r18c4 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度一")
    r18c5 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度二")
    r18c6 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-進度三")
    r18c7 = models.CharField(default=".",max_length=99,verbose_name="自動噴霧-備註說明")
    r19c3 = models.CharField(default=".",max_length=99,verbose_name="自動取出-零件")
    r19c4 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度一")
    r19c5 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度二")
    r19c6 = models.CharField(default=".",max_length=99,verbose_name="自動取出-進度三")
    r19c7 = models.CharField(default=".",max_length=99,verbose_name="自動取出-備註說明")
    r20c3 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-零件")
    r20c4 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度一")
    r20c5 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度二")
    r20c6 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-進度三")
    r20c7 = models.CharField(default=".",max_length=99,verbose_name="自動切邊去毛-備註說明")

#--- code1 for model.py (end) -----

  
    def __str__(self):
        return self.field1



class Item004(models.Model):
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
 
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")        	  	        	
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    
    f05 = models.CharField(default=".", max_length=99,verbose_name="計劃交期")
   # f05 = models.CharField(default=".", max_length=99,verbose_name="計劃交期")
    f05 = models.DateField(verbose_name="計劃交期")
    # f06 = models.CharField(default=".", max_length=99,verbose_name="訂單量")
    #  f07 = models.CharField(default=".", max_length=99,verbose_name="已交量")
    # f08 = models.CharField(default=".", max_length=99,verbose_name="未交量")
    # f09 = models.CharField(default=".", max_length=99,verbose_name="備庫量")
    # f10 = models.CharField(default=".", max_length=99,verbose_name="欠備庫量")
    # f11 = models.CharField(default=".", max_length=99,verbose_name="客訴量")
    # http://stackoverflow.com/questions/16527308/how-to-set-null-for-integerfield-instead-of-setting-0
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    f11 = models.IntegerField(default=0,verbose_name="客訴量")
    f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
        
# by Mark,2016-08-24 10:20 copy Item004
# http://stackoverflow.com/questions/16527308/how-to-set-null-for-integerfield-instead-of-setting-0
class Item002v2(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")        	  	        	
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    f05 = models.DateField(null=True, verbose_name="計劃交期")
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    f11 = models.IntegerField(default=0,verbose_name="客訴量")
    f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
 
    
class Item005(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")        	  	        	
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    f04a = models.CharField(default=".", max_length=99,verbose_name="單件品名")
    f04b = models.CharField(default=".", max_length=99,verbose_name="機台噸位")
    f05 = models.DateField(null=True, verbose_name="計劃交期")
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    # f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    # f11 = models.IntegerField(default=0,verbose_name="客訴量")
    # f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
    stat1 = models.CharField(default=".", max_length=99,verbose_name="進度一")
    stat2 = models.CharField(default=".", max_length=99,verbose_name="進度二")
    stat3 = models.CharField(default=".", max_length=99,verbose_name="進度三")
    
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
    
class Item006(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="客戶")
    f02 = models.CharField(default=".", max_length=99,verbose_name="量產訂單號")
    f03 = models.CharField(default=".", max_length=99,verbose_name="產品代碼")        	  	        	
    f04 = models.CharField(default=".", max_length=99,verbose_name="產品名稱")
    f04a = models.CharField(default=".", max_length=99,verbose_name="單件品名")
    f04b = models.CharField(default=".", max_length=99,verbose_name="機台噸位")
    f05 = models.DateField(null=True, verbose_name="計劃交期")
    f06 = models.IntegerField(default=0,verbose_name="訂單量")
    f07 = models.IntegerField(default=0,verbose_name="已交量")
    f08 = models.IntegerField(default=0,verbose_name="未交量")
    # f09 = models.IntegerField(default=0,verbose_name="備庫量")
    f10 = models.IntegerField(default=0,verbose_name="欠備庫量")
    # f11 = models.IntegerField(default=0,verbose_name="客訴量")
    # f12 = models.CharField(default=".", max_length=99,verbose_name="模具壽命")
    stat1 = models.CharField(default=".", max_length=99,verbose_name="進度一")
    stat2 = models.CharField(default=".", max_length=99,verbose_name="進度二")
    stat3 = models.CharField(default=".", max_length=99,verbose_name="進度三")
    
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
     