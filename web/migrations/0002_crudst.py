# Generated by Django 3.2 on 2021-04-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crudst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(max_length=100)),
                ('stemail', models.CharField(max_length=100)),
                ('staddress', models.CharField(max_length=100)),
                ('stmobile', models.CharField(max_length=100)),
                ('stgender', models.CharField(max_length=100)),
            ],
        ),
    ]