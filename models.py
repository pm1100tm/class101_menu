from django.db import models


class MainMenu(models.Model):
    id         = models.PositiveSmallIntegerField(primary_key=True)
    name       = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table     = 'main_menus'
        verbose_name = 'main_menus_table'
        ordering     = ['id']


class FirstCategory(models.Model):
    id           = models.PositiveSmallIntegerField(primary_key=True)
    name         = models.CharField(max_length=12, unique=True)
    index_number = models.PositiveSmallIntegerField()
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table     = 'first_category'
        verbose_name = 'first_category_table'
        ordering     = ['index_number']


class SecondCategory(models.Model):
    id             = models.PositiveSmallIntegerField(primary_key=True)
    name           = models.CharField(max_length=20, unique=True)
    index_number   = models.PositiveSmallIntegerField()
    is_deleted     = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    first_category = models.ForeignKey('FirstCategory', related_name="first_category", on_delete=models.CASCADE)

    class Meta:
        db_table     = 'second_category'
        verbose_name = 'second_category_table'
        ordering     = ['index_number']


class ThirdCategory(models.Model):
    id              = models.PositiveSmallIntegerField(primary_key=True)
    name            = models.CharField(max_length=20)
    index_number    = models.PositiveSmallIntegerField()
    is_deleted      = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    second_category = models.ForeignKey('SecondCategory', related_name="second_category", on_delete=models.CASCADE)

    class Meta:
        db_table = 'third_category'
        verbose_name = 'third_category_table'
        ordering = ['index_number']
