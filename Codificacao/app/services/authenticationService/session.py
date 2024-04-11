from flask import session


class SessionManager:
    @staticmethod
    def is_logged_in():
        return 'usuario' in session

    @staticmethod
    def get_usuario():
        return session.get('usuario')

    def close_session(self):
        session.clear()