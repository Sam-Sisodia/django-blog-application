# Generated by Django 4.2.7 on 2023-11-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_share_blog_email_blog_commnet"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog_commnet",
            name="date_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="share_blog",
            name="date_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
