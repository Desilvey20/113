# Generated by Django 4.0.6 on 2022-07-21 02:51

from django.db import migrations

from articles.models import Status


def populate_status(apps, schemaeditor):
    status = {
        "Published": "Content that is displayed on the site",
        "Pending Review": "Content that has not yet been validated by an editor",
        "Revision Requested": "Content that requires modifications based on an editorial review",
        "Denied": "Content that will not be displayed on the site",
        "Draft": "A work in progress",
    }
    Status = apps.get_model("articles", "Status")
    for name, desc in status.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_status_article_status'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]
