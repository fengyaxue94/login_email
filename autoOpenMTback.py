from selenium import webdriver
import datetime
import xlrd
import sys
import time
import pymysql

def autoOpenQQemail():
    driver=webdriver.Chrome()
    driver.implicitly_wait(3) #设定隐式等待时间
    driver.get('https://waimaieapp.meituan.com/bizdata/#/report')

    # user='2874565414'
    # password='wangqiu19951030'

    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/a[1]').click() #选择 基本版
    # driver.implicitly_wait(3)
    # driver.find_element_by_xpath('//*[@id="u"]').clear()
    # driver.find_element_by_xpath('//*[@id="u"]').send_keys(user)  #输入账号
    # driver.find_element_by_xpath('//*[@id="p"]').clear()
    # driver.find_element_by_xpath('//*[@id="p"]').send_keys(password) #输入密码
    # driver.find_element_by_xpath('//*[@id="go"]').click()       #登录
    # driver.implicitly_wait(2)
    # driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/ul/li[1]/a/span[2]/span').click()  
    # driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div[1]/div[2]/form/div[1]/div/a/div[1]/div[1]').click()  
    # driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[1]/a').click()  

    # time.sleep(3)
    # file_path = r'C:/Users/aaa/Downloads/2018-08-30_2018-08-30_全店数据_订单1535694121526.xls' #路径前加 r，读取的文件路径
    # # file_path = file_path.encode('utf-8') #文件路径的中文转码
    # data = xlrd.open_workbook(file_path) #获取数据
    # table = data.sheet_by_name('2018-08-30_2018-08-30_全店数据_订单15') #获取sheet
    # nrows = table.nrows #获取总行数
    # # ncols = table.ncols #获取总列数
    # # rowvalue = table.row_values(5) #获取一行的数值，例如第6行
    # # col_values = table.col_values(6) #获取一列的数值，例如第7列
    # # cell_value = table.cell(5,5).value #获取一个单元格的数值，例如第5行第6列
    # print(nrows)
    # arraydata=[]

    # for i in range(1,nrows):
    #     findNull=int(table.row_values(i)[1].strip().find(" "))
    #     orderdate=table.row_values(i)[1].strip()[0:findNull]
    #     orderid=table.row_values(i)[0].strip()
    #     create_time=table.row_values(i)[1].strip()
    #     single_time=table.row_values(i)[2].strip()
    #     storename=table.row_values(i)[3].strip()
    #     storeid=table.row_values(i)[4]
    #     inmark=table.row_values(i)[5].strip()
    #     ordretype=table.row_values(i)[6].strip()
    #     orderstatus=table.row_values(i)[7].strip()
    #     ordergivestatus=table.row_values(i)[8].strip()
    #     isReserve=table.row_values(i)[9].strip()
    #     orderMoney=table.row_values(i)[10]
    #     orderDiscountMoney=table.row_values(i)[11]
    #     orderMeituanActive=table.row_values(i)[12]
    #     orderBusinessActive=table.row_values(i)[13]
    #     shopinfo=table.row_values(i)[14].strip()
    #     dispatch=table.row_values(i)[15]
    #     isActiveOrder=table.row_values(i)[16].strip()
    #     discountOrder=table.row_values(i)[17].strip()
    #     isReminder=table.row_values(i)[18].strip()
    #     replyStatus=table.row_values(i)[19].strip()
    #     businessReply=table.row_values(i)[20].strip()
    #     deliveryTime=table.row_values(i)[21].strip()
    #     lunchBoxFee=table.row_values(i)[22]
    #     lunchBoxSum=table.row_values(i)[23]
    #     orderCompleteTime=table.row_values(i)[24].strip()
    #     orderCancelReason=table.row_values(i)[25].strip()
    #     operate_time=datetime.date.today()
    #     operator="zwq"
        
    #     meituandata=(orderdate,orderid,create_time,single_time,storename,storeid,inmark,ordretype,orderstatus,
    #     ordergivestatus,isReserve,orderMoney,orderDiscountMoney,orderMeituanActive,orderBusinessActive,shopinfo,
    #     dispatch,isActiveOrder,discountOrder,isReminder,replyStatus,businessReply,deliveryTime,lunchBoxFee,
    #     lunchBoxSum,orderCompleteTime,orderCancelReason,operate_time,operator)
        
    #     arraydata.append(meituandata)
    # # print(arraydata)
    # db=pymysql.connect(host="localhost",user="root",password="123456",db="reptiliandata",port=3306)
    # cursor=db.cursor()
    # sql="INSERT INTO meituan_order_original(日期,订单编号,下单时间,接单时长,店铺名称,\
    # 店铺id,店铺所在城市,订单支付类型,订单状态,订单配送状态,是否预定单,订单总金额,订单优惠后金额,\
    # 订单美团承担活动金额,订单商家承担活动金额,菜品信息,配送费,是否活动订单,优惠活动,是否催单,\
    # 回复状态,商家回复内容,配送时间,餐盒费总金额,餐盒总数量,订单完成时间,订单取消原因,operate_time,\
    # operator) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # try:
    #     cursor.executemany(sql,arraydata)
    #     db.commit()
    # except Exception as e:
    #     db.rollback()
    #     print("Error",str(e),sql)

if __name__=="__main__":
    # sleepTime=0
    # while True:
    #     sleepTime=sleepTime+1
    #     time.sleep(sleepTime)
    #     print(sleepTime)
    #     autoOpenQQemail()
    #     print(str(datetime.date.today())+"数据上传完毕！")
    #     sleepTime=86000
        autoOpenQQemail()
