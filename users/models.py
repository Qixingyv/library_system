from django.db import models

class User(models.Model):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='登录用户名'
    )
    password = models.CharField(
        max_length=128,
        verbose_name='加密密码'
    )
    ROLE_CHOICES = (
        (0, '管理员'),
        (1, '图书管理员'),
        (2, '读者'),
    )
    role = models.SmallIntegerField(
        choices=ROLE_CHOICES,
        verbose_name='角色（0-管理员/1-图书管理员/2-读者）'
    )
    student_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name='学号/教师编号（读者必填）'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='真实姓名'
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='手机号'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='通知邮箱'
    )
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男'),
    )
    gender = models.SmallIntegerField(
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        verbose_name='性别（0-女/1-男）'
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='年龄'
    )
    hobby = models.TextField(
        null=True,
        blank=True,
        verbose_name='爱好（逗号分隔）'
    )
    is_approved = models.BooleanField(
        default=False,
        verbose_name='审核状态（0-未审核/1-已通过）'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='注册时间'
    )

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username