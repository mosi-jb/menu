from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=48, db_index=True, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    title = models.CharField(max_length=48, db_index=True, verbose_name='عنوان')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='product')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ایتم"
        verbose_name_plural = "ایتم ها"
