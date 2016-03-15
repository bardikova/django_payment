# coding: utf-8

from django.db import models

class Categorie(models.Model):
	name = models.CharField(u'Услуги', max_length=50)

	def __unicode__(self):
		return self.name

class Providers(models.Model):
	name = models.CharField(u'Наименование провайдера', max_length=20)
	img = models.ImageField(u'Логотип', upload_to='uoloads_provaider/')
	account = models.IntegerField(u'л/с провайдера', unique=True)
	description = models.TextField(u'Информация о провайдере')
	display = models.BooleanField(u'Включить/Отключить', default=False)
	categorie = models.ForeignKey(Categorie)

	def __unicode__(self):
		return self.name


# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     profile_name = models.CharField(u'Логин', max_length=30)
#     email = models.CharField(u'Email', max_length=50)
