# Generated by Django 3.2.5 on 2021-07-23 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.question'),
        ),
    ]
