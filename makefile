# Makefile para rodar o programa de grafos em Python

.PHONY: run run-pcv4 run-pcv10 run-pcv50 run-pcv177 help clean

# Execução padrão: utiliza o arquivo pcv4.txt
run:
	@echo "Executando com pcv4.txt (padrão)..."
	python3 main.py --file pcv4.txt

# Targets para executar com um arquivo específico
run-pcv4:
	@echo "Executando com pcv4.txt..."
	python3 main.py --file pcv4.txt

run-pcv10:
	@echo "Executando com pcv10.txt..."
	python3 main.py --file pcv10.txt

run-pcv50:
	@echo "Executando com pcv50.txt..."
	python3 main.py --file pcv50.txt

run-pcv177:
	@echo "Executando com pcv177.txt..."
	python3 main.py --file pcv177.txt

# Target para exibir as instruções de uso
help:
	@echo "Makefile para rodar o programa de Grafos"
	@echo "Uso:"
	@echo "  make run         # Executa o programa com o arquivo padrão pcv4.txt"
	@echo "  make run-pcv4    # Executa o programa com o arquivo pcv4.txt"
	@echo "  make run-pcv10   # Executa o programa com o arquivo pcv10.txt"
	@echo "  make run-pcv50   # Executa o programa com o arquivo pcv50.txt"
	@echo "  make run-pcv177  # Executa o programa com o arquivo pcv177.txt"
	@echo "  make help        # Exibe esta mensagem de ajuda"

# Limpeza de arquivos temporários ou cache
clean:
	@echo "Removendo arquivos temporários..."
	rm -rf __pycache__ *.pyc
