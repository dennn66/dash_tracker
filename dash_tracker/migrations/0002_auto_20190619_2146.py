# Generated by Django 2.2.2 on 2019-06-19 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingradient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('portions', models.DecimalField(decimal_places=1, max_digits=4)),
                ('calories', models.IntegerField()),
                ('calories_fat', models.DecimalField(decimal_places=3, max_digits=6)),
                ('total_fat', models.DecimalField(decimal_places=3, max_digits=6)),
                ('saturated_fat', models.DecimalField(decimal_places=3, max_digits=6)),
                ('monosaturated_fat', models.DecimalField(decimal_places=3, max_digits=6)),
                ('polyunsaturated_fat', models.DecimalField(decimal_places=3, max_digits=6)),
                ('cholestreol', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sodium', models.DecimalField(decimal_places=3, max_digits=6)),
                ('potassium', models.DecimalField(decimal_places=3, max_digits=6)),
                ('total_carbohydrate', models.DecimalField(decimal_places=3, max_digits=6)),
                ('dietary_fiber', models.DecimalField(decimal_places=3, max_digits=6)),
                ('sugars', models.DecimalField(decimal_places=3, max_digits=6)),
                ('protein', models.DecimalField(decimal_places=3, max_digits=6)),
                ('calcium', models.DecimalField(decimal_places=3, max_digits=6)),
                ('iron', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='IngradientName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ingradient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Ingradient')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MealName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Language')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Mesurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MesurementName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Language')),
                ('mesurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Mesurement')),
            ],
        ),
        migrations.CreateModel(
            name='OnTheDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ingradient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Ingradient')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Meal')),
                ('mesurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Mesurement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroupName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Language')),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.ProductGroup')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductTypeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Language')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MouseEvent',
        ),
        migrations.AddField(
            model_name='productgroup',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.ProductType'),
        ),
        migrations.AddField(
            model_name='ingradientname',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Language'),
        ),
        migrations.AddField(
            model_name='ingradient',
            name='mesurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.Mesurement'),
        ),
        migrations.AddField(
            model_name='ingradient',
            name='product_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash_tracker.ProductGroup'),
        ),
    ]