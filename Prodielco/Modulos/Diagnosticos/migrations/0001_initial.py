# Generated by Django 2.2.10 on 2021-03-15 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Pruebas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Clase_Transformador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase_transformador', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_Conexion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_conexion', models.CharField(max_length=100)),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=30)),
                ('depto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Depto')),
            ],
        ),
        migrations.CreateModel(
            name='Nomenclatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomenclatura', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Cliente')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Depto')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Tap_Nominal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tap_nominal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Pruebas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prueba', models.CharField(max_length=500)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Categoria_Pruebas')),
            ],
        ),
        migrations.CreateModel(
            name='Transformador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_transformador', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('referencia', models.CharField(max_length=500)),
                ('fecha_fabricacion', models.DateField()),
                ('peso_kg', models.FloatField()),
                ('litros_l', models.FloatField()),
                ('trension_at', models.IntegerField()),
                ('trension_bt', models.IntegerField()),
                ('potencia_kVA', models.IntegerField()),
                ('temperatura', models.CharField(max_length=100)),
                ('humedad', models.IntegerField()),
                ('factor_correccion_k', models.IntegerField()),
                ('medidor_De_Aislamiento', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('clase_transformador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Clase_Transformador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Cliente')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Depto')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Fabricante')),
                ('grupo_de_conexion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Grupo_Conexion')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Municipio')),
                ('nomenclatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Nomenclatura')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Responsable')),
                ('tap_nominal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Tap_Nominal')),
            ],
        ),
        migrations.CreateModel(
            name='TTR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion_tap', models.IntegerField()),
                ('voltios', models.IntegerField()),
                ('valor_esperado', models.FloatField()),
                ('tolerancia_maxima', models.FloatField()),
                ('p_inicial_1', models.FloatField()),
                ('p_final_1', models.FloatField()),
                ('p_inicial_2', models.FloatField()),
                ('p_final_2', models.FloatField()),
                ('p_inicial_3', models.FloatField()),
                ('p_final_3', models.FloatField()),
                ('Transformador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Transformador')),
                ('categoria_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Categoria_Pruebas')),
                ('formula_relacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Formula')),
                ('grupo_conexion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Grupo_Conexion')),
                ('posicion_Tap_Nominal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Tap_Nominal')),
                ('tipo_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Tipo_Pruebas')),
            ],
        ),
        migrations.CreateModel(
            name='Resistencia_aislamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EJECUCION', models.CharField(max_length=10)),
                ('AT_BT_T', models.CharField(max_length=10)),
                ('segundo_15', models.IntegerField()),
                ('segundo_30', models.IntegerField()),
                ('minuto_1', models.IntegerField()),
                ('minuto_2', models.IntegerField()),
                ('minuto_3', models.IntegerField()),
                ('minuto_4', models.IntegerField()),
                ('minuto_5', models.IntegerField()),
                ('minuto_6', models.IntegerField()),
                ('minuto_7', models.IntegerField()),
                ('minuto_8', models.IntegerField()),
                ('minuto_9', models.IntegerField()),
                ('minuto_10', models.IntegerField()),
                ('indice_absorcion', models.FloatField()),
                ('indice_polaridad', models.FloatField()),
                ('Transformador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Transformador')),
                ('categoria_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Categoria_Pruebas')),
                ('tipo_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Tipo_Pruebas')),
            ],
        ),
        migrations.CreateModel(
            name='Conexion_TTR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conexion_TTR_1', models.CharField(max_length=100)),
                ('conexion_TTR_2', models.CharField(max_length=100)),
                ('conexion_TTR_3', models.CharField(max_length=100)),
                ('conexion_TTR_4', models.CharField(max_length=100)),
                ('conexion_TTR_5', models.CharField(max_length=100)),
                ('conexion_TTR_6', models.CharField(max_length=100)),
                ('grupo_conexion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Grupo_Conexion')),
                ('nomenclatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Nomenclatura')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Depto'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnosticos.Municipio'),
        ),
    ]
