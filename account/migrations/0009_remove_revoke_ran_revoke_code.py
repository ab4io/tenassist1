# Generated by Django 4.2.1 on 2023-06-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_revoke_code_alter_revoke_ran'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revoke',
            name='ran',
        ),
        migrations.AddField(
            model_name='revoke',
            name='code',
            field=models.CharField(default='381348', max_length=6),
        ),
    ]
