from django.db import models


# модели для сайта
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    image = models.ImageField(upload_to='news_images/', verbose_name="Изображение",null=True, blank=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=255, default=" ", verbose_name="Название")
    head = models.CharField(max_length=255, default=" ", verbose_name="Руководитель")
    description = models.TextField(verbose_name="Описание")
    address = models.CharField(max_length=255, default=" ", verbose_name="Адрес")
    phone = models.CharField(max_length=20, default=" ", verbose_name="Телефон")
    email = models.EmailField(default=" ", verbose_name="Email")

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Содержание")
    date = models.DateTimeField(verbose_name="Дата")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата")

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField(upload_to="partner_photos", blank=True, null=True, verbose_name="Изображение")
    url = models.URLField(verbose_name="Ссылка")

    def __str__(self):
        return self.name
