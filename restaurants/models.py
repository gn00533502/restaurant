#!/usr/bin/env python
# encoding: utf-8

#所有模型繼承自django.db.models.Model類別
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        """
        :returns: name string

        """
        return self.name


class Food(models.Model):
    #max_length限制資料長度
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    #blank 表示允許資料留空
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    #資料表關聯性的概念
    #表示多種食物對應到一家餐聽的概念(Many-to-one)
    restaurant = models.ForeignKey(Restaurant)

    def __unicode__(self):
        """
        :returns: name string

        """
        return self.name

    class Meta:

        """Meta: attribute, options"""

        ordering = ['price']

class Comment(models.Model):
    content = models.CharField(max_length=255)
    visitor = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant)

