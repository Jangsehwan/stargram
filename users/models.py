
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager


# 장고모델이 db로 쿼리를 날릴때 제공해주는 interface
# why? 일반사용자와 superuse를 생성할때 다르게 지정해줘야하기 때문에 수정필요!
class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 값입니다.')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password=None, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password=None, **extra_fields)


# Custom User생성, AbstractUser기존 필드에 phone추가
class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호', max_length=11)

    objects = UserManager()


# 확장으로 뺄수도 있어!
# class UserInfo(models.Model):
#     phone_sub = models.CharField(verbose_name='보조 전화번호', max_length=11)

#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)


# 장고의 인증시스템
# 그중심에 User객체가들어가!***
# 별도로 User객체를 만들면 안돼!!
# 항상 기존의 User객체를 사용하거나, User객체를 커스텀해서 사용하거나, 다른테이블과 관계를 지정해서 확장해서사용
