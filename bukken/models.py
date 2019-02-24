from django.db import models

class Bukken_Itiran(models.Model):
    タイトル = models.CharField(max_length=100)
    公開日 = models.DateField()
    住所 = models.CharField(max_length=100)
    都道府県 = models.CharField(max_length=100)
    市区町村 = models.CharField(max_length=100)
    地名_俗名 = models.CharField(max_length=100)
    面積 = models.CharField(max_length=100)
    間取り = models.CharField(max_length=100)
    取引物件_土地_建物 = models.CharField(max_length=100)
    取引形態_売買_賃貸 = models.CharField(max_length=100)
    取引態様_媒介_代理_自己取引 = models.CharField(max_length=100)
    写真1 = models.ImageField(upload_to='image/')
    紹介文 = models.TextField()
    