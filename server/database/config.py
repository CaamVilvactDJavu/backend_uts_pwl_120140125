from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/backend_uts_ilham")
