# Generated by Django 4.2.1 on 2023-06-05 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_conversation_id_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]