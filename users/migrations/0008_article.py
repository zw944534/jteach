# Generated by Django 3.2.7 on 2022-03-15 14:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220313_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unique Id for this table', primary_key=True, serialize=False)),
                ('src', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('pic', models.ImageField(default='default.jpg', upload_to='article_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='users.product')),
            ],
        ),
    ]
