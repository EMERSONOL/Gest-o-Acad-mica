# 📊 Dashboard de Gestão Acadêmica com Streamlit

![Python](https://img.shields.io/badge/python-3.10+-blue) ![Streamlit](https://img.shields.io/badge/streamlit-✔️-orange) ![License](https://img.shields.io/badge/license-MIT-green)

Um **dashboard interativo** desenvolvido com **Streamlit** para gestão e análise de dados acadêmicos, permitindo acompanhar **professores, disciplinas, semestres** e **número de alunos** de forma simples e intuitiva.

---

## ✨ Funcionalidades

* **📈 Visão Geral Rápida**: Cards com métricas como total de alunos, professores, disciplinas e semestres.
  ![Exemplo de Visão Geral].

* **➕ Cadastro de Dados**: Adicione registros de professores, disciplinas e alunos por semestre.
  ![Exemplo de Cadastro].

* **📋 Visualização da Base**: Tabela interativa com todos os registros.
  ![Exemplo de Tabela].
* **💾 Download de Dados**: Exportação completa em **CSV**.
  ![Download CSV].

* **🔎 Filtros Dinâmicos**: Filtre por semestre, ano, professor ou disciplina.
  ![Filtros Dinâmicos].

* **📊 Análises Interativas**:

  * **Resumo**: Gráficos de pizza e barras por categoria.
    ![Resumo].
  * **Comparação**: Compare desempenho de até dois professores ou disciplinas.
    ![Comparação].
  * **🔥 Heatmap**: Concentração de alunos ao longo dos semestres.
    ![Heatmap].

---

## 🚀 Como Executar

### Pré-requisitos

Instale o Python e as bibliotecas necessárias:

```bash
pip install streamlit pandas plotly openpyxl
```

### Estrutura do Projeto

* `app.py` – Código-fonte do dashboard.
* `dados_professores.xlsx` – Base de dados em Excel (criada automaticamente no primeiro uso).
* `assets/` – Pasta com imagens de exemplo (como mostrado acima).

### Executando a Aplicação

```bash
streamlit run app.py
```

Abra o navegador para acessar a interface web do dashboard.

---

## 🛠️ Como Usar

1. **Adicionar Registros**: Clique em **➕ Adicionar novo registro**, preencha e salve.
2. **Visualizar e Filtrar**: Use os menus em **🔎 Filtros** para refinar os dados.
3. **Analisar Dados**: Explore as abas **📊 Resumo**, **📌 Comparação** e **🔥 Heatmap**.

---

Se você quiser, posso criar **uma versão final do README já com layout GitHub pronto**, incluindo **links para imagens externas** e **badges mais chamativos**, que fica perfeita para publicação sem precisar da pasta `assets`.

Quer que eu faça essa versão final?
