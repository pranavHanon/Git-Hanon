# Generated by Django 4.2.4 on 2024-01-04 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0022_remove_product_program_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('cage_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('cage_name', models.CharField(max_length=20, unique=True)),
                ('number_of_duts', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chamber',
            fields=[
                ('chamber_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('chamber_name', models.CharField(max_length=20, unique=True)),
                ('cooling_type', models.CharField(max_length=20, null=True)),
                ('power', models.SmallIntegerField(null=True)),
                ('humidity', models.BooleanField(null=True)),
                ('operation_team', models.CharField(max_length=20, null=True)),
                ('working_condition', models.SmallIntegerField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=20, null=True)),
                ('heating_power', models.SmallIntegerField()),
                ('cooling_power', models.SmallIntegerField()),
                ('heating_gradient', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DAR',
            fields=[
                ('dar_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('dar_name', models.CharField(max_length=20, unique=True)),
                ('ac_input_voltage', models.SmallIntegerField(null=True)),
                ('ac_input_phase', models.CharField(max_length=20, null=True)),
                ('operation_team', models.CharField(max_length=20, null=True)),
                ('working_condition', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DARChannel',
            fields=[
                ('channel_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('channel_number', models.SmallIntegerField(null=True)),
                ('power_supply_type', models.CharField(max_length=20, null=True)),
                ('power_supply_voltage', models.SmallIntegerField(null=True)),
                ('max_current', models.SmallIntegerField(null=True)),
                ('lin', models.BooleanField(null=True)),
                ('pwn', models.BooleanField(null=True)),
                ('can', models.BooleanField(null=True)),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar')),
            ],
        ),
        migrations.CreateModel(
            name='DUT',
            fields=[
                ('dut_name', models.CharField(max_length=12, unique=True)),
                ('received_date', models.DateField(null=True)),
                ('storage_date', models.DateField(null=True)),
                ('storage_bin', models.CharField(max_length=20, null=True)),
                ('dut_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fluid',
            fields=[
                ('fluid_name', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(max_length=20, null=True)),
                ('storage_location', models.CharField(max_length=20, null=True)),
                ('fluid_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Harness',
            fields=[
                ('harness_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('harness_name', models.CharField(max_length=50, unique=True)),
                ('storage_location', models.CharField(max_length=20, null=True)),
                ('test_screening_resutl', models.BooleanField(null=True)),
                ('harness_connector_condition', models.BooleanField(null=True)),
                ('insulation_condition', models.BooleanField(null=True)),
                ('rtv_condition', models.BooleanField(null=True)),
                ('dunk_testing', models.BooleanField(null=True)),
                ('average_resistance', models.FloatField(null=True)),
                ('comments', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_name', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=15, null=True)),
                ('supervisor', models.CharField(max_length=25, null=True)),
                ('lab_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('laptop_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('laptop_name', models.CharField(max_length=20, unique=True)),
                ('brand', models.CharField(max_length=20, null=True)),
                ('mac_address', models.CharField(max_length=30, null=True)),
                ('system_type', models.CharField(max_length=20, null=True)),
                ('ram_slot1', models.SmallIntegerField(null=True)),
                ('ram_slot2', models.SmallIntegerField(null=True)),
                ('total_ram', models.SmallIntegerField(null=True)),
                ('ram_limit', models.SmallIntegerField(null=True)),
                ('ram_type', models.CharField(max_length=20, null=True)),
                ('ram_upgrade_date', models.DateField(null=True)),
                ('mfg_year', models.SmallIntegerField(null=True)),
                ('model', models.CharField(max_length=30, null=True)),
                ('model_number', models.CharField(max_length=30, null=True)),
                ('serial_number', models.CharField(max_length=30, null=True)),
                ('operating_system', models.CharField(max_length=20, null=True)),
                ('keyboard_cover', models.BooleanField(null=True)),
                ('comments', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_name', models.CharField(max_length=50, null=True, unique=True)),
                ('status', models.SmallIntegerField(null=True)),
                ('phase', models.SmallIntegerField(null=True)),
                ('enterproj_id', models.IntegerField(null=True)),
                ('wbs_number', models.CharField(max_length=30, null=True)),
                ('oem', models.CharField(max_length=20, null=True)),
                ('program_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill', models.CharField(max_length=25, unique=True)),
                ('skill_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('technician_name', models.CharField(max_length=30)),
                ('technician_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('lab_id', models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('scheduling', models.SmallIntegerField(null=True)),
                ('status', models.SmallIntegerField(null=True)),
                ('started_start', models.DateField(null=True)),
                ('targeted_end', models.DateField(null=True)),
                ('supervisor_comments', models.CharField(max_length=4000, null=True)),
                ('hours_planned', models.SmallIntegerField(null=True)),
                ('setup_date', models.DateField(null=True)),
                ('cage_id', models.ForeignKey(db_column='cage_id', on_delete=django.db.models.deletion.CASCADE, to='database.cage')),
                ('chamber_id', models.ForeignKey(db_column='chamber_id', on_delete=django.db.models.deletion.CASCADE, to='database.chamber')),
                ('channel_id', models.ForeignKey(db_column='channel_id', on_delete=django.db.models.deletion.CASCADE, to='database.darchannel')),
                ('lab_id', models.ForeignKey(db_column='lab_id', on_delete=django.db.models.deletion.CASCADE, to='database.lab')),
                ('technician_id', models.ForeignKey(db_column='technician_id', on_delete=django.db.models.deletion.CASCADE, to='database.technician')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('test_type_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestMap',
            fields=[
                ('test_map_name', models.CharField(max_length=30, null=True)),
                ('tr', models.CharField(max_length=14, null=True, unique=True)),
                ('test_map_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Harness',
            fields=[
                ('date', models.DateField(null=True)),
                ('circuit_number', models.SmallIntegerField(null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('harness_id', models.ForeignKey(db_column='harness_id', on_delete=django.db.models.deletion.CASCADE, to='database.harness')),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test')),
            ],
        ),
        migrations.CreateModel(
            name='Test_DUT',
            fields=[
                ('date', models.DateField(null=True)),
                ('circuit_number', models.SmallIntegerField(null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dut_id', models.ForeignKey(db_column='dut_id', on_delete=django.db.models.deletion.CASCADE, to='database.dut')),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Chamber',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('chamber_id', models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.chamber')),
                ('test_type_id', models.ForeignKey(db_column='test_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.testtype')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='test_map_id',
            field=models.ForeignKey(db_column='test_map_id', on_delete=django.db.models.deletion.CASCADE, to='database.testmap'),
        ),
        migrations.AddField(
            model_name='test',
            name='test_type_id',
            field=models.ForeignKey(db_column='test_type_id', on_delete=django.db.models.deletion.CASCADE, to='database.testtype'),
        ),
        migrations.CreateModel(
            name='Technician_Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_id', models.ForeignKey(db_column='skill_id', on_delete=django.db.models.deletion.CASCADE, to='database.skill')),
                ('technician_id', models.ForeignKey(db_column='technician_id', on_delete=django.db.models.deletion.CASCADE, to='database.technician')),
            ],
        ),
        migrations.CreateModel(
            name='Program_Fluid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fluid_id', models.ForeignKey(db_column='fluid_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.fluid')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program')),
            ],
        ),
        migrations.CreateModel(
            name='Program_DAR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program')),
            ],
        ),
        migrations.CreateModel(
            name='Program_Cage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cage_id', models.ForeignKey(db_column='cage_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.cage')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_family', models.CharField(max_length=10, null=True)),
                ('platform', models.CharField(max_length=15, null=True)),
                ('communication_protocol', models.CharField(max_length=15, null=True)),
                ('voltage', models.CharField(max_length=3, null=True)),
                ('variant', models.CharField(max_length=30, null=True)),
                ('product_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program')),
            ],
        ),
        migrations.AddField(
            model_name='dut',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.product'),
        ),
        migrations.CreateModel(
            name='DAR_Laptop',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('laptop_id1', models.SmallIntegerField(null=True)),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar')),
                ('laptop_id', models.ForeignKey(db_column='laptop_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.laptop')),
            ],
        ),
        migrations.AddField(
            model_name='dar',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab'),
        ),
        migrations.CreateModel(
            name='ChamberLogInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pretest_inspection_and_photo', models.BooleanField(null=True)),
                ('setup_photo', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('system_pressure', models.FloatField(null=True)),
                ('voltage', models.FloatField(null=True)),
                ('system_restriction_target', models.CharField(max_length=50, null=True)),
                ('system_restriction_record', models.BooleanField(null=True)),
                ('trial_run_record_and_process', models.BooleanField(null=True)),
                ('special_requirements', models.CharField(max_length=300, null=True)),
                ('chamber_id', models.ForeignKey(db_column='chameber_id', on_delete=django.db.models.deletion.CASCADE, to='database.chamber')),
                ('program_id', models.ForeignKey(db_column='program_id', on_delete=django.db.models.deletion.CASCADE, to='database.program')),
                ('technician_id', models.ForeignKey(db_column='technician_id', on_delete=django.db.models.deletion.CASCADE, to='database.technician')),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test')),
            ],
        ),
        migrations.CreateModel(
            name='ChamberLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('circuit_number', models.SmallIntegerField()),
                ('total_hours', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('fluid_temp', models.FloatField(null=True)),
                ('ambient_temp', models.FloatField(null=True)),
                ('system_pressure', models.FloatField(null=True)),
                ('lin_speed', models.FloatField(null=True)),
                ('voltage', models.FloatField(null=True)),
                ('current', models.FloatField(null=True)),
                ('head', models.FloatField(null=True)),
                ('comments', models.CharField(max_length=300)),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test')),
            ],
        ),
        migrations.AddField(
            model_name='chamber',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab'),
        ),
    ]