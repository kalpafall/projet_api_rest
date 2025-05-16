# usersModel.py
import psycopg2
import os
from dotenv import load_dotenv

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

class UserModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_users(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id, username, email, is_active FROM users;")
                return cur.fetchall()
        except Exception as e:
            print("Erreur lors de la récupération des utilisateurs:", e)
            return []

    def get_user_by_id(self, user_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id, username, email, is_active FROM users WHERE id = %s;", (user_id,))
                return cur.fetchone()
        except Exception as e:
            print("Erreur lors de la récupération de l'utilisateur:", e)
            return None
    def create_user(self, username, email, password_hash):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO users (username, email, password_hash, is_active)
                    VALUES (%s, %s, %s, TRUE)
                    RETURNING id;
                """, (username, email, password_hash))
                self.conn.commit()
                return cur.fetchone()[0]
        except Exception as e:
            print("Erreur lors de la création de l'utilisateur:", e)
            self.conn.rollback()
            return None
    def close(self):
        if self.conn:
            self.conn.close()
if __name__ == "__main__":
    user_model = UserModel()
    users = user_model.get_all_users()
    print(users)
    user_model.close()
