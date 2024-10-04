{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7fafd60f-3067-468b-895a-5b17b20ca4cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from scipy.stats import boxcox\n",
    "\n",
    "def carregar_dados(file_path):\n",
    "    \"\"\"Carrega os dados de um arquivo Excel.\"\"\"\n",
    "    dados = pd.read_excel(file_path)\n",
    "    return dados\n",
    "\n",
    "def transformar_boxcox(dados, coluna):\n",
    "    \"\"\"Aplica a transformação de Box-Cox em uma coluna específica.\"\"\"\n",
    "    dados[coluna], _ = boxcox(dados[coluna])\n",
    "    return dados"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
