from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.conf import settings
#from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from module import func0
from module import func
from module import func2
from module import func2x
from module import func2t
from module import func3
from module import func3x
from module import func4
from module import func4x
from module import func5
from module import func5x2
from module import func6
from module import func7
from module import func8, func_usbond
##################函式位置改寫，一個函式一個檔案，棄用func
from module_PERseg import Price5yDB, Price5y, PERseg, PERsegPEG, PERsegPEGxDB, PERsegStable, PERsegx, PERsegxDB, NetCapDB, PERseg3
from module_Kn import KnQuery, Kn8yPrice

#################
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

from myapp.models import Stock6Sign
from myapp.models import StockPERseg

from myapp.models import DCStock6Sign202011
from myapp.models import DCStock6Sign2020Q4
from myapp.models import DCStock6Sign202101
from myapp.models import DCStock6Sign202102
from myapp.models import DCStock6Sign202103
from myapp.models import DCStock6Sign202104
from myapp.models import DCStock6Sign202105
from myapp.models import DCStock6Sign202106
from myapp.models import DCStock6Sign202107
from myapp.models import DCStock6Sign202108
from myapp.models import DCStock6Sign202109
from myapp.models import DCStock6Sign202110
from myapp.models import DCStock6Sign202111
from myapp.models import DCStock6Sign202112


from myapp.models import Stock6Sign202005
from myapp.models import Stock6Sign202006

from myapp.models import Stock6Sign2020Q2
from myapp.models import Stock6Sign202008
from myapp.models import Stock6Sign202009
from myapp.models import Stock6Sign2020Q3
from myapp.models import Stock6Sign202011
from myapp.models import Stock6Sign2020Q4
from myapp.models import Stock6Sign202101
from myapp.models import Stock6Sign202102
from myapp.models import Stock6Sign202103
from myapp.models import Stock6Sign202104
from myapp.models import Stock6Sign202105
from myapp.models import Stock6Sign202106
from myapp.models import Stock6Sign202107
from myapp.models import Stock6Sign202108
from myapp.models import Stock6Sign202109
from myapp.models import Stock6Sign202110
from myapp.models import Stock6Sign202111
from myapp.models import Stock6Sign202112
from myapp.models import Stock6Sign202201
from myapp.models import Stock6Sign202202
from myapp.models import Stock6Sign202203
from myapp.models import Stock6Sign202204
from myapp.models import Stock6Sign202205
from myapp.models import Stock6Sign202206
from myapp.models import Stock6Sign202207
from myapp.models import Stock6Sign202208
from myapp.models import Stock6Sign202209
from myapp.models import Stock6Sign202210
from myapp.models import Stock6Sign202211
from myapp.models import Stock6Sign202212

from myapp.models import Stock6Sign202301
from myapp.models import Stock6Sign202302
from myapp.models import Stock6Sign202303
from myapp.models import Stock6Sign202304
from myapp.models import Stock6Sign202305
from myapp.models import Stock6Sign202306
from myapp.models import Stock6Sign202307
from myapp.models import Stock6Sign202308
from myapp.models import Stock6Sign202309
from myapp.models import Stock6Sign202310
from myapp.models import Stock6Sign202311
from myapp.models import Stock6Sign202312

#from myapp.models import Stock6sta2021
#from myapp.models import Stock6Sign202109
#from myapp.models import Stock6Sign202110
#from myapp.models import Stock6Sign202111
#from myapp.models import Stock6Sign202112



from myapp.models import StockPERseg202005
from myapp.models import StockPERseg202006
from myapp.models import StockPERseg2020Q2
from myapp.models import StockPERseg202008
from myapp.models import StockPERseg202009
from myapp.models import StockPERseg2020Q3
from myapp.models import StockPERseg202011
from myapp.models import StockPERseg2020Q4
from myapp.models import StockPERseg202101
from myapp.models import StockPERseg202102
from myapp.models import StockPERseg202103
from myapp.models import StockPERseg202104
from myapp.models import StockPERseg202105
from myapp.models import StockPERseg202106
from myapp.models import StockPERseg202107
from myapp.models import StockPERseg202108
from myapp.models import StockPERseg202109
from myapp.models import StockPERseg202110
from myapp.models import StockPERseg202111
from myapp.models import StockPERseg202112
from myapp.models import StockPERseg202201
from myapp.models import StockPERseg202202
from myapp.models import StockPERseg202203
from myapp.models import StockPERseg202204
from myapp.models import StockPERseg202205
from myapp.models import StockPERseg202206
from myapp.models import StockPERseg202207
from myapp.models import StockPERseg202208
from myapp.models import StockPERseg202209
from myapp.models import StockPERseg202210
from myapp.models import StockPERseg202211
from myapp.models import StockPERseg202212

from myapp.models import StockPERseg202301
from myapp.models import StockPERseg202302
from myapp.models import StockPERseg202303
from myapp.models import StockPERseg202304
from myapp.models import StockPERseg202305
from myapp.models import StockPERseg202306
from myapp.models import StockPERseg202307
from myapp.models import StockPERseg202308
from myapp.models import StockPERseg202309
from myapp.models import StockPERseg202310
from myapp.models import StockPERseg202311
from myapp.models import StockPERseg202312



from myapp.models import EpsProfit2020Q1
from myapp.models import EpsProfit2020Q2
from myapp.models import EpsProfit2020Q3
from myapp.models import EpsProfit2020Q4
from myapp.models import EpsProfit2021Q1
from myapp.models import EpsProfit2021Q2
from myapp.models import EpsProfit2021Q3
from myapp.models import EpsProfit2021Q4
from myapp.models import EpsProfit2022Q1
from myapp.models import EpsProfit2022Q3

from myapp.models import StockPERsegStable2020
from myapp.models import StockPERsegStable2020Q2
from myapp.models import StockPERsegStable2020Q3
from myapp.models import StockPERsegStable2020Q3x
from myapp.models import StockPERsegStable2020Q4
from myapp.models import StockPERsegStable2021Q1
from myapp.models import StockPERsegStable2021Q2
from myapp.models import StockPERsegStable2021Q3
from myapp.models import StockPERsegStable2021Q4
from myapp.models import StockPERsegStable2022Q1
from myapp.models import StockPERsegStable2022Q3



from myapp.models import EPSachieve
from myapp.models import EPSachieve2020Q2
from myapp.models import EPSachieve2020Q3
from myapp.models import EPSachieve2021Q1
from myapp.models import EPSachieve2021Q2
from myapp.models import EPSachieve2021Q3
from myapp.models import EPSachieve2022Q1
from myapp.models import EPSachieve2022Q3

from myapp.models import StockCapVar
from myapp.models import StockCapVar2020Q2
from myapp.models import StockCapVar2020Q3
from myapp.models import StockCapVar2020Q4
from myapp.models import StockCapVar2021Q1
from myapp.models import StockCapVar2021Q2
from myapp.models import StockCapVar2021Q3
from myapp.models import StockCapVar2021Q4
from myapp.models import StockCapVar2022Q1
from myapp.models import StockCapVar2022Q3

from myapp.models import SubCats202011
from myapp.models import SubCats202102
from myapp.models import SubCats202103
from myapp.models import SubCats202104
from myapp.models import SubCats202105
from myapp.models import SubCats202106
from myapp.models import SubCats202107
from myapp.models import SubCats202108
from myapp.models import SubCats202109
from myapp.models import SubCats202110
from myapp.models import SubCats202111
from myapp.models import SubCats202112

from myapp.models import StockFavs_test168
from myapp.models import StockFavDB

from myapp.models import PriEPSPER_DB

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

from myapp.models import City


@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def adminmain(request, pageindex=None):  #管理頁面

    #個別績效串列 
    #一週 一個月 六個月一年
    try:
        Lists3m = func_usbond.getUSBondYield3m()
    except:
        Lists3m = func_usbond.getUSBondYield3m()
        
    try:
        Lists6m = func_usbond.getUSBondYield6m()
    except:
        Lists6m = func_usbond.getUSBondYield6m()
    
    try:
        Lists2y = func_usbond.getUSBondYield2y()
    except:
        Lists2y = func_usbond.getUSBondYield2y()
    
    
    try:
        Lists3y = func_usbond.getUSBondYield3y()
    except:
        Lists3y = func_usbond.getUSBondYield3y()
        
    try:
        Lists5y = func_usbond.getUSBondYield5y()
    except:
        Lists5y = func_usbond.getUSBondYield5y()

    try:
        Lists7y = func_usbond.getUSBondYield7y()
    except:
        Lists7y = func_usbond.getUSBondYield7y()

    try:
        Lists10y = func_usbond.getUSBondYield10y()
    except:
        Lists10y = func_usbond.getUSBondYield10y()
    
    
    try:
        Lists30y = func_usbond.getUSBondYield30y()
    except:
        Lists30y = func_usbond.getUSBondYield30y()

    
    global page1u
    pagesize = 20  #8
    newsall = models.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex==None:
        page1u = 1
        newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
    elif pageindex=='1':
        start = (page1u-2)*pagesize
        if start >= 0:
            newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
            page1u -= 1
    elif pageindex=='2':
        start = page1u*pagesize
        if start < datasize:
            newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
            page1u += 1
    elif pageindex=='3':
        start = (page1u-1)*pagesize
        newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
        currentpage = page1u
    
    global page1
    pagesize = 20 #8
    newsall = models.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex==None:
        page1 = 1
        newsunits = models.StockFavs_test168.objects.order_by('-id')[:pagesize]
    elif pageindex=='1':
        start = (page1-2)*pagesize
        if start >= 0:
            newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
            page1 -= 1
    elif pageindex=='2':
        start = page1*pagesize
        if start < datasize:
            newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
            page1 += 1
    elif pageindex=='3':
        start = (page1-1)*pagesize
        newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
    currentpage = page1
    
    
    
    global page1m #MacroWaveA
    pagesize = 3 #8
    newsall = models.MacroWaveA.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex==None:
        page1m = 1
        newsunitsm = models.MacroWaveA.objects.order_by('-id')[:pagesize]
    elif pageindex=='1':
        start = (page1-2)*pagesize
        if start >= 0:
            newsunitsm = models.MacroWaveA.objects.order_by('-id')[start:(start+pagesize)]
            page1m -= 1
    elif pageindex=='2':
        start = page1m*pagesize
        if start < datasize:
            newsunitsm = models.MacroWaveA.objects.order_by('-id')[start:(start+pagesize)]
            page1m += 1
    elif pageindex=='3':
        start = (page1m-1)*pagesize
        newsunitsm = models.MacroWaveA.objects.order_by('-id')[start:(start+pagesize)]
    currentpage = page1m
    
    
    
    global page1m2 #MacroWaveB
    pagesize = 5 #8
    newsall = models.MacroWaveB.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex==None:
        page1m2 = 1
        newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[:pagesize]
    elif pageindex=='1':
        start = (page1-2)*pagesize
        if start >= 0:
            newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[start:(start+pagesize)]
            page1m2 -= 1
    elif pageindex=='2':
        start = page1m2*pagesize
        if start < datasize:
            newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[start:(start+pagesize)]
            page1m2 += 1
    elif pageindex=='3':
        start = (page1m2-1)*pagesize
        newsunitsm2 = models.MacroWaveB.objects.order_by('-id')[start:(start+pagesize)]
    currentpage = page1m2
    
    
    global page1m3 #MacroWaveC
    pagesize = 5 #8
    newsall = models.MacroWaveC.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex==None:
        page1m3 = 1
        newsunitsm3 = models.MacroWaveC.objects.order_by('-id')[:pagesize]
    elif pageindex=='1':
        start = (page1-2)*pagesize
        if start >= 0:
            newsunitsm3 = models.MacroWaveC.objects.order_by('-id')[start:(start+pagesize)]
            page1m3 -= 1
    elif pageindex=='2':
        start = page1m3*pagesize
        if start < datasize:
            newsunitsm3 = models.MacroWavec.objects.order_by('-id')[start:(start+pagesize)]
            page1m3 += 1
    elif pageindex=='3':
        start = (page1m3-1)*pagesize
        newsunitsm3 = models.MacroWaveC.objects.order_by('-id')[start:(start+pagesize)]
    currentpage = page1m3
    
    return render(request, "adminmain.html", locals())

