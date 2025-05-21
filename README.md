# DataCleaningAgent

Este projeto contém uma classe Python para realizar a limpeza automática de dados em um DataFrame do pandas. A classe `DataCleaningAgent`
oferece métodos para remover duplicatas, preencher valores ausentes, converter tipos de dados automaticamente e remover outliers baseados em z-score.

## Funcionalidades

- **Remover duplicatas**: Identifica e remove linhas duplicadas no DataFrame.
- **Preencher valores ausentes**: Permite preencher valores nulos usando diferentes estratégias, como média, mediana, moda ou valor fixo.
- **Converter tipos de dados**: Converte os tipos de dados das colunas para os tipos mais apropriados automaticamente.
- **Remover outliers**: Remove linhas que possuem valores fora do intervalo considerado aceitável de acordo com um limite definido pelo z-score (padrão 3).
- **Pipeline completo de limpeza**: Método `clean()` que executa todas as etapas de limpeza na ordem correta.

## Como usar

1. Tenha o arquivo CSV com os dados que deseja limpar. No exemplo do código.
2. Ajuste este caminho para o local correspondente no seu sistema.
3. Importe o arquivo CSV usando `pandas` e crie uma instância do `DataCleaningAgent` com o DataFrame:

```python
import pandas as pd

df = pd.read_csv("D:/Estudante/arquivo.csv") #Ex: caminho do arquivo

agent = DataCleaningAgent(df)
cleaned_df = agent.clean()
```
Após executar ```clean()```, você terá o DataFrame limpo, sem duplicatas, com valores ausentes tratados,
tipos de dados atualizados, e outliers removidos.

## Requisitos
```Python 3.x```
```pandas```
```numpy```
```scipy```
Você pode instalar as dependências necessárias com:
```python
pip install pandas numpy scipy
```



