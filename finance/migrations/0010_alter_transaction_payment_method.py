# Generated by Django 4.2.13 on 2024-06-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_transaction_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(choices=[('EFECTIVO', 'Efectivo'), ('BANCO', 'Cuenta de Banco'), ('CRIPTO', 'Criptomonedas')], default='EFECTIVO', max_length=10),
        ),
    ]