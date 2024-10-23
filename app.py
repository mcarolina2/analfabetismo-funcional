import pandas as pd
from pandas import read_csv
import streamlit as st
import plotly.express as plt


# Leitura dos dados
base_2019 = pd.read_csv('dados/pnad_2019_filtrado.csv',sep=',',decimal='.')
base_2023 = pd.read_csv('dados/pnad_2023_filtrado.csv',sep=',',decimal='.')


# Customizar a aba da janela do APP
st.set_page_config(page_icon=':school:', page_title='Analfabetismo Funcional')

#Menu 
menu = st.sidebar.selectbox('Menu', ['Tela Inicial', 'Dados do Brasil de Acordo Com a Região', 'Dados do Brasil de Acordo Com o Sexo','Dados do Brasil de Acordo Com a Cor e Raça', 'Dados do Brasil de Acordo com a Faixa Étaria'])

if menu == 'Tela Inicial':
    with st.container():
        st.header('Analfabetismo Funcional No Brasil Período Pré e Pós Pandemia') 
        st.write(
            """
            Ficamos encarregados de abordar o tema do analfabetismo
            funcional, considerando os grandes desafios que a pandemia
            representou para a educação brasileira, utilizamos uma
            metodologia comparativa para analisar os períodos antes e
            depois da pandemia. Os dados do período pré-pandemia são
            provenientes da PNAD 2019, enquanto os dados pós-pandemia
            foram extraídos da PNAD 2023.
            """
        )
        st.title('Você sabe o que é analfabetismo funcional ?')
        st.write(
            """
            Segundo o IBGE e abordagens científicas, é uma condição que
            descreve indivíduos que, embora tenham sido alfabetizados
            em um nível básico, não possuem habilidades suficientes para
            compreender, interpretar e aplicar informações escritas ou
            matemáticas de maneira eficaz em situações cotidianas.
            Essa forma de analfabetismo impede o pleno uso da leitura,
            escrita e cálculos simples para tarefas que exigem maior
            complexidade, como a interpretação de textos ou a resolução
            de problemas mais avançados.
            """
        )
 #Dados dos analfabetos distribuidos nas regiões:       
elif menu == 'Dados do Brasil de Acordo Com a Região':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo Com a Região")
        st.write("Visualização dos dados e gráficos comparando os de 2019 com os de 2023:")
    
        regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']  # Definição das regiões e criação do DataFrame de regiões
        df_regioes = pd.DataFrame(regioes, columns=['Região'])

        # os códigos UF são: 11-17 Norte, 21-29 Nordeste, 31-35 Sudeste, 41-43 Sul, 50-53 Centro-Oeste
        uf_para_regiao = {
            11: 'Norte', 12: 'Norte', 13: 'Norte', 14: 'Norte', 15: 'Norte', 16: 'Norte', 17: 'Norte',
            21: 'Nordeste', 22: 'Nordeste', 23: 'Nordeste', 24: 'Nordeste', 25: 'Nordeste', 26: 'Nordeste', 27: 'Nordeste', 28: 'Nordeste', 29: 'Nordeste',
            31: 'Sudeste', 32: 'Sudeste', 33: 'Sudeste', 34: 'Sudeste', 35: 'Sudeste',
            41: 'Sul', 42: 'Sul', 43: 'Sul',
            50: 'Centro-Oeste', 51: 'Centro-Oeste', 52: 'Centro-Oeste', 53: 'Centro-Oeste'
        }

        base_2019.loc[:, 'Região'] = base_2019['UF'].map(uf_para_regiao)
        base_2023.loc[:, 'Região'] = base_2023['UF'].map(uf_para_regiao)

        # Agrupando por região para 2019 e 2023
        df_total_2019 = base_2019.groupby('Região').size().reset_index(name='Quantidade')
        df_total_2023 = base_2023.groupby('Região').size().reset_index(name='Quantidade')

        # Nomeando as regiões (certifique-se de que a variável esteja definida corretamente)
        regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
        df_regioes = pd.DataFrame(regioes, columns=['Região'])

        # Merge com df_regioes para garantir todas as regiões no resultado final para 2019 e 2023
        df_total_2019 = df_regioes.merge(df_total_2019, on='Região', how='left').fillna(0)
        df_total_2023 = df_regioes.merge(df_total_2023, on='Região', how='left').fillna(0)

        # Convertendo a coluna 'Quantidade' para int (2019 e 2023)
        df_total_2019['Quantidade'] = df_total_2019['Quantidade'].astype(int)
        df_total_2023['Quantidade'] = df_total_2023['Quantidade'].astype(int)

        # Visualização
        st.write("Filtrando nas regiões do Brasil, a quantidade de analfabetos funcionais no brasil")
        col1, col2 = st.columns(2)
        with col1:
            st.write(df_total_2019)
        with col2:
            st.write(df_total_2023)
            
        col1, col2 = st.columns(2)
        with col1:
            fig = plt.bar(df_total_2019, 
                    x='Região', 
                    y='Quantidade', 
                    title='Distribuição dos Analfabetos Funcionais em 2019', 
                    labels={'Quantidade': 'Total'})
            st.plotly_chart(fig)
        with col2:
            fig = plt.bar(df_total_2023, 
                    x='Região', 
                    y='Quantidade', 
                    title='Distribuição dos Analfabetos Funcionais em 2023', 
                    labels={'Quantidade': 'Total'})
            st.plotly_chart(fig)
        
