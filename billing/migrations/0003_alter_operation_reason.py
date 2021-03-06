# Generated by Django 4.0.1 on 2022-03-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_operation_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='reason',
            field=models.CharField(choices=[('OTHER', 'Прочее'), ('FEE', 'Абонентская плата'), ('PROMO', 'Активация промо-кода'), ('HELLO', 'Приветственный бонус'), ('PAY', 'Входящий платеж')], default='OTHER', help_text='Причина операции', max_length=5),
        ),
    ]
