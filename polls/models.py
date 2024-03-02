from django.db import models
from django.urls import reverse

class Kategory(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    kategory_name = models.CharField(max_length=250, verbose_name='Kateqoriya adı')
    kat_url = models.CharField(max_length=250, verbose_name='Kateqoriya yolu (url)')

    def __str__(self):
        return self.kategory_name

    def get_absolute_url(self):
        return reverse('polls:categories', kwargs={'page_slug':self.kat_url})


class News(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    kat_id = models.ForeignKey(Kategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Başlıq')
    body = models.TextField(verbose_name='Mətin qismi')
    picture = models.ImageField(upload_to='img',blank=True,verbose_name='Şəkil')
    created_at = models.DateTimeField(verbose_name='İndiki vaxt')

    def __str__(self):
        return self.title


