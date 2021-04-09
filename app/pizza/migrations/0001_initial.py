# Generated by Django 3.0.6 on 2021-04-09 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pizza.models.managers.likes
import pizza.models.managers.pizza
import pizza.models.managers.pizzeria
import pizza.models.validators.likes
import pizza.models.validators.pizza
import pizza.models.validators.pizzeria


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('address', models.CharField(max_length=512, verbose_name='Address')),
                ('phone', models.CharField(max_length=40, verbose_name='Phone')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Update')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Pizzeria',
                'verbose_name_plural': 'Pizzerias',
                'ordering': ['name'],
                'get_latest_by': 'id',
            },
            bases=(models.Model, pizza.models.validators.pizzeria.Validator, pizza.models.managers.pizzeria.Manager),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.CharField(max_length=240, verbose_name='Description')),
                ('thumbnail_url', models.URLField(blank=True, null=True, verbose_name='Photo URL')),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Update')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Pizzeria', verbose_name='Pizzeria')),
            ],
            bases=(models.Model, pizza.models.validators.pizza.Validator, pizza.models.managers.pizza.Manager),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Pizza', verbose_name='Pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            bases=(models.Model, pizza.models.validators.likes.Validator, pizza.models.managers.likes.Manager),
        ),
    ]