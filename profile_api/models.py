from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin , BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user Profiles """
    def create_user(self,email , name ,password=None):
        """ create a new user profile """
        if not email :
            raise ValueError('User must have an email')
        
        email = self.normalize_email(email)
        user = self.model(name=name , email=email)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self , email , name , password):
        """create as superuser"""
        user = self.create_user(email , name ,password)
        user.is_superuser = True # aitomaticaly added by PermissionsMixins
        user.is_staff =True 
        user.save(using=self._db)
        
        return user 
            
            
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for UserProfile """
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] #email automatic add by USERNAME_FIELD
    
    def getFullName(self):
        """get user full name"""
        return self.name
    
    def __str__(self):
        """return string representation for UserProfile """
        return self.email
    