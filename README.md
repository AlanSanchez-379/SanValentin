# Despliegue en Render

1. Sube este repositorio a GitHub (incluye `app.py`, `requirements.txt` y `corazon.py`).

2. En Render crea un nuevo servicio Web conectando el repositorio.

3. Configuración en Render:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

4. Probar localmente:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
gunicorn app:app
```

5. Opcional: pasar un mensaje personalizado en la URL, por ejemplo:

`https://TU_DOMINIO/?message=Te+quiero`
