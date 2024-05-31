# Generated by Django 4.2.4 on 2024-05-30 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_remove_product_created_remove_program_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='dut',
            name='pedigree',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cage',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cage',
            name='number_of_duts',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cage',
            name='product',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='billing_category',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='cooling_power',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='cooling_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='currency',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='heating_gradient',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='heating_power',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='humidity',
            field=models.CharField(max_length=3, null=True, verbose_name='Humidity'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab'),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='max_daily_hours',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='operation_team',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='power',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='working_condition',
            field=models.CharField(max_length=50, null=True, verbose_name='Working Condition'),
        ),
        migrations.AlterField(
            model_name='chamberlog',
            name='cage_id',
            field=models.ForeignKey(db_column='cage_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.cage', verbose_name='Cage'),
        ),
        migrations.AlterField(
            model_name='chamberlog',
            name='comments',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='chamberlog',
            name='dar_id',
            field=models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR'),
        ),
        migrations.AlterField(
            model_name='chamberlog',
            name='shaker_direction',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chamberlog',
            name='status',
            field=models.CharField(max_length=20, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='chamberlog',
            name='technician',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='chamber_id',
            field=models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.chamber', verbose_name='Chamber'),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='chamber_profile',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='comments',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='coolant',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='pretest_inspection_and_photo',
            field=models.CharField(max_length=10, null=True, verbose_name='Pretest Inspection and Photo'),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='pump_profile',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='setup_photo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='shaker_profile',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='special_requirements',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='system_pressure',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='system_restriction_record',
            field=models.CharField(max_length=10, null=True, verbose_name='System Restriction Record'),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='system_restriction_target',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='technician_id',
            field=models.ForeignKey(db_column='technician_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.technician', verbose_name='Technician'),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='test_profile',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='trial_run_record_and_process',
            field=models.CharField(max_length=10, null=True, verbose_name='Trial Run Record And Process'),
        ),
        migrations.AlterField(
            model_name='chamberloginfo',
            name='voltage',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dar',
            name='ac_input_phase',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dar',
            name='ac_input_voltage',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dar',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab', verbose_name='Lab'),
        ),
        migrations.AlterField(
            model_name='dar',
            name='operation_team',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dar',
            name='working_condition',
            field=models.CharField(max_length=50, null=True, verbose_name='Working Condition'),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='can',
            field=models.CharField(max_length=50, null=True, verbose_name='CAN'),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='channel_number',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='dar_id',
            field=models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR'),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='eCF',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='eTMOP',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='eWP_Med_Aux',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='eWP_Primary',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='lin',
            field=models.CharField(max_length=50, null=True, verbose_name='LIN'),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='max_current_12V',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='max_current_48V',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='number_of_duts',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='power_supply_12V',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='power_supply_48V',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='power_supply_model',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='power_supply_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='pressure_transducer_inlet',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='pressure_transducer_outlet',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='darchannel',
            name='pwn',
            field=models.CharField(max_length=50, null=True, verbose_name='PWN'),
        ),
        migrations.AlterField(
            model_name='dut',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.product', verbose_name='Product name'),
        ),
        migrations.AlterField(
            model_name='dut',
            name='received_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='dut',
            name='storage_bin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dut',
            name='storage_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fluid',
            name='manufacturer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fluid',
            name='storage_location',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='harness',
            name='average_resistance',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='harness',
            name='dunk_testing',
            field=models.CharField(max_length=4, null=True, verbose_name='Dunk Testing'),
        ),
        migrations.AlterField(
            model_name='harness',
            name='harness_connector_condition',
            field=models.CharField(max_length=4, null=True, verbose_name='Harness Connector Condition'),
        ),
        migrations.AlterField(
            model_name='harness',
            name='insulation_condition',
            field=models.CharField(max_length=4, null=True, verbose_name='Insulation Condition'),
        ),
        migrations.AlterField(
            model_name='harness',
            name='rtv_condition',
            field=models.CharField(max_length=4, null=True, verbose_name='RTV Condition'),
        ),
        migrations.AlterField(
            model_name='harness',
            name='storage_location',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='harness',
            name='test_screening_result',
            field=models.CharField(max_length=4, null=True, verbose_name='Test Screening Result'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='country',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='lab_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='supervisor',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='comments',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='dar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.dar', verbose_name='DAR'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='keyboard_cover',
            field=models.CharField(max_length=3, null=True, verbose_name='Keyboard Cover'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='mac_address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='mfg_year',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='model',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='model_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='operating_system',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='processor_type',
            field=models.SmallIntegerField(null=True, verbose_name='Processor Type (32 or 64)'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram_slot1',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram_slot2',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram_upgrade_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='serial_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='system_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='teamviewer_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='total_ram',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='communication_protocol',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='platform',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_family',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='voltage',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='enterproj_id',
            field=models.CharField(max_length=10, null=True, verbose_name='EnterProj ID'),
        ),
        migrations.AlterField(
            model_name='program',
            name='oem',
            field=models.CharField(max_length=20, null=True, verbose_name='OEM'),
        ),
        migrations.AlterField(
            model_name='program',
            name='phase',
            field=models.CharField(max_length=10, null=True, verbose_name='Phase'),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='program',
            name='status',
            field=models.CharField(max_length=20, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='program',
            name='wbs_number',
            field=models.CharField(max_length=30, null=True, verbose_name='WBS'),
        ),
        migrations.AlterField(
            model_name='program_cage',
            name='cage_id',
            field=models.ForeignKey(db_column='cage_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.cage', verbose_name='Cage'),
        ),
        migrations.AlterField(
            model_name='program_cage',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='program_dar',
            name='dar_id',
            field=models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR'),
        ),
        migrations.AlterField(
            model_name='program_dar',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='program_fluid',
            name='fluid_id',
            field=models.ForeignKey(db_column='fluid_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.fluid', verbose_name='Fluid'),
        ),
        migrations.AlterField(
            model_name='program_fluid',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='subcomponent',
            name='dut_id',
            field=models.ForeignKey(db_column='dut_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dut', verbose_name='DUT name'),
        ),
        migrations.AlterField(
            model_name='technician',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab', verbose_name='Lab'),
        ),
        migrations.AlterField(
            model_name='test',
            name='hours_planned',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='priority',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='test',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='test',
            name='scheduling',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='status',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='supervisor_comments',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='targeted_end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='targeted_start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='total_hours',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test_chamber',
            name='chamber_id',
            field=models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.chamber', verbose_name='Chamber'),
        ),
        migrations.AlterField(
            model_name='test_chamber',
            name='test_type_id',
            field=models.ForeignKey(db_column='test_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.testtype', verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='test_dut',
            name='circuit_number',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test_dut',
            name='date_removed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='test_harness',
            name='circuit_number',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test_harness',
            name='date_removed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='testmap',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='testmap',
            name='test_map_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Test Map name'),
        ),
        migrations.AlterField(
            model_name='testmap',
            name='tr',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='TR'),
        ),
    ]
