from datetime import timezone, datetime
from django.db import models


class Ovo(models.Model):
    STATUS_CHOICES = (
        ("armazenado", "Armazenado"),
        ("chocando", "Chocando"),
        ("pintinho", "Pintinho"),
    )
    data_cadastro = models.DateTimeField(auto_now_add=True, editable=True)
    codigo = models.CharField(max_length=10, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default="armazenado", editable=True)
    chocadeira = models.CharField(max_length=3, default=1)
    data_chocadeira = models.DateField(null=True, blank=True)
    dias_chocadeira = models.IntegerField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f'Ovo { self.codigo } - Status: { self.status }'

    def data_eclosao(self):
        agora = timezone.now()
        if self.status == "chocando":
            estimado = agora + timezone.timedelta(days=21)
            self.data_chocadeira = timezone.now()
            return estimado
        return None

    def tempo_armazenado(self):
        if self.status == "armazenado":
            diferenca = timezone.now() - self.data_cadastro
            return diferenca
        return None

    def aviso_vencimento(self):
        if self.status == "armazenado" and self.tempo_armazenado().days >= 28:
            return True
        return False

    def set_dias_chocadeira(self):
        if self.status == "chocando":
            dias_chocadeira = timezone.now() - self.data_chocadeira
            self.dias_chocadeira = dias_chocadeira
            return dias_chocadeira
        return None

    def get_imagem_ovo(self):
        if self.dias_chocadeira < 1:
            return None
        elif self.dias_chocadeira == 1:
            return "ovoscopia/1dia.png"
        elif self.dias_chocadeira > 1 and self.dias_chocadeira <= 21:
            return f"ovoscopia/{self.dias_chocadeira}dia.png"
        else:
            return "ovoscopia/pintinho.png"

    def save(self, *args, **kwargs):
        if not self.codigo:
            data_atual = datetime.now()
            ano = int(data_atual.strftime('%y'))
            mes = int(data_atual.strftime('%m'))
            dia = int(data_atual.strftime('%d'))
            ultimo_id_dia = Ovo.objects.filter(
                data_cadastro__date=data_atual).count()
            codigo = f'{ano}-{mes}-{dia}-{ultimo_id_dia+1:01d}'
            self.codigo = codigo
        super(Ovo, self).save(*args, **kwargs)


class Raca(models.Model):
    nome = models.CharField(max_length=20)
    nome_cientifico = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f" {self.nome} "

    def save(self, *args, **kwargs):
        super(Raca, self).save(*args, **kwargs)


class Pintinho(models.Model):
    ovo = models.OneToOneField(Ovo, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    deficiencia = models.BooleanField(default=False)
    data_eclosao = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    codigo_ovo = Ovo.codigo

    def __str__(self):
        return f"{ self.codigo }"

    def save(self, *args, **kwargs):
        if not self.codigo.startswith("p-"):
            self.codigo = "p-" + self.codigo_ovo
        super(Pintinho, self).save(*args, **kwargs)
