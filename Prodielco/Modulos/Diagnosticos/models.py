from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Depto(models.Model):
    departamento = models.CharField(max_length=30)

    def __str__(self):
        return self.departamento


class Municipio(models.Model):
    municipio = models.CharField(max_length=30)
    depto = models.ForeignKey(Depto, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipio


class Clase_Transformador(models.Model):
    clase_transformador = models.CharField(max_length=50)

    def __str__(self):
        return self.clase_transformador


class Fabricante(models.Model):
    fabricante = models.CharField(max_length=50)

    def __str__(self):
        return self.fabricante


class Tap_Nominal(models.Model):
    tap_nominal = models.CharField(max_length=50)

    def __str__(self):
        return self.tap_nominal


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    departamento = models.ForeignKey(Depto, on_delete=models.CASCADE)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    barrio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre


class Responsable(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.ForeignKey(Depto, on_delete=models.CASCADE)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    barrio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombres


class Categoria_Pruebas(models.Model):
    categoria = models.CharField(max_length=500)

    def __str__(self):
        return self.categoria


class Tipo_Pruebas(models.Model):
    prueba = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria_Pruebas, on_delete=models.CASCADE)

    def __str__(self):
        return self.prueba


class Nomenclatura(models.Model):
    nomenclatura = models.CharField(max_length=50)

    def __str__(self):
        return self.nomenclatura


class Formula(models.Model):
    formula = models.CharField(max_length=100)

    def __str__(self):
        return self.formula


class Grupo_Conexion(models.Model):
    grupo_conexion = models.CharField(max_length=100)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)

    def __str__(self):
        return self.grupo_conexion


class Conexion_TTR(models.Model):
    nomenclatura = models.ForeignKey(Nomenclatura, on_delete=models.CASCADE)
    grupo_conexion = models.ForeignKey(Grupo_Conexion, on_delete=models.CASCADE)
    conexion_TTR_1 = models.CharField(max_length=100)
    conexion_TTR_2 = models.CharField(max_length=100)
    conexion_TTR_3 = models.CharField(max_length=100)
    conexion_TTR_4 = models.CharField(max_length=100)
    conexion_TTR_5 = models.CharField(max_length=100)
    conexion_TTR_6 = models.CharField(max_length=100)


class Transformador(models.Model):
    tipo_transformador = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    referencia = models.CharField(max_length=500)
    fecha_fabricacion = models.DateField()
    peso_kg = models.FloatField()
    litros_l = models.FloatField()
    tension_at = models.IntegerField()
    tension_bt = models.IntegerField()
    potencia_kVA = models.IntegerField()
    temperatura = models.FloatField()
    humedad = models.IntegerField()
    factor_correccion_k = models.FloatField()
    medidor_De_Aislamiento = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsable = ChainedForeignKey(
        Responsable,
        chained_field="cliente",
        chained_model_field="cliente",
        show_all=False,
        auto_choose=True
    )
    clase_transformador = models.ForeignKey(Clase_Transformador, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    nomenclatura = models.ForeignKey(Nomenclatura, on_delete=models.CASCADE)
    tap_nominal = models.ForeignKey(Tap_Nominal, on_delete=models.CASCADE)
    grupo_de_conexion = models.ForeignKey(Grupo_Conexion, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Depto, on_delete=models.CASCADE)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    barrio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)

    def __str__(self):
        return self.serial

    @property
    def factor_correccion(self):
        a, b = (0.5, (20 - self.temperatura) / 10)
        factor_correccion_k = operator.pow(a, b)
        return (factor_correccion_k)

    def factor_correccion(self):
        return self.cantidad * self.valor_unitario

    def save(self):
        self.factor_correccion_k = self.factor_correccion
        super(Transformador, self).save()


class Resistencia_aislamiento(models.Model):
    EJECUCION = models.CharField(max_length=10)
    AT_BT_T = models.CharField(max_length=10)
    segundo_15 = models.IntegerField()
    segundo_30 = models.IntegerField()
    minuto_1 = models.IntegerField()
    minuto_2 = models.IntegerField()
    minuto_3 = models.IntegerField()
    minuto_4 = models.IntegerField()
    minuto_5 = models.IntegerField()
    minuto_6 = models.IntegerField()
    minuto_7 = models.IntegerField()
    minuto_8 = models.IntegerField()
    minuto_9 = models.IntegerField()
    minuto_10 = models.IntegerField()
    indice_absorcion = models.FloatField()
    indice_polaridad = models.FloatField()
    categoria_prueba = models.ForeignKey(Categoria_Pruebas, on_delete=models.CASCADE)
    tipo_prueba = models.ForeignKey(Tipo_Pruebas, on_delete=models.CASCADE)
    Transformador = models.ForeignKey(Transformador, on_delete=models.CASCADE)


class TTR(models.Model):
    formula_relacion = models.ForeignKey(Formula, on_delete=models.CASCADE)
    posicion_Tap_Nominal = models.ForeignKey(Tap_Nominal, on_delete=models.CASCADE)
    categoria_prueba = models.ForeignKey(Categoria_Pruebas, on_delete=models.CASCADE)
    tipo_prueba = models.ForeignKey(Tipo_Pruebas, on_delete=models.CASCADE)
    Transformador = models.ForeignKey(Transformador, on_delete=models.CASCADE)
    posicion_tap = models.IntegerField()
    voltios = models.IntegerField()
    valor_esperado = models.FloatField()
    tolerancia_maxima = models.FloatField()
    tolerancia_minima = models.FloatField
    grupo_conexion = models.ForeignKey(Grupo_Conexion, on_delete=models.CASCADE)
    p_inicial_1 = models.FloatField()
    p_final_1 = models.FloatField()
    p_inicial_2 = models.FloatField()
    p_final_2 = models.FloatField()
    p_inicial_3 = models.FloatField()
    p_final_3 = models.FloatField()

    """    
    conexion_TTR_3_1 = models.CharField(max_length=100)
    conexion_TTR_3_2 = models.CharField(max_length=100)
    conexion_TTR_3_3 = models.CharField(max_length=100)
    conexion_TTR_4_1 = models.CharField(max_length=100)
    conexion_TTR_4_2 = models.CharField(max_length=100)
    conexion_TTR_4_3 = models.CharField(max_length=100)
    conexion_TTR_5_1 = models.CharField(max_length=100)
    conexion_TTR_5_2 = models.CharField(max_length=100)
    conexion_TTR_5_3 = models.CharField(max_length=100)
    conexion_TTR_6_1 = models.CharField(max_length=100)
    conexion_TTR_6_2 = models.CharField(max_length=100)
    conexion_TTR_6_3 = models.CharField(max_length=100)
"""