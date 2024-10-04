{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "afcef77f-1744-49d4-b5d8-c95181d8ad59",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import statsmodels.api as sm\n",
    "\n",
    "def plot_residuos(modelo):\n",
    "    \"\"\"Gera gráficos de resíduos para avaliar o modelo.\"\"\"\n",
    "    residuos = modelo.resid\n",
    "    sns.histplot(residuos, kde=True)\n",
    "    plt.title('Distribuição dos Resíduos')\n",
    "    plt.show()\n",
    "\n",
    "    sm.qqplot(residuos, line='s')\n",
    "    plt.title('Gráfico Q-Q dos Resíduos')\n",
    "    plt.show()\n"
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
