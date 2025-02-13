from django.db import models

class Medicamento(models.Model):
    substancia = models.TextField() 
    cnpj = models.CharField(max_length=20)
    laboratorio = models.CharField(max_length=255)
    codigo_ggrem = models.CharField(max_length=40)  
    registro = models.CharField(max_length=50)
    ean_1 = models.CharField(max_length=50)
    ean_2 = models.CharField(max_length=50) 
    ean_3 = models.CharField(max_length=50) 
    produto = models.CharField(max_length=255) 
    apresentacao = models.CharField(max_length=255)
    classe_terapeutica = models.CharField(max_length=255)
    tipo_de_produto_status = models.CharField(max_length=30)
    regime_de_preco = models.CharField(max_length=30)
    pf_sem_imposto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    pf_0 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pf_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)   
    pf_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)   
    pf_17_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pf_17_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pf_17_5_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pf_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pf_18_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pf_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_0 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_12 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_17 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_17_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_17_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_17_5_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_18 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_18_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    pmc_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    restricao_hospitalar = models.CharField(max_length=10) 
    cap = models.CharField(max_length=10) 
    confaz_87 = models.CharField(max_length=10)
    icms_0 = models.CharField(max_length=10) 
    analise_recursal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lista_de_concessao_de_credito_tributario = models.CharField(max_length=10)
    comercializado_2020 = models.CharField(max_length=10, default='Não')
    tarja = models.CharField(max_length=50)


    