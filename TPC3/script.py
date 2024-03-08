import sys

def somador(caracteres, resultado):
    somar = True  # Inicialmente, a soma está ativada
    numero_atual = ""
    off_block = False
    
    for i, char in enumerate(caracteres):
        if char.isdigit():
            numero_atual += char
        elif char == '-':
            numero_atual = "-"  # Inicia um novo número negativo
        else:
            if numero_atual: # Se não for um número ou um "-", guarda o valor do inteiro até ao momento e soma-o ao resultado
                if somar and not off_block:
                    resultado += int(numero_atual)
                numero_atual = ""
            
            # Verifica os comandos "On" e "Off" para ativar ou desativar a soma
            if char.upper() == 'O' and i < len(caracteres) - 1: # se o caracter for alguma variação da letra "o" e não for o último caracter da linha
                if caracteres[i+1].upper() == 'N':
                    somar = True
                    off_block = False
                elif i < len(caracteres) - 2 and caracteres[i+1:i+3].upper() == 'FF':
                    somar = False
                    off_block = True
            
            # Se encontrar o caractere "=", imprime o resultado até esse ponto
            elif char == '=':
                print("Resultado da soma até agora:", resultado)
    
    # Verifica se há algum número restante após a última iteração
    if numero_atual and not off_block:
        resultado += int(numero_atual)
    
    return resultado

def main(nome_arquivo):
    try:
        resultado = 0
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                resultado = somador(linha, resultado)
        # Imprime o resultado final após processar todo o arquivo
        print("Resultado final da soma:", resultado)
    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <nome_do_arquivo>")
    else:
        nome_arquivo = sys.argv[1]
        main(nome_arquivo)
