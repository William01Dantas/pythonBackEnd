from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = "Smurf@2006"
encoded_password = quote_plus(password)

DATABASE_URL = f"mysql+mysqlconnector://root:{encoded_password}@localhost/db_stock"

engine = create_engine(DATABASE_URL)