def home(request):
    return render(request, 'home.html')




def stock6x_chart(request):
    labels = []
    data = []

    queryset = Stock6Sign202205.objects.get(cStockID = "3034")

    #queryset = City.objects.order_by('-population')[:5]
    #for city in queryset:
    labels = ["2022/4", "2022/3", "2022/2", "2022/1", "2021/12", "2021/11", "2021/10", "2021/9"]
    data = [float(queryset.sCore2204),float(queryset.sCore2203), float(queryset.sCore2202), float(queryset.sCore2201), float(queryset.sCore2112), float(queryset.sCore2111), float(queryset.sCore2110), float(queryset.sCore2109)]


    return render(request, 'stock6x_chart.html', {
        'labels': labels,
        'data': data,
    })



def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })
####################


# Create your views here.
#################################判斷是否為數字的自創函數
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
####################################台股代號
tseotc_dict = {'台泥': '1101', '亞泥': '1102', '嘉泥': '1103', '環泥': '1104', '幸福': '1108', '信大': '1109', '東泥': '1110', '味全': '1201', '味王': '1203', '大成': '1210', '大飲': '1213', '卜蜂': '1215', '統一': '1216', '愛之味': '1217', '泰山': '1218', '福壽': '1219', '台榮': '1220', '福懋油': '1225', '佳格': '1227', '聯華': '1229', '聯華食': '1231', '大統益': '1232', '天仁': '1233', '黑松': '1234', '興泰': '1235', '宏亞': '1236', '鮮活果汁-KY': '1256', '台塑': '1301', '南亞': '1303', '台聚': '1304', '華夏': '1305', '三芳': '1307', '亞聚': '1308', '台達化': '1309', '台苯': '1310', '國喬': '1312', '聯成': '1313', '中石化': '1314', '達新': '1315', '上曜': '1316', '東陽': '1319', '大洋': '1321', '永裕': '1323', '地球': '1324', '恆大': '1325', '台化': '1326', '再生-KY': '1337', '廣華-KY': '1338', '昭輝': '1339', '勝悅-KY': '1340', '富林-KY': '1341', '八貫': '1342', '遠東新': '1402', '新纖': '1409', '南染': '1410', '宏洲': '1413', '東和': '1414', '廣豐': '1416', '嘉裕': '1417', '東華': '1418', '新紡': '1419', '利華': '1423', '大魯閣': '1432', '福懋': '1434', '中福': '1435', '華友聯': '1436', '勤益控': '1437', '三地開發': '1438', '中和': '1439', '南紡': '1440', '大東': '1441', '名軒': '1442', '立益': '1443', '力麗': '1444', '大宇': '1445', '宏和': '1446', '力鵬': '1447', '佳和': '1449', '年興': '1451', '宏益': '1452', '大將': '1453', '台富': '1454', '集盛': '1455', '怡華': '1456', '宜進': '1457', '聯發': '1459', '宏遠': '1460', '強盛': '1463', '得力': '1464', '偉全': '1465', '聚隆': '1466', '南緯': '1467', '昶和': '1468', '大統新創': '1470', '首利': '1471', '三洋紡': '1472', '台南': '1473', '弘裕': '1474', '業旺': '1475', '儒鴻': '1476', '聚陽': '1477', '士電': '1503', '東元': '1504', '正道': '1506', '永大': '1507', '瑞利': '1512', '中興電': '1513', '亞力': '1514', '力山': '1515', '川飛': '1516', '利奇': '1517', '華城': '1519', '大億': '1521', '堤維西': '1522', '耿鼎': '1524', '江申': '1525', '日馳': '1526', '鑽全': '1527', '恩德': '1528', '樂士': '1529', '亞崴': '1530', '高林股': '1531', '勤美': '1532', '車王電': '1533', '中宇': '1535', '和大': '1536', '廣隆': '1537', '正峰': '1538', '巨庭': '1539', '喬福': '1540', '錩泰': '1541', '伸興': '1558', '中砂': '1560', '倉佑': '1568', '信錦': '1582', '程泰': '1583', '吉茂': '1587', '永冠-KY': '1589', '亞德客-KY': '1590', '英瑞-KY': '1592', '直得': '1597', '岱宇': '1598', '華電': '1603', '聲寶': '1604', '華新': '1605', '華榮': '1608', '大亞': '1609', '中電': '1611', '宏泰': '1612', '三洋電': '1614', '大山': '1615', '億泰': '1616', '榮星': '1617', '合機': '1618', '艾美特-KY': '1626', '中化': '1701', '南僑': '1702', '葡萄王': '1707', '東鹼': '1708', '和益': '1709', '東聯': '1710', '永光': '1711', '興農': '1712', '國化': '1713', '和桐': '1714', '長興': '1717', '中纖': '1718', '生達': '1720', '三晃': '1721', '台肥': '1722', '中碳': '1723', '台硝': '1724', '元禎': '1725', '永記': '1726', '中華化': '1727', '花仙子': '1730', '美吾華': '1731', '毛寶': '1732', '五鼎': '1733', '杏輝': '1734', '日勝化': '1735', '喬山': '1736', '臺鹽': '1737', '寶齡富錦': '1760', '中化生': '1762', '勝一': '1773', '展宇': '1776', '和康生': '1783', '科妍': '1786', '神隆': '1789', '美時': '1795', '台玻': '1802', '寶徠': '1805', '冠軍': '1806', '潤隆': '1808', '中釉': '1809', '和成': '1810', '凱撒衛': '1817', '士紙': '1903', '正隆': '1904', '華紙': '1905', '寶隆': '1906', '永豐餘': '1907', '榮成': '1909', '中鋼': '2002', '東和鋼鐵': '2006', '燁興': '2007', '高興昌': '2008', '第一銅': '2009', '春源': '2010', '春雨': '2012', '中鋼構': '2013', '中鴻': '2014', '豐興': '2015', '官田鋼': '2017', '美亞': '2020', '聚亨': '2022', '燁輝': '2023', '志聯': '2024', '千興': '2025', '大成鋼': '2027', '威致': '2028', '盛餘': '2029', '彰源': '2030', '新光鋼': '2031', '新鋼': '2032', '佳大': '2033', '允強': '2034', '海光': '2038', '上銀': '2049', '川湖': '2059', '橋椿': '2062', '運錩': '2069', '南港': '2101', '泰豐': '2102', '台橡': '2103', '國際中橡': '2104', '正新': '2105', '建大': '2106', '厚生': '2107', '南帝': '2108', '華豐': '2109', '鑫永銓': '2114', '六暉-KY': '2115', '裕隆': '2201', '中華': '2204', '三陽工業': '2206', '和泰車': '2207', '台船': '2208', '裕日車': '2227', '劍麟': '2228', '為升': '2231', '宇隆': '2233', '百達-KY': '2236', '英利-KY': '2239', '艾姆勒': '2241', '宏旭-KY': '2243', '汎德永業': '2247', '光寶科': '2301', '麗正': '2302', '聯電': '2303', '全友': '2305', '台達電': '2308', '金寶': '2312', '華通': '2313', '台揚': '2314', '楠梓電': '2316', '鴻海': '2317', '東訊': '2321', '中環': '2323', '仁寶': '2324', '國巨': '2327', '廣宇': '2328', '華泰': '2329', '台積電': '2330', '精英': '2331', '友訊': '2332', '旺宏': '2337', '光罩': '2338', '光磊': '2340', '茂矽': '2342', '華邦電': '2344', '智邦': '2345', '聯強': '2347', '海悅': '2348', '錸德': '2349', '順德': '2351', '佳世達': '2352', '宏碁': '2353', '鴻準': '2354', '敬鵬': '2355', '英業達': '2356', '華碩': '2357', '廷鑫': '2358', '所羅門': '2359', '致茂': '2360', '藍天': '2362', '矽統': '2363', '倫飛': '2364', '昆盈': '2365', '燿華': '2367', '金像電': '2368', '菱生': '2369', '大同': '2371', '震旦行': '2373', '佳能': '2374', '凱美': '2375', '技嘉': '2376', '微星': '2377', '瑞昱': '2379', '虹光': '2380', '廣達': '2382', '台光電': '2383', '群光': '2385', '精元': '2387', '威盛': '2388', '云辰': '2390', '正崴': '2392', '億光': '2393', '研華': '2395', '友通': '2397', '映泰': '2399', '凌陽': '2401', '毅嘉': '2402', '漢唐': '2404', '浩鑫': '2405', '國碩': '2406', '南亞科': '2408', '友達': '2409', '中華電': '2412', '環科': '2413', '精技': '2414', '錩新': '2415', '圓剛': '2417', '仲琦': '2419', '新巨': '2420', '建準': '2421', '固緯': '2423', '隴華': '2424', '承啟': '2425', '鼎元': '2426', '三商電': '2427', '興勤': '2428', '銘旺科': '2429', '燦坤': '2430', '聯昌': '2431', '互盛電': '2433', '統懋': '2434', '偉詮電': '2436', '翔耀': '2438', '美律': '2439', '太空梭': '2440', '超豐': '2441', '新美齊': '2442', '億麗': '2443', '兆勁': '2444', '京元電子': '2449', '神腦': '2450', '創見': '2451', '凌群': '2453', '聯發科': '2454', '全新': '2455', '奇力新': '2456', '飛宏': '2457', '義隆': '2458', '敦吉': '2459', '建通': '2460', '光群雷': '2461', '良得電': '2462', '盟立': '2464', '麗臺': '2465', '冠西電': '2466', '志聖': '2467', '華經': '2468', '資通': '2471', '立隆電': '2472', '可成': '2474', '鉅祥': '2476', '美隆電': '2477', '大毅': '2478', '敦陽科': '2480', '強茂': '2481', '連宇': '2482', '百容': '2483', '希華': '2484', '兆赫': '2485', '一詮': '2486', '漢平': '2488', '瑞軒': '2489', '吉祥全': '2491', '華新科': '2492', '揚博': '2493', '普安': '2495', '卓越': '2496', '怡利電': '2497', '宏達電': '2498', '國建': '2501', '國產': '2504', '國揚': '2505', '太設': '2506', '全坤建': '2509', '太子': '2511', '龍邦': '2514', '中工': '2515', '新建': '2516', '冠德': '2520', '京城': '2524', '宏璟': '2527', '皇普': '2528', '華建': '2530', '宏盛': '2534', '達欣工': '2535', '宏普': '2536', '聯上發': '2537', '基泰': '2538', '櫻花建': '2539', '愛山林': '2540', '興富發': '2542', '皇昌': '2543', '皇翔': '2545', '根基': '2546', '日勝生': '2547', '華固': '2548', '潤弘': '2597', '益航': '2601', '長榮': '2603', '新興': '2605', '裕民': '2606', '榮運': '2607', '嘉里大榮': '2608', '陽明': '2609', '華航': '2610', '志信': '2611', '中航': '2612', '中櫃': '2613', '東森': '2614', '萬海': '2615', '山隆': '2616', '台航': '2617', '長榮航': '2618', '亞航': '2630', '台灣高鐵': '2633', '漢翔': '2634', '台驊投控': '2636', '慧洋-KY': '2637', '宅配通': '2642', '萬企': '2701', '華園': '2702', '國賓': '2704', '六福': '2705', '第一店': '2706', '晶華': '2707', '遠雄來': '2712', '夏都': '2722', '美食-KY': '2723', '王品': '2727', '雄獅': '2731', '寒舍': '2739', '雲品': '2748', '彰銀': '2801', '京城銀': '2809', '台中銀': '2812', '旺旺保': '2816', '華票': '2820', '中壽': '2823', '台產': '2832', '臺企銀': '2834', '高雄銀': '2836', '聯邦銀': '2838', '台開': '2841', '遠東銀': '2845', '安泰銀': '2849', '新產': '2850', '中再保': '2851', '第一保': '2852', '統一證': '2855', '三商壽': '2867', '華南金': '2880', '富邦金': '2881', '國泰金': '2882', '開發金': '2883', '玉山金': '2884', '元大金': '2885', '兆豐金': '2886', '台新金': '2887', '新光金': '2888', '國票金': '2889', '永豐金': '2890', '中信金': '2891', '第一金': '2892', '王道銀行': '2897', '欣欣': '2901', '遠百': '2903', '匯僑': '2904', '三商': '2905', '高林': '2906', '特力': '2908', '統領': '2910', '麗嬰房': '2911', '統一超': '2912', '農林': '2913', '潤泰全': '2915', '鼎固-KY': '2923', '淘帝-KY': '2929', '客思達-KY': '2936', '凱羿-KY': '2939', '歐格': '3002', '健和興': '3003', '豐達科': '3004', '神基': '3005', '晶豪科': '3006', '大立光': '3008', '華立': '3010', '今皓': '3011', '晟銘電': '3013', '聯陽': '3014', '全漢': '3015', '嘉晶': '3016', '奇鋐': '3017', '同開': '3018', '亞光': '3019', '鴻名': '3021', '威強電': '3022', '信邦': '3023', '憶聲': '3024', '星通': '3025', '禾伸堂': '3026', '盛達': '3027', '增你強': '3028', '零壹': '3029', '德律': '3030', '佰鴻': '3031', '偉訓': '3032', '威健': '3033', '聯詠': '3034', '智原': '3035', '文曄': '3036', '欣興': '3037', '全台': '3038', '遠見': '3040', '揚智': '3041', '晶技': '3042', '科風': '3043', '健鼎': '3044', '台灣大': '3045', '建碁': '3046', '訊舟': '3047', '益登': '3048', '和鑫': '3049', '鈺德': '3050', '力特': '3051', '夆典': '3052', '立萬利': '3054', '蔚華科': '3055', '總太': '3056', '喬鼎': '3057', '立德': '3058', '華晶科': '3059', '銘異': '3060', '建漢': '3062', '日電貿': '3090', '聯傑': '3094', '一零四': '3130', '耀登': '3138', '正達': '3149', '景岳': '3164', '大量': '3167', '景碩': '3189', '全科': '3209', '晟鈦': '3229', '緯創': '3231', '虹冠電': '3257', '昇陽': '3266', '勝德': '3296', '昇貿': '3305', '聯德': '3308', '閎暉': '3311', '弘憶股': '3312', '同泰': '3321', '泰碩': '3338', '麗清': '3346', '奇偶': '3356', '新日興': '3376', '明泰': '3380', '新世紀': '3383', '玉晶光': '3406', '京鼎': '3413', '融程電': '3416', '譁裕': '3419', '台端': '3432', '榮創': '3437', '創意': '3443', '聯鈞': '3450', '晶睿': '3454', '群創': '3481', '誠研': '3494', '維熹': '3501', '揚明光': '3504', '華擎': '3515', '柏騰': '3518', '安馳': '3528', '晶相光': '3530', '台勝科': '3532', '嘉澤': '3533', '晶彩科': '3535', '誠創': '3536', '州巧': '3543', '敦泰': '3545', '聯穎': '3550', '嘉威': '3557', '牧德': '3563', '聯合再生': '3576', '辛耘': '3583', '通嘉': '3588', '艾笛森': '3591', '力銘': '3593', '智易': '3596', '宏致': '3605', '谷崧': '3607', '碩天': '3617', '洋華': '3622', '達邁': '3645', '健策': '3653', '世芯-KY': '3661', '貿聯-KY': '3665', '圓展': '3669', 'TPK-KY': '3673', '新至陞': '3679', '亞太電': '3682', '達能': '3686', '海華': '3694', '大眾控': '3701', '大聯大': '3702', '欣陸': '3703', '合勤控': '3704', '永信': '3705', '神達': '3706', '上緯投控': '3708', '日月光投控': '3711', '永崴投控': '3712', '富采': '3714', '佳醫': '4104', '雃博': '4106', '懷特': '4108', '旭富': '4119', '亞諾法': '4133', '麗豐-KY': '4137', '龍燈-KY': '4141', '國光生': '4142', '全宇生技-KY': '4148', '訊映': '4155', '承業醫': '4164', '佐登-KY': '4190', '炎洲': '4306', '如興': '4414', '利勤': '4426', '廣越': '4438', '冠星-KY': '4439', '東台': '4526', '瑞智': '4532', '拓凱': '4536', '全球傳動': '4540', '銘鈺': '4545', '智伸科': '4551', '力達-KY': '4552', '氣立': '4555', '永新-KY': '4557', '強信-KY': '4560', '穎漢': '4562', '元翎': '4564', '時碩工業': '4566', '鈞興-KY': '4571', '駐龍': '4572', '大銀微系統': '4576', '光隆精密-KY': '4581', '德淵': '4720', '國精化': '4722', '華廣': '4737', '康普': '4739', '台耀': '4746', '三福化': '4755', '材料-KY': '4763', '雙鍵': '4764', '南寶': '4766', '日成-KY': '4807', '遠傳': '4904', '正文': '4906', '聯德控股-KY': '4912', '致伸': '4915', '事欣科': '4916', '新唐': '4919', '泰鼎-KY': '4927', '燦星網': '4930', '太極': '4934', '茂林-KY': '4935', '和碩': '4938', '嘉彰': '4942', '康控-KY': '4943', '凌通': '4952', '光鋐': '4956', '臻鼎-KY': '4958', '誠美材': '4960', '天鈺': '4961', '十銓': '4967', '立積': '4968', '佳凌': '4976', '眾達-KY': '4977', '榮科': '4989', '傳奇': '4994', '鑫禾': '4999', '三星': '5007', '訊連': '5203', '科嘉-KY': '5215', '東科-KY': '5225', '達興材料': '5234', '乙盛-KY': '5243', '虹堡': '5258', '祥碩': '5269', '禾聯碩': '5283', 'jpp-KY': '5284', '界霖': '5285', '豐祥-KY': '5288', '中磊': '5388', '崇越': '5434', '瀚宇博': '5469', '松翰': '5471', '慧友': '5484', '建國': '5515', '隆大': '5519', '工信': '5521', '遠雄': '5522', '順天': '5525', '鄉林': '5531', '皇鼎': '5533', '長虹': '5534', '東明-KY': '5538', '永固-KY': '5546', '遠雄港': '5607', '四維航': '5608', '鳳凰': '5706', '中租-KY': '5871', '上海商銀': '5876', '合庫金': '5880', '台南-KY': '5906', '大洋-KY': '5907', '群益證': '6005', '群益期': '6024', '競國': '6108', '聚碩': '6112', '鎰勝': '6115', '彩晶': '6116', '迎廣': '6117', '達運': '6120', '上福': '6128', '鈞泰': '6131', '金橋': '6133', '富爾特': '6136', '亞翔': '6139', '柏承': '6141', '友勁': '6142', '百一': '6152', '嘉聯益': '6153', '鈞寶': '6155', '華興': '6164', '捷泰': '6165', '凌華': '6166', '宏齊': '6168', '互億': '6172', '瑞儀': '6176', '達麗': '6177', '關貿': '6183', '大豐電': '6184', '豐藝': '6189', '精成科': '6191', '巨路': '6192', '帆宣': '6196', '佳必琪': '6197', '亞弘電': '6201', '盛群': '6202', '詮欣': '6205', '飛捷': '6206', '今國光': '6209', '聯茂': '6213', '精誠': '6214', '和椿': '6215', '居易': '6216', '聚鼎': '6224', '天瀚': '6225', '光鼎': '6226', '尼得科超眾': '6230', '華孚': '6235', '力成': '6239', '迅杰': '6243', '定穎': '6251', '矽格': '6257', '台郡': '6269', '同欣電': '6271', '宏正': '6277', '台表科': '6278', '全國電': '6281', '康舒': '6282', '淳安': '6283', '啟碁': '6285', '聯嘉': '6288', '華上': '6289', '悅城': '6405', '旭隼': '6409', '群電': '6412', '樺漢': '6414', '矽力-KY': '6415', '瑞祺電通': '6416', '光麗-KY': '6431', '迅得': '6438', '光聖': '6442', '元晶': '6443', '鈺邦': '6449', '訊芯-KY': '6451', 'GIS-KY': '6456', '台數科': '6464', '安集': '6477', '晶碩': '6491', '南六': '6504', '台塑化': '6505', '穎崴': '6515', '捷敏-KY': '6525', '愛普': '6531', '晶心科': '6533', '泰福-KY': '6541', '易華電': '6552', '興能高': '6558', '虹揚-KY': '6573', '研揚': '6579', '鋼聯': '6581', '申豐': '6582', '動力-KY': '6591', '和潤企業': '6592', 'ABC-KY': '6598', '帝寶': '6605', '必應': '6625', '基士德-KY': '6641', '科定': '6655', '羅麗芬-KY': '6666', '中揚光': '6668', '緯穎': '6669', '復盛應用': '6670', '三能-KY': '6671', '騰輝電子-KY': '6672', '鋐寶科技': '6674', '旭暉應材': '6698', '惠特': '6706', '嘉基': '6715', '安普新': '6743', '匯僑設計': '6754', '威鋒電子': '6756', 'AES-KY': '6781', '台通': '8011', '矽創': '8016', '尖點': '8021', '昇陽半導體': '8028', '雷虎': '8033', '台虹': '8039', '南電': '8046', '長華*': '8070', '陞泰': '8072', '致新': '8081', '華冠': '8101', '瀚荃': '8103', '錸寶': '8104', '凌巨': '8105', '華東': '8110', '至上': '8112', '振樺電': '8114', '福懋科': '8131', '南茂': '8150', '達方': '8163', '無敵': '8201', '勤誠': '8210', '志超': '8213', '明基材': '8215', '寶一': '8222', '菱光': '8249', '富鼎': '8261', '宇瞻': '8271', '日友': '8341', '建新國際': '8367', '羅昇': '8374', '百和興業-KY': '8404', '福貞-KY': '8411', '可寧衛': '8422', '基勝-KY': '8427', '金麗-KY': '8429', '威宏-KY': '8442', '阿瘦': '8443', '富邦媒': '8454', '柏文': '8462', '潤泰材': '8463', '億豐': '8464', '美吉吉-KY': '8466', '波力-KY': '8467', '山林水': '8473', '東哥遊艇': '8478', '泰昇-KY': '8480', '政伸': '8481', '商億-KY': '8482', '吉源-KY': '8488', '鼎炫-KY': '8499', '台汽電': '8926', '新天地': '8940', '高力': '8996', '泰金寶-DR': '9105', '晨訊科-DR': '912000', '友佳-DR': '912398', '鈺齊-KY': '9802', '台火': '9902', '寶成': '9904', '大華': '9905', '欣巴巴': '9906', '統一實': '9907', '大台北': '9908', '豐泰': '9910', '櫻花': '9911', '偉聯': '9912', '美利達': '9914', '中保科': '9917', '欣天然': '9918', '康那香': '9919', '巨大': '9921', '福興': '9924', '新保': '9925', '新海': '9926', '泰銘': '9927', '中視': '9928', '秋雨': '9929', '中聯資源': '9930', '欣高': '9931', '中鼎': '9933', '成霖': '9934', '慶豐富': '9935', '全國': '9937', '百和': '9938', '宏全': '9939', '信義': '9940', '裕融': '9941', '茂順': '9942', '好樂迪': '9943', '新麗': '9944', '潤泰新': '9945', '三發地產': '9946', '佳龍': '9955', '世紀鋼': '9958', '茂生農經': '1240', '其祥-KY': '1258', '安心': '1259', '德麥': '1264', '漢來美食': '1268', '台翰': '1336', '精華': '1565', '濱川': '1569', '力肯': '1570', '新麥': '1580', '精剛': '1584', '和勤': '1586', '駿吉-KY': '1591', '祺驊': '1593', '川寶': '1595', '宏佳騰': '1599', '台蠟': '1742', '南光': '1752', '生泰': '1777', '合世': '1781', '訊聯': '1784', '光洋科': '1785', '杏昌': '1788', '金穎生技': '1796', '易威': '1799', '寶利徠': '1813', '富喬': '1815', '唐榮公司': '2035', '風青': '2061', '世鎧': '2063', '晉椿': '2064', '世豐': '2065', '世德': '2066', '嘉鋼': '2067', '精湛': '2070', '大甲': '2221', '泰茂': '2230', '謚源': '2235', '綠意': '2596', '大車隊': '2640', '正德': '2641', '捷迅': '2643', '晶悅': '2718', '燦星旅': '2719', '富驛-KY': '2724', '雅茗-KY': '2726', '瓦城': '2729', '六角': '2732', '易飛網': '2734', '高野': '2736', '天蔥': '2740', '山富': '2743', '五福': '2745', '豆府': '2752', '亞洲藏壽司': '2754', '揚秦': '2755', '滿心': '2916', '東凌-KY': '2924', '誠品生活': '2926', '紅馬-KY': '2928', '集雅社': '2937', '泰偉': '3064', '李洲': '3066', '全域': '3067', '協禧': '3071', '天方能源': '3073', '僑威': '3078', '聯亞': '3081', '網龍': '3083', '新零售': '3085', '華義': '3086', '艾訊': '3088', '元炬': '3089', '鴻碩': '3092', '港建': '3093', '及成': '3095', '穩懋': '3105', '好德': '3114', '寶島極': '3115', '進階': '3118', '笙泉': '3122', '昇銳': '3128', '弘塑': '3131', '晶宏': '3141', '新揚科': '3144', '大綜': '3147', '璟德': '3152', '精確': '3162', '波若威': '3163', '亞信': '3169', '新洲': '3171', '基亞': '3176', '公準': '3178', '鑫龍騰': '3188', '和進': '3191', '樺晟': '3202', '佰研': '3205', '志豐': '3206', '耀勝': '3207', '順達': '3211', '茂訊': '3213', '優群': '3217', '大學光': '3218', '倚強': '3219', '台嘉碩': '3221', '三顧': '3224', '至寶電': '3226', '原相': '3227', '金麗科': '3228', '錦明': '3230', '昱捷': '3232', '光環': '3234', '千如': '3236', '海灣': '3252', '鑫創': '3259', '威剛': '3260', '欣銓': '3264', '台星科': '3265', '海德威': '3268', '東碩': '3272', '宇環': '3276', '太普高': '3284', '微端': '3285', '廣寰科': '3287', '點晶': '3288', '宜特': '3289', '東浦': '3290', '鈊象': '3293', '英濟': '3294', '杭特': '3297', '岱稜': '3303', '鼎天': '3306', '佳穎': '3310', '斐成': '3313', '尼克森': '3317', '建舜電': '3322', '加百裕': '3323', '雙鴻': '3324', '旭品': '3325', '幸康': '3332', '泰谷': '3339', '律勝': '3354', '尚立': '3360', '先進光': '3362', '上詮': '3363', '典範': '3372', '熱映': '3373', '精材': '3374', '彬台': '3379', '崇越電': '3388', '旭軟': '3390', '漢科': '3402', '台興': '3426', '哲固': '3434', '類比科': '3438', '聯一光': '3441', '利機': '3444', '由田': '3455', '進泰電子': '3465', '致振': '3466', '安勤': '3479', '力致': '3483', '崧騰': '3484', '森寶': '3489', '單井': '3490', '昇達科': '3491', '長盛': '3492', '陽程': '3498', '環天科': '3499', '位速': '3508', '矽瑪': '3511', '皇龍': '3512', '亞帝歐': '3516', '華盈': '3520', '鴻翊': '3521', '御頂': '3522', '迎輝': '3523', '凡甲': '3526', '聚積': '3527', '力旺': '3529', '先益': '3531', '堡達': '3537', '曜越': '3540', '西柏': '3541', '宇峻': '3546', '兆利': '3548', '世禾': '3551', '同致': '3552', '重鵬': '3555', '禾瑞亞': '3556', '神準': '3558', '其陽': '3564', '逸昌': '3567', '大塚': '3570', '泓格': '3577', '友威科': '3580', '博磊': '3581', '閎康': '3587', '磐儀': '3594', '映興': '3597', '東林': '3609', '鼎翰': '3611', '安可': '3615', '富晶通': '3623', '光頡': '3624', '西勝': '3625', '盈正': '3628', '地心引力': '3629', '新鉅科': '3630', '晟楠': '3631', '研勤': '3632', '駿熠電': '3642', '艾恩特': '3646', '精聯': '3652', '鑫科': '3663', '安瑞-KY': '3664', '光耀': '3666', '康聯訊': '3672', '德微': '3675', '家登': '3680', '榮昌': '3684', '元創精密': '3685', '歐買尬': '3687', '湧德': '3689', '碩禾': '3691', '營邦': '3693', '漢磊': '3707', '鑫聯大投控': '3709', '連展投控': '3710', '新晶投控': '3713', '永日': '4102', '東洋': '4105', '邦特': '4107', '加捷生醫': '4109', '濟生': '4111', '聯上': '4113', '健喬': '4114', '明基醫': '4116', '友華': '4120', '優盛': '4121', '晟德': '4123', '太醫': '4126', '天良': '4127', '中天': '4128', '聯合': '4129', '健亞': '4130', '晶宇': '4131', '曜亞': '4138', '馬光-KY': '4139', '中裕': '4147', '台微體': '4152', '鈺緯': '4153', '康樂-KY': '4154', '太景*-KY': '4157', '創源': '4160', '聿新科': '4161', '智擎': '4162', '鐿鈦': '4163', '松瑞藥': '4167', '醣聯': '4168', '瑞基': '4171', '久裕': '4173', '浩鼎': '4174', '杏一': '4175', '福永生技': '4183', '安克': '4188', '杏國': '4192', '欣大健康': '4198', '中華食': '4205', '環泰': '4207', '信立': '4303', '勝昱': '4304', '世坤': '4305', '東隆興': '4401', '福大': '4402', '新昕纖': '4406', '飛寶企業': '4413', '三圓': '4416', '金洲': '4417', '元勝': '4419', '光明': '4420', '聚紡': '4429', '耀億': '4430', '銘旺實': '4432', '興采': '4433', '健信': '4502', '金雨': '4503', '崇友': '4506', '高鋒': '4510', '福裕': '4513', '永彰': '4523', '方土霖': '4527', '江興鍛': '4528', '淳紳': '4529', '宏易': '4530', '協易機': '4533', '慶騰': '4534', '至興': '4535', '大詠城': '4538', '晟田': '4541', '科嶠': '4542', '萬在': '4543', '桓達': '4549', '長佳': '4550', '橙的': '4554', '旭然': '4556', '健椿': '4561', '百德': '4563', '科際精密': '4568', '捷流閥業': '4580', '唐鋒': '4609', '中美實': '4702', '大恭': '4706', '磐亞': '4707', '永純': '4711', '南璋': '4712', '永捷': '4714', '大立': '4716', '美琪瑪': '4721', '永昕': '4726', '雙美': '4728', '熒茂': '4729', '豪展': '4735', '泰博': '4736', '泓瀚': '4741', '合一': '4743', '皇將': '4744', '合富-KY': '4745', '強生': '4747', '國碳科': '4754', '勤凱科技': '4760', '誠泰科技': '4767', 'VHQ-KY': '4803', '大略-KY': '4804', '昇華': '4806', '聯光通': '4903', '台聯電': '4905', '富宇': '4907', '前鼎': '4908', '新復興': '4909', '德英': '4911', '欣厚-KY': '4924', '新盛力': '4931', '友輝': '4933', '亞電': '4939', '兆遠': '4944', '陞達科技': '4945', '辣椒': '4946', '牧東': '4950', '緯軟': '4953', '譜瑞-KY': '4966', 'IET-KY': '4971', '湯石照明': '4972', '廣穎': '4973', '亞泰': '4974', '華星光': '4979', '科誠': '4987', '環宇-KY': '4991', '晶達': '4995', '榮剛': '5009', '久陽': '5011', '強新': '5013', '建錩': '5014', '華祺': '5015', '松和': '5016', '富強': '5102', '凱衛': '5201', '力新': '5202', '中茂': '5205', '坤悅': '5206', '新鼎': '5209', '寶碩': '5210', '蒙恬': '5211', '凌網': '5212', '亞昕': '5213', '萬達光電': '5220', '安力-KY': '5223', '立凱-KY': '5227', '雷笛克光學': '5230', '智晶': '5245', '天鉞電': '5251', '智崴': '5263', '笙科': '5272', '信驊': '5274', '達輝-KY': '5276', '尚凡': '5278', '大峽谷-KY': '5281', '數字': '5287', '宜鼎': '5289', '邑昇': '5291', '杰力': '5299', '寶得利': '5301', '太欣': '5302', '桂盟': '5306', '系統電': '5309', '天剛': '5310', '寶島科': '5312', '世紀': '5314', '光聯': '5315', '友銓': '5321', '士開': '5324', '華容': '5328', '建榮': '5340', '立衛': '5344', '天揚': '5345', '世界': '5347', '系通': '5348', '鈺創': '5351', '台林': '5353', '佳總': '5355', '協益': '5356', '力麗店': '5364', '中光電': '5371', '合正': '5381', '金利': '5383', '青雲': '5386', '應華': '5392', '慕康生醫': '5398', '中菲': '5403', '國眾': '5410', '台半': '5425', '振發': '5426', '達威': '5432', '東友': '5438', '高技': '5439', '均豪': '5443', '南良': '5450', '佶優': '5452', '昇益': '5455', '宣德': '5457', '同協': '5460', '霖宏': '5464', '富驊': '5465', '凱鈺': '5468', '聰泰': '5474', '德宏': '5475', '智冠': '5478', '新華': '5481', '中美晶': '5483', '通泰': '5487', '松普': '5488', '彩富': '5489', '同亨': '5490', '三聯': '5493', '凱崴': '5498', '永信建': '5508', '德昌': '5511', '力麒': '5512', '三豐': '5514', '雙喜': '5516', '力泰': '5520', '豐謙': '5523', '志嘉': '5529', '龍巖': '5530', '聖暉': '5536', '桓鼎-KY': '5543', '台聯櫃': '5601', '陸海': '5603', '中連貨': '5604', '中菲行': '5609', '劍湖山': '5701', '亞都': '5703', '老爺知': '5704', '日盛金': '5820', '致和證': '5864', '台名': '5878', '德記': '5902', '全家': '5903', '寶雅': '5904', '南仁湖': '5905', '宏遠證': '6015', '康和證': '6016', '大展證': '6020', '大慶證': '6021', '元大期貨': '6023', '福邦證': '6026', '寬魚國際': '6101', '合邦': '6103', '創惟': '6104', '亞元': '6109', '大宇資': '6111', '亞矽': '6113', '久威': '6114', '建達': '6118', '新普': '6121', '擎邦': '6122', '上奇': '6123', '業強': '6124', '廣運': '6125', '信音': '6126', '九豪': '6127', '普誠': '6129', '星寶國際': '6130', '萬旭': '6134', '茂達': '6138', '訊達電腦': '6140', '振曜': '6143', '得利影': '6144', '耕興': '6146', '頎邦': '6147', '驊宏資': '6148', '撼訊': '6150', '晉倫': '6151', '順發': '6154', '松上': '6156', '禾昌': '6158', '欣技': '6160', '捷波': '6161', '華電網': '6163', '久正': '6167', '昱泉': '6169', '統振': '6170', '亞銳士': '6171', '信昌電': '6173', '安碁': '6174', '立敦': '6175', '亞通': '6179', '橘子': '6180', '合晶': '6182', '幃翔': '6185', '新潤': '6186', '萬潤': '6187', '廣明': '6188', '萬泰科': '6190', '育富': '6194', '詩肯': '6195', '凌泰': '6198', '天品': '6199', '海韻電': '6203', '艾華': '6204', '雷科': '6207', '日揚': '6208', '慶生': '6210', '理銘': '6212', '中探針': '6217', '豪勉': '6218', '富旺': '6219', '岳豐': '6220', '晉泰': '6221', '上揚': '6222', '旺矽': '6223', '茂綸': '6227', '全譜': '6228', '研通': '6229', '系微': '6231', '旺玖': '6233', '高僑': '6234', '康呈': '6236', '驊訊': '6237', '松崗': '6240', '易通展': '6241', '立康': '6242', '茂迪': '6244', '立端': '6245', '臺龍': '6246', '淇譽電': '6247', '沛波': '6248', '百徽': '6259', '久元': '6261', '普萊德': '6263', '富裔': '6264', '方土昶': '6265', '泰詠': '6266', '倍微': '6270', '台燿': '6274', '元山': '6275', '安鈦克': '6276', '胡連': '6279', '佳邦': '6284', '元隆': '6287', '良維': '6290', '沛亨': '6291', '迅德': '6292', '智基': '6294', '通訊-KY': '6404', '晶焱': '6411', '韋僑': '6417', '詠昇': '6418', '京晨科': '6419', '易發': '6425', '統新': '6426', '今展科': '6432', '大中': '6435', '廣錠': '6441', '藥華藥': '6446', '紘康': '6457', '益得': '6461', '神盾': '6462', '威潤': '6465', '大樹': '6469', '宇智': '6470', '保瑞': '6472', '弘煜科': '6482', '點序': '6485', '互動': '6486', '環球晶': '6488', '生華科': '6492', '九齊': '6494', '科懋': '6496', '益安': '6499', '雙邦': '6506', '惠光': '6508', '聚和': '6509', '精測': '6510', '啟發電': '6512', '芮特-KY': '6514', '勤崴國際': '6516', '達爾膚': '6523', '明達醫': '6527', '創威': '6530', '瑞耘': '6532', '順藥': '6535', '倉和': '6538', '隆中': '6542', '高端疫苗': '6547', '長科*': '6548', '勝品': '6556', '欣普羅': '6560', '是方': '6561', '宏觀': '6568', '醫揚': '6569', '維田': '6570', '霈方': '6574', '逸達': '6576', '勁豐': '6577', '達邦蛋白': '6578', '東典': '6588', '台康生技': '6589', '普鴻': '6590', '台灣銘板': '6593', '展匯科': '6594', '寬宏藝術': '6596', '富強鑫': '6603', '瀧澤科': '6609', '奈米醫材': '6612', '朋億': '6613', '慧智': '6615', '特昇-KY': '6616', '萬年清': '6624', '泰金-KY': '6629', '均華': '6640', '富致': '6642', 'M31': '6643', '台生材': '6649', '全宇昕': '6651', '天正國際': '6654', '威健生技': '6661', '樂斯科': '6662', '群翊': '6664', '信紘科': '6667', '鈺太': '6679', '鑫創電子': '6680', '雍智科技': '6683', '安碁資訊': '6690', '東捷資訊': '6697', '軒郁': '6703', '長聖': '6712', '應廣': '6716', '亞泰金屬': '6727', '上洋': '6728', '昇佳電子': '6732', '博晟生醫': '6733', '亨泰光': '6747', '智聯服務': '6751', '叡揚': '6752', '達亞': '6762', '台微醫': '6767', '崑鼎': '6803', '邑錡': '7402', '意德士科技': '7556', '佑華': '8024', '鈦昇': '8027', '光菱': '8032', '榮群': '8034', '長園科': '8038', '九暘': '8040', '金山電': '8042', '蜜望實': '8043', '網家': '8044', '星雲': '8047', '德勝': '8048', '晶采': '8049', '廣積': '8050', '安國': '8054', '凱碩': '8059', '東捷': '8064', '來思達': '8066', '志旭': '8067', '全達': '8068', '元太': '8069', '能率網通': '8071', '鉅橡': '8074', '伍豐': '8076', '洛碁': '8077', '永利聯合': '8080', '瑞穎': '8083', '巨虹': '8084', '福華': '8085', '宏捷科': '8086', '華鎂鑫': '8087', '品安': '8088', '康全電訊': '8089', '翔名': '8091', '建暐': '8092', '保銳': '8093', '擎亞': '8096', '常珵': '8097', '大世科': '8099', '大億金茂': '8107', '博大': '8109', '立碁': '8111', '越峰': '8121', '正淩': '8147', '博智': '8155', '天宇': '8171', '智捷': '8176', '加高': '8182', '精星': '8183', '新漢': '8234', '華宏': '8240', '朋程': '8255', '商丞': '8277', '生展': '8279', '三竹': '8284', '泰藝': '8289', '尚茂': '8291', '群聯': '8299', '益張': '8342', '恒耀國際': '8349', '冠好': '8354', '金居': '8358', '千附': '8383', '金益鼎': '8390', '白紗科': '8401', '盛弘': '8403', '金可-KY': '8406', '商之器': '8409', '森田': '8410', '大國鋼': '8415', '實威': '8416', '捷必勝-KY': '8418', '明揚': '8420', '旭源': '8421', '保綠-KY': '8423', '惠普': '8424', '紅木-KY': '8426', '匯鑽科': '8431', '東生華': '8432', '弘帆': '8433', '鉅邁': '8435', '大江': '8436', '大地-KY': '8437', '綠電': '8440', '綠河-KY': '8444', '華研': '8446', '霹靂': '8450', '大拓-KY': '8455', '夠麻吉': '8472', '台境': '8476', '創業家': '8477', '三貝德': '8489', '裕國': '8905', '花王': '8906', '欣雄': '8908', '光隆': '8916', '欣泰': '8917', '沈氏': '8921', '時報': '8923', '大田': '8924', '北基': '8927', '鉅明': '8928', '富堡': '8929', '青鋼': '8930', '大汽電': '8931', '宏大': '8932', '愛地雅': '8933', '邦泰': '8935', '國統': '8936', '合騏': '8937', '明安': '8938', '關中': '8941', '森鉅': '8942', '琉園': '9949', '萬國通': '9950', '皇田': '9951', '邁達康': '9960', '有益': '9962'}





