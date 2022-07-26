# Generated by Django 4.0.5 on 2022-07-11 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('cursos', '0006_autor_curso_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=256, null=True, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('curso', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='aulas',
                    to='cursos.curso')
                 ),
            ],
        ),
    ]
