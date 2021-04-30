# Especificações do exercício

Sintaxe do comando:

```shell
zezinho@linux$ ./zipador.sh <relatorio> <diretorio>
```

Em que `<relatorio>` é o nome do arquivo do relatório, e `<diretorio>` é o nome do diretório(ou pasta). Ambos estarão no mesmo diretório do arquivo `zipador.sh`

- O diretório terá um nome do tipo `KT-213_LabN`, em que `N` é um inteiro, tal que `1 <= N <= 9`;
- O arquivo do relatório poderá ter qualquer nome, e.g. `meu_relatorio.pdf` ou `oi.txt`;
- Os conteúdos do diretório devem ser integralmente comprimidos. Se, por exemplo, ele tiver três imagens e um vídeo, todas esses arquivos devem ser "zipados";

Exemplo de uso:

Digamos que eu tenha a pasta `KT-213_Lab3`, com 5 arquivos de texto, e um relatório `relatorio.pdf`. Então, para criar o arquivo `ze_zinho_lab3.zip`, com a pasta e o relatório comprimidos dentro dele, basta executar o script da seguinte maneira:

```shell
zezinho@linux$ ./zipador.sh relatorio.pdf KT-213_Lab3
```

# Critério de nota
1. (40%) O nome do arquivo de saída deve estar correto, com o padrão `ze_zinho_labN.zip`, e `N` deve ser o mesmo do arquivo `KT-213_LabN`
2. (20%) O diretório deve ter sido comprimido corretamente, com todos os arquivos filhos nele
3. (20%) O programa deve rodar sem erros
4. (10%) O código deve ser livre de erros de sintaxe(passível de zerar tudo se o código estiver totalmente errado)
5. (10%) O código deve ser comentado, quando necessário, para maior clareza. Se o código já estiver claro, os comentários podem ser dispensados(depende caso a caso)


# Como são executados os testes?

Para executar os testes, foi criado um script de python (`main.py`) para criar os arquivos e enviá-los para seu script.

Se você quiser testar por conta própria, basta ter python 3 e git instalado em seu linux, e rodar `make run` após clonar este repositório. Seu arquivo `zipador.sh` deve ser copiado para o seu repositório local.

Para limpar os arquivos e pastas criados no diretório, faça `make clean`.
