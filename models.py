from django.db import models


class MainMenu(models.Model):
    id         = models.PositiveSmallIntegerField(primary_key=True)
    name       = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table     = 'main_menus'
        verbose_name = 'main_menus_table'


class FirstCategory(models.Model):
    id           = models.PositiveSmallIntegerField(primary_key=True)
    name         = models.CharField(max_length=12, unique=True)
    index_number = models.PositiveSmallIntegerField()
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table     = 'first_category'
        verbose_name = 'first_category_table'
        ordering     = ['index_number']


class SecondCategory(models.Model):
    id           = models.PositiveSmallIntegerField(primary_key=True)
    name         = models.CharField(max_length=20, unique=True)
    index_number = models.PositiveSmallIntegerField()
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table     = 'second_category'
        verbose_name = 'second_category_table'
        ordering     = ['index_number']


class ThirdCategory(models.Model):
    id           = models.PositiveSmallIntegerField(primary_key=True)
    name         = models.CharField(max_length=20, unique=True)
    index_number = models.PositiveSmallIntegerField()
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'third_category'
        verbose_name = 'third_category_table'
        ordering = ['index_number']
