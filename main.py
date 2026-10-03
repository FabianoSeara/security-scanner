import scanner

def main():
    caminho_pasta = input("Digite o caminho da pasta: ")
    print(f"\n Iniciando a varredura: {caminho_pasta}")

    scanner.scan_folder(caminho_pasta)

    print("\n Varredura concluída.")


if __name__== "__main__":
    main()

