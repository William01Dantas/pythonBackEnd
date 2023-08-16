from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus

# Dados de conexão
user = "root"
password = "Smurf@2006"
host = "localhost"
database = "db_stock"

# Faz o URL encoding da senha
encoded_password = quote_plus(password)

# Cria a URL de conexão
DATABASE_URL = f"mysql+mysqlconnector://{user}:{encoded_password}@{host}/{database}"

try:
    # Cria a engine de conexão
    engine = create_engine(DATABASE_URL)

    # Testa a conexão
    connection = engine.connect()
    print("Conexão bem-sucedida!")

except SQLAlchemyError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

finally:
    if connection:
        connection.close()
