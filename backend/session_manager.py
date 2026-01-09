import asyncio

class SessionManager:
    def __init__(self):
        self.sessions = {}

    async def create_session(self, session_id):
        self.sessions[session_id] = asyncio.Queue()

    async def close_session(self, session_id):
        self.sessions.pop(session_id, None)
