from django.contrib.auth.models import BaseUserManager

#custom user manger 

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User must have an email Address")
        if not username:
            raise ValueError("User must have  a username  ")
        if not first_name:
            raise ValueError("User must have name")
        
       
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        user=self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password               
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self.db)
        return user