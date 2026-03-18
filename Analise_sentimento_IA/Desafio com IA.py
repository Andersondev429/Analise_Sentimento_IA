from openai import OpenAI
import json
import pandas as pd

# =========================
# CONFIGURAÇÃO DO CLIENT
# =========================
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

# =========================
# FUNÇÃO: CHAMAR LLM
# =========================


def analisar_resenha(resenha):
    resposta = client.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {
                "role": "system",
                "content": """
Você é um especialista em análise de dados.

Receberá uma resenha de produto.
Retorne um JSON com:
- usuario
- resenha_original
- avaliacao ('Positiva', 'Negativa' ou 'Neutra')

Regras:
- Responda APENAS com JSON válido
- Não escreva nada fora do JSON
- Se não tiver certeza, use "Neutra"
"""
            },
            {
                "role": "user",
                "content": f"Resenha: {resenha}"
            }
        ],
        temperature=0.0
    )

    return resposta.choices[0].message.content


# =========================
# FUNÇÃO: PARSE SEGURO
# =========================
def parse_json_seguro(resposta):
    try:
        resposta_limpa = resposta.replace("```json", "").replace("```", "")
        return json.loads(resposta_limpa)
    except Exception as e:
        print(f"Erro ao converter JSON: {e}")
        print(f"Resposta recebida: {resposta}")
        return None


# =========================
# FUNÇÃO: CONTADOR
# =========================
def contar_avaliacoes(lista):
    contagem = {
        "Positiva": 0,
        "Negativa": 0,
        "Neutra": 0
    }

    for item in lista:
        avaliacao = item.get("avaliacao", "Neutra")
        if avaliacao in contagem:
            contagem[avaliacao] += 1

    return contagem


# =========================
# ETAPA 1: LER CSV
# =========================
df_entrada = pd.read_csv("resenhas_produto_formatado.csv", sep=";")

lista_resenhas = (
    df_entrada["usuario"] + ": " + df_entrada["resenha"]
).tolist()

# =========================
# ETAPA 2: PROCESSAR
# =========================
resultados = []

for resenha in lista_resenhas:
    resposta = analisar_resenha(resenha)
    resenha_dict = parse_json_seguro(resposta)

    if resenha_dict:
        resultados.append(resenha_dict)

# =========================
# ETAPA 3: CRIAR DATAFRAME
# =========================
df_resultado = pd.DataFrame(resultados)

# =========================
# ETAPA 4: SALVAR CSV
# =========================
df_resultado.to_csv("respostas.csv", index=False, encoding="utf-8")

# =========================
# ETAPA 5: MÉTRICAS
# =========================
contagem = contar_avaliacoes(resultados)

print("\nResumo das avaliações:")
print(f"Positivas: {contagem['Positiva']}")
print(f"Negativas: {contagem['Negativa']}")
print(f"Neutras: {contagem['Neutra']}")
