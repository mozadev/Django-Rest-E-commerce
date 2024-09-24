from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin       
from simple_history.models import HistoricalRecords



class UserManager(BaseUserManager):
    def _create_user(self, username, email,name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password,False, False, **extra_fields)
    
    def create_superuser(self,username,email,name,last_name, password = None,**extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Name de User',unique = True, max_length=100)
    email = models.EmailField('Email', max_length=254,unique = True)
    name = models.CharField('name', max_length=200, blank = True, null = True)
    last_name = models.CharField('Last Name', max_length=200,blank = True, null = True)
    #rol = models.ForeignKey(Rol, on_delete=models.CASCADE,blank = True,null = True)
    image = models.ImageField('Image of Profile', upload_to='profile/', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name', 'last_name']

    def natural_key(self):
        return (self.username)
    
    def __str__(self):
        return f'{self.name},{self.last_name},{self.username}'


    