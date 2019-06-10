# Generated by Django 2.1.7 on 2019-06-07 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190531_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notifier_type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_to_user', to='api.Notification'),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_notification', to=settings.AUTH_USER_MODEL),
        ),
    ]