# ✅ Mi App de Tareas

¡Bienvenida/o a _Mi App de Tareas_! Una aplicación web construida con Django, HTML y CSS puro para ayudarte a organizar tus pendientes, tareas semanales y actividades diarias.

---

## 🌟 Funcionalidades

- ✍️ Crear, editar y eliminar tareas fácilmente.
- ✅ Marcar tareas como completadas.
- 🔍 Buscar tareas por título.
- 📆 Filtros: ver tareas de hoy, de la semana, incompletas o todas.
- 📱 Diseño responsivo, adaptable a dispositivos móviles.
- 🎨 Interfaz colorida y amigable.

---

## 🖼️ Vista previa

<img src="https://github.com/CamilaTorres1035/mi-app-de-tareas/blob/main/preview.png" alt="Vista previa de la app" width="600"/>

> 💡 _Guarda esta imagen como `preview.png` en la raíz del repositorio para que se muestre correctamente._

---

## 🚀 Tecnologías usadas

- [Django](https://www.djangoproject.com/) – Framework backend en Python
- HTML5 y CSS3 – Interfaz responsiva y limpia (sin frameworks)
- Plantillas Django – Para mostrar y manejar datos dinámicos

---

## 🛠️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/CamilaTorres1035/mi-app-de-tareas.git
cd mi-app-de-tareas
```
2. Crea un entorno virtual:
```bash
python -m venv env
source env/bin/activate  # en Windows: env\Scripts\activate
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecuta las migraciones y el servidor:
```bash
python manage.py migrate
python manage.py runserver
```
5. Abre en el navegador:
👉 http://127.0.0.1:8000/


👩‍💻 Autora
Camila Torres
🔗 GitHub: CamilaTorres1035

---
## 📌 Notas
- Este proyecto no incluye autenticación de usuarios.

- Base de datos SQLite por defecto (puedes cambiarla en settings.py si deseas usar otra).