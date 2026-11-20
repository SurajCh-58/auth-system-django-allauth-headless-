from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError("The username field must be set.")
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff must have is_staff True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser must have is_superuser True")

        return self.create_user(username,password,**extra_fields)

class User(AbstractUser):
    first_name=None
    last_name=None

    full_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    USERNAME_FIELD="username"
    REQUIRED_FIELDS=[]
    objects=UserManager()
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image=models.ImageField(upload_to="profile_images/",blank=True,null=True)
    
