from django.db import models

# Create your models here.

class Toilets(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True,null=True, verbose_name='Изображение')
    coords1 = models.FloatField(verbose_name='Координата 1')
    coords2 = models.FloatField(verbose_name='Координата 2')

    
    class Meta:
        db_table = 'toilet'
        verbose_name = 'Туалет'
        verbose_name_plural= 'Туалеты'


    def __str__(self):
        return self.name
    

class Comments(models.Model):
    
    text = models.TextField(blank=True,null=True,verbose_name='текст')
    toilet = models.ForeignKey(to=Toilets, on_delete=models.CASCADE, verbose_name='Туалет')

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural= 'Комментарии'


    def __str__(self):
        return f'{self.toilet} comment {self.id}'