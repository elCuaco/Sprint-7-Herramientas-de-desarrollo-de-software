# 🚗 Sprint 7 - Proyecto de Análisis de Vehículos

## Descripción General

Este repositorio contiene el proyecto completo del Sprint 7, que consiste en el desarrollo de una aplicación web interactiva para el análisis de datos de anuncios de venta de coches en Estados Unidos. El proyecto demuestra habilidades en ingeniería de software, análisis de datos, desarrollo web y despliegue en la nube.

## Objetivo del Proyecto

Desarrollar y desplegar una aplicación web que permita explorar y visualizar datos de vehículos mediante gráficos interactivos, utilizando Python, Streamlit, Plotly Express y servicios de despliegue en la nube (Render).

## Estructura del Proyecto

```
sprint7_project/
│
├── notebooks/
│   └── EDA.ipynb                    # Análisis Exploratorio de Datos
│
├── version_buttons/
│   ├── app.py                       # Aplicación con botones
│   ├── vehicles_us.csv              # Dataset
│   ├── requirements.txt             # Dependencias
│   └── README.md                    # Documentación específica
│
├── version_checkboxes/
│   ├── app.py                       # Aplicación con checkboxes
│   ├── vehicles_us.csv              # Dataset
│   ├── requirements.txt             # Dependencias
│   └── README.md                    # Documentación específica
│
├── vehicles_us.csv                  # Dataset principal
├── .gitignore                       # Archivos ignorados por Git
└── README.md                        # Este archivo
```

## Componentes del Proyecto

### 1. Análisis Exploratorio de Datos (EDA)

El notebook `notebooks/EDA.ipynb` contiene:
- Carga y exploración inicial del dataset
- Estadísticas descriptivas
- Visualizaciones con Plotly Express:
  - Histogramas de kilometraje y precios
  - Gráficos de dispersión
  - Análisis de correlación
  - Box plots por condición
  - Gráficos de barras por tipo de vehículo

### 2. Aplicación Web - Versión con Botones

Ubicación: `version_buttons/`

**Características:**
- Interfaz simple e intuitiva
- Botones para generar visualizaciones bajo demanda
- Histograma del odómetro
- Gráfico de dispersión precio vs kilometraje
- Métricas del dataset
- Visualización de datos en bruto

**Ideal para:** Usuarios que prefieren una experiencia guiada y simple

### 3. Aplicación Web - Versión con Checkboxes

Ubicación: `version_checkboxes/`

**Características:**
- Interfaz más flexible y personalizable
- Casillas de verificación para seleccionar visualizaciones
- Múltiples visualizaciones simultáneas
- Histograma del odómetro
- Histograma de precios
- Gráfico de dispersión precio vs kilometraje
- Gráfico de dispersión con color por condición
- Métricas del dataset
- Visualización de datos en bruto

**Ideal para:** Usuarios que desean comparar múltiples visualizaciones al mismo tiempo

## Dataset

El archivo `vehicles_us.csv` contiene **51,525 registros** de anuncios de venta de coches con las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| `price` | Precio del vehículo (USD) |
| `model_year` | Año del modelo |
| `model` | Modelo del vehículo |
| `condition` | Condición (excellent, good, fair, etc.) |
| `cylinders` | Número de cilindros |
| `fuel` | Tipo de combustible |
| `odometer` | Kilometraje |
| `transmission` | Tipo de transmisión |
| `type` | Tipo de vehículo (sedan, SUV, pickup, etc.) |
| `paint_color` | Color del vehículo |
| `is_4wd` | Tracción 4x4 (1.0 = sí) |
| `date_posted` | Fecha de publicación |
| `days_listed` | Días que estuvo activo el anuncio |

## Tecnologías Utilizadas

- **Python 3.11**: Lenguaje de programación
- **Pandas**: Manipulación y análisis de datos
- **Plotly Express**: Visualizaciones interactivas
- **Streamlit**: Framework para aplicaciones web
- **Jupyter Notebook**: Análisis exploratorio
- **Git/GitHub**: Control de versiones
- **Render**: Plataforma de despliegue en la nube

