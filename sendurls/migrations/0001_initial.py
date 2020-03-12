# Generated by Django 2.2.10 on 2020-03-10 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urlinput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.IntegerField()),
                ('url_input', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('url_id',),
            },
        ),
    ]
