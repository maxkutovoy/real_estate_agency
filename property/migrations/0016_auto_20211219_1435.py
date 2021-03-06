# Generated by Django 2.2.24 on 2021-12-19 11:35

from django.db import migrations


def move_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner, defaults={
            'owners_phonenumber': flat.owners_phonenumber,
            'owner_pure_phone': flat.owner_pure_phone,

        })


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20211219_1434'),
    ]

    operations = [
        migrations.RunPython(move_owners)
    ]
