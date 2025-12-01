from django.contrib.auth.models import BaseUserManager
from polymorphic.managers import PolymorphicManager


class UserManager(BaseUserManager,PolymorphicManager):

     def create_user(self,national_id,password=None,**extrafields):
          if not national_id:
               raise ValueError("user must have national_id")
          
          user = self.model(
               national_id=national_id,
               **extrafields
          )
          user.set_password(password)
          user.save(using=self._db)
          return user
     
     def create_superuser(self,national_id,password=None,**extrafields):
          extrafields.setdefault('is_active',True)
          extrafields.setdefault('is_staff',True)
          extrafields.setdefault('is_superuser',True)

          return self.create_user(national_id,password,**extrafields)
     