# Dados em relação ao sexo 
elif menu == 'Dados do Brasil de Acordo Com o Sexo':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo Com o Sexo")
        st.write("Este indicador mede a porcentagem de indivíduos considerados analfabetos funcionais, divididos entre homens e mulheres, com a visualização dos dados e gráficos que comparam os resultados de 2019 com os de 2023")


        distribuicao_sexo_2019 = base_2019['V2007'].value_counts().rename(index={1: 'Masculino', 2: 'Feminino'}).reset_index()
        distribuicao_sexo_2019.columns = ['Sexo', 'Quantidade'] 
        distribuicao_sexo_2023 = base_2023['V2007'].value_counts().rename(index={1: 'Masculino', 2: 'Feminino'}).reset_index()
        distribuicao_sexo_2023.columns = ['Sexo', 'Quantidade'] 

        # criando o grafico usando a msm ideia do outro, colocando apenas a cor para diferenciar...
        #... feminino do masculino
        col1, col2 = st.columns(2)
        with col1:
            fig = plt.bar(distribuicao_sexo_2019, 
                        x='Sexo', 
                        y='Quantidade', 
                        color='Sexo', 
                        color_discrete_map={'Masculino': 'blue', 'Feminino': 'pink'},
                        title='Distribuição de 2019')
            st.plotly_chart(fig)

        with col2:
            fig = plt.bar(distribuicao_sexo_2023, 
                        x='Sexo', 
                        y='Quantidade', 
                        color='Sexo', 
                        color_discrete_map={'Masculino': 'blue', 'Feminino': 'pink'},
                        title='Distribuição de 2023')
            st.plotly_chart(fig)
        
# Filtrando a raça, fazendo a msm coisa que fiz c as outras duas, renomeando as colunas para facilitar o uso
elif menu == 'Dados do Brasil de Acordo Com a Cor e Raça':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo Com a Cor e Raça")
        st.write("Esse indicador mede a proporção de pessoas consideradas analfabetas funcionais por raça/cor, com a visualização de dados e gráficos comparando os resultados de 2019 com os de 2023")
        distribuicao_raca_2019 = base_2019['V2010'].value_counts().rename(
            index={
                1: 'Branca',
                2: 'Preta',
                3: 'Amarela',
                4: 'Parda',
                5: 'Indígena',
                9: 'Ignorado'
            }).reset_index()

        distribuicao_raca_2019.columns = ['Raça', 'Quantidade']

        distribuicao_raca_2023 = base_2023['V2010'].value_counts().rename(
            index={
                1: 'Branca',
                2: 'Preta',
                3: 'Amarela',
                4: 'Parda',
                5: 'Indígena',
                9: 'Ignorado'
            }).reset_index()

        distribuicao_raca_2023.columns = ['Raça', 'Quantidade']

        col1, col2 = st.columns(2)
        with col1:
            fig = plt.bar(distribuicao_raca_2019, 
                        x='Raça', 
                        y='Quantidade', 
                        title='Distribuição de 2019')

            # mostrando o grafico no streamlit
            st.plotly_chart(fig)
        with col2: 
            fig = plt.bar(distribuicao_raca_2023, 
                        x='Raça', 
                        y='Quantidade', 
                        title='Distribuição de 2023')

            # mostrando o grafico no streamlit
            st.plotly_chart(fig)
    
# Distribuição da faixa étaria
elif menu == 'Dados do Brasil de Acordo com a Faixa Étaria':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo com a Faixa Étaria")
        st.write("Esse indicador mede a proporção de pessoas consideradas analfabetas funcionais em diferentes faixas etárias, com a visualização dos dados e gráficos comparando os resultados de 2019 com os de 2023.")

        bins = [0, 18, 30, 40, 50, 60, 70, 120]  # Ajustando para incluir o limite superior
        labels = ['0-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70+']

        # Usar .loc[] para evitar o aviso de erro
        base_2019.loc[:, 'Faixa_Etaria'] = pd.cut(base_2019['V2009'], bins=bins, labels=labels, right=False)
        base_2023.loc[:, 'Faixa_Etaria'] = pd.cut(base_2023['V2009'], bins=bins, labels=labels, right=False)
        # Contador de pessoas em cada faixa
        distribuicao_faixa_etaria_2019= base_2019['Faixa_Etaria'].value_counts(sort=False).reset_index()
        distribuicao_faixa_etaria_2019.columns = ['Faixa Etária', 'Quantidade']  
        distribuicao_faixa_etaria_2023= base_2023['Faixa_Etaria'].value_counts(sort=False).reset_index()
        distribuicao_faixa_etaria_2023.columns = ['Faixa Etária', 'Quantidade']  

        # Criando o gráfico interativo com Plotly
        col1, col2 = st.columns(2)
        with col1:
            fig = plt.bar(distribuicao_faixa_etaria_2019, 
                        x='Faixa Etária', 
                        y='Quantidade', 
                        title='Distribuição de 2019')

            # mostrando o grafico no streamlit
            st.plotly_chart(fig)
        with col2:
            fig = plt.bar(distribuicao_faixa_etaria_2023, 
                        x='Faixa Etária', 
                        y='Quantidade', 
                        title='Distribuição de 2023')

            # mostrando o grafico no streamlit
            st.plotly_chart(fig)