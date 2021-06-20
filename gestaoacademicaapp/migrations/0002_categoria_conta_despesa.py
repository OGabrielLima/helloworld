# Generated by Django 2.2.19 on 2021-05-26 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestaoacademicaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaocategoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoconta', models.CharField(max_length=100)),
                ('descricaobanco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valordespesa', models.CharField(max_length=10)),
                ('descricaodespesa', models.CharField(max_length=100)),
                ('datacriacaodespesa', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pago', 'Pago'), ('pendente', 'Pendente')], max_length=11)),
                ('categoriadespesa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestaoacademicaapp.Categoria', verbose_name='Categoria')),
                ('contadespesa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestaoacademicaapp.Conta', verbose_name='Conta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]