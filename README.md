

````markdown
# 🤖 Classificador de Dados com Árvore de Decisão

Este projeto foi desenvolvido como parte da participação na **ONIA - Olimpíada Nacional de Inteligência Artificial**.

Utilizamos **Python** e a biblioteca **Scikit-Learn** para treinar um modelo de **Árvore de Decisão** com base em dados de treino, e fazer previsões sobre novos dados.

---

## 📂 Estrutura do Projeto

- `treino.csv`: Arquivo com dados rotulados para treinar o modelo (contém colunas `id`, variáveis de entrada e `target`).
- `teste.csv`: Arquivo com dados sem o rótulo final (`target`) que serão usados para previsão.
- `predicoes.csv`: Arquivo gerado com os resultados das previsões.
- `main.py`: Script principal com todo o processo de treino e previsão.
- `README.md`: Este arquivo com explicações do projeto.

---

## ⚙️ Tecnologias Usadas

- Python 3.x
- Pandas
- Scikit-learn (DecisionTreeClassifier)

---

## 🚀 Como Executar

1. Certifique-se de ter os arquivos `treino.csv` e `teste.csv` na mesma pasta do script.
2. Instale as dependências:
   ```bash
   pip install pandas scikit-learn
````

3. Execute o script:

   ```bash
   python main.py
   ```
4. O arquivo `predicoes.csv` será gerado com as colunas:

   * `id`: identificador de cada entrada
   * `target`: previsão feita pelo modelo

---

## 📈 O que o modelo faz?

* Treina um **classificador de árvore de decisão** usando os dados de treino.
* Remove colunas desnecessárias (`id`, `target`) na preparação.
* Faz previsões com os dados de teste.
* Salva os resultados em um arquivo `.csv` pronto para submissão ou análise.

---

## 🎯 Objetivo

Este projeto foi criado para explorar técnicas de **Inteligência Artificial** e **aprendizado supervisionado**, com foco educacional e competitivo na **ONIA (Olimpíada Nacional de Inteligência Artificial)**.

---

## 👩‍💻 Autora

Desenvolvido por **Priscila Sousa**, com foco em aprendizado e desenvolvimento de habilidades em IA e programação aplicada à resolução de problemas reais.


