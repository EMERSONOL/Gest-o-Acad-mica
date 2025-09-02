# ==============================
#    Sistema de Gestão Acadêmica
# ==============================

# --- Importação de bibliotecas ---
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração inicial do Streamlit ---
# Define título da página, ícone e layout "wide" (tela cheia)
st.set_page_config(page_title="Gestão Acadêmica", page_icon="📊", layout="wide")

# --- Função para carregar os dados ---
def carregar_dados():
    """
    Tenta abrir o arquivo Excel 'dados_professores.xlsx'.
    Caso não exista, cria um DataFrame vazio com as colunas necessárias.
    """
    try:
        df = pd.read_excel("dados_professores.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "Professor", "Disciplina", "Categoria", "Carga Horária",
            "Semestre", "Ano", "Nº de Alunos"
        ])
    return df

# --- Função para salvar os dados ---
def salvar_dados(df):
    """
    Salva o DataFrame no arquivo Excel.
    Sobrescreve o arquivo anterior.
    """
    df.to_excel("dados_professores.xlsx", index=False)


# =================================================
# 🔹 INÍCIO DO APLICATIVO
# =================================================

st.title("📊 Gestão de Professores e Disciplinas do SePLE")

# --- Carregar a base de dados inicial ---
df = carregar_dados()


# =================================================
# 🔹 DASHBOARD DE VISÃO GERAL
# =================================================
st.subheader("📌 Visão Geral")

if not df.empty:
    # Calcula métricas gerais
    total_alunos = df["Nº de Alunos"].sum()
    total_professores = df["Professor"].nunique()
    total_disciplinas = df["Disciplina"].nunique()
    total_semestres = df["Semestre"].nunique()

    # Exibe as métricas em formato de "cards"
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total de Alunos", f"{total_alunos}")
    col2.metric("👨‍🏫 Professores", f"{total_professores}")
    col3.metric("📚 Disciplinas", f"{total_disciplinas}")
    col4.metric("🗓️ Semestres", f"{total_semestres}")
else:
    st.info("Nenhum dado cadastrado ainda.")


# =================================================
# 🔹 FORMULÁRIO DE CADASTRO
# =================================================
with st.expander("➕ Adicionar novo registro", expanded=False):
    with st.form("cadastro"):
        # Divide o formulário em duas colunas
        col1, col2 = st.columns(2)

        # Coluna 1: dados básicos do professor
        with col1:
            professor = st.text_input("👨‍🏫 Professor")
            disciplina = st.text_input("📚 Disciplina")
            categoria = st.selectbox("🏷️ Categoria do Docente/ Professor",
                                     ["Professor efetivo", "Professor substituto", "Professor em formação/monitor"])

        # Coluna 2: dados acadêmicos
        with col2:
            semestre = st.text_input("🗓️ Semestre (ex.: 2025.1)")
            ano = semestre.split(".")[0] if semestre else ""   # Extrai apenas o ano (antes do ponto)
            alunos = st.number_input("👥 Nº de Alunos", min_value=0, step=1)
            carga_horaria = st.selectbox("⏰ Carga Horária (em horas)", ["15h","20h", "30h", "45h", "60h", "90h"])

        # Botão de salvar
        submitted = st.form_submit_button("Salvar")

        if submitted and semestre:
            # Cria um novo registro no formato de DataFrame
            novo = pd.DataFrame([[professor, disciplina, categoria, carga_horaria, semestre, ano, alunos]],
                                columns=df.columns)

            # Concatena o novo registro com a base existente
            df = pd.concat([df, novo], ignore_index=True)

            # Salva a nova versão da base
            salvar_dados(df)

            st.success("✅ Registro adicionado com sucesso!")


# =================================================
# 🔹 BASE DE DADOS
# =================================================
st.subheader("📋 Base de Dados")

# Exibe a tabela em tela
st.dataframe(df, use_container_width=True)

# Botão para baixar a base em CSV
st.download_button(
    label="⬇️ Baixar Excel atualizado",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='dados_professores.csv',
    mime='text/csv'
)


# =================================================
# 🔹 FILTROS
# =================================================
st.subheader("🔎 Filtros")

if not df.empty:
    # Gera listas únicas para os filtros
    semestres_disp = df["Semestre"].unique().tolist()
    anos_disp = df["Ano"].unique().tolist()
    professores_disp = df["Professor"].unique().tolist()
    disciplinas_disp = df["Disciplina"].unique().tolist()
else:
    semestres_disp, anos_disp, professores_disp, disciplinas_disp = [], [], [], []

# Seletores múltiplos (com valores padrão preenchidos)
filtro_semestre = st.multiselect("📅 Filtrar por semestre:", semestres_disp, default=semestres_disp)
filtro_ano = st.multiselect("📆 Filtrar por ano:", anos_disp, default=anos_disp)
filtro_professor = st.multiselect("👨‍🏫 Filtrar por professor:", professores_disp, default=professores_disp)
filtro_disciplina = st.multiselect("📚 Filtrar por disciplina:", disciplinas_disp, default=disciplinas_disp)

