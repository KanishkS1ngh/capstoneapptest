# Generated by Django 5.1.2 on 2024-11-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_goalplan_saved_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goalplan',
            old_name='goal_months',
            new_name='monthly_percentage',
        ),
        migrations.RenameField(
            model_name='goalplan',
            old_name='goal_amount',
            new_name='savings_goal',
        ),
        migrations.RenameField(
            model_name='goalplan',
            old_name='income',
            new_name='total_income',
        ),
        migrations.RemoveField(
            model_name='goalplan',
            name='goal_name',
        ),
        migrations.RemoveField(
            model_name='goalplan',
            name='percentage_towards_goal',
        ),
        migrations.RemoveField(
            model_name='goalplan',
            name='user',
        ),
        migrations.AddField(
            model_name='goalplan',
            name='remaining_income',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goalplan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]