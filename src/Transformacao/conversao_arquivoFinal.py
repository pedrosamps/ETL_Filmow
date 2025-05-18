import pandas as pd

arquivo_csv = 'C:\\Users\\pedro\OneDrive\\Área de Trabalho\\Python-projetos\\ETL_Filmow\\arquivoFilmes\\filmesDetalhado.csv'
arquivo_xlsx = 'C:\\Users\\pedro\OneDrive\\Área de Trabalho\\Python-projetos\\ETL_Filmow\\arquivoFilmes\\filmesExtraidos_V0.xlsx'

filme = pd.read_csv(arquivo_csv)
filme.to_excel(arquivo_xlsx, index=False)
print(f'Arquivo {arquivo_csv} convertido para {arquivo_xlsx} com sucesso!')