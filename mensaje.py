from datetime import datetime
import uuid

class Mensaje:
    def __init__(self, emisor, receptor, asunto: str, cuerpo: str, urgente: bool = False):
        self._id = str(uuid.uuid4())
        self._timestamp = datetime.utcnow()
        self._emisor = emisor
        self._receptor = receptor
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._urgente = urgente

    @property
    def id(self) -> str:
        return self._id

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def emisor(self):
        return self._emisor

    @property
    def receptor(self):
        return self._receptor

    @property
    def asunto(self) -> str:
        return self._asunto

    @property
    def cuerpo(self) -> str:
        return self._cuerpo

    @property
    def urgente(self) -> bool:
        return self._urgente

    def __str__(self):
        t = self._timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{t}] De: {self._emisor.email} | Para: {self._receptor.email} | Asunto: {self._asunto} | Urgente: {self._urgente}"
