import requests

def main():
    # 1️⃣ Solicitar o número do aluno
    numero_aluno = int(input("Digite o seu número de aluno: "))

    # 2️⃣ Obter todos os países da API (especificando os campos necessários)
    url = "https://restcountries.com/v3.1/all?fields=name,population,currencies"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao obter os dados da API.")
        return

    paises = response.json()

    # 3️⃣ Selecionar o país com base no número do aluno (mod para não ultrapassar o índice)
    indice = numero_aluno % len(paises)
    pais = paises[indice]

    # 4️⃣ Extrair o nome do país
    nome_pais = pais.get("name", {}).get("common", "Desconhecido")

    # 5️⃣ Extrair dinamicamente o nome da moeda e o símbolo
    moedas = pais.get("currencies", {})
    if moedas:
        primeira_chave = list(moedas.keys())[0]  # pega a primeira chave do dicionário
        nome_moeda = moedas[primeira_chave].get("name", "Desconhecida")
        simbolo_moeda = moedas[primeira_chave].get("symbol", "?")
    else:
        nome_moeda = "Desconhecida"
        simbolo_moeda = "?"

    # 6️⃣ Calcular o Índice de Riqueza Fictícia
    populacao = pais.get("population", 0)
    letras_nome = len(nome_pais)
    indice_riqueza = populacao / letras_nome if letras_nome > 0 else 0

    # 7️⃣ Apresentar a saída formatada
    print(f"O país sorteado pelo aluno {numero_aluno} é {nome_pais}. "
          f"A sua moeda é {nome_moeda} ({simbolo_moeda}) "
          f"e o Índice é {indice_riqueza:.2f}.")

if __name__ == "__main__":
    main()
