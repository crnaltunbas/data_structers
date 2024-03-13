#  Veri yapılarına giriş ve Hızlı özet

#  Sayılar : integer
y = 5
type(y)

#  Sayılar : float
x=10.3
type(x)

#  Sayılar : complex
z= 4j + 1
type(z)

#  String
x = "Hello ai era"
type(x)

#  Boolean
True
False
type(True)
5 == 5
5 ==100
type(5==100)

#  Liste
x = ["btc", "eth", "xrp"]
type(x)

#  Sözlük (Dictionary)
x = {"name":"Ceren", "Age": 22}
type(x)

#  Tuple (Demet)
x = ("python", "ml", "ds")
type(x)

#  Set (Kümeler olarak düşünülebilir)
x ={"python", "ml", "ds"}
type(x)
#  Sözlüklerden tek farkı ,key- value durumu, iki nokta kullanımı yoktur.

#  Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections(Arrays) olarak geçmektedir.

#  Sayılar(Numbers): int, float, complex

a = 3.5
b = 10
a * 10
b / 2
b ** 3
#  **işlemi ile kübü alınması sağlandı.

#  Tipleri değiştirmek: Yani float verisini integera veya tam tersi işlem için  yukarıda a yı float olarak tanımlamış
#  bunu integera çevirmek için
int(a)
float(b)

#  Karakter dizileri (Strings)
#  Çift tırnak kullanmakla tek tırnak kullanmak ayı göreve sahiptir.

print("John")
print('John')
"John"
name =  "John"
#  print() fonksiyonu ekrana bir bilgi paylaşmak istediğimizde genellikle kullanılır.

#  Çok Satırlı Karakter Dizileri
#  3 tane tek tırnağın veya 3tane çift tırnağın arasına  dizinizi girdiğinizde bunu çok satırlı karakter dizileri olarak
#  algılayacaktır.

""" Selam!
 Veri yapıları modülüne hoşgeldin
 Umarım senin için yararlı olur
 :) """

#  Veya bu karakter dizinine değişken olarak atayabilirisiniz
long_string = """ Selam!
 Veri yapıları modülüne hoşgeldin
 Umarım senin için yararlı olur
 :) """

#  Karakter Dizilerinin Elemanlarına Erişmek
#  Yukarıda name isimli bir string tanımlamıştık bunun içinden herhangi bir harfini veya birinci harfini sormak
#  istiyorsak bunu aşağıdaki gibi gösterebiliriz:Python köşeli parantezi index olarak algılar.

name
name[0]

#  Karakter Dizilerinde Slice İşlemi

#  name değişkeninde 0. ile 2. arasındaki değerlerine erişmek istersek aşağıdaki gibi komutlandırmalıyız.

name[0:2]
#  0 dan başla2 ye kadar git

long_string[0:14]


#  String İçerisinde Karakter Sorgulamak

#  python case sensetive bir yazılım dilidir. Bu yüzden büyük-küçük harf önem taşır. Herhangi bir string içerisinde bir
#  karakter var mı yok mu anlamak için aşağıdaki komutlar kullanılır.
"veri" in long_string
#  çıktısı false olur çünkü küçük harfle yazdık.
"Veri" in long_string
#  çıktısı true olur.



