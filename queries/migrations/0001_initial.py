# Generated by Django 4.0.2 on 2022-02-01 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField()),
                ('type', models.CharField(choices=[('O', 'Object Oreanted programming'), ('F', 'Functional programming')], max_length=300)),
                ('descripton', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('municipality', models.CharField(max_length=64)),
                ('streat', models.CharField(max_length=64)),
                ('building_number', models.IntegerField()),
                ('branch_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField(max_length=64)),
                ('joined_date', models.DateTimeField()),
                ('languages', models.ManyToManyField(to='queries.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queries.location')),
            ],
        ),
    ]