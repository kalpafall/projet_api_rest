import psycopg2
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

def get_connection():
    """
    Crée et retourne une connexion PostgreSQL en utilisant psycopg2
    Les paramètres sont récupérés à partir des variables d'environnement.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print("Erreur lors de la connexion à la base de données:", e)
        return None
