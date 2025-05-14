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

    

    def close(self):
        if self.conn:
            self.conn.close()
