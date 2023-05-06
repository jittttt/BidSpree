from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200816_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
