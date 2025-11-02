class Mensaje:
    def __init__(self, emisor, receptor, asunto: str, cuerpo: str):
        self._emisor = emisor 
        self._receptor = receptor 
        self._asunto = asunto 
        self._cuerpo = cuerpo 

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

    def __str__(self):
        return f"De: {self._emisor.email} | Para: {self._receptor.email} | Asunto: {self._asunto} | Cuerpo: {self._cuerpo}"