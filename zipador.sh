#! /usr/bin/env bash

PDF=${1}
PASTA=${2}
N=${PASTA: -1}
zip -r ze_zinho_lab$N $PDF $PASTA
