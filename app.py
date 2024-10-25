import pandas as pd
from pandas import read_csv
import streamlit as st
import numpy as np
import plotly.express as plt

# Leitura dos dados
base_2019 = pd.read_csv('dados/pnad_2019_filtrado.csv',sep=',',decimal='.')
base_2023 = pd.read_csv('dados/pnad_2023_filtrado.csv',sep=',',decimal='.')


# Customizar a aba da janela do APP
st.set_page_config(page_icon=':school:', page_title='Analfabetismo Funcional')

#Menu 
menu = st.sidebar.selectbox('Menu', ['Tela Inicial', 'Dados Por Região', 'Dados Por Sexo','Dados Por Cor e Raça', 'Dados Por Faixa Étaria'])

#tela inicial: 
if menu == 'Tela Inicial':
    with st.container():
        st.header('Analfabetismo Funcional No Brasil Período Pré e Pós Pandemia') 
        st.write('Fomos responsáveis por abordar o tema do analfabetismo funcional, levando em conta os grandes desafios que a pandemia trouxe para a educação no Brasil. Adotamos uma metodologia comparativa para analisar os períodos antes e depois da pandemia. Os dados referentes ao período pré-pandemia foram obtidos da PNAD 2019, enquanto os dados pós-pandemia são da PNAD 2023.')
        with st.expander('Você sabe o que é analfabetismo funcional ?', False):
            st.write('Segundo o IBGE e abordagens científicas, é uma condição que descreve indivíduos que, embora tenham sido alfabetizados em um nível básico, não possuem habilidades suficientes para compreender, interpretar e aplicar informações escritas o matemáticas de maneira eficaz em situações cotidianas. Essa forma de analfabetismo impede o pleno uso da leitura, escrita e cálculos simples para tarefas que exigem maior complexidade, como a interpretação de textos ou a resolução de problemas mais avançados.')
        with st.expander('Analfabetismo funcional no período pré-pandemia?', False):
            st.write('Na PNAD 2019, a escolaridade é um dos principais critérios usados para avaliar o analfabetismo funcional. De acordo com o IBGE, no Brasil, uma pessoa é considerada analfabeta funcional se tiver menos de quatro anos de estudo formal. Para fins de comparação, em países como o Canadá, esse limite é de nove anos; nos Estados Unidos, é de oito anos; e na Espanha, de seis anos. Essa condição afeta diretamente a capacidade dos indivíduos de desempenharem tarefas cotidianas que exigem habilidades básicas de leitura e escrita.')
        with st.expander('Analfabetismo funcional no período pós-pandemia?', False):
            st.write('O analfabetismo funcional no Brasil foi intensificado após a pandemia de COVID-19, em razão das dificuldades enfrentadas no ensino remoto, como a falta de acesso à tecnologia e à internet. Esse cenário terá impactos de longo prazo, comprometendo o desempenho escolar e as oportunidades no mercado de trabalho, especialmente entre as populações mais vulneráveis. A recuperação demandará investimentos em políticas educacionais voltadas à alfabetização e à redução das desigualdades, com ênfase no desenvolvimento das habilidades básicas de leitura e escrita, essenciais para o pleno exercício da cidadania.')
 
 # Objetivo e Importância :
    st.header('Comparar os dados sobre analfabetismo funcional nos períodos pré e pós-pandemia.') 
    st.write('É importante para entender como a pandemia afetou a educação e as habilidades básicas de leitura e escrita da população. Essa comparação ajuda a identificar o aumento das desigualdades, os grupos mais impactados, e orienta a formulação de políticas educacionais focadas na recuperação e redução do analfabetismo, garantindo melhor acesso à educação e mais oportunidades no futuro.')
# Metogologia e resultados :
    st.header('Exposição dos resultados')
    st.write('A visualização dos dados e gráficos comparando os de 2019 com os de 2023 permite entender as mudanças ocorridas no período, especialmente após o impacto da pandemia. Esses gráficos facilitam a análise das variações nas taxas de analfabetismo funcional, destacando tendências, diferenças entre grupos (como faixa etária, raça/cor e sexo) e ajudando a identificar quais áreas ou populações foram mais impactadas. A comparação visual simplifica a identificação de padrões, auxiliando na tomada de decisões fundamentadas para direcionar políticas públicas e estratégias educacionais de forma mais eficaz. Nosso aplicativo desenvolvido com Streamlit desempenha exatamente essa função, permitindo a exibição interativa de gráficos que comparam os dados sobre analfabetismo funcional nos períodos pré e pós-pandemia. Isso facilita a visualização clara e acessível das informações, ajudando a compreender o impacto da pandemia na educação e apoiando a criação de políticas públicas mais informadas e direcionadas.')
    
    st.write('Verifique os gráficos dos respectivos indicadores no menu lateral')
    col1, col2 = st.columns(2)
    with col1:
        st.image('img/dados_regiao_2019.jpg')
    with col2:
        st.image('img/dados_sexo_2023.jpg')
        
 #Dados dos analfabetos distribuidos nas regiões:       
elif menu == 'Dados Por Região':
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
        st.write("Filtrar os dados por regiões do Brasil permite identificar a quantidade de analfabetos funcionais em cada área geográfica, revelando onde essa condição é mais prevalente. Ao fazer essa análise, é possível observar diferenças significativas entre as regiões, como o Norte e Nordeste, que historicamente apresentam maiores índices de analfabetismo funcional, em comparação com o Sul e Sudeste. Esse filtro regional ajuda a direcionar políticas educacionais mais eficazes e focadas nas áreas que mais necessitam de intervenção, visando reduzir as desigualdades educacionais no país.")
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
elif menu == 'Dados Por Sexo':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo Com o Sexo")
        st.write("Este indicador mede a porcentagem de indivíduos considerados analfabetos funcionais, separados por gênero, mostrando a diferença entre homens e mulheres no que diz respeito à capacidade de ler e escrever de forma básica. Através da visualização de dados e gráficos que comparam os resultados de 2019 com os de 2023, é possível analisar como a pandemia afetou cada grupo. Essa comparação permite identificar se houve mudanças nas taxas de analfabetismo funcional entre homens e mulheres, ajudando a direcionar políticas educacionais que abordem as necessidades específicas de cada gênero.")


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
elif menu == 'Dados Por Cor e Raça':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo Com a Cor e Raça")
        st.write("Esse indicador mede a proporção de pessoas consideradas analfabetas funcionais por raça/cor, destacando as diferenças no nível de alfabetização entre os grupos raciais no Brasil. Ao visualizar os dados e criar gráficos comparando os resultados de 2019 com os de 2023, é possível observar o impacto da pandemia nas desigualdades educacionais entre diferentes raças. Essa comparação ajuda a identificar se houve aumento ou redução do analfabetismo funcional em certos grupos, orientando políticas públicas para combater essas desigualdades e promover uma educação mais inclusiva.")
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
elif menu == 'Dados Por Faixa Étaria':
    with st.container():
        st.title("Analfabetismo Funcional: Dados do Brasil de Acordo com a Faixa Étaria")
        st.write("Esse indicador avalia a proporção de pessoas consideradas analfabetas funcionais em diferentes faixas etárias, mostrando a parcela da população que, mesmo tendo alguma escolaridade, possui dificuldades significativas em ler, escrever e interpretar textos. Ele permite identificar quais grupos de idade enfrentam mais barreiras de alfabetização, ajudando a direcionar políticas públicas e intervenções educacionais para reduzir essa deficiência, principalmente nas faixas etárias mais vulneráveis.")

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