# Generated by Django 3.2.5 on 2021-07-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
