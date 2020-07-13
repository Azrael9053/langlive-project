import eel
import requests
import time
import os
import threading

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

eel.init('web')



def marge():
    file_list = []
    for root, dirs, files in os.walk(file_path + 'ts_files/'):  # 生成器
        for fn in files:
            p = str(root + '/' + fn)
            file_list.append(p)
    newlist = sorted(file_list)
    mkdir('./合併檔案')
    fpath = './合併檔案/' + file_path + '.ts'
    with open(fpath, 'wb+') as fw:
        for i in range(len(newlist)):
            fw.write(open(newlist[i], 'rb').read())


def mkdir(path):
    f = os.path.exists(path)
    if not f:
        os.makedirs(path)


def todownload(t):
    mkdir(file_path + 'ts_files/')
    url = ts_url + t
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            tspath = file_path + 'ts_files/' + t.split('.')[0] + '.ts'
            print('正在下載' + t.split('.')[0] + '.ts')
            with open(tspath, "wb+") as file:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        file.flush()
        else:
            with open(file_path + 'failQQ.txt', 'a') as f:
                f.write(url)
                f.write('\n')
            print(t + '下載失敗')

    except:
        with open(file_path + 'failQQ.txt', 'a') as f:
            f.write(url)
            f.write('\n')
        print('下載超時')


def tsdownload():
    tflag = 0
    ts_list = []
    first_ts = 0
    count = 0
    global tail
    global m3u8_url
    while True:
        try:
            r = requests.get(m3u8_url, headers=headers)
            if r.status_code == 200:
                ts_text = r.text
                for t in ts_text.split('\n'):
                    if '.ts' in t and t not in ts_list:
                        if first_ts == 0:
                            first_ts = int(t.split('.')[0])
                            tail = t.replace(t.split('.')[0], '')
                        ts_list.append(t)
                        # if tflag == 1:
                        #     thh.join()
                        thh = threading.Thread(target=todownload(t))
                        thh.start()
                        tflag = 1
                        print(t + '已新增至記事本')
                        with open(file_path + 'ts.txt', 'a') as f:
                            f.write(ts_url + t)
                            f.write('\n')
                count = 0
                time.sleep(1)
            else:
                if count % 5 == 0:
                    print('尋找中')

                if count % 10 == 0:
                    try:
                        m = requests.get(m3u8, headers=headers)
                        if m.status_code == 200:
                            for x in m.text.split('\n'):
                                if '.m3u8?' in x:
                                    m3u8_url = x
                                    break
                    except:
                        print('請求超時拉QAQ')
                count += 1
                time.sleep(3)
            if count == 100:
                print('end')
                return first_ts
        except:
            print('請求m3u8網址超時123')
            count += 1
            time.sleep(1)


def revdownload(n, tstail):
    while True:
        n -= 1
        url = ts_url + str(n) + tstail
        print(url)
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                x = 0
                mkdir(file_path + 'ts_files/')
                tspath = file_path + 'ts_files/' + str(n) + '.ts'
                print('正在下載' + str(n) + '.ts')
                with open(tspath, "wb+") as file:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
            else:
                x += 1
            if x >= 20:
                print("下載結束!")
                break
        except:
            x += 1
            print('請求超時')


def failfiledownload():
    mkdir(file_path + 'ts_files/')
    with open(file_path + 'failQQ.txt', 'r') as f:
        ts_list = f.readlines()
    for i in ts_list:
        url = i.replace('\n', '')
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                tspath = file_path + 'ts_files/' + i.replace(ts_url, '').replace(tail, '') + '.ts'
                print('正在下載' + i.replace(ts_url, '').replace(tail, '') + '.ts')
                with open(tspath, "wb+") as file:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            file.flush()
        except:
            print('下載faill')




