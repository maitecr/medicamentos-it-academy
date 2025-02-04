import psycopg2

class Database:
    _dbname = "postgres"
    _user = "postgres"
    _password = "postgres"

    def __init__(self):
        self.conn = psycopg2.connect(
                                    dbname= Database._dbname, 
                                    user=Database._user, 
                                    password=Database._password
                                    )
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        #self.cur.execute("DROP TABLE IF EXISTS medicamento;")

        self.cur.execute('''CREATE TABLE IF NOT EXISTS medicamento (
                                substancia text, 
                                cnpj varchar(20), 
                                laboratorio varchar(255), 
                                codigo_ggrem varchar(40),  
                                registro varchar(50),
                                ean_1 varchar(50), 
                                ean_2 varchar(50), 
                                ean_3 varchar(50), 
                                produto varchar(255), 
                                apresentacao varchar(255), 
                                classe_terapeutica varchar(255), 
                                tipo_de_produto_status varchar(30), 
                                regime_de_preco varchar(30), 
                                pf_sem_imposto float8, 
                                pf_0 float8, 
                                pf_12 float8, 
                                pf_17 float8, 
                                pf_17_alc float8, 
                                pf_17_5 float8, 
                                pf_17_5_alc float8, 
                                pf_18 float8, 
                                pf_18_alc float8, 
                                pf_20 float8, 
                                pmc_0 float8, 
                                pmc_12 float8, 
                                pmc_17 float8, 
                                pmc_17_alc float8, 
                                pmc_17_5 float8, 
                                pmc_17_5_alc float8, 
                                pmc_18 float8, 
                                pmc_18_alc float8, 
                                pmc_20 float8, 
                                restricao_hospitalar varchar(10), 
                                cap varchar(10), 
                                confaz_87 varchar(10), 
                                icms_0 varchar(10), 
                                analise_recursal integer, 
                                lista_de_concessa_de_credito_tributario varchar(10), 
                                comercializado_2020 varchar(10), 
                                tarja varchar(50)
                                );''')
        self.conn.commit()

