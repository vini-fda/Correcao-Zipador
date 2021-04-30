#!/usr/bin/bash

relatorio=${1}
diretorio=${2}

# Numero do laboratório
N=0

# Este é um padrão de formato do nome do relatório(cancerizado)
#
# Primeiro, o nome do diretório tem que conter "KT-213_LabN",
# com N inteiro, podendo começar com 0(exemplo 02), mas não pode ser 0000...
# Por fim, opcionalmente, pode terminar com uma /
# Exemplo: "KT-213_Lab03/"
#
# Para visualizar regex, consulte os sites:
#  - https://regex101.com
#  - https://regexr.com
# E jogue o padrão lá :D
padrao="KT-213_Lab([0-9]*[1-9][0-9]*)\/?$"

# Checar se o diretório existe
# Caso não exista, sair com mensagem de erro
if ! [[ -d $diretorio ]]; then
	echo "Diretório $diretorio não encontrado!"
	exit 1
fi

# Checar se o arquivo existe
# Caso não exista, sair com mensagem de erro
if ! [[ -f $relatorio ]]; then
	echo "Arquivo do relatório $relatorio não encontrado!"
	exit 1
fi

# Identificar se o nome do diretório está de acordo com o padrão
# O padrao é escrito em uma expressão regular(regular expression/regex)
# Aqui, usamos o chamado pattern matching(pesquise no google!)
if [[ $diretorio =~ $padrao ]]; 
	# Se der match...
	then
		# Pegar o 2º grupo de captura da regex, que está entre parênteses ([0-9]+)
		N=${BASH_REMATCH[1]}
		# Zipar o arquivo e o diretório
		zip -r "ze_zinho_lab$N.zip" $relatorio $diretorio
	# Se não der match...
	else
		echo "Erro! Seu diretório tem que ser na forma KT-213_LabN, sendo que N é um número inteiro, ex.: 1, 2, 24, etc"
		exit 1
fi