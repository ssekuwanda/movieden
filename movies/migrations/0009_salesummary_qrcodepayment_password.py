# Generated by Django 4.0.5 on 2022-07-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_qrcodepayment_creator_alter_qrcodepayment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Sale Summary',
                'verbose_name_plural': 'Sales Summary',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movies.qrcodepayment',),
        ),
        migrations.AddField(
            model_name='qrcodepayment',
            name='password',
            field=models.CharField(default='122', max_length=100),
            preserve_default=False,
        ),
    ]
