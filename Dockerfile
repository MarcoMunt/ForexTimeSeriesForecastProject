FROM python:3.9-slim

# Instala as dependências do projeto
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para a pasta /app
COPY ./src /app

# Configura o diretório padrão para /app
WORKDIR /app

# Expõe a porta 5000, porta utilizada pelo Flask
EXPOSE 5000

# Executa o arquivo inference.py quando o container for iniciado
CMD ["python", "inference.py"]