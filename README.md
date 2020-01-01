# Ekşi Sözlük Komut Satırı Arayüzü (Cli)

## Başlangıç
Bu uygulama bilgisayarınızdan Ekşi Sözlük web sitesine bağlanarak bilgi alır. Ekşi Sözlük Kullanım Koşulları'na aykırı kullanımlarda sorumluluk tarafıma ait değildir.



### Kurulum

Python kurulu değilse en yeni sürümü kurun. Sonrasında projeyi indirin:

```
git clone https://github.com/sinantan/eksi_cli.git
```

Projeyi indirdikten sonra proje kök dizinine gidin ve pip install diyerek gerekli paketleri kurun:
```
pip install
```
Gerekli paketler kurulunca kök dizin içerisinden eksi_cli klasörüne gidip:
```
pipenv run python eksi.py
```
komutu ile uygulamayı çalıştırabilirsiniz.

# Kullanım

## Komutlar:  
gundem [başlık sayısı(opsiyonel)]  
ara [başlık veya kullanıcı flagi] [başlık veya kullanıcı adı]  
  
## Ayarlar:  
    gundem:  
      başlık sayısı <int>  
    ara:  
      -b, baslik  
      -k, kullanici  
  
Örnek kullanım:   25 başlık listele
```
gundem 25
```
Örnek kullanım:   ssg adlı kullanıcıyı ara
```
ara -k ssg VEYA ara kullanici ssg
```

## Ekran Görüntüleri
![alt text](https://i.ibb.co/JdJZDt9/2.png)  
![alt text](https://i.ibb.co/QX1fcPn/2-2.png)  
![alt text](https://i.ibb.co/rQFBmbd/3.png)  

