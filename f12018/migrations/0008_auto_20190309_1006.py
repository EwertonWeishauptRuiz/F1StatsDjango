# Generated by Django 2.1.5 on 2019-03-09 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f12018', '0007_auto_20190213_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_nationality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='f12018.Country'),
        ),
    ]
