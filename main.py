from datetime import datetime
import time

print("------------Yaş Hesaplama Uygulamasına Hoş Geldiniz------------")

dogumy = int(input("Lütfen Doğum Yılınızı Giriniz: "))

print("Yaşınız Hesaplanıyor Lütfen Bekleyiniz")
time.sleep(3)

yas = datetime.now().year - dogumy

print("Yaşınız:", yas)
