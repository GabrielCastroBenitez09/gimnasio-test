# 🏋️‍♀️ Sistema de Gestión para Gimnasio — Proyecto Programación II

Este repositorio contiene el desarrollo de un sistema para la administración de un gimnasio, construido como proyecto académico para el curso **Programación II — Pregrado en Ciencia de Datos**.

El objetivo del proyecto es aplicar principios de **Programación Orientada a Objetos (POO)**, manejo de archivos para **persistencia de datos**, desarrollo de una **interfaz de línea de comandos (CLI)** y **pruebas automatizadas**, siguiendo buenas prácticas de diseño de software.

---

## 🚀 Funcionalidades

### 👥 Gestión de usuarios
- Registro y administración de clientes y empleados  
- Validación de datos  
- Manejo de roles  

### 📅 Clases y reservas
- Creación y asignación de clases  
- Validación de cupos  
- Cancelación de reservas  
- Historial de actividades  

### 🏋️‍♂️ Equipos del gimnasio
- Registro y control de máquinas  
- Estado y mantenimiento  

### 🧾 Pagos y membresías _(si el equipo lo incluye)_
- Registro de pagos  
- Gestión de membresías activas y vencidas  

### 💾 Persistencia
- Almacenamiento local de datos (JSON / CSV / Pickle según implementación)

### 🛠️ CLI
- Menús interactivos para las operaciones principales  

### ✅ Pruebas
- Pruebas unitarias con `unittest` o `pytest`

---

## 🧱 Arquitectura del proyecto

📦 gimnasio-sistema  
 ┣ 📂 src  
 │ ┣ 📜 usuario.py  
 │ ┣ 📜 cliente.py  
 │ ┣ 📜 empleado.py  
 │ ┣ 📜 maquina.py  
 │ ┣ 📜 gimnasio.py  
 │ ┗ 📜 main.py              # CLI principal  
 ┣ 📂 data  
 │ ┗ 📜 *.json / *.csv       # Persistencia  
 ┣ 📂 tests  
 │ ┗ 📜 test_*.py  
 ┣ 📜 README.md  
 ┣ 📜 requirements.txt  
 ┗ 📜 .gitignore  

---

## 🧪 Ejecución del programa

### ✅ Requisitos
- Python 3.10 o superior  
- Pip  

### ▶️ Instalar dependencias

`pip install -r requirements.txt`

### ▶️ Ejecutar el sistema

`python src/main.py`

### ✅ Ejecutar pruebas

`pytest`

---

## 🧠 Conceptos aplicados

- Programación Orientada a Objetos  
  - Clases, herencia, composición  
  - Encapsulamiento  
  - Métodos mágicos (`__str__`, `__repr__`, etc.)  
- Manejo de archivos para persistencia  
- Control de errores y validaciones  
- CLI con estructuras de control  
- Testing automatizado  
- Buenas prácticas: pep8, modularidad, docstrings  

---

## 🌟 Extensiones posibles (opcionales)

- Lista de espera automática para clases llenas  
- Reportes por rango de fechas o entrenador  
- Exportación de reportes a CSV  
- Decorador para logging de acciones  
- Uso de context manager (`__enter__`, `__exit__`)

---

## 👨‍💻 Equipo de desarrollo

| Integrante | Rol | Contacto |
|-----------|-----|---------|
| Nombre 1 | Backend / Persistencia | @github |
| Nombre 2 | CLI / Control de flujo | @github |
| Nombre 3 | Testing / QA | @github |
| Nombre 4 | Documentación / UX CLI | @github |

> **Profesor:** Camilo Andrés De la Cruz Arboleda  

---

## 📜 Licencia

Proyecto académico — uso educativo.
