# StockGuard 🚀

Sistema automatizado para la gestión y clasificación de inventarios, desarrollado como proyecto práctico para la asignatura de **Big Data**. El proyecto cuenta con una arquitectura modular en Python, pruebas unitarias automatizadas y un flujo de Integración Continua (CI) a través de GitHub Actions.

---

## 📂 Estructura del Proyecto

```text
github-actions-stockguard/
├── .github/
│   └── workflows/
│       └── ci.yml             # Configuración de GitHub Actions (CI)
├── src/
│   ├── __init__.py
│   └── inventario.py          # Lógica principal de clasificación de stock
├── tests/
│   └── test_inventario.py     # Pruebas unitarias con Pytest
├── README.md                  # Documentación del proyecto
└── requirements.txt           # Dependencias del sistema (pytest)
```

---

## 🛠️ Desarrollo e Hitos Alcanzados

1. **Inicialización del Entorno:** Configuración inicial del repositorio local Git en la rama principal `main`.
2. **Vinculación Remota:** Creación del repositorio en la nube y enlace con GitHub (`origin`).
3. **Casos de Prueba:** Cobertura de código mediante 5 pruebas unitarias locales orientadas a evaluar los diferentes estados del inventario (Agotado, Crítico, Bajo, Normal, Inválido).
4. **Automatización:** Configuración exitosa de un pipeline de Integración Continua que valida la sintaxis y ejecuta las pruebas en un contenedor Linux limpio ante cada cambio del código.

---

## 📝 Bitácora de Errores y Soluciones (Troubleshooting)

Durante el despliegue del proyecto en entornos locales y remotos se solventaron los siguientes inconvenientes técnicos:

### 1. Error de Rutas en Local (`ModuleNotFoundError: No module named 'src'`)
* **Problema:** Al ejecutar el comando directo `pytest -v` en la terminal de Windows, Python no lograba reconocer la carpeta raíz del proyecto y fallaba al importar los módulos desde `src`.
* **Solución:** Se cambió el método de ejecución al modo módulo de Python (`python -m pytest -v`), lo que obliga al intérprete a inyectar el directorio de trabajo actual directamente en el `sys.path`.

### 2. Concatenación de Comandos en YAML (`no such option: -m`)
* **Problema:** En el flujo de trabajo de GitHub Actions, los comandos de actualización de `pip` e instalación de dependencias se agruparon incorrectamente en una sola línea. Al ejecutarse consecutivamente sin separación formal, la consola asumió que `-m` era un parámetro erróneo del gestor de paquetes.
* **Solución:** Se utilizó el operador de bloque multilínea de YAML (`run: |`) estructurando las instrucciones en líneas independientes y limpias.

### 3. Falla de Localización en Servidor de CI (Entorno Linux)
* **Problema:** Al igual que en la máquina local, el contenedor automatizado fallaba en la ejecución de la prueba final debido a que invocaba a Pytest sin el contexto de la ruta raíz.
* **Solución:** Se migró el paso de testing en el archivo `ci.yml` a la instrucción estandarizada `python -m pytest -v`.

---

## ⚙️ Pipeline de GitHub Actions (`ci.yml`)

El flujo automatizado actual realiza las siguientes tareas en cada `push` o `pull_request`:
* Descarga el código actualizado (`actions/checkout@v4`).
* Despliega un entorno aislado con Python 3.12 (`actions/setup-python@v5`).
* Instala de forma limpia las dependencias de `requirements.txt`.
* Realiza un escaneo preventivo de la sintaxis del código completo con `compileall`.
* Ejecuta el conjunto de pruebas unitarias esperando un resultado 100% exitoso (`PASSED`).