@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def stockNetCapAdmin(request):   #查詢本益比區間，給付費使用者使用。
    if request.method == "POST":  #假如是以POST方式才處理
        #mess = request.POST['stockid']  #取得表單輸入內容

        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotc_dict[mess0]
        #mess2 = request.POST['monthid']

        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:10]  #取得獲取資料時間
        #取得股票名稱
        stock_name = func2.GetStockName(mess)
        #stock_description, latest_trade_date, open, close, high, low, thisYearGain, newest_Rev_month, stock_id_name, yahoo_latest_tradePrice, stock_name = func2.stockdef(mess)


        Net1, Net2, Net3, Net4, pNet1, pNet2, pNet3, pNet4, cap1, cap2, cap3, cap4, capital_stock, Net4Average, pNet4Average = NetCapDB.NetCapDB(mess)
        #, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict =func3.PERseg(mess)
        #, pNet1, pNet2, pNet3, pNet4, pNet4Average
        #, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average
           

            #每次都必須更改
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            seg = models.NetCap_DB.objects.get(cStockID=mess)

            seg.cNet21Q4 = Net1            
            seg.cNet21Q3 = Net2
            seg.cNet21Q2 = Net3
            seg.cNet21Q1 = Net4
            seg.cNet20Q4 = Net5
            seg.cCap21Q3 = cap6
            seg.cCap21Q2 = cap7
            seg.cCap21Q1 = cap8
            seg.cCap20Q4 = cap9
            seg.pubtime=realtime
            seg.save()

        except:  #針對沒有的股票，抓取資料存入資料庫
            #每次都必須更改
            seg = models.NetCap_DB.objects.create(cStockID=mess, cStockName=stock_name, cNet21Q3 = Net1,cNet21Q2 = Net2,cNet21Q1 = Net3,cNet20Q4 = Net4,cCap21Q3 = cap1,cCap21Q2 = cap2,cCap21Q1 = cap3,cCap20Q4 = cap4,pubtime=realtime)
            seg.save()
            
            
    else:
        mess = "台股代號尚未送出！"
        #mess2 = "營收月份代號尚未送出！"

        #mess2 = "該表單尚未送出！2"
    return render(request, "stockNetCapAdmin.html", locals())


