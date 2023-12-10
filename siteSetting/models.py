from django.db import models


# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=48, verbose_name='عنوان')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT, verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری ها"


class Header(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    site_logo = models.ForeignKey('media.Image', on_delete=models.PROTECT, verbose_name='لوگو')

    class Meta:
        verbose_name = 'header'
        verbose_name_plural = 'headers'

    def __str__(self):
        return self.site_name


class Footer(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_image = models.ForeignKey('media.Image', on_delete=models.PROTECT, verbose_name='تصویر')
    map = models.CharField(max_length=200, verbose_name='نقشه')

    class Meta:
        verbose_name = ' footer'
        verbose_name_plural = 'footers'

    def __str__(self):
        return self.title
