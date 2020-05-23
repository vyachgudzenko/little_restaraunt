# Generated by Django 3.0.1 on 2020-05-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_room', '0003_dish_small_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('type', models.CharField(choices=[('Chef', 'Chef'), ('Su Chef', 'Su Chef'), ('Pizza Maker', 'Pizza Maker'), ('Confectioner', 'Confectioner')], max_length=200, verbose_name='Type')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('img', models.ImageField(upload_to='chefs/', verbose_name='Image')),
                ('status', models.BooleanField(verbose_name='Status')),
            ],
        ),
    ]