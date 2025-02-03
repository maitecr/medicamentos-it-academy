import config.Database as db

class MedicamentoModel(db.Database):
    
    def __init__(self):
        super().__init__()
        self._db = db.Database() 

    def insert_into_table(self, substancia, cnpj, laboratorio, codigo_ggrem, registro,
                         ean_1, ean_2, ean_3, produto, apresentacao, classe_terapeutica, 
                         tipo_de_produto_status, regime_de_preco, pf_sem_imposto, pf_0, 
                         pf_12, pf_17, pf_17_alc, pf_17_5, pf_17_5_alc, pf_18, pf_18_alc, 
                         pf_20, pmc_0, pmc_12, pmc_17, pmc_17_alc, pmc_17_5, pmc_17_5_alc, 
                         pmc_18, pmc_18_alc, pmc_20, restricao_hospitalar, cap, confaz_87, 
                         icms_0, analise_recursal, lista_de_concessa_de_credito_tributario, 
                         comercializado_2020, tarja):

        _query = """ insert into medicamento (
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
        self._db.cur.execute(_query, (substancia, cnpj, laboratorio, codigo_ggrem, registro,
                         ean_1, ean_2, ean_3, produto, apresentacao, classe_terapeutica, 
                         tipo_de_produto_status, regime_de_preco, pf_sem_imposto, pf_0, 
                         pf_12, pf_17, pf_17_alc, pf_17_5, pf_17_5_alc, pf_18, pf_18_alc, 
                         pf_20, pmc_0, pmc_12, pmc_17, pmc_17_alc, pmc_17_5, pmc_17_5_alc, 
                         pmc_18, pmc_18_alc, pmc_20, restricao_hospitalar, cap, confaz_87, 
                         icms_0, analise_recursal, lista_de_concessa_de_credito_tributario, 
                         comercializado_2020, tarja))

        self._db.conn.commit()
        