## Instalación y Configuración

### Requisitos Previos

- Python 3.11 o superior
- Git
- Cuenta en GitHub
- Cuenta en Render (opcional, para despliegue)

### Configuración del Entorno

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd sprint7_project
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv vehicles_env
   ```

3. **Activar entorno virtual**
   - Windows:
     ```bash
     vehicles_env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source vehicles_env/bin/activate
     ```

4. **Instalar dependencias** (para cualquiera de las versiones)
   ```bash
   cd version_buttons  # o version_checkboxes
   pip install -r requirements.txt
   ```

## Ejecución Local

### Ejecutar el Notebook de EDA

```bash
jupyter notebook notebooks/EDA.ipynb
```

### Ejecutar la Aplicación Web (Versión Botones)

```bash
cd version_buttons
streamlit run app.py
```

### Ejecutar la Aplicación Web (Versión Checkboxes)

```bash
cd version_checkboxes
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

## Despliegue en Render

### Pasos para Desplegar

1. **Crear cuenta en Render**: Visita [render.com](https://render.com) y vincula tu cuenta de GitHub

2. **Crear nuevo Web Service**:
   - Selecciona tu repositorio
   - Elige la carpeta de la versión que deseas desplegar

3. **Configurar comandos**:
   - **Build Command**: 
     ```bash
     pip install --upgrade pip && pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```bash
     streamlit run app.py
     ```

4. **Desplegar**: Haz clic en "Create Web Service"

5. **Acceder**: Tu aplicación estará disponible en `https://<APP_NAME>.onrender.com/`

### Actualizar la Aplicación

```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

En Render: "Manual Deploy" → "Latest Commit"

## Comparación de Versiones

| Característica | Versión Botones | Versión Checkboxes |
|----------------|-----------------|---------------------|
| Interfaz | Simple y directa | Flexible y personalizable |
| Visualizaciones | 2 gráficos | 4 gráficos |
| Interacción | Botones (uno a la vez) | Checkboxes (múltiples) |
| Visualización simultánea | No | Sí |
| Complejidad | Baja | Media |
| Ideal para | Principiantes | Usuarios avanzados |

## Buenas Prácticas Implementadas

✅ Código limpio y bien documentado  
✅ Estructura de proyecto organizada  
✅ Control de versiones con Git  
✅ Entornos virtuales para dependencias  
✅ Archivo .gitignore configurado  
✅ Documentación completa (README)  
✅ Análisis exploratorio previo  
✅ Visualizaciones interactivas  
✅ Métricas y estadísticas relevantes  
✅ Interfaz de usuario intuitiva  

## Aprendizajes Clave

Este proyecto permitió practicar:
- Creación y gestión de entornos virtuales de Python
- Desarrollo de aplicaciones web con Streamlit
- Visualización de datos con Plotly Express
- Análisis exploratorio de datos con Pandas
- Control de versiones con Git y GitHub
- Despliegue de aplicaciones en la nube con Render
- Documentación técnica de proyectos

## Próximos Pasos

Posibles mejoras futuras:
- Agregar filtros interactivos por tipo de vehículo, año, condición
- Implementar análisis predictivo de precios
- Añadir mapas geográficos si se incluyen datos de ubicación
- Crear dashboard con múltiples páginas
- Implementar caché para mejorar rendimiento
- Agregar tests unitarios

## Autor

Proyecto desarrollado como parte del Sprint 7 del programa de Análisis de Datos

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## Recursos Adicionales

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Documentación de Plotly Express](https://plotly.com/python/plotly-express/)
- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Guía de Render](https://render.com/docs)

---

**Nota**: Este proyecto incluye dos versiones completas de la aplicación web. Puedes elegir la que mejor se adapte a tus necesidades o usarlas como referencia para aprender diferentes enfoques de desarrollo.
