# Generated by Django 4.2.4 on 2024-01-02 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_test1_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test1',
            name='id',
        ),
        migrations.AlterField(
            model_name='test1',
            name='a',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test1',
            name='b',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test1',
            name='q',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.test1'),
        ),
    ]