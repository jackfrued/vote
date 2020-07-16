from django.db import models


class Subject(models.Model):
    """学科"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tb_subject'
        verbose_name = '学科'
        verbose_name_plural = '学科'


SEX_OPTIONS = (
    (True, '男'),
    (False, '女')
)


class Teacher(models.Model):
    """老师"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.BooleanField(default=True, choices=SEX_OPTIONS, verbose_name='性别')
    birth = models.DateField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    photo = models.ImageField(max_length=255, verbose_name='照片')
    good_count = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    subject = models.ForeignKey(to=Subject, on_delete=models.DO_NOTHING, db_column='sno', verbose_name='所属学科')

    class Meta:
        managed = False
        db_table = 'tb_teacher'
        verbose_name = '老师'
        verbose_name_plural = '老师'


class User(models.Model):
    """用户"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    # 用户密码在数据库中需要保存为对应的哈希摘要（签名、指纹）
    password = models.CharField(max_length=32, verbose_name='密码')
    tel = models.CharField(max_length=20, verbose_name='手机号')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    last_visit = models.DateTimeField(null=True, verbose_name='最后登录时间')

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'
