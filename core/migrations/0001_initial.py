# Generated by Django 4.2.3 on 2023-08-09 19:28

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='data de atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('preço', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='preço')),
                ('estoque', models.IntegerField(verbose_name='estoque')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='produtos', variations={'thumb': (124, 124)}, verbose_name='imagem')),
            ],
            bases=('core.base',),
        ),
    ]