####################


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def listallscore(request):
    signs = Stock6Sign.objects.all().order_by('-cAverageScore')
    return render(request, "listallscore.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def listallseg(request):
    segs = StockPERseg.objects.all().order_by('cStockID')
    return render(request, "listallseg.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def listallsegscore(request):
    segs = StockPERseg.objects.all().order_by('-cRisk_reward')
    return render(request, "listallsegscore.html", locals())

#########################################

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def listallEPS(request):
    alleps = EPSachieve.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "listallEPS.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def listallCAP(request):
    caps = StockCapVar.objects.all().order_by('id')
    return render(request, "listallCAP.html", locals())






################
def index2(request):
	if request.user.is_authenticated:
	   name=request.user.username
	return render(request, "index2.html", locals())

def login2(request):  #付費使用者專專用
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None:


			if user.username == "jonyi729":
				auth.login(request,user)
				return redirect('/usersmain_common/jonyi729/')
				#return redirect('/usersmain_jonyi/')

                #return redirect('/index/')
				message = '登入成功！'

			elif user.username == "bobson808":
				auth.login(request,user)
				#return redirect('/usersmain_chenchi/')
				return redirect('/usersmain_common/chenchi/')
                #return redirect('/index/')
				message = '登入成功！'
                
			elif user.username == "chenchi":
				auth.login(request,user)
				#return redirect('/usersmain_chenchi/')
				return redirect('/usersmain_common/chenchi/')
                #return redirect('/index/')
				message = '登入成功！'
                
			elif user.username == "test268":
				auth.login(request,user)
				#return redirect('/usersmain_chenchi/')
				return redirect('/usersmain_common/chenchi/')
                #return redirect('/index/')
				message = '登入成功！'

                
                
			elif user.username == "test168":
				auth.login(request,user)
				return redirect('/usersmain_common/test168/')
                #return redirect('/index/')
				message = '登入成功！'
			elif user.is_active:
				auth.login(request,user)
				return redirect('/usersmain/')
                #return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login2.html", locals())


def login3(request):  #付費使用者專專用
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None:



                

			if user.is_active:
				auth.login(request,user)
				return redirect('/usersmain_app/')
                #return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login3.html", locals())

	
def logout2(request):  #付費使用者專專用
	auth.logout(request)
	return redirect('/index/')	


def logout3(request):  #app試用者專專用
	auth.logout(request)
	return redirect('/index/')	


def adduser(request):	
	try:
		user=User.objects.get(username="test")
	except:
		user=None
	if user!=None:
		message = user.username + " 帳號已建立!"
		return HttpResponse(message)
	else:	# 建立 test 帳號			
		user=User.objects.create_user("test","test@test.com.tw","aa123456")
		user.first_name="wen" # 姓名
		user.last_name="lin"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')


def signup(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        #cellphone = request.POST['cellphone']
                		
        user=User.objects.create_user(username,email,password)
        user.first_name = first_name # 名
        user.last_name = last_name  # 姓氏
        #user.cCellphone = cellphone #手機
        user.is_staff = False	# 工作人員狀態
        user.save()
        #message = user.username + " 帳號已建立!，請登入"
        #return HttpResponse(message)
        return redirect('/index/')
    
    return render(request, "signup.html", locals()) 



    
#https://docs.djangoproject.com/en/3.0/topics/auth/default/

        
        
  
######################
#from django.shortcuts import render, redirect
from myapp import models
#from myapp.models import NewsUnit
#from django.contrib.auth import authenticate
#from django.contrib import auth
#from django.contrib import messages
#from django.contrib.auth.models import User
#from django.views.decorators.csrf import ensure_csrf_cookie
#from django import template
import math

page1 = 1

def index(request, pageindex=None):  #首頁
    
	global page1
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "index.html", locals())

def detail(request, detailid=None):  #詳細頁面
	unit = models.NewsUnit.objects.get(id=detailid)
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1
	unit.save()
	return render(request, "detail.html", locals())


#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def login(request):  #登入   #管理人專用
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['password']  #取得輸入密碼
		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				return redirect('/adminmain/')  #開啟管理頁面
			else:  #帳號無效
				messages = '帳號尚未啟用！'
		else:  #驗證未通過
			messages = '登入失敗！'
	return render(request, "login.html", locals())

def logout(request):  #登出  #管理人專用
	auth.logout(request)
	return redirect('/index/')




@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsadd(request):  #新增資料
	message = ''  #清除訊息
	category = request.POST.get('news_type', '')  #取得輸入的類別
	subject = request.POST.get('news_subject', '')
	editor = request.POST.get('news_editor', '')
	content = request.POST.get('news_content', '')
	ok = request.POST.get('news_ok', '')
	if subject=='' or editor=='' or content=='':  #若有欄位未填就顯示訊息
		message = '每一個欄位都要填寫...'
	else:
		if ok=='yes':  #根據ok值設定enabled欄位
			enabled = True
		else:
			enabled = False
		unit = models.NewsUnit.objects.create(catego=category, nickname=editor, title=subject, message=content, enabled=enabled, press=0)
		unit.save()
		return redirect('/adminmain/')
	return render(request, "newsadd.html", locals())

@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsedit(request, newsid=None, edittype=None):  #修改資料
	unit = models.NewsUnit.objects.get(id=newsid)  #讀取指定資料
	categories = ["公告", "更新", "活動", "其他"]
	if edittype == None:  #進入修改頁面,顯示原有資料
		type = unit.catego
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		ok = unit.enabled
	elif edittype == '1':  #修改完畢,存檔
		category = request.POST.get('news_type', '')
		subject = request.POST.get('news_subject', '')
		editor = request.POST.get('news_editor', '')
		content = request.POST.get('news_content', '')
		ok = request.POST.get('news_ok', '')
		if ok=='yes':
			enabled = True
		else:
			enabled = False
		unit.catego=category
		unit.nickname=editor
		unit.title=subject
		unit.message=content
		unit.enabled=enabled
		unit.save()
		return redirect('/adminmain/')
	return render(request, "newsedit.html", locals())

@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.NewsUnit.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.catego.strip())
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/adminmain/')
	return render(request, "newsdelete.html", locals())

'''
def listone(request):
    try:
        sign = Stock6Sign.objects.get(cStockID="2330")
    except:
        eroormessage = " (讀取錯誤！)"
    return render(request, "listone.html", locals())

@permission_required('myapp.Can_enter_PaidUsersOnly', login_url='/listall/')
def listall(request):
    signs = Stock6Sign.objects.all().order_by('id')
    return render(request, "listall.html", locals())
'''



@permission_required('myapp.Can_enter_AdminOnly', login_url='/login2/')
def UsersListAll(request):
    users = User.objects.all().order_by('-last_login')
    return render(request, "UsersListAll.html", locals())




def usersmain(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u
	return render(request, "usersmain.html", locals())
####################################################################



       



@permission_required('myapp.Can_enter_stock6', login_url='/login2/')
def viewsISQuery(request):  #查詢六大指標，給付費使用者使用

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotc_dict[mess0]
        
        IS_Time, ISitem = func0.ISQuery(mess)
        


        stock_name = func2x.GetStockName(mess)
        
    else:
        mess = "台股代號尚未送出！"
        stock_name = "台股名稱尚未查到！"

    return render(request, "viewsISQuery.html", locals())


@permission_required('myapp.Can_enter_stock6', login_url='/login2/')
def viewsBSQuery(request):  #查詢六大指標，給付費使用者使用

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotc_dict[mess0]
        
        BS_Time, BSitem = func0.BSQuery(mess)
        


        stock_name = func2x.GetStockName(mess)
        
    else:
        mess = "台股代號尚未送出！"
        stock_name = "台股名稱尚未查到！"

    return render(request, "viewsBSQuery.html", locals())















def stockprice(request):    #查詢股價
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容

        stock_description, latest_trade_date, open, close, high, low, thisYearGain, newest_Rev_month, stock_id_name, yahoo_latest_tradePrice =func2.stockdef(mess)
        
        #mess2 = request.POST['xdays']  #取得表單輸入內容
    else:
        mess = "台股代號尚未送出！"
        

        #mess2 = "該表單尚未送出！2"
    return render(request, "stockprice.html", locals())






###############




##################################範例
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202009test(request):
    
    tse1 = ['2330','3034']
    signs = Stock6Sign202009.objects.filter(cStockID__in = tse1).order_by('cStockID')
    return render(request, "stock6listall202009test.html", locals())

################################################################






#子產業趨勢平均總表
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202011(request):
    subs = SubCats202011.objects.all().order_by('id')
    return render(request, "SubCatslistall202011.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202102(request):
    subs = SubCats202102.objects.all().order_by('id')
    return render(request, "SubCatslistall202102.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202103(request):
    subs = SubCats202103.objects.all().order_by('id')
    return render(request, "SubCatslistall202103.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202104(request):
    subs = SubCats202104.objects.all().order_by('id')
    return render(request, "SubCatslistall202104.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202105(request):
    subs = SubCats202105.objects.all().order_by('id')
    return render(request, "SubCatslistall202105.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202106(request):
    subs = SubCats202106.objects.all().order_by('id')
    return render(request, "SubCatslistall202106.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202107(request):
    subs = SubCats202107.objects.all().order_by('id')
    return render(request, "SubCatslistall202107.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202108(request):
    subs = SubCats202108.objects.all().order_by('id')
    return render(request, "SubCatslistall202108.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202109(request):
    subs = SubCats202109.objects.all().order_by('id')
    return render(request, "SubCatslistall202109.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202110(request):
    subs = SubCats202110.objects.all().order_by('id')
    return render(request, "SubCatslistall202110.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202111(request):
    subs = SubCats202111.objects.all().order_by('id')
    return render(request, "SubCatslistall202111.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def SubCatslistall202112(request):
    subs = SubCats202112.objects.all().order_by('id')
    return render(request, "SubCatslistall202112.html", locals())
###################################################






############################################################六大指標資料庫
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202005(request):
    signs = Stock6Sign202005.objects.all().order_by('id')
    return render(request, "stock6listall202005.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202006(request):
    signs = Stock6Sign202006.objects.all().order_by('cStockID')
    return render(request, "stock6listall202006.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall2020Q2(request):
    signs = Stock6Sign2020Q2.objects.all().order_by('cStockID')
    return render(request, "stock6listall2020Q2.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202008(request):
    signs = Stock6Sign202008.objects.all().order_by('cStockID')
    return render(request, "stock6listall202008.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202009(request):
    signs = Stock6Sign202009.objects.all().order_by('cStockID')
    return render(request, "stock6listall202009.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall2020Q3(request):

    
    signs = Stock6Sign2020Q3.objects.all().order_by('cStockID')
    return render(request, "stock6listall2020Q3.html", locals())



@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202011(request):

    
    signs = Stock6Sign202011.objects.all().order_by('cStockID')
    return render(request, "stock6listall202011.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall2020Q4(request):

    
    signs = Stock6Sign2020Q4.objects.all().order_by('cStockID')
    return render(request, "stock6listall2020Q4.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202101(request):

    
    signs = Stock6Sign202101.objects.all().order_by('cStockID')
    return render(request, "stock6listall202101.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202102(request):
    '''
    TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
    OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
    Allcompany = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958','1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']

    threeCategLength = 0
    twoCategLength = 0
    oneCategLength = 0
    zeroCategLength = 0
    
    gainCategLength = 0
    lossCategLength = 0 
    tieCategLength = 0 

    for c in Allcompany:
        try:
            sign = models.Stock6Sign2020Q4.objects.get(cStockID = c)
            if (float(sign.cAverageScore) >= 3):
                threeCategLength += 1
            elif (3 > float(sign.cAverageScore) >= 2):
                twoCategLength += 1
            elif (2 > float(sign.cAverageScore) >= 1):
                oneCategLength += 1
            elif (1 > float(sign.cAverageScore) >= 0):
                zeroCategLength += 1
                
        except:
            pass

    for c in Allcompany:
        try:
            sign = models.Stock6Sign2020Q4.objects.get(cStockID = c)
            if (float(sign.cLossGain) > 0):
                gainCategLength += 1
            elif (float(sign.cLossGain) < 0):
                lossCategLength += 1
            elif (float(sign.cLossGain) == 0):
                tieCategLength += 1

                
        except:
            pass
    '''
    
    signs = Stock6Sign202102.objects.all().order_by('cStockID')
    return render(request, "stock6listall202102.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202103(request):

    
    signs = Stock6Sign202103.objects.all().order_by('cStockID')
    return render(request, "stock6listall202103.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202104(request):

    
    signs = Stock6Sign202104.objects.all().order_by('cStockID')
    return render(request, "stock6listall202104.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202105(request):

    
    signs = Stock6Sign202105.objects.all().order_by('cStockID')
    return render(request, "stock6listall202105.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202106(request):

    
    signs = Stock6Sign202106.objects.all().order_by('cStockID')
    return render(request, "stock6listall202106.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202107(request):

    
    signs = Stock6Sign202107.objects.all().order_by('cStockID')
    return render(request, "stock6listall202107.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202108(request):

    
    signs = Stock6Sign202108.objects.all().order_by('cStockID')
    return render(request, "stock6listall202108.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202109(request):

    
    signs = Stock6Sign202109.objects.all().order_by('cStockID')
    return render(request, "stock6listall202109.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202110(request):

    
    signs = Stock6Sign202110.objects.all().order_by('cStockID')
    return render(request, "stock6listall202110.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202111(request):

    
    signs = Stock6Sign202111.objects.all().order_by('cStockID')
    return render(request, "stock6listall202111.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202112(request):

    
    signs = Stock6Sign202112.objects.all().order_by('cStockID')
    return render(request, "stock6listall202112.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202201(request):

    
    signs = Stock6Sign202201.objects.all().order_by('cStockID')
    return render(request, "stock6listall202201.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202202(request):

    
    signs = Stock6Sign202202.objects.all().order_by('cStockID')
    return render(request, "stock6listall202202.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202203(request):

    
    signs = Stock6Sign202203.objects.all().order_by('cStockID')
    return render(request, "stock6listall202203.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202204(request):

    
    signs = Stock6Sign202204.objects.all().order_by('cStockID')
    return render(request, "stock6listall202204.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202205(request):

    
    signs = Stock6Sign202205.objects.all().order_by('cStockID')
    return render(request, "stock6listall202205.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202206(request):

    
    signs = Stock6Sign202206.objects.all().order_by('cStockID')
    return render(request, "stock6listall202206.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202207(request):

    
    signs = Stock6Sign202207.objects.all().order_by('cStockID')
    return render(request, "stock6listall202207.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202208(request):

    
    signs = Stock6Sign202208.objects.all().order_by('cStockID')
    return render(request, "stock6listall202208.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202208v(request):

    
    signs = Stock6Sign202208.objects.all().order_by('cStockID')
    return render(request, "stock6listall202208.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202209(request):

    
    signs = Stock6Sign202209.objects.all().order_by('cStockID')
    return render(request, "stock6listall202209.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202210(request):

    
    signs = Stock6Sign202210.objects.all().order_by('cStockID')
    return render(request, "stock6listall202210.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202211(request):

    
    signs = Stock6Sign202211.objects.all().order_by('cStockID')
    return render(request, "stock6listall202211.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202212(request):

    
    signs = Stock6Sign202212.objects.all().order_by('cStockID')
    return render(request, "stock6listall202212.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202301(request):

    
    signs = Stock6Sign202301.objects.all().order_by('cStockID')
    return render(request, "stock6listall202301.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202302(request):

    
    signs = Stock6Sign202302.objects.all().order_by('cStockID')
    return render(request, "stock6listall202302.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202303(request):

    
    signs = Stock6Sign202303.objects.all().order_by('cStockID')
    return render(request, "stock6listall202303.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202304(request):

    
    signs = Stock6Sign202304.objects.all().order_by('cStockID')
    return render(request, "stock6listall202304.html", locals())
#################################################
'''
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6sta202105(request):
    
    TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
    OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
    Allcompany = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958','1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']

    threeCategLength = 0
    twoCategLength = 0
    oneCategLength = 0
    zeroCategLength = 0
    
    gainCategLength = 0
    lossCategLength = 0 
    tieCategLength = 0 

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202105.objects.get(cStockID = c)
            if (float(sign.cAverageScore) >= 3):
                threeCategLength += 1
            elif (3 > float(sign.cAverageScore) >= 2):
                twoCategLength += 1
            elif (2 > float(sign.cAverageScore) >= 1):
                oneCategLength += 1
            elif (1 > float(sign.cAverageScore) >= 0):
                zeroCategLength += 1
                
        except:
            pass

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202105.objects.get(cStockID = c)
            if (float(sign.cLossGain) > 0):
                gainCategLength += 1
            elif (float(sign.cLossGain) < 0):
                lossCategLength += 1
            elif (float(sign.cLossGain) == 0):
                tieCategLength += 1

                
        except:
            pass
    
    import datetime
    wholetime = str(datetime.datetime.now()) 
    realtime = wholetime[:16]  #取得獲取資料時間
        #取得六大指標平均分數


    #if mess_db2 == "04":    ########選擇寫入的六大指標評分平均資料庫
        #DB2 = SubCats202104   
    #elif mess_db2 == "05":
        #DB2 = SubCats202105



    try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理

            #不存在，發生錯誤，跳到except            
        sign = Stock6sta2021.objects.get(cTime="2021/05")






    except:  #針對沒有的股票，抓取資料存入資料庫
            #先創建7月資料，儲存
        sign = Stock6sta2021.objects.create(cTime="2021/05", cOver3p=threeCategLength, cOver2p=twoCategLength, cOver1p=oneCategLength, cOver0p=zeroCategLength, cMorep=gainCategLength, cSamep=tieCategLength, cLessp=lossCategLength, pubtime=realtime)
        sign.save()

    
    signs = Stock6Sign202105.objects.all().order_by('cStockID')
    return render(request, "stock6sta202105.html", locals())
#################################################

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6sta202106(request):
    
    TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
    OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
    Allcompany = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958','1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']

    threeCategLength = 0
    twoCategLength = 0
    oneCategLength = 0
    zeroCategLength = 0
    
    gainCategLength = 0
    lossCategLength = 0 
    tieCategLength = 0 

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202106.objects.get(cStockID = c)
            if (float(sign.cAverageScore) >= 3):
                threeCategLength += 1
            elif (3 > float(sign.cAverageScore) >= 2):
                twoCategLength += 1
            elif (2 > float(sign.cAverageScore) >= 1):
                oneCategLength += 1
            elif (1 > float(sign.cAverageScore) >= 0):
                zeroCategLength += 1
                
        except:
            pass

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202106.objects.get(cStockID = c)
            if (float(sign.cLossGain) > 0):
                gainCategLength += 1
            elif (float(sign.cLossGain) < 0):
                lossCategLength += 1
            elif (float(sign.cLossGain) == 0):
                tieCategLength += 1

                
        except:
            pass
    
    import datetime
    wholetime = str(datetime.datetime.now()) 
    realtime = wholetime[:16]  #取得獲取資料時間
        #取得六大指標平均分數


    #if mess_db2 == "04":    ########選擇寫入的六大指標評分平均資料庫
        #DB2 = SubCats202104   
    #elif mess_db2 == "05":
        #DB2 = SubCats202105



    try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理

            #不存在，發生錯誤，跳到except            
        sign = Stock6sta2021.objects.get(cTime="2021/06")






    except:  #針對沒有的股票，抓取資料存入資料庫
            #先創建7月資料，儲存
        sign = Stock6sta2021.objects.create(cTime="2021/06", cOver3p=threeCategLength, cOver2p=twoCategLength, cOver1p=oneCategLength, cOver0p=zeroCategLength, cMorep=gainCategLength, cSamep=tieCategLength, cLessp=lossCategLength, pubtime=realtime)
        sign.save()

    
    signs = Stock6Sign202106.objects.all().order_by('cStockID')
    return render(request, "stock6sta202106.html", locals())

#################################################
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6sta2021(request):


    
    signs = Stock6sta2021.objects.all().order_by('cTime')
    return render(request, "stock6sta2021.html", locals())
    '''


########################################################################

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202005score(request):
    signs = Stock6Sign202005.objects.all().order_by('-cAverageScore')
    return render(request, "stock6listall202005score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202006score(request):
    signs = Stock6Sign202006.objects.all().order_by('-cAverageScore')
    return render(request, "stock6listall202006score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall2020Q2score(request):
    signs = Stock6Sign2020Q2.objects.all().order_by('-cAverageScore')
    return render(request, "stock6listall2020Q2score.html", locals())



@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202008score(request):
    signs = Stock6Sign202008.objects.all().order_by('-cAverageScore')
    return render(request, "stock6listall202008score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202009score(request):
    signs = Stock6Sign202009.objects.all().order_by('-cAverageScore')
    return render(request, "stock6listall202009score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall2020Q3score(request):


    #twoCateg = []
    #oneCateg = []
    #zeroCateg = []
    

        
        #aveScore = float(sign.cAverageScore)
        #aStockID = str(sign.cStockID)
        

            
        #elif 3 > (float(sign.cAverageScore)) >= 2:
            #twoCateg.append(sign.cStockID) 
            
        #elif 2 > (float(sign.cAverageScore)) >= 1:
            #oneCateg.append(sign.cStockID) 
            
        #elif 1 > (float(sign.cAverageScore)) >= 0:
            #zeroCateg.append(sign.cStockID)


    #threeCategLength = len(threeCateg)   
    #twoCategLength = len(twoCateg)   
    #oneCategLength = len(oneCateg)      
    #zeroCategLength = len(zeroCateg)       
    signs = Stock6Sign2020Q3.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall2020Q3score.html", locals())



@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202011score(request):

    signs = Stock6Sign202011.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202011score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall2020Q4score(request):

    
    signs = Stock6Sign2020Q4.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall2020Q4score.html", locals())    


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202101score(request):

    
    signs = Stock6Sign202101.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202101score.html", locals()) 


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202102score(request):
    '''    
    TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
    OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
    Allcompany = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958','1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']

    threeCategLength = 0
    twoCategLength = 0
    oneCategLength = 0
    zeroCategLength = 0
    
    gainCategLength = 0
    lossCategLength = 0 
    tieCategLength = 0 

    for c in Allcompany:
        try:
            sign = models.Stock6Sign2020Q4.objects.get(cStockID = c)
            if (float(sign.cAverageScore) >= 3):
                threeCategLength += 1
            elif (3 > float(sign.cAverageScore) >= 2):
                twoCategLength += 1
            elif (2 > float(sign.cAverageScore) >= 1):
                oneCategLength += 1
            elif (1 > float(sign.cAverageScore) >= 0):
                zeroCategLength += 1
                
        except:
            pass

    for c in Allcompany:
        try:
            sign = models.Stock6Sign2020Q4.objects.get(cStockID = c)
            if (float(sign.cLossGain) > 0):
                gainCategLength += 1
            elif (float(sign.cLossGain) < 0):
                lossCategLength += 1
            elif (float(sign.cLossGain) == 0):
                tieCategLength += 1

                
        except:
            pass
    '''
    
    signs = Stock6Sign202102.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202102score.html", locals()) 

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202103score(request):

    signs = Stock6Sign202103.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202103score.html", locals()) 


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202104score(request):

    signs = Stock6Sign202104.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202104score.html", locals())



@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202105score(request):

    signs = Stock6Sign202105.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202105score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202106score(request):

    signs = Stock6Sign202106.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202106score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202107score(request):

    signs = Stock6Sign202107.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202107score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202108score(request):

    signs = Stock6Sign202108.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202108score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202109score(request):

    signs = Stock6Sign202109.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202109score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202110score(request):

    signs = Stock6Sign202110.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202110score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202111score(request):

    signs = Stock6Sign202111.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202111score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202112score(request):

    signs = Stock6Sign202112.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202112score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202201score(request):

    signs = Stock6Sign202201.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202201score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202202score(request):

    signs = Stock6Sign202202.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202202score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202203score(request):

    signs = Stock6Sign202203.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202203score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202204score(request):

    signs = Stock6Sign202204.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202204score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202205score(request):

    signs = Stock6Sign202205.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202205score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202206score(request):

    signs = Stock6Sign202206.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202206score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202207score(request):

    signs = Stock6Sign202207.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202207score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202208score(request):

    signs = Stock6Sign202208.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202208score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202209score(request):

    signs = Stock6Sign202209.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202209score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202210score(request):

    signs = Stock6Sign202210.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202210score.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202211score(request):

    signs = Stock6Sign202211.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202211score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202212score(request):

    signs = Stock6Sign202212.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202212score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202301score(request):

    signs = Stock6Sign202301.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202301score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202302score(request):

    signs = Stock6Sign202302.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202302score.html", locals())
@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202303score(request):

    signs = Stock6Sign202303.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202303score.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def stock6listall202304score(request):

    signs = Stock6Sign202304.objects.all().order_by('-cAverageScore')

    
    return render(request, "stock6listall202304score.html", locals())







#############本益比區間##################################################



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202005(request):
    segs = StockPERseg202005.objects.all().order_by('id')
    return render(request, "stockPERseglistall202005.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202006(request):
    segs = StockPERseg202006.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202006.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q2(request):
    segs = StockPERseg2020Q2.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall2020Q2.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202008(request):
    segs = StockPERseg202008.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202008.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202009(request):
    segs = StockPERseg202009.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202009.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q3(request):
    segs = StockPERseg2020Q3.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall2020Q3.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202011(request):
    segs = StockPERseg202011.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202011.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q4(request):
    segs = StockPERseg2020Q4.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall2020Q4.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202101(request):
    segs = StockPERseg202101.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202101.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202102(request):
    segs = StockPERseg202102.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202102.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202103(request):
    segs = StockPERseg202103.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202103.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202104(request):
    segs = StockPERseg202104.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202104.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202105(request):
    segs = StockPERseg202105.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202105.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202106(request):
    segs = StockPERseg202106.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202106.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202107(request):
    segs = StockPERseg202107.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202107.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202108(request):
    segs = StockPERseg202108.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202108.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202109(request):
    segs = StockPERseg202109.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202109.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202110(request):
    segs = StockPERseg202110.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202110.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202111(request):
    segs = StockPERseg202111.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202111.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202112(request):
    segs = StockPERseg202112.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202112.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202201(request):
    segs = StockPERseg202201.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202201.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202202(request):
    segs = StockPERseg202202.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202202.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202203(request):
    segs = StockPERseg202203.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202203.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202204(request):
    segs = StockPERseg202204.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202204.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202205(request):
    segs = StockPERseg202205.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202205.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202206(request):
    segs = StockPERseg202206.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202206.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202207(request):
    segs = StockPERseg202207.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202207.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202208(request):
    segs = StockPERseg202208.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202208.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202209(request):
    segs = StockPERseg202209.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202209.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202210(request):
    segs = StockPERseg202210.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202210.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202211(request):
    segs = StockPERseg202211.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202211.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202212(request):
    segs = StockPERseg202212.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202212.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202301(request):
    segs = StockPERseg202301.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202301.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202302(request):
    segs = StockPERseg202302.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202302.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202303(request):
    segs = StockPERseg202303.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202303.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202304(request):
    segs = StockPERseg202304.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202304.html", locals())


##########################################################################







@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202005score(request):
    segs = StockPERseg202005.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202005score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202006score(request):
    segs = StockPERseg202006.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202006score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q2score(request):
    segs = StockPERseg2020Q2.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall2020Q2score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202008score(request):
    segs = StockPERseg202008.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202008score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202009score(request):
    segs = StockPERseg202009.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202009score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q3score(request):
    segs = StockPERseg2020Q3.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall2020Q3score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202011score(request):
    segs = StockPERseg202011.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202011score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q4score(request):
    segs = StockPERseg2020Q4.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall2020Q4score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202101score(request):
    segs = StockPERseg202101.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202101score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202102score(request):
    segs = StockPERseg202102.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202102score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202103score(request):
    segs = StockPERseg202103.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202103score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202104score(request):
    segs = StockPERseg202104.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202104score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202105score(request):
    segs = StockPERseg202105.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202105score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202106score(request):
    segs = StockPERseg202106.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202106score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202107score(request):
    segs = StockPERseg202107.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202107score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202108score(request):
    segs = StockPERseg202108.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202108score.html", locals())




@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202109score(request):
    segs = StockPERseg202109.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202109score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202110score(request):
    segs = StockPERseg202110.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202110score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202111score(request):
    segs = StockPERseg202111.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202111score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202112score(request):
    segs = StockPERseg202112.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202112score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202201score(request):
    segs = StockPERseg202201.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202201score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202202score(request):
    segs = StockPERseg202202.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202202score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202203score(request):
    segs = StockPERseg202203.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202203score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202204score(request):
    segs = StockPERseg202204.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202204score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202205score(request):
    segs = StockPERseg202205.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202205score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202206score(request):
    segs = StockPERseg202206.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202206score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202207score(request):
    segs = StockPERseg202207.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202207score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202208score(request):
    segs = StockPERseg202208.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202208score.html", locals())



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202209score(request):
    segs = StockPERseg202209.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202209score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202210score(request):
    segs = StockPERseg202210.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202210score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202211score(request):
    segs = StockPERseg202211.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202211score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202212score(request):
    segs = StockPERseg202212.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202212score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202301score(request):
    segs = StockPERseg202301.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202301score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202302score(request):
    segs = StockPERseg202302.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202302score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202303score(request):
    segs = StockPERseg202303.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202303score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202304score(request):
    segs = StockPERseg202304.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202304score.html", locals())





###################





    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
##################下載區#############################################################    
@permission_required('myapp.Can_enter_PaidUsersOnly', login_url='/login2/')
def AREAdownloads(request):
    return render(request,"AREAdownloads.html")


   
@permission_required('myapp.Can_enter_stock6', login_url='/login2/')
def stock6downloads(request):
    return render(request,"stock6downloads.html")


@permission_required('myapp.Can_enter_stockPERseg', login_url='/login2/')
def stockPERsegdownloads(request):
    return render(request,"stockPERsegdownloads.html")



@permission_required('myapp.Can_enter_All', login_url='/login2/')
def stockEnterAlldownloads(request):
    return render(request,"stockEnterAlldownloads.html")

##################EPS達成率區##################################################
@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2020Q2listall(request):
    alleps = EPSachieve2020Q2.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2020Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2020Q3listall(request):
    alleps = EPSachieve2020Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2020Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2021Q1listall(request):
    alleps = EPSachieve2021Q1.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2021Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2021Q2listall(request):
    alleps = EPSachieve2021Q2.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2021Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2021Q3listall(request):
    alleps = EPSachieve2021Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2021Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2022Q1listall(request):
    alleps = EPSachieve2022Q1.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2022Q1listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSachieve2022Q3listall(request):
    alleps = EPSachieve2022Q3.objects.all().order_by('-cEPSAchieveRate')
    return render(request, "EPSachieve2022Q3listall.html", locals())
####################################################################################




@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2020Q2listall(request):
    caps = StockCapVar2020Q2.objects.all().order_by('id')
    return render(request, "StockCapVar2020Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2020Q3listall(request):
    caps = StockCapVar2020Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2020Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2020Q4listall(request):
    caps = StockCapVar2020Q4.objects.all().order_by('id')
    return render(request, "StockCapVar2020Q4listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q1listall(request):
    caps = StockCapVar2021Q1.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q2listall(request):
    caps = StockCapVar2021Q2.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q3listall(request):
    caps = StockCapVar2021Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2021Q4listall(request):
    caps = StockCapVar2021Q4.objects.all().order_by('id')
    return render(request, "StockCapVar2021Q4listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2022Q1listall(request):
    caps = StockCapVar2022Q1.objects.all().order_by('id')
    return render(request, "StockCapVar2022Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2022Q3listall(request):
    caps = StockCapVar2022Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2022Q3listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def StockCapVar2022Q4listall(request):
    caps = StockCapVar2022Q3.objects.all().order_by('id')
    return render(request, "StockCapVar2022Q4listall.html", locals())
######################################################################



@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfitlistall2020Q1(request):
    allepsprof = EpsProfit2020Q1.objects.all().order_by('id')
    return render(request, "EPSnProfitlistall2020Q1.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2020Q2listall(request):
    allepsprof = EpsProfit2020Q2.objects.all().order_by('id')
    return render(request, "EPSnProfit2020Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2020Q3listall(request):
    allepsprof = EpsProfit2020Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2020Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2020Q4listall(request):
    allepsprof = EpsProfit2020Q4.objects.all().order_by('id')
    return render(request, "EPSnProfit2020Q4listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q1listall(request):
    allepsprof = EpsProfit2021Q1.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q1listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q2listall(request):
    allepsprof = EpsProfit2021Q2.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q2listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q3listall(request):
    allepsprof = EpsProfit2021Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q3listall.html", locals())

@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2021Q4listall(request):
    allepsprof = EpsProfit2021Q4.objects.all().order_by('id')
    return render(request, "EPSnProfit2021Q4listall.html", locals())


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def EPSnProfit2022Q1listall(request):
    allepsprof = EpsProfit2022Q1.objects.all().order_by('id')
    return render(request, "EPSnProfit2022Q1listall.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def EPSnProfit2022Q3listall(request):
    allepsprof = EpsProfit2022Q3.objects.all().order_by('id')
    return render(request, "EPSnProfit2022Q3listall.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def EPSnProfit2022Q4listall(request):
    allepsprof = EpsProfit2022Q4.objects.all().order_by('id')
    return render(request, "EPSnProfit2022Q4listall.html", locals())
##############################################################

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020(request):
    stas = StockPERsegStable2020.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020.html", locals())



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q2(request):
    stas = StockPERsegStable2020Q2.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020Q2.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q3(request):
    stas = StockPERsegStable2020Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020Q3.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q4(request):
    stas = StockPERsegStable2020Q4.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2020Q4.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q1(request):
    stas = StockPERsegStable2021Q1.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q1.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q2(request):
    stas = StockPERsegStable2021Q2.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q2.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q3(request):
    stas = StockPERsegStable2021Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q3.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2021Q4(request):
    stas = StockPERsegStable2021Q4.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2021Q4.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2022Q1(request):
    stas = StockPERsegStable2022Q1.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2022Q1.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2022Q3(request):
    stas = StockPERsegStable2022Q3.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2022Q3.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2022Q4(request):
    stas = StockPERsegStable2022Q4.objects.all().order_by('id')
    return render(request, "stockPERsegStablelistall2022Q4.html", locals())
'''

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERsegStablelistall2020Q2(request):
    stas = StockPERsegStable2020Q2.objects.all().order_by('cStockID')
    return render(request, "StockPERsegStable2020Q2.html", locals())
'''
######################################################################


@permission_required('myapp.Can_enter_All', login_url='/login2/')
def BigMoney(request):  #查詢大戶持股比率，給付費使用者使用

    if request.method == "POST":  #假如是以POST方式才處理
        #mess = request.POST['stockid']  #取得表單輸入內容
        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotc_dict[mess0]


        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        stock_name, pBoard, pForeign, pInvest, pSecurity, pBig, pIndiv =func4.InstituRate(mess) #取得六大指標平均
        #取得股票名稱
        
        
        #try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #sign = models.Stock6Sign.objects.get(cStockID=mess)

        #except:  #針對沒有的股票，抓取資料存入資料庫
            #sign = models.Stock6Sign.objects.create(cStockID=mess, cStockName=stock_name, cSign1=result1, cSign2=result2, cSign3=result3, cSign4=result4, cSign5=result5, cSign6=result6, cAverageScore=average6stock, pubtime=realtime)
            #sign.save()
               
       
        #mess2 = request.POST['xdays']  #取得表單輸入內容
    else:
        mess = "台股代號尚未送出！"


        #mess2 = "該表單尚未送出！2"
    return render(request, "BigMoney.html", locals())
#######################################################################################################

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202011(request):

    
    signs = DCStock6Sign202011.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202011.html", locals())



@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall2020Q4(request):

    
    signs = DCStock6Sign2020Q4.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall2020Q4.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202101(request):

    
    signs = DCStock6Sign202101.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202101.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202102(request):
    '''    
    TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
    OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
    Allcompany = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958','1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']

    threeCategLength = 0
    twoCategLength = 0
    oneCategLength = 0
    zeroCategLength = 0
    
    gainCategLength = 0
    lossCategLength = 0 
    tieCategLength = 0 

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202011.objects.get(cStockID = c)
            if (float(sign.cAverageScore) >= 3):
                threeCategLength += 1
            elif (3 > float(sign.cAverageScore) >= 2):
                twoCategLength += 1
            elif (2 > float(sign.cAverageScore) >= 1):
                oneCategLength += 1
            elif (1 > float(sign.cAverageScore) >= 0):
                zeroCategLength += 1
                
        except:
            pass

    for c in Allcompany:
        try:
            sign = models.Stock6Sign202011.objects.get(cStockID = c)
            if (float(sign.cLossGain) > 0):
                gainCategLength += 1
            elif (float(sign.cLossGain) < 0):
                lossCategLength += 1
            elif (float(sign.cLossGain) == 0):
                tieCategLength += 1

                
        except:
            pass
    '''
    
    signs = DCStock6Sign202102.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202102.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202103(request):

    
    signs = DCStock6Sign202103.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202103.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202104(request):

    
    signs = DCStock6Sign202104.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202104.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202105(request):

    
    signs = DCStock6Sign202105.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202105.html", locals())

@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202106(request):

    
    signs = DCStock6Sign202106.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202106.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202107(request):

    
    signs = DCStock6Sign202107.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202107.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202108(request):

    
    signs = DCStock6Sign202108.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202108.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202109(request):

    
    signs = DCStock6Sign202109.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202109.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202110(request):

    
    signs = DCStock6Sign202110.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202110.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202111(request):

    
    signs = DCStock6Sign202111.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202111.html", locals())


@permission_required('myapp.Can_enter_stock6 DB', login_url='/login2/')
def DCstock6listall202112(request):

    
    signs = DCStock6Sign202112.objects.all().order_by('cStockID')
    return render(request, "DCstock6listall202112.html", locals())
###########各資料庫分頁########################################################
def DB_stock6sign(request):
    return render(request,"DB_stock6sign.html")


def DB_stockPERseg(request):
    return render(request,"DB_stockPERseg.html")


def DB_DCstock6sign(request):
    return render(request,"DB_DCstock6sign.html")

def DB_stockPERsegStable(request):
    return render(request,"DB_stockPERsegStable.html")

def DB_EPSachiever(request):
    return render(request,"DB_EPSachiever.html")


def DB_StockCapGetter(request):
    return render(request,"DB_StockCapGetter.html")

def DB_EPSnProfitGetter(request):
    return render(request,"DB_EPSnProfitGetter.html")
###########################

@permission_required('myapp.Can_enter_stockKn', login_url='/login2/')
def stockKn(request):  #查詢六大指標，給付費使用者使用

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess0 = request.POST['stockid']  #取得表單輸入內容
        
        if is_number(mess0) == True:  #是數字
            mess = mess0
        else:
            mess = tseotc_dict[mess0]
    
        bt1q, sh1q, bt_roe1_4sum, bt_roe1_4sump, b1q, yahoo_latest_tradePrice, pb1q, kn1_4sum, kn1_4sump, bt1qN, bt2qN, bt3qN, bt4qN, bt_roe1qp, bt_roe2qp, bt_roe3qp, bt_roe4qp = KnQuery.KnQuery(mess) 

        #bt1, sh1, bt_roe1, bt_roe1p, b1, yahoo_latest_tradePrice, pb1, kn1, kn1p = KnQuery.KnQuery(mess) 
        H0, H1, H2, H3, H4, H5, H6, H7, H8, H9, L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, bt1N, bt2N, bt3N, bt4N, bt5N, bt6N, bt7N, bt8N, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, bt_roe1p, bt_roe2p, bt_roe3p, bt_roe4p, bt_roe5p, bt_roe6p, bt_roe7p, bt_roe8p, b1, b2, b3, b4, b5, b6, b7, b8, kn1_Hp, kn1_Lp, kn2_Hp, kn2_Lp, kn3_Hp, kn3_Lp, kn4_Hp, kn4_Lp, kn5_Hp, kn5_Lp, kn6_Hp, kn6_Lp, kn7_Hp, kn7_Lp, kn8_Hp, kn8_Lp, pb1_H, pb1_L, pb2_H, pb2_L, pb3_H, pb3_L, pb4_H, pb4_L, pb5_H, pb5_L, pb6_H, pb6_L, pb7_H, pb7_L, pb8_H, pb8_L, bt_roe1_8avep, pb1_8_Have, pb1_8_Lave, kn1_8_Havep, kn1_8_Lavep, buyin_price, notbuyin_price  = Kn8yPrice.Kn8yPrice(mess) 

        stock_name = func2x.GetStockName(mess)
        
    else:
        mess = "台股代號尚未送出！"
        stock_name = "台股名稱尚未查到！"

        #mess2 = "該表單尚未送出！2"
    return render(request, "stockKn.html", locals())


###############################################################################

################
def index_sns(request):

	return render(request, "index_sns.html", locals())