def main(name, time1):
    startday = time1.split('T')[0]
    starttime = time1.split('T')[1]
    timetuple = time.localtime()
    tlist = list(timetuple)
    tlist[0] = int(startday.split('-')[0])
    tlist[1] = int(startday.split('-')[1])
    tlist[2] = int(startday.split('-')[2])
    timelist = starttime.split(':')
    tlist[3] = int(timelist[0])
    tlist[4] = int(timelist[1])
    tlist[5] = 0
    timetuple = tuple(tlist)
    print(timetuple)
    iddic = {'吳婉淩':'4210533', '李孟純':'1985963', '李采潔':'3651219', '林潔心':'3650718', '林佳霓':'4663716', '冼迪琦':'3687493', '柏靈':'3650740', '宮田留佳':'4663724', '陳詩雅':'3652550', '國興瑀':'4560592', '董子瑄':'3800370', '賈宜蓁':'3650741', '蔡亞恩':'3650734', '潘姿怡':'2028726', '王逸嘉':'3650583', '李佳俐':'3619520', '邱品涵':'3686707', '周家安':'4663718', '林倢':'3650580', '翁彤薰':'4663722', '高云珏':'3650590', '張法法':'3652111', '蔡伊柔':'1398860', '鄭妤葳':'3793753', '劉語晴':'3686711', '劉潔明':'3686715', '藤井麻由':'3794774', '羅瑞婷':'3650751', '小山美玲':'3795137', '本田柚萱':'no', '吳騏卉':'4663715', '周佳郁':'3650735', '林易沄':'3650589', '林家瑩':'3650755', '林于馨':'3686713', '林亭莉':'4663721', '袁子筑':'4663738', '高硯晨':'no', '張羽翎':'3686709', '曾詩羽':'3686725', '鄭佳郁':'3650753', '劉曉晴':'3686708'}
    ID = iddic[name]
    print(ID)
    while True:
        if time.mktime(timetuple) < time.mktime(time.localtime()):
            print('程式開始執行!')
            break
        else:
            time.sleep(1)
            os.system('cls')
            print('下載成員ID :', ID)
            print('現在時間 :', time.strftime("%b %d %Y %H:%M:%S", time.localtime()))
            print('設定下載開始時間 :', time.strftime("%b %d %Y %H:%M:%S", timetuple))
    Year = time.strftime('%Y', time.localtime())
    month = time.strftime('%m', time.localtime())
    day = time.strftime('%d', time.localtime())
    global file_path, m3u8, m3u8_url, ts_url
    file_path = './' + Year + '_' + month + '_' + day + ' ' + ID + '_'
    flvflag = 0

    while True:
        r = requests.get('https://langapi.lv-show.com/langweb/v1/room/liveinfo?room_id=' + ID).json()
        try:
            print('這次的網址 : ' + r['data']['live_info']['liveurl_hls'])
            m3u8_url = r['data']['live_info']['liveurl_hls']
            m3u8 = m3u8_url
            ts_url = m3u8_url.replace('playlist.m3u8', '')
            # print(ts_url)
        except:
            print('尋找中')
            time.sleep(60)
        else:
            try:
                flv = r['data']['live_info']['liveurl']
                flvflag = 1
            except:
                flvflag = 0
            break

    while True:
        try:
            r = requests.get(m3u8_url, headers=headers)
            if r.status_code == 200:
                if flvflag == 1:
                    for x in r.text.split('\n'):
                        if '.m3u8?' in x:
                            m3u8_url = x
                            break
                temp = 1
                firstts = tsdownload()
                # print(firstts, tail)
                revdownload(firstts, tail)
                if os.path.isfile(file_path + 'failQQ.txt'):
                    ask = input('是否要重新下載失敗的檔案? y/n : ')
                    if ask == 'y':
                        failfiledownload()
                marge()
                print('檔案下載合併完成')
                os.system('pause')

            elif temp == 1:
                break

            else:
                print('尋找中')
                time.sleep(30)

        except:
            print('請求m3u8網址超時')

# @eel.expose
# def start(arr)


eel.start('main.html', size = (720, 400))
