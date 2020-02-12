
# coding: utf-8

# In[165]:


#PR PYTHON PROBSTAT
#DAVID PETRA NATANAEL - 18217011


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#LOAD DARI FILE
data = pd.read_csv('454480_PR_STEI.csv')

datatest = data.select_dtypes(include=['object']).copy()
df = datatest.loc[:,datatest.columns]=datatest.apply(lambda x : pd.factorize(x)[0])


warna = ['#42f4aa','#e2f441','#9d64c9','#a80850','#e7efaa','#ff3030','#5e2f2f','#157200',
         '#9af9e0','#d3f999','#f99999','#7c7a7a','#a06d06','#e8914a','#3d3631']


# In[166]:


#NOMOR 1

#BAR CHART JENIS KELAMIN

print("NOMOR 1")

data['Jenis Kelamin'].value_counts().plot.barh()


# In[167]:


#BAR CHART USIA

print("NOMOR 1")

data['Usia'].value_counts().plot.barh()


# In[168]:


#BARCHART PENDIDIKAN TERAKHIR

print("NOMOR 1")

data['Pendidikan Terakhir'].value_counts().plot.barh()


# In[169]:


#BARCHART PEKERJAAN

print("NOMOR 1")

data['Pekerjaan'].value_counts().plot.barh()


# In[170]:


#BARCHART PENGHASILAN PERBULAN

print("NOMOR 1")

data['Penghasilan Perbulan'].value_counts().plot.barh()


# In[223]:


#BARCHART KATEGORI E-MONEY APA SAJA YANG DIPAKAI

print("NOMOR 1")

GoPay           = (data['Go-Pay'] == 1).sum()
OVO             = (data['OVO'] == 1).sum()
iSaku           = (data['iSaku'] == 1).sum()
Sakuku          = (data['Sakuku'] == 1).sum()
FlazzBCA        = (data['Flazz BCA'] == 1).sum()
Brizzi          = (data['Brizzi'] == 1).sum()
Megacash        = (data['Megacash'] == 1).sum()
EMoneyMandiri   = (data['eMoney Mandiri'] == 1).sum()
Tcash           = (data['Tcash'] == 1).sum()
ECashMandiri    = (data['E-cash Mandiri'] == 1).sum()
RekeningPonsel  = (data['Rekening ponsel'] == 1).sum()
BNITapcash      = (data['BNI Tapcash'] == 1).sum()
XLTunai         = (data['XL tunai'] == "1PENGGUNA iSAKU").sum()
Paytren         = (data['Paytren'] == 1).sum()
Jakcard         = (data['Jakcard'] == 1).sum()


y = [GoPay, OVO, iSaku, Sakuku, FlazzBCA, Brizzi, Megacash, EMoneyMandiri, Tcash, ECashMandiri, 
         RekeningPonsel, BNITapcash, XLTunai, Paytren, Jakcard]
bar = ('Go-Pay', 'OVO', 'iSaku', 'Sakuku', 'Flazz BCA', 'Brizzi', 'Megacash', 'E-Money Mandiri', 'Tcash', 
       'E-Cash Mandiri', 'Rekening Ponsel', 'BNI Tapcash', 'XL Tunai', 'Paytren', 'Jakcard')
y_pos = np.arange(len(y))
plt.title("Jumlah Kategori E-Money yang Dipakai")
plt.barh(y_pos, y, color=warna)
plt.xlabel("Frekuensi")
plt.yticks(y_pos, bar)
plt.show()


# In[224]:


#BARCHART KATEGORI FITUR APA SAJA YANG DIPAKAI DENGAN GO-PAY

print("NOMOR 1")

GoRide_GoCar      = (data['Go-Ride / Go-Car'] == 1).sum()
GoSend            = (data['Go-Send'] == 1).sum()
GoPulsa           = (data['Go-Pulsa'] == 1).sum()
GoFood            = (data['Go-Food'] == 1).sum()
GoShop_GoMart     = (data['Go-Shop/ Go-Mart'] == 1).sum()
GoBill            = (data['Go-Bill'] == 1).sum()
GoClean_GoMassage = (data['Go-Clean / Go-Massage'] == 1).sum()
GoTix             = (data['Go-Tix'] == 1).sum()
BayarOffline      = (data['Membayar makanan di restoran/ merchant offline'] == 1).sum()


