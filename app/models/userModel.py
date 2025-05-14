# usersModel.py
from config import get_connection

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
