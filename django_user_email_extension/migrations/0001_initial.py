# Generated by Django 2.1.1 on 2018-09-08 20:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(blank=True, max_length=128, verbose_name='User Name')),
                ('first_name', models.CharField(blank=True, max_length=32, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=32, verbose_name='Last Name')),
                ('address', models.TextField(blank=True, default='', max_length=500)),
                ('city', models.CharField(blank=True, default='', max_length=30)),
                ('country', models.CharField(blank=True, default='', max_length=30)),
                ('postal_code', models.IntegerField(blank=True, default=0)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format of: '+18501234567'. Minimum 12 digits and up to 15 digits allowed.", regex='^\\+?1?\\d{12,15}$')])),
                ('linkedin', models.URLField(blank=True, max_length=255)),
                ('facebook', models.URLField(blank=True, max_length=255)),
                ('github', models.URLField(blank=True, max_length=255)),
                ('twitter', models.URLField(blank=True, max_length=255)),
                ('registration_ip', models.GenericIPAddressField(null=True, verbose_name='Registered From')),
                ('language', models.CharField(default='EN', max_length=2, verbose_name='Users Language')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Define if this user should be treated as active. ', verbose_name='Active Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(blank=True, default=None, null=True)),
                ('last_login_ip', models.GenericIPAddressField(blank=True, default=None, null=True, verbose_name='Logged in from')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='DjangoEmailVerifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified')),
                ('verification_uuid', models.UUIDField(default=uuid.uuid4, verbose_name='Unique Verification UUID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_verification_obj', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'email verifications',
                'verbose_name_plural': 'email verifications',
                'db_table': 'email_verifications',
            },
        ),
    ]
