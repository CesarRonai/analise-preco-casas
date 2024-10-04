from src.preprocessamento import carregar_dados, transformar_boxcox
from src.modelagem import treinar_modelo
from src.visualizacao import plot_residuos

def main():
    # Carregar dados
    dados = carregar_dados('data/preço_casas.xlsx')

    # Transformar dados
    dados = transformar_boxcox(dados, 'preco')

    # Treinar modelo
    modelo = treinar_modelo(dados, ['area_sqm', 'quartos', 'banheiros', 'vagas_garagem'], 'preco')

    # Visualizar resíduos
    plot_residuos(modelo)

if __name__ == '__main__':
    main()
