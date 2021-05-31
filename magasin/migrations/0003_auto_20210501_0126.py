# Generated by Django 3.2 on 2021-05-01 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_produit_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiere', models.CharField(max_length=100)),
                ('couleur', models.CharField(choices=[('bl', 'blanc'), ('rg', 'rouge'), ('ble', 'bleur'), ('vr', 'vert'), ('muli', 'multicolore')], default='Transparent', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='emballage',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.emballage'),
        ),
    ]
