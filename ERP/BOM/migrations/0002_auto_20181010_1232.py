# Generated by Django 2.1.1 on 2018-10-10 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOM', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='name',
            new_name='nameforn',
        ),
        migrations.RenameField(
            model_name='matp',
            old_name='name',
            new_name='namemp',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='name',
            new_name='namep',
        ),
    ]