y = [GoRide_GoCar, GoSend, GoPulsa, GoFood, GoShop_GoMart, GoBill, GoClean_GoMassage, GoTix, BayarOffline]
bar = ('Go-Ride/Go-Car', 'Go-Send', 'Go-Pulsa', 'Go-Food', 'Go-Shop/Go-Mart', 'Go-Bill', 
       'Go-Clean/Go-Massage', 'Go-Tix', 'Bayar Offline')
y_pos = np.arange(len(y))
plt.title("Jumlah Pemakaian Fitur Dengan Go-Pay")
plt.xlabel("Frekuensi")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.show()


# In[81]:


#BARCHART KATEGORI 

print("NOMOR 1")

GoRide_GoCar      = (data['Go-Ride / Go-Car'] == 1).sum()
GoSend            = (data['Go-Send'] == 1).sum()
GoPulsa           = (data['Go-Pulsa'] == 1).sum()
GoFood            = (data['Go-Food'] == 1).sum()
GoTix             = (data['Go-Tix'] == 1).sum()
BayarOffline      = (data['Membayar makanan di restoran/ merchant offline'] == 1).sum()


y = [GoRide_GoCar, GoSend, GoPulsa, GoFood, GoTix, BayarOffline]
bar = ('Go-Ride/Go-Car', 'Go-Send', 'Go-Pulsa', 'Go-Food', 'Go-Tix', 'Bayar Offline')
y_pos = np.arange(len(y))
plt.title("Jumlah ")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.xlabel("Frekuensi")
plt.show()


# In[82]:


#BARCHART KATEGORI ALASAN MEMAKAI GO-PAY

print("NOMOR 1")

Promo         = (data['Promo'] == 1).sum()
Simple_Mudah  = (data['Simple, Mudah, Tidak perlu kembalian'] == 1).sum()
Dapat_GoPoint = (data['Bisa memperoleh Go-Point'] == 1).sum()
Aman          = (data['Aman'] == 1).sum()


y = [Promo, Simple_Mudah, Dapat_GoPoint, Aman]
bar = ('Promo', 'Simple, Mudah, Tidak perlu kembalian', 'Bisa memperoleh Go-Point', 'Aman')
y_pos = np.arange(len(y))
plt.title("Alasan Memakai Go-Pay")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.xlabel("Frekuensi")
plt.show()


# In[83]:


#BARCHART TERAKHIR PAKAI GO-PAY

print("NOMOR 1")

data['TERAKHIR PAKAI GOPAY'].value_counts().plot.barh()


# In[225]:


#BARCHART KATEGORI CARA TOP-UP SALDO GO-PAY

print("NOMOR 1")

Driver          = (data['Melalui driver'] == 1).sum()
Alfamart        = (data['Top up di alfamart'] == 1).sum()
Pegadaian       = (data['Melalui pegadaian'] == 1).sum()
ATM             = (data['ATM'] == 1).sum()
MobileBanking   = (data['Mobile Banking'] == 1).sum()
InternetBanking = (data['Internet Banking'] == 1).sum()
SMSBanking      = (data['SMS Banking'] == 1).sum()
LoketPPOB       = (data['Melalui loket PPOB (Payment Point Online Bank)'] == 1).sum()
TellerBank      = (data['Teller Bank'] == 1).sum()


y = [Driver, Alfamart, Pegadaian, ATM, MobileBanking, InternetBanking, SMSBanking, LoketPPOB, TellerBank]
bar = ('Driver', 'Alfamart', 'Pegadaian', 'ATM', 'Mobile Banking', 'Internet Banking', 'SMS Banking', 
       'Loket PPOB', 'Teller Bank')
y_pos = np.arange(len(y))
plt.title("Cara Top-Up Saldo Go-Pay")
plt.xlabel("Frekuensi")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.show()


# In[221]:


#BARCHART JENIS BANK YANG DIGUNAKAN KETIKA TOP-UP SALDO

print("NOMOR 1")

data['Jika menggunakan layanan bank (ATM, SMS/Mobile/Internet Banking, Teller), Mohon sebutkan nama bank !'].value_counts().plot.barh()


# In[86]:


#BARCHART SALDO SEKALI TOP-UP

print("NOMOR 1")

data['SALDO SEKALI TOP -UP'].value_counts().plot.barh()


# In[87]:


#BARCHART FREKUENSI TOP-UP GO-PAY

print("NOMOR 1")

data['Frekuensi top -up Go -Pay'].value_counts().plot.barh()


# In[88]:


#BARCHART PENGETAHUAN QR CODE

print("NOMOR 1")

data['QR CODE'].value_counts().plot.barh()


# In[89]:


#BARCHART KATEGORI PENILAIAN TERHADAP GO-PAY

print("NOMOR 1")

SangatMemuaskan = (data['Baik, sangat memuaskan'] == 1).sum()
CukupMemuaskan  = (data['Cukup memuaskan'] == 1).sum()
KurangMemuaskan = (data['Kurang memuaskan'] == 1).sum()


y = [SangatMemuaskan, CukupMemuaskan, KurangMemuaskan]
bar = ('Sangat Memuaskan', 'Cukup Memuaskan', 'Kurang Memuaskan')
y_pos = np.arange(len(y))
plt.title("Penilaian Terhadap Go-Pay")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.xlabel("Frekuensi")
plt.show()


# In[222]:


#BARCHART KATEGORI KENDALA YANG DIHADAPI KETIKA MENGGUNAKAN GO-PAY

print("NOMOR 1")

GoPayGabisa         = (data['Go-Pay tidak bisa diakses/ digunakan'] == 1).sum()
NominalBerkurang    = (data['Nominal Go-Pay berkurang tanpa digunakan untuk bertransaksi'] == 1).sum()
TopUpTidakBertambah = (data['Telah Top Up Go-Pay tapi saldo tidak bertambah'] == 1).sum()


y = [GoPayGabisa, NominalBerkurang, TopUpTidakBertambah]
bar = ('Go-Pay tidak bisa diakses/digunakan', 'Nominal Go-Pay berkurang tanpa digunakan untuk bertransaksi', 
       'Telah Top Up Go-Pay tapi saldo tidak bertambah')
y_pos = np.arange(len(y))
plt.title("Kendala Penggunaan Go-Pay")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.xlabel("Frekuensi")
plt.show()


# In[91]:


#BARCHART KATEGORI HARAPAN UNTUK GO-PAY KEDEPANNYA

print("NOMOR 1")

GoPayPerluasMerchant = (data['Go-Pay dapat digunakan lebih luas lagi untuk pembayaran merchant offline seperti di restauran, cafe, maupun toko lain'] == 1).sum()
Tol                  = (data['Dapat digunakan untuk membayar tol'] == 1).sum()
Parkir               = (data['Dapat digunakan untuk membayar parkir'] == 1).sum()
TokoOnline           = (data['Dapat digunakan untuk membayar toko online/ online marketplace'] == 1).sum()


y = [GoPayPerluasMerchant, Tol, Parkir, TokoOnline]
bar = ('Go-Pay memperluas merchant offline', 'Membayar Tol', 'Membayar Parkir', 'Membayar Toko Online')
y_pos = np.arange(len(y))
plt.title("Harapan Penggunaan Go-Pay")
plt.barh(y_pos, y, color=warna)
plt.yticks(y_pos, bar)
plt.xlabel("Frekuensi")
plt.show()


# In[115]:


#NOMOR 2

print("NOMOR 2")
print()

data['Penghasilan Perbulan'] = data['Penghasilan Perbulan'].astype('category').cat.codes
data['Frekuensi top -up Go -Pay'] = data['Frekuensi top -up Go -Pay'].astype('category').cat.codes
hub1 = data['Penghasilan Perbulan'].corr(data['Frekuensi top -up Go -Pay'])
print("Hubungan penghasilan perbulan dengan frekuensi Top Up Go-Pay yaitu = ", hub1, "(Hubungan linier sangat lemah)")

data['Penghasilan Perbulan'] = data['Penghasilan Perbulan'].astype('category').cat.codes
data['SALDO SEKALI TOP -UP'] = data['SALDO SEKALI TOP -UP'].astype('category').cat.codes
hub2 = data['Penghasilan Perbulan'].corr(data['SALDO SEKALI TOP -UP'])
print("Hubungan antara penghasilan perbulan dengan saldo sekali Top Up = ", hub2, "(tidak punya hubungan linier)")


# In[28]:


#NOMOR 3

print("NOMOR 3")

GoPay           = (data['Go-Pay'] == 1).sum()
OVO             = (data['OVO'] == 1).sum()
iSaku           = (data['iSaku'] == 1).sum()
Sakuku          = (data['Sakuku'] == 1).sum()
FlazzBCA        = (data['Flazz BCA'] == 1).sum()
Brizzi          = (data['Brizzi'] == 1).sum()
Megacash        = (data['Megacash'] == 1).sum()
EMoneyMandiri   = (data['eMoney Mandiri'] == 1).sum()
Tcash           = (data['Tcash'] == 1).sum()
ECashMandiri    = (data['E-cash Mandiri'] == 1).sum()
RekeningPonsel  = (data['Rekening ponsel'] == 1).sum()
BNITapcash      = (data['BNI Tapcash'] == 1).sum()
XLTunai         = (data['XL tunai'] == "1PENGGUNA iSAKU").sum()
Paytren         = (data['Paytren'] == 1).sum()
Jakcard         = (data['Jakcard'] == 1).sum()


y = [GoPay, OVO, iSaku, Sakuku, FlazzBCA, Brizzi, Megacash, EMoneyMandiri, Tcash, ECashMandiri, 
         RekeningPonsel, BNITapcash, XLTunai, Paytren, Jakcard]
bar = ('Go-Pay', 'OVO', 'iSaku', 'Sakuku', 'Flazz BCA', 'Brizzi', 'Megacash', 'E-Money Mandiri', 'Tcash', 'E-Cash Mandiri', 
         'Rekening Ponsel', 'BNI Tapcash', 'XL Tunai', 'Paytren', 'Jakcard')
y_pos = np.arange(len(y))
plt.title("Jumlah Kategori E-Money yang Dipakai")
plt.barh(y_pos, y, color=warna)
plt.xlabel("Frekuensi")
plt.yticks(y_pos, bar)
plt.show()

print("Dari data chart diatas, dapat dilihat bahwa E-Money yang paling banyak dipakai adalah : Go-Pay")

print(data.groupby('Go-Pay')['Go-Pay'].count())

print("Jumlah pemakai sebanyak =",(data['Go-Pay'] == 1).sum(),"orang")


# In[189]:


#NOMOR 4

print("NOMOR 4")

datatest = data.select_dtypes(include=['object']).copy()
df = datatest.loc[:,datatest.columns]=datatest.apply(lambda x : pd.factorize(x)[0])

pd.get_dummies(df)


# In[190]:


#NOMOR 5

print("Jumlah yang ada missing value :")
print()
print((df == -1).sum())


# In[191]:


#NOMOR 5

print("Cara mengatasi missing value ada 2 bisa meremove semua baris yang ada NaN atau mengisinya dengan mean")
print("Disini akan dipilih remove baris")
print()

#data missing value diganti NaN dulu
df = df.replace(-1, np.NaN)
df.dropna(inplace = True)
df


# In[215]:


#NOMOR 6

print("Distribusi dari ke 11 fitur kategorial diatas yaitu :")

for i, kolom in enumerate(df.columns):
    plt.figure(i)
    plt.grid()
    sns.distplot(df[kolom],hist=False,color='chartreuse')

