# TPC1 : Mapa das Ruas de Braga
## 2024-02-05

## Autor
- a100665
- Tiago Nuno de Magalhães Teixeira

# Resumo

Este trabalho consiste numa "calculadora" que soma todos os números inteiros, positivos ou negativos, contidos num ficheiro de texto, que podem estar interpolados por caracteres não numéricos. Além disso, a "calculadora" apenas somas os inteiros caso esteja "ligada".
Para tal, deve aparecer, antes dos números, a string "ON" ou uma combinação de caracteres upper e lower que formem a mesma, e deixa de contablilizar caso apareça a string "OFF" (ou uma combinação de caracteres upper e lower que formem a mesma).

Para este trabalho foram desenvolvidas 2 versões, uma que não utiliza bibliotecas relacionadas com expressões regulares ou léxicos, fazendo assim um parsing manual, caracter a caracter, do conteúdo lido diretamente do ficheiro, e outra que utiliza a lib "ply.lex" para associar tokens a expressões regulares, sobre as quais se aplicam os determinados tratamentos, nomeadamente, a adição, o print do valor total, e a alteração do estado da "calculadora".

Sempre que esteja escrito no texto o caracter "=", o programa deve imprimir o resultado do inteiro que somou até ao momento, bem como no final do programa correr por completo, por omissão.