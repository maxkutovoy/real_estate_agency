# Generated by Django 2.2.24 on 2021-12-19 14:13

from django.db import migrations


def add_owne_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(owner=flat.owner)
        owner[0].own_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20211219_1435'),
    ]

    operations = [
        migrations.RunPython(add_owne_flats)
    ]
