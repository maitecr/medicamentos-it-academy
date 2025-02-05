import config.Database as db

class MedicamentoModel(db.Database):
    
    def __init__(self):
        super().__init__()
        self._db = db.Database() 

    def post_from_csv(self, *columns):

        _query = """ insert into medicamento (
                         substancia, cnpj, laboratorio, codigo_ggrem, registro,
                         ean_1, ean_2, ean_3, produto, apresentacao, classe_terapeutica, 
                         tipo_de_produto_status, regime_de_preco, pf_sem_imposto, pf_0, 
                         pf_12, pf_17, pf_17_alc, pf_17_5, pf_17_5_alc, pf_18, pf_18_alc, 
                         pf_20, pmc_0, pmc_12, pmc_17, pmc_17_alc, pmc_17_5, pmc_17_5_alc, 
                         pmc_18, pmc_18_alc, pmc_20, restricao_hospitalar, cap, confaz_87, 
                         icms_0, analise_recursal, lista_de_concessao_de_credito_tributario, 
                         comercializado_2020, tarja
						)
				values (
	                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
					   );
                """
        self._db.cur.execute(_query, columns)

        self._db.conn.commit()

    def get_product_by_name(self, product_name):
        _query_select = """SELECT produto, pf_sem_imposto, apresentacao FROM medicamento
                         WHERE produto ILIKE %s 
                         AND comercializado_2020 = 'Sim';"""
        
        _search_product_by_name = product_name

        _binding_params = ('%' + _search_product_by_name + '%',)

        self._db.cur.execute(_query_select, _binding_params)
        
        _results = self._db.cur.fetchall()

        return _results

    def get_product_by_code(self, code) :
        _query_select = """ SELECT produto, max(pmc_0), min(pmc_0), max(pmc_0) - min(pmc_0) AS result 
                    FROM medicamento 
                    WHERE ean_1 = %s
                    GROUP BY produto;"""

        _binding_params = (code,)

        self._db.cur.execute(_query_select, _binding_params)

        _results = self._db.cur.fetchall()

        return _results

    def get_percentual_lista_de_concessao_de_credito_tributario(self):
        _query_select = """ SELECT lista_de_concessao_de_credito_tributario, 
                                   COUNT(lista_de_concessao_de_credito_tributario) as total , 
                                   count(*) * 100.0 / (select count(*) from medicamento) as percentual
                            FROM medicamento 
                            WHERE comercializado_2020 = 'Sim'
                            GROUP BY lista_de_concessao_de_credito_tributario ;"""
        
        self._db.cur.execute(_query_select)

        _results = self._db.cur.fetchall()

        return _results