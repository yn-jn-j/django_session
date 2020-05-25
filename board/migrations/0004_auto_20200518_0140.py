# Generated by Django 3.0.6 on 2020-05-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200517_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='board.Tag'),
        ),
    ]