# Aplica os filtros na base
if not df.empty:
    df_filtrado = df[
        (df["Semestre"].isin(filtro_semestre)) &
        (df["Ano"].isin(filtro_ano)) &
        (df["Professor"].isin(filtro_professor)) &
        (df["Disciplina"].isin(filtro_disciplina))
    ]
else:
    df_filtrado = df


# =================================================
# 🔹 ANÁLISES E VISUALIZAÇÕES
# =================================================
st.subheader("📈 Análises e Visualizações")

# Cria abas de navegação
abas = st.tabs(["📊 Resumo", "📌 Comparação", "🔥 Heatmap"])


# -------------------------------
# Aba 1 - Resumo
# -------------------------------
with abas[0]:
    if not df_filtrado.empty:
        # Usuário escolhe como agrupar os dados
        opcao = st.selectbox("Agrupar por:", ["Professor", "Disciplina", "Semestre", "Ano"])

        # Gera resumo (soma de alunos agrupados)
        resumo = df_filtrado.groupby(opcao)["Nº de Alunos"].sum().reset_index()
        st.write(resumo)

        # Exibe gráficos comparativos
        col1, col2 = st.columns(2)
        with col1:
            fig = px.pie(resumo, values="Nº de Alunos", names=opcao, title=f"Distribuição por {opcao}")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.bar(resumo, x=opcao, y="Nº de Alunos", title=f"Totais por {opcao}", text="Nº de Alunos")
            fig.update_layout(xaxis_title=opcao, yaxis_title="Total de Alunos")
            st.plotly_chart(fig, use_container_width=True)

        # Evolução temporal
        st.write("📊 Evolução")
        fig = px.line(df_filtrado, x="Semestre", y="Nº de Alunos", color=opcao,
                      markers=True, title=f"Evolução por {opcao}")
        st.plotly_chart(fig, use_container_width=True)


# -------------------------------
# Aba 2 - Comparação
# -------------------------------
with abas[1]:
    # Usuário escolhe se quer comparar professores ou disciplinas
    tipo_comparacao = st.radio("Comparar por:", ["Professor", "Disciplina"])
    
    # Comparação entre 2 professores
    if tipo_comparacao == "Professor":
        profs = st.multiselect("Escolha até 2 professores:", professores_disp, default=professores_disp[:2])
        if len(profs) == 2:
            df_comp = df_filtrado[df_filtrado["Professor"].isin(profs)]

            # Gráfico de barras
            fig = px.bar(df_comp, x="Semestre", y="Nº de Alunos", color="Professor", barmode="group",
                         title="Comparação de Professores por Semestre")
            st.plotly_chart(fig, use_container_width=True)

            # Gráfico de linha
            fig = px.line(df_comp, x="Semestre", y="Nº de Alunos", color="Professor", markers=True,
                          title="Evolução de Professores ao longo dos semestres")
            st.plotly_chart(fig, use_container_width=True)

    # Comparação entre 2 disciplinas
    elif tipo_comparacao == "Disciplina":
        discs = st.multiselect("Escolha até 2 disciplinas:", disciplinas_disp, default=disciplinas_disp[:2])
        if len(discs) == 2:
            df_comp = df_filtrado[df_filtrado["Disciplina"].isin(discs)]

            fig = px.bar(df_comp, x="Semestre", y="Nº de Alunos", color="Disciplina", barmode="group",
                         title="Comparação de Disciplinas por Semestre")
            st.plotly_chart(fig, use_container_width=True)

            fig = px.line(df_comp, x="Semestre", y="Nº de Alunos", color="Disciplina", markers=True,
                          title="Evolução de Disciplinas ao longo dos semestres")
            st.plotly_chart(fig, use_container_width=True)


# -------------------------------
# Aba 3 - Heatmap
# -------------------------------
with abas[2]:
    st.write("🔥 **Mapa de Calor - Semestre x Disciplina**")
    if not df_filtrado.empty:
        # Heatmap de alunos por disciplina e semestre
        tabela_heatmap = df_filtrado.pivot_table(index="Disciplina", columns="Semestre",
                                                 values="Nº de Alunos", aggfunc="sum", fill_value=0)
        fig = px.imshow(tabela_heatmap,
                        labels=dict(x="Semestre", y="Disciplina", color="Nº de Alunos"),
                        text_auto=True,
                        title="Heatmap de Alunos por Disciplina e Semestre",
                        aspect="auto",
                        color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)

        # Heatmap de alunos por professor e semestre
        st.write("🔥 **Mapa de Calor - Semestre x Professor**")
        tabela_heatmap2 = df_filtrado.pivot_table(index="Professor", columns="Semestre",
                                                  values="Nº de Alunos", aggfunc="sum", fill_value=0)
        fig2 = px.imshow(tabela_heatmap2,
                         labels=dict(x="Semestre", y="Professor", color="Nº de Alunos"),
                         text_auto=True,
                         title="Heatmap de Alunos por Professor e Semestre",
                         aspect="auto",
                         color_continuous_scale="Oranges")
        st.plotly_chart(fig2, use_container_width=True)


