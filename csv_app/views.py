from django.shortcuts import render
from django.contrib import messages
from .models import Medicamento
import csv, io

def parse_decimal(value):
            if value is None or value.strip() == "" or not any(char.isdigit() for char in value):
                return None  

            try:
                return float(value.replace(',', '.'))
            except ValueError:
                return None 

def parse_negative(value):
    if value is None or value.strip() == "" or not any(char.isdigit() for char in value):
        return None  

    try:
        # Remove espaços e verifica se o número está entre parênteses
        value = value.strip()
        if value.startswith('(') and value.endswith(')'):
            value = '-' + value[1:-1]  # Remove parênteses e adiciona o sinal negativo

        return float(value.replace(',', '.'))
    except ValueError:
        return None

def medicamento_upload(request):
    template = "csv_app/medicamento_csv_upload.html"
    
    if request.method == 'GET':
        return render(request, template)

    if request.method == 'POST':
        csv_file = request.FILES['file']

        data_set = csv_file.read().decode('ISO-8859-1')
        read_header = io.StringIO(data_set)
        csv_reader = csv.reader(read_header, delimiter=';')
        check_header = next(csv_reader)
        check_length = len(check_header)
        # print(check_header)
        # print(check_length)       

        if not csv_file.name.endswith('.csv') or check_length < 40:
            messages.error(request, 'Extensão de arquivo inválida | Número de colunas incompatível')
        else:
            #data_set = csv_file.read().decode('ISO-8859-1')
            io_string = io.StringIO(data_set)
            next(io_string)
            reader = csv.reader(io_string, delimiter=';', quotechar='"')

            for column in reader:

                column_numbers = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                                23, 24, 25, 26, 27, 28, 29, 30, 31]

                for c in column_numbers:
                    column[c] = parse_decimal(column[c])  

                column[36] = parse_negative(column[36])  

                _, created = Medicamento.objects.update_or_create (
                    substancia = column[0],
                    cnpj = column[1], 
                    laboratorio = column[2],
                    codigo_ggrem = column[3],  
                    registro = column[4],
                    ean_1 = column[5],
                    ean_2 = column[6],
                    ean_3 = column[7],
                    produto = column[8],
                    apresentacao = column[9],
                    classe_terapeutica = column[10],
                    tipo_de_produto_status = column[11],
                    regime_de_preco = column[12],
                    pf_sem_imposto = column[13],  
                    pf_0 = column[14],
                    pf_12 = column[15],  
                    pf_17 = column[16],
                    pf_17_alc = column[17],
                    pf_17_5 = column[18],
                    pf_17_5_alc = column[19],
                    pf_18 = column[20],
                    pf_18_alc = column[21],
                    pf_20 = column[22],
                    pmc_0 = column[23],
                    pmc_12 = column[24],
                    pmc_17 = column[25],
                    pmc_17_alc = column[26],
                    pmc_17_5 = column[27],
                    pmc_17_5_alc = column[28],
                    pmc_18 = column[29],
                    pmc_18_alc = column[30],
                    pmc_20 = column[31],
                    restricao_hospitalar = column[32],
                    cap = column[33],
                    confaz_87 = column[34],
                    icms_0 = column[35],
                    analise_recursal = column[36],
                    lista_de_concessao_de_credito_tributario = column[37],
                    comercializado_2020 = column[38],
                    tarja = column[39],
                )

        context = {}
        return render(request, template, context)


