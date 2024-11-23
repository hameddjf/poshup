from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

# create and manage of accounts


class MyAccountManager(BaseUserManager):
    # create the normal user
    def create_user(self, first_name, last_name, username,
                    email, password=None):
        if not email:
            raise ValueError('email address is required !!')
        if not username:
            raise ValueError('username is required !!')

        """
        Creating a new instance (user)
        using the data given as parameters to the function.
        """
        user = self.model(
            # Converts incoming email to standard format : Lowercase letters
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        """
        hashing the entering password
        / and next line /
        saving the hashed password in database
        """
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create the super user
    def create_superuser(self, first_name, last_name, email,
                         username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        # giving permission to super user
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


# Specify the specifications and behaviors of a user account
class Account(AbstractBaseUser):
    """
        in the `AbstractBaseUser` class, the `password`
        field is provided by default
        and its field name is already translated in the same class.
    """
    first_name = models.CharField(_("اسم"), max_length=50)
    last_name = models.CharField(_("نام خوانوادگی"), max_length=50)

    username = models.CharField(_("نام کاربری"), max_length=50, unique=True)
    email = models.EmailField(_("ادرس ایمیل"), max_length=254, unique=True)
    # phone_number= models.PhoneNumberField(_("شماره تماس") , unique = True)
    phone_number = models.CharField(
        _("شماره تماس"), max_length=50, unique=True, blank=True, null=True)

    # required
    # manager of account
    objects = MyAccountManager()
    date_joined = models.DateTimeField(
        _("زمان ثبت نام"), auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(
        _("اخرین ورود"), auto_now=False, auto_now_add=True)
    is_admin = models.BooleanField(
        _("کاربر مورد نظر ادمین است ؟"), default=False)
    is_staff = models.BooleanField(
        _("کاربر مورد نظر کارمند است ؟"), default=False)
    is_active = models.BooleanField(
        _("کاربر مورد نظر فعال است ؟"), default=False)
    is_superadmin = models.BooleanField(
        _("کاربر مورد نظر ادمین اصلی است ؟"), default=False)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # login with email instead user_name
    USERNAME_FIELD = 'email'
    # required fields to login
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت‌ها'

    def __str__(self):
        return self.email

    # check the user for is admin                       : its low level
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # check the permissions for specific moduls         : its low level
    def has_module_perms(self, add_label):
        return True


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(Account, verbose_name=_(
        "کاربر"), on_delete=models.CASCADE)
    address_line_1 = models.CharField(_(" ادرس تحویل"), max_length=50)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    postal_code = models.CharField(_(" کد پستی"), max_length=50)
    state = models.CharField(_(" استان"), max_length=50)
    city = models.CharField(_("شهر "), max_length=50)
    street = models.CharField(_("خیابان "), max_length=50)
    tag = models.CharField(_(" پلاک"), max_length=50)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1}'

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
