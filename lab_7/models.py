from django.db import models
from django.contrib.auth.models import AbstractUser

class GroupModel (models.Model):
    group_name = models.CharField(max_length=20, unique=True)  #музыкальная группа
    base_date = models.DateField()
    genre = models.CharField(max_length=255)

    def __str__(self):
        return str(self.group_name)

class MembershipModel (models.Model): #членство
    membership_num = models.IntegerField(unique=True)
    join_date = models.DateField()
    out_date = models.DateField()
    group = models.ForeignKey('GroupModel', null=True)


class MemberModel (models.Model):
    membership_num = models.ForeignKey('MembershipModel', null=True)
    member_name = models.CharField(max_length=20)
    member_surname = models.CharField(max_length=20)
    member_thirdname = models.CharField(max_length=20)
    member_bdate = models.DateField()

    def __str__(self):
        return str(self.member_name)

class User(AbstractUser):
    phone = models.CharField(max_length=15, default='')
    adress = models.TextField(verbose_name='Адрес', default='')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
