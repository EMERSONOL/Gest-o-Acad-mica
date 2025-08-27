📊 Dashboard de Gestão Acadêmica com Streamlit
Este é um projeto de um dashboard interativo construído com Streamlit para a gestão e análise de dados acadêmicos, focando em informações sobre professores, disciplinas, semestres e número de alunos.

A aplicação permite a visualização, cadastro, filtragem e análise de dados de forma simples e intuitiva, tudo em uma única interface web.

✨ Funcionalidades Principais
Visão Geral Rápida: Cards que exibem métricas chave como o total de alunos, professores, disciplinas e semestres cadastrados.

Cadastro de Dados: Um formulário expansível para adicionar novos registros de professores, disciplinas e o número de alunos por semestre.

Visualização da Base de Dados: Uma tabela interativa que exibe todos os dados cadastrados.

Download de Dados: Botão para baixar a base de dados completa no formato .csv.

Filtros Dinâmicos: Filtre os dados por semestre, ano, professor ou disciplina para análises mais específicas.

Análises e Gráficos Interativos:

Resumo: Gráficos de pizza e de barras que agrupam o número de alunos por categoria (professor, disciplina, etc.).

Comparação: Compare o desempenho (número de alunos) de até dois professores ou duas disciplinas lado a lado.

Heatmap: Mapas de calor que mostram a concentração de alunos por disciplina/professor ao longo dos semestres.

🚀 Como Executar o Projeto
Para rodar esta aplicação em sua máquina local, siga os passos abaixo.

1. Pré-requisitos
Certifique-se de que você tem o Python instalado. Você precisará instalar as seguintes bibliotecas:

streamlit

pandas

plotly

openpyxl (para manipulação de arquivos Excel)

Você pode instalar todas de uma vez com o seguinte comando:

pip install streamlit pandas plotly openpyxl

2. Estrutura de Arquivos
O projeto utiliza um arquivo Excel para persistir os dados.

app.py: O código-fonte da aplicação Streamlit (o código que você forneceu).

dados_professores.xlsx: Arquivo Excel que armazena os dados. A aplicação criará este arquivo automaticamente no primeiro uso se ele não existir.

3. Executando a Aplicação
Salve o código fornecido em um arquivo chamado app.py.

Abra o seu terminal ou prompt de comando.

Navegue até o diretório onde você salvou o arquivo app.py.

Execute o seguinte comando:

streamlit run app.py

O Streamlit abrirá uma nova aba no seu navegador com a aplicação em execução.

🛠️ Como Usar a Aplicação
Adicionar Registros: Clique no botão "➕ Adicionar novo registro" para expandir o formulário. Preencha os campos e clique em "Salvar".

Visualizar e Filtrar: Utilize os menus de seleção na seção "🔎 Filtros" para refinar os dados exibidos nos gráficos e tabelas.

Analisar: Navegue pelas abas "📊 Resumo", "📌 Comparação" e "🔥 Heatmap" para explorar as diferentes visualizações de dados.
