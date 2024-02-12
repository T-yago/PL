# Abrir o arquivo CSV
with open("emd.csv", "r") as file:
    lines = file.readlines()

# Remover o cabeçalho
header = lines.pop(0)
header_columns = header.strip().split(",")

# Dicionário para guardar nomes das colunas para o seu índice   
column_indices = {}
for idx, column_name in enumerate(header_columns):
    column_indices[column_name] = idx

# Verifica colunas requeridas
required_columns = ["nome/primeiro", "nome/último", "idade", "modalidade", "resultado"]
for column_name in required_columns:
    if column_name not in column_indices:
        print(f"Erro: Coluna '{column_name}' não encontrada.")
        exit(1)

# Lista para armazenar as modalidades desportivas
modalidades = []

# Dicionário para contar os atletas por faixa etária
escaloes_etarios = {}

# Dicionário para armazenar os nomes completos dos atletas por faixa etária
nomes_por_faixa_etaria = {}

# Contadores para atletas aptos e inaptos
total_atletas = 0
atletas_aptos = 0

# Processa cada linha do arquivo
for line_number, line in enumerate(lines, start=2):
    # Divide os valores da linha
    values = line.strip().split(",")

    try:
        # Nome do atleta (primeiro e último nome)
        primeiro_nome = values[column_indices["nome/primeiro"]]
        ultimo_nome = values[column_indices["nome/último"]]
        nome_atleta = f"{primeiro_nome} {ultimo_nome}"
        
        # Modalidade desportiva
        modalidade = values[column_indices["modalidade"]]

        # Adicionar a modalidade à lista se ainda não estiver lá
        if modalidade not in modalidades:
            modalidades.append(modalidade)

        # Verificar resultado
        resultado = values[column_indices["resultado"]]
        if resultado == "true":
            atletas_aptos += 1

        # Contar atletas por faixa etária
        idade = int(values[column_indices["idade"]])
        faixa_etaria = (idade // 5) * 5
        if faixa_etaria not in escaloes_etarios:
            escaloes_etarios[faixa_etaria] = []
        escaloes_etarios[faixa_etaria].append(nome_atleta)

        # Incrementar contador total de atletas
        total_atletas += 1

    except ValueError:
        print(f"Erro: Linha {line_number} possui valor inválido para a idade.")
    except IndexError:
        print(f"Erro: Linha {line_number} está faltando alguma(s) coluna(s).")

# Ordenar as modalidades alfabeticamente
modalidades.sort()

# Calcular percentagem de atletas aptos
percentagem_aptos = (atletas_aptos / total_atletas) * 100

# Calcular percentagem de atletas inaptos
percentagem_inaptos = 100 - percentagem_aptos

# Ordenar as faixas etárias
faixas_etarias_ordenadas = sorted(escaloes_etarios.keys())

# Calcular o total de atletas
total_atletas = sum([len(escaloes_etarios[faixa]) for faixa in faixas_etarias_ordenadas])

# Escrever os resultados num ficheiro "resultado.txt"
with open("resultado.txt", "w") as output_file:
    output_file.write("Lista ordenada alfabeticamente das modalidades desportivas:\n")
    for modalidade in modalidades:
        output_file.write(modalidade + "\n")

    output_file.write("\nPercentagem de atletas aptos para a prática desportiva: " + str(percentagem_aptos) + "%\n")
    output_file.write("Percentagem de atletas inaptos para a prática desportiva: " + str(percentagem_inaptos) + "%\n\n")

    output_file.write("Distribuição de atletas por escalão etário:\n")
    for faixa_etaria in faixas_etarias_ordenadas:
        quantidade_atletas = len(escaloes_etarios[faixa_etaria])
        percentagem = (quantidade_atletas / total_atletas) * 100
        output_file.write(f"{faixa_etaria}-{faixa_etaria + 4}: {quantidade_atletas}/{total_atletas} : {percentagem:.2f}%\n")
        for atleta in escaloes_etarios[faixa_etaria]:
            output_file.write(atleta + "\n")
        output_file.write("\n")
