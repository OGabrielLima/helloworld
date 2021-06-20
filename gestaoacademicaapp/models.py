from django.db import models
from django.contrib.auth import get_user_model
#-Categoria-----------------------------------------------------------------------------------------------------
class Categoria(models.Model):

    descricaocategoria = models.CharField(max_length=100)
    #descricao = models.TextField(),
    #datacriacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descricaocategoria
#--------------------------------------------------------------------------------------------------------------
#-Conta corrente-----------------------------------------------------------------------------------------------
class Conta(models.Model):

    descricaoconta = models.CharField(max_length=100)
    descricaobanco = models.CharField(max_length=100)
    #descricao = models.TextField(),
    #datacriacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descricaoconta
#--------------------------------------------------------------------------------------------------------------
#-Despesa------------------------------------------------------------------------------------------------------
class Despesa(models.Model):

    STATUS = (
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
    )
    STATUS = (
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
    )
    valordespesa = models.CharField(max_length=10, blank=False, null=False)
    descricaodespesa = models.CharField(max_length=100, blank=False, null=False)
    datacriacaodespesa = models.DateTimeField(auto_now_add=True)
    categoriadespesa = models.ForeignKey('Categoria', verbose_name="Categoria", on_delete=models.CASCADE, blank=True, null=True)
    contadespesa = models.ForeignKey('Conta', verbose_name="Conta", on_delete=models.CASCADE, blank=True, null=True)

    #turno = models.CharField(max_length=10, blank=True, null=True)
    #diadasemana = models.CharField(max_length=20, blank=True, null=True)
    #local = models.CharField(max_length=20, blank=True, null=True)
    #descricao = models.TextField()

    status = models.CharField(
        max_length=11,
        choices=STATUS,
    )

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    #datacriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.titulo,self.estudante,self.curso
        return f"{self.valordespesa},{self.descricaodespesa},{self.datacriacaodespesa},{self.categoriadespesa},{self.contadespesa}"


#Antigos models
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
class Curso(models.Model):

    titulo = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(max_length=255, blank=True, null=True),
    datacriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Disciplina(models.Model):

    STATUS = (
        ('ativa', 'Ativa'),
        ('desativada', 'Desativada'),
    )

    titulo = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=10, blank=True, null=True)
    diadasemana = models.CharField(max_length=20, blank=True, null=True)
    local = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TextField()
    status = models.CharField(
        max_length=11,
        choices=STATUS,
    )

    estudante = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', verbose_name="Cursos", on_delete=models.CASCADE, blank=True, null=True)
    datacriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.titulo,self.estudante,self.curso
        return f"{self.curso},{self.titulo},{self.turno},{self.diadasemana}"

class Matricula(models.Model):

    STATUS = (
        ('matriculado', 'Em andamento'),
        ('prevista', 'Prevista'),
        ('aprovado', 'Aprovado'),
        ('dependencia', 'Dependência'),
    )

    semestre = models.CharField(max_length=255)
    status = models.CharField(
        max_length=12,
        choices=STATUS,
    )
    estudante = models.ForeignKey(get_user_model(), related_name='+', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', verbose_name="Disciplinas", related_name="disciplinafk", on_delete=models.CASCADE, blank=True, null=True)
    datacriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.semestre},{self.status}"