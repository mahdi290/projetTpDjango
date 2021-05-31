# Generated by Django 3.2 on 2021-04-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('description', models.TextField(default='nom definie')),
                ('prix', models.DecimalField(decimal_places=3, max_digits=10)),
                ('type', models.CharField(choices=[('em', 'empballé'), ('fr', 'frais'), ('cs', 'conserver')], default='em', max_length=2)),
            ],
        ),
    ]