# Generated by Django 3.1 on 2022-08-20 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='despesa',
            old_name='decricao',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='receita',
            old_name='decricao',
            new_name='descricao',
        ),
    ]
