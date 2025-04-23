from mean_var_std import calculate

if __name__ == "__main__":
    # Teste básico
    try:
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        print("Resultado para [0,1,2,3,4,5,6,7,8]:")
        for k, v in result.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Erro: {e}")

    # Teste de erro
    try:
        calculate([1, 2, 3])
    except Exception as e:
        print(f"Erro esperado: {e}") 