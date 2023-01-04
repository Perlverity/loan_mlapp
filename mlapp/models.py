from django.db import models
from datetime import date


# Create your models here.
# テーブルの中を定義
class Customer(models.Model):
    # 左: DBか格納 右: UI表表示
    education_options = (
        (1, 'graduate_school'),
        (2, 'university'),
        (3, 'high_school'),
        (4, 'other'),
    )

    marriage_options = (
        (1, 'married'),
        (2, 'single'),
        (3, 'others')
    )

    # DBのカラムに相当する部分の定義
    id = models.AutoField(primary_key=True)
    last_name = models.CharField('名字', max_length=30)
    first_name = models.CharField('名前', max_length=30)
    limit_balance = models.IntegerField('残高', default=100000)
    education = models.IntegerField('学歴', choices=education_options, default=0)
    marriage = models.IntegerField('結婚歴', choices=marriage_options, default=0)
    age = models.IntegerField('年齢')
    result = models.IntegerField(blank=True, null=True)
    proba = models.FloatField(default=0.0)
    comment = models.CharField(max_length=200, blank=True, null=True)
    registered_date = models.DateField(default=date.today())

    # 管理画面に表示方法を定義
    def __str__(self):
        if self.proba == 0.0:
            return '%s, %s' % (self.registered_date.strftime('%Y-%m-%d'), self.last_name + self.first_name)
        else:
            return '%s, %s, %d, %s' % (self.registered_date.strftime('%Y-%m-%d'), self.last_name + self.first_name, self.result, self.comment)
