import pandas as pd
import numpy as np
from scipy.stats import zscore

# Caminho do seu arquivo CSV
df = pd.read_csv("D:/Estudante/amazon_sales_data_2025.csv")  # Caminho do arquivo no armazenamento

class DataCleaningAgent:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def remove_duplicates(self):
        before = len(self.df)
        self.df.drop_duplicates(inplace=True)
        after = len(self.df)
        print(f"Removidas {before - after} duplicatas.")

    def fill_missing(self, strategy='mean', columns=None):
        if columns is None:
            columns = self.df.select_dtypes(include=np.number).columns
        for col in columns:
            if strategy == 'mean':
                value = self.df[col].mean()
            elif strategy == 'median':
                value = self.df[col].median()
            elif strategy == 'mode':
                value = self.df[col].mode()[0]
            else:
                value = strategy  # valor fixo
            self.df[col].fillna(value, inplace=True)
            print(f"Preenchidos valores ausentes na coluna '{col}' com {value}.")

    def convert_dtypes(self):
        self.df = self.df.convert_dtypes()
        print("Tipos de dados convertidos automaticamente.")

    def remove_outliers(self, columns=None, z_thresh=3):
        if columns is None:
            columns = self.df.select_dtypes(include=np.number).columns

        mask = pd.Series(True, index=self.df.index)  # Inicia com todas as linhas válidas

        for col in columns:
            # Ignora colunas constantes ou com poucos valores
            if self.df[col].std() == 0 or self.df[col].isnull().all():
                continue
            col_zscore = zscore(self.df[col].dropna())
            valid_idx = self.df[col].dropna().index[np.abs(col_zscore) < z_thresh]
            col_mask = self.df.index.isin(valid_idx)
            mask &= col_mask  # Combina as máscaras para todas as colunas

        before = len(self.df)
        self.df = self.df[mask]
        after = len(self.df)
        print(f"Removidos {before - after} outliers (z-score > {z_thresh}).")

    def clean(self):
        print("Iniciando limpeza de dados...")
        self.remove_duplicates()
        self.convert_dtypes()
        self.fill_missing()
        self.remove_outliers()
        print("Limpeza concluída.")
        return self.df

# Exemplo de uso
if __name__ == "__main__":
    agent = DataCleaningAgent(df)
    cleaned_df = agent.clean()

