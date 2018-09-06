from bs4 import BeautifulSoup
import requests

headers={
'Cookie':'_lxsdk_cuid=164d96f4bde0-0633cd36c79054-47e1039-e1000-164d96f4be1c8;__mta=155064967.1532656307217.1532656307217.1532656307217.1;_ga=GA1.3.1634844756.1532656317;_ga=GA1.2.1634844756.1532656317;uuid=7fb1472708e5ae8bfa5d.1533733087.0.0.0;oc=0j3HiNsG760hdhhaQbJQFzi5zb2Qp4YnHg1mPJGJbnUjo8AY4ZSZOw7SnJ1IpcyF4QFl-S8WbfztgcpJC6nfJKNKIKo4Dwagb45LwN3NdwzpiW2zTEQyBeAPAyFFKyYUXdSgNAjiz8uP4bMI32wshQol0Jq3cPmKCKwaI6i78pM;ci=1;iuuid=A2713225BDFFB4DFE67414D7EC594B953599ADA3EDB80E7BED80127EF8E5E4D8;oops=Dah10w2_AxhaaYqs7gUkFRWUcTUAAAAAPAYAAM-uDFR2Y0VxbEw_kc7eUcykxcYi3pE_YSYw18kcNm5EWEjXdFBBYVyjI3M-VkKo_Q;logintype=normal;cityname=%E5%8C%97%E4%BA%AC;__utma=74597006.1634844756.1532656317.1533733089.1533733089.1;__utmz=74597006.1533733089.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;_lxsdk=A2713225BDFFB4DFE67414D7EC594B953599ADA3EDB80E7BED80127EF8E5E4D8;__mta=155064967.1532656307217.1532656307217.1533733234638.2;device_uuid=!d3c984c8-4490-400f-9316-cecbac66ae6c;uuid_update=true;acctId=21735968;brandId=-1;city_id=0;isChain=1;existBrandPoi=true;ignore_set_router_proxy=true;region_id=;region_version=0;token=0TAEkmPAe-YQ5JoCzJbWkCIJ13B06R4MytsH5hhzxCB8*;cityId=440300;provinceId=440000;city_location_id=0;location_id=0;pushToken=0TAEkmPAe-YQ5JoCzJbWkCIJ13B06R4MytsH5hhzxCB8*;wpush_server_url=wss://wpush.meituan.com;isOfflineSelfOpen=0;logistics_support=;wmPoiId=3424449;wmPoiName=%E4%B9%90%E5%87%AF%E6%92%92%E6%AF%94%E8%90%A8(%E5%A3%B9%E6%96%B9%E5%A4%A9%E5%9C%B0%E5%BA%97);set_info=%7B%22wmPoiId%22%3A3424449%2C%22ignoreSetRouterProxy%22%3Atrue%7D;_lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic;JSESSIONID=1n6cskwbm7gxw1xpcv56oaasol;shopCategory=food;_lxsdk_s=165a99f8342-325-b5e-b6b%7C%7C32',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# url="http://e.waimai.meituan.com/?time=1534833285750#https://waimaieapp.meituan.com/bizdata/#/report"
url="https://waimaieapp.meituan.com/bizdata/#/report"
web_data=requests.get(url,headers=headers)
getdata=web_data.text
f=open("index.html","wb")
f.write(getdata.encode())
f.close()
print(getdata)