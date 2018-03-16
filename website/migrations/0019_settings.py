# Generated by Django 2.0.3 on 2018-03-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20180315_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=32, null=True)),
                ('site_tag_line', models.CharField(blank=True, max_length=1024, null=True)),
                ('www_root', models.URLField(help_text='This is the location where your site is located.http://www.example.com', max_length=1024)),
            ],
        ),
    ]