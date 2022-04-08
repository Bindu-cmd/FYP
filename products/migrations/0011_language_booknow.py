# Generated by Django 4.0 on 2022-03-13 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_product_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languagename', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=255)),
                ('authorname', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('description', models.TextField()),
                ('publish_year', models.IntegerField()),
                ('pdf_file', models.FileField(upload_to='static/pdffile')),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.language')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]