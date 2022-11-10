# Generated by Django 4.1.2 on 2022-11-06 12:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('insurance', models.IntegerField(blank=True, null=True)),
                ('fuel', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CancelledOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(max_length=50, null=True)),
                ('licenceID', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('payed', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=25, null=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, null=True)),
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('question', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUpLocation', models.CharField(max_length=150, null=True)),
                ('dropLocation', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=175)),
                ('last_name', models.CharField(max_length=175)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, max_length=11, null=True)),
                ('session_token', models.CharField(default=0, max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(max_length=50, null=True)),
                ('carModel', models.CharField(max_length=70, null=True)),
                ('licenceID', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('rentNow', models.DateField(null=True)),
                ('finishNow', models.DateField(null=True)),
                ('orderDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('fullFuel', models.BooleanField(blank=True, default=False, null=True)),
                ('insurance', models.BooleanField(blank=True, default=False, null=True)),
                ('payed', models.BooleanField(default=False, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarApp.customer')),
                ('pickUP', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarApp.location')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(blank=True, null=True)),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('model', models.CharField(blank=True, max_length=120, null=True)),
                ('topSpeed', models.IntegerField(blank=True, null=True)),
                ('torque', models.IntegerField(blank=True, null=True)),
                ('horsePower', models.IntegerField(blank=True, null=True)),
                ('fuelType', models.CharField(blank=True, max_length=12, null=True)),
                ('seats', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=10, null=True)),
                ('insurance', models.IntegerField(blank=True, null=True)),
                ('tank', models.IntegerField(blank=True, null=True)),
                ('img1', models.ImageField(null=True, upload_to='')),
                ('img2', models.ImageField(null=True, upload_to='')),
                ('img3', models.ImageField(null=True, upload_to='')),
                ('img4', models.ImageField(null=True, upload_to='')),
                ('img5', models.ImageField(null=True, upload_to='')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarApp.year')),
            ],
        ),
    ]