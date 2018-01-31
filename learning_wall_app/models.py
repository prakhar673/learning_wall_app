from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist



class UserManager(BaseUserManager):
	def create_user(self, username,password=None):
		"""
		Creates and saves a User with the given username
		 and password.
		"""
		if not username:
			raise ValueError('Users must have an username')

		user = self.model(username=self.normalize_username(username),)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_moderator(self, username, password=None):
		"""
		Creates and saves a staff user with the given username
		 and password.
		"""
		user = self.create_user(username,password=password)
		user.moderator = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	username = models.CharField(max_length=255,unique=True)
	name = models.CharField(max_length=25,default='')
	moderator = models.BooleanField(default=False) 
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [] # username & Password are required by default.

	def get_name(self):
		# The user is identified by their username
		return self.username

	def __str__(self):              # __unicode__ on Python 2
		return self.username


	@property
	def is_moderator(self):
		"Is the user a member of moderator"
		return self.moderator
		
	objects = UserManager()

	   


class Posts(models.Model):
	id = models.AutoField(primary_key=True,max_length=200)
	body = models.CharField('body of the post', max_length=250)
	time = models.DateTimeField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	likes =models.ManyToManyField(User,related_name='likes')
	moderated= models.BooleanField(default=False) 

	class Meta:
		db_table='posts'