# 💳🏬 Superstore Korea 2025 - Análisis de Ventas y Tendencias

## 📌 Descripción del proyecto

Este proyecto analiza un dataset de una tienda retail en Corea del Sur.
El objetivo es identificar insights clave relacionados con ventas, rentabilidad, descuentos y devoluciones para apoyar la toma de decisiones de negocio.

---

## 🎯 Objetivos

- Analizar la distribución de ventas por categoría y región
- Identificar las categorías más rentables
- Evaluar el impacto de los descuentos en la rentabilidad
- Analizar la tasa de devoluciones

---

## 🛠 Herramientas utilizadas

- Python (Pandas) → limpieza y análisis de datos
- Jupyter Notebook → análisis exploratorio
- Power BI → visualización de datos (en proceso)

---

## 🧹 Limpieza de datos

- Traducción de columnas del coreano a inglés
- Estandarización de variables categóricas (segmento, categoría, envíos)
- Conversión de fechas a formato datetime
- Limpieza de valores booleanos en la columna "returned"
- Validación de calidad de datos (sin valores nulos y tipos correctos)

---

## 📊 Insights clave

- Office Supplies es la categoría con mayor volumen de ventas, lo que indica alta demanda, pero no necesariamente alta rentabilidad.
- Technology es la categoría más rentable, lo que sugiere mejores márgenes de ganancia.
- Los descuentos mayores al 25% generan pérdidas significativas.
- La tasa de devoluciones es de aproximadamente 7.13%, considerada moderada pero con impacto en la rentabilidad.
- Las ventas se concentran en regiones clave como Seúl (서울특별시) y Gyeonggi (경기도).
- Existe estacionalidad en las ventas, con picos en junio, agosto, octubre y noviembre.

---

## 🧠 Conclusiones

- Un alto volumen de ventas no garantiza rentabilidad
- La estrategia de descuentos impacta directamente en las ganancias
- El negocio depende de ciertas regiones clave
- Las devoluciones y descuentos combinados afectan negativamente el margen

---

## 💡 Recomendaciones

- Reducir descuentos agresivos (>25%)
- Priorizar la categoría Technology por su alta rentabilidad
- Analizar productos con alta tasa de devolución
- Expandir la presencia en regiones con menor participación

---
## 📂 Estructura del proyecto

superstore-korea-analysis/
│
├── data/
│   └── KR_Superstore_sample_2025.csv
|   └── KR_superstore_clean.csv
|
│
├── notebooks/
│   └── analysis.ipynb
│
├── images/
│
└── README.md

---

## 🐍 Proyecto en Python
Este proyecto fue desarrollado en Python por **Barbara Badillo** para análisis de datos.

