import streamlit as st

st.set_page_config(page_title="GreenWings AI", layout="wide")

# Sidebar de navegación
st.sidebar.title("Menú de Navegación")
seccion = st.sidebar.radio("Ir a:", [
    "Inicio",
    "Producto",
    "Beneficios",
    "Casos de uso",
    "Demo",
    "Contacto"
])

# Contenido de secciones
if seccion == "Inicio":
    st.title("🌍 GreenWings AI")
    st.subheader("Sustainable Aviation Compliance & Optimization Platform")
    st.markdown("""
    GreenWings AI es la solución que permite a las aerolíneas cumplir con normativas medioambientales de forma proactiva, optimizar el uso de SAF (combustibles sostenibles) y reducir sanciones y emisiones.
    """)

elif seccion == "Producto":
    st.header("🧠 Plataforma Inteligente")
    st.markdown("""
    - **Monitoreo de consumo y emisiones** en tiempo real
    - **Alertas predictivas de incumplimiento** normativo (tankering, SAF)
    - **Simulaciones de escenarios regulatorios y rutas óptimas**
    - **Reportes automatizados para auditores y stakeholders**
    """)

elif seccion == "Beneficios":
    st.header("📈 Beneficios Estratégicos")
    col1, col2, col3 = st.columns(3)
    col1.metric("🚫 Multas evitadas", "hasta 150.000 €", "por vuelo")
    col2.metric("🌱 SAF optimizado", "+30%", "uso efectivo")
    col3.metric("🏆 Reputación ESG", "↑ fuerte", "impacto positivo")

elif seccion == "Casos de uso":
    st.header("✈️ Aplicaciones Reales")
    st.markdown("""
    - Flotas expuestas al Reglamento (UE) 2023/2405 (antitankering)
    - Aerolíneas que reportan a sistemas de verificación ambiental (EU-ETS, CORSIA)
    - Directivos que necesitan simulaciones de cumplimiento financiero/regulatorio
    """)

elif seccion == "Demo":
    st.header("🧪 Demo Interactiva")
    st.markdown("Explora la demo funcional [aquí](https://aerosustain-demo.streamlit.app/) y conoce cómo predecimos riesgos y optimizamos sostenibilidad.")

elif seccion == "Contacto":
    st.header("📬 Conversemos")
    st.markdown("""
    ¿Quieres evitar sanciones y mejorar tu posicionamiento ESG?
    Escríbenos:

    📧 contacto@greenwings.ai  

    """)

# Footer
st.markdown("""
---
(c) 2025 GreenWings AI. Todos los derechos reservados.
""")
