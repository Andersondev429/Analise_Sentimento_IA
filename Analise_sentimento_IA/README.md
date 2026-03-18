# 📊 Análise de Sentimento com LLM Local (Gemma + LM Studio)

Este projeto realiza a análise de sentimento de resenhas de produtos utilizando um modelo de linguagem (LLM) executado localmente via LM Studio.

O sistema lê um arquivo CSV contendo usuários e suas resenhas, processa cada entrada com um modelo de IA e retorna os dados estruturados em JSON, permitindo análise com Python e Pandas.

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- OpenAI SDK (compatível com LM Studio)
- LM Studio (LLM local)
- Modelo: Gemma 3B

---

## ⚙️ Como funciona

1. Leitura de um arquivo CSV contendo:
   - Usuário
   - Resenha

2. Envio de cada resenha para um LLM local

3. O modelo retorna um JSON com:
   - `usuario`
   - `resenha_original`
   - `avaliacao` (Positiva, Negativa ou Neutra)

4. Os dados são estruturados em um DataFrame

5. Geração de:
   - Arquivo CSV com resultados
   - Estatísticas de sentimento

---

## 📁 Estrutura esperada do CSV

Arquivo: `resenhas_produto_formatado.csv`

Separador: `;`

Exemplo:

```csv
usuario;resenha
joao123;Produto excelente, gostei muito!
maria456;Não funcionou como esperado
```

---

## ▶️ Como executar

### 1. Instalar dependências

```bash
pip install pandas openai
```

---

### 2. Rodar o LM Studio

- Abra o LM Studio
- Carregue o modelo (ex: `gemma-3-1b`)
- Inicie o servidor local em:

http://127.0.0.1:1234

---

### 3. Executar o script

```bash
python main.py
```

---

## 📊 Exemplo de saída

```json
{
  "usuario": "joao123",
  "resenha_original": "Produto excelente, gostei muito!",
  "avaliacao": "Positiva"
}
```

---

## 📈 Resultado

O projeto gera:

- `respostas.csv` → dataset estruturado
- Contagem de sentimentos:
  - Positivas
  - Negativas
  - Neutras

---

## 💡 Possíveis melhorias

- Processamento assíncrono (melhor performance)
- Dashboard com Streamlit
- Análise de tópicos (principais reclamações e elogios)
- Integração com APIs externas
- Deploy como aplicação web

---

## 🧠 Aprendizados

Este projeto demonstra na prática:

- Integração com LLMs locais
- Engenharia de prompts
- Processamento de dados com Pandas
- Estruturação de dados não estruturados
- Tratamento de erros em respostas de IA

---

## 🔗 Uso para portfólio

Este projeto é ideal para demonstrar habilidades em:

- IA aplicada
- Engenharia de dados
- Automação com Python
- Construção de pipelines com LLM

---

## 📌 Autor

Desenvolvido por Anderson Pinheiro

---

## ⭐ Se este projeto te ajudou

Deixe uma estrela no repositório!
