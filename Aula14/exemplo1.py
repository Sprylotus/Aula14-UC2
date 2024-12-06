# import pandas as pd 
import polars as pl 
from matplotlib import pyplot as plt
import os
import numpy as np 
from datetime import datetime
ENDERECO_DADOS = r'./dados/'

# try:     
#     print('Obtendo Dados...')
#     inicio = datetime.now()
#     lista_arquivos = []
#     #lista final dos arquivos de dados que vira do diretorio
#     lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

#     for arquivo in lista_dir_arquivos:
#         if arquivo.endswith('.csv'):
#             lista_arquivos.append(arquivo)
#     print(lista_arquivos)

#     for arquivo in lista_arquivos:
#         print(f"Processando arquivo {arquivo}")
#         #leitura de cada um dos dataframes
#         df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
    
#         if 'df_bolsa_familia' in locals():
#             df_bolsa_familia = pl.concat([df_bolsa_familia, df])
#         else: 
#             df_bolsa_familia = df

                
#         fim = datetime.now()
#         print(f"Tempo de execução: '{fim - inicio}")
#         print("Gravação do Arquivo Parquet realizado com sucesso")

#     df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia_parquet')
        
#     print(df_bolsa_familia)

#     # print(df.head())
#     # print(df.shape)
#     # print(df.columns)
#     # print(df.dtypes)

#     #limpar df da memoria
#     del df
#     # residuos da memoria
#     gc.collect()
    
# except ImportError as e:
#     print ("Erro ao obter dados: ", e)
     

try:
    print('\nIniciando leitura do arquivo parquet...')

    inicio = datetime.now()

    # df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia_plan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = df_bolsa_familia_plan.collect()
    
    print(df_bolsa_familia.head())

    fim = datetime.now()

    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except ImportError as e:
    print(f'Erro ao ler os dados do parquet: {e}')

try:
    print('Visualizar disposição')

    hora_inicio = datetime.now()

    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição dos valores das parcelas')

    hora_fim = datetime.now()

    plt.show()

    print(f'Tempo de execução: {hora_fim - hora_inicio}')

except ImportError as e:
    print(f'Erro ao visualizar dados')