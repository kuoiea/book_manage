from django.db import models


# Create your models here.

class Book(models.Model):
    '''
    书籍类： 书名,出版日期,是否出版,价格
    外键连接： 作者,出版社
    '''
    name = models.CharField(max_length=32,unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_pub = models.BooleanField()
    pub_date = models.DateField()

    # 与出版社表建立多(书)对一(出版社)的关系

    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)

    # 与作者表建立多对多的关系

    authors = models.ManyToManyField(to='Author',)

    def __str__(self):
        return self.name


class Author(models.Model):
    '''
    作者类：姓名,年龄
    '''
    name = models.CharField(max_length=32,unique=True)
    age = models.IntegerField()
    # 与性别表建立多对一的关系

    sex = models.ForeignKey(to='gander',on_delete=models.CASCADE)

    # 与作者详细信息表建立一对一的关系
    authorDetial = models.OneToOneField(to='AuthorDetial', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetial(models.Model):
    '''
    作者详细信息类：,电话,邮箱,详细地址
    '''
    tel = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.tel


class Publish(models.Model):
    '''
    出版社类： 出版社名称,电话,邮箱,地址.
    '''
    name = models.CharField(max_length=32,unique=True)
    tel = models.IntegerField(unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class gander(models.Model):
    '性别类'
    sex = models.CharField(max_length=32)
    # author = models.OneToOneField(to='Author',on_delete=models.CASCADE)

    def __str__(self):
        return self.sex

