import psycopg2
import csv

from model import MedicamentoModel as model

conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres")
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS medicamento;")
# cur.execute('''CREATE TABLE IF NOT EXISTS medicamento (
#                          substancia text, 
# 						  cnpj varchar(20), 
# 						  laboratorio varchar(255), 
# 						  codigo_ggrem varchar(40),  
# 						  registro varchar(50),
#                           ean_1 varchar(50), 
#                           ean_2 varchar(50), 
#                           ean_3 varchar(50), 
#                           produto varchar(255), 
#                           apresentacao varchar(255), 
#                           classe_terapeutica varchar(255), 
#                           tipo_de_produto_status varchar(30), 
#                           regime_de_preco varchar(30), 
#                           pf_sem_imposto float8, 
#                           pf_0 float8, 
#                           pf_12 float8, 
#                           pf_17 float8, 
#                           pf_17_alc float8, 
#                           pf_17_5 float8, 
#                           pf_17_5_alc float8, 
#                           pf_18 float8, 
#                           pf_18_alc float8, 
#                           pf_20 float8, 
#                           pmc_0 float8, 
#                           pmc_12 float8, 
#                           pmc_17 float8, 
#                           pmc_17_alc float8, 
#                           pmc_17_5 float8, 
#                           pmc_17_5_alc float8, 
#                           pmc_18 float8, 
#                           pmc_18_alc float8, 
#                           pmc_20 float8, 
#                           restricao_hospitalar varchar(10), 
#                           cap varchar(10), 
#                           confaz_87 varchar(10), 
#                           icms_0 varchar(10), 
#                           analise_recursal varchar(5), 
#                           lista_de_concessa_de_credito_tributario varchar(10), 
#                           comercializado_2020 varchar(10), 
#                           tarja varchar(50)
#                           );''')
# conn.commit()

query_insert = """ insert into medicamento (
                         substancia, cnpj, laboratorio, codigo_ggrem, registro,
                         ean_1, ean_2, ean_3, produto, apresentacao, classe_terapeutica, 
                         tipo_de_produto_status, regime_de_preco, pf_sem_imposto, pf_0, 
                         pf_12, pf_17, pf_17_alc, pf_17_5, pf_17_5_alc, pf_18, pf_18_alc, 
                         pf_20, pmc_0, pmc_12, pmc_17, pmc_17_alc, pmc_17_5, pmc_17_5_alc, 
                         pmc_18, pmc_18_alc, pmc_20, restricao_hospitalar, cap, confaz_87, 
                         icms_0, analise_recursal, lista_de_concessa_de_credito_tributario, 
                         comercializado_2020, tarja
						)
				values (
	                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
					   );
                """

medicamento_model = model.MedicamentoModel()


# def parse_decimal(value):
#     if value is None or value.strip() == "" or not any(char.isdigit() for char in value):
#         return None  

#     try:
#         return float(value.replace(',', '.'))
#     except ValueError:
#         return None 


# with open('./data/TA_PRECO_MEDICAMENTO.csv', newline='', encoding="ISO-8859-1") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
#     next(spamreader)
#     # primeira_linha = next(spamreader) 
#     # seg = next(spamreader) # Lê a primeira linha de dados
#     # print(seg)
    
#     for row in spamreader:
#         #print(f"Número de colunas lidas: {len(row)}")  # Deve ser 40

#         numeric_fields = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
#                           23, 24, 25, 26, 27, 28, 29, 30, 31]
        
#         # Converte apenas os valores numéricos
#         for index in numeric_fields:
#             row[index] = parse_decimal(row[index])

#         medicamento_model.insert_into_table(*row)

query_select = "SELECT produto, pf_sem_imposto, apresentacao FROM medicamento WHERE produto ILIKE %s AND comercializado_2020 = 'Sim';"
search_name = 'max'
binding_param = ('%' + search_name + '%',)
#print(type(binding_param))
cur.execute(query_select, binding_param)

resultados = cur.fetchall()

for r in resultados:
    print(r)