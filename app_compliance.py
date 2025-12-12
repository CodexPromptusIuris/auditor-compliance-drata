import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Gestor de Cumplimiento y Auditoría", layout="wide")

# --- CARGA DE DATOS (Basado en el PDF proporcionado) ---
# Se han extraído las políticas clave y sus marcos asociados del documento.
@st.cache_data
def load_data():
    data = [
        {
            "Política": "Política de uso aceptable",
            "Descripción": "Especifica el uso aceptable de dispositivos y tecnología.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "CCPA", "COBIT 2019", "HIPAA", "SOC 2", "PCI DSS"],
            "Control Principal": "DCF-37",
            "Fuente": "Página 2"
        },
        {
            "Política": "Política de gestión de activos",
            "Descripción": "Define la implementación y documentación de activos.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "HIPAA", "NIST CSF 2.0", "SOC 2"],
            "Control Principal": "DCF-182",
            "Fuente": "Página 3"
        },
        {
            "Política": "Política de copias de seguridad",
            "Descripción": "Define procedimientos para copiar información y recuperación de datos.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "HIPAA", "PCI DSS v4.0", "SOC 2"],
            "Control Principal": "DCF-169",
            "Fuente": "Página 4"
        },
        {
            "Política": "Plan de Continuidad del Negocio",
            "Descripción": "Describe cómo la empresa continuará operaciones durante interrupciones.",
            "Marcos Clave": ["ISO/IEC 27001:2022", "SOC 2", "FedRAMP", "HIPAA"],
            "Control Principal": "DCF-166",
            "Fuente": "Página 6"
        },
        {
            "Política": "Código de conducta",
            "Descripción": "Define el comportamiento esperado de los empleados.",
            "Marcos Clave": ["ISO/IEC 27001:2022", "SOC 2", "CCPA", "COBIT 2019"],
            "Control Principal": "DCF-44",
            "Fuente": "Página 7"
        },
        {
            "Política": "Política de clasificación de datos",
            "Descripción": "Define objetivos e instrucciones para clasificar datos.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "HIPAA", "SOC 2"],
            "Control Principal": "DCF-102",
            "Fuente": "Página 8"
        },
        {
            "Política": "Política de retención de datos",
            "Descripción": "Describe cuándo los datos deben eliminarse o retenerse.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "CCPA", "SOC 2"],
            "Control Principal": "DCF-101",
            "Fuente": "Página 9"
        },
        {
            "Política": "Política de protección de datos",
            "Descripción": "Procedimientos y controles técnicos para proteger datos.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "HIPAA", "SOC 2", "NIST CSF"],
            "Control Principal": "DCF-45",
            "Fuente": "Página 10"
        },
        {
            "Política": "Plan de Recuperación ante Desastres",
            "Descripción": "Enfoque estructurado para reanudar el trabajo tras un incidente.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "SOC 2", "HIPAA"],
            "Control Principal": "DCF-25",
            "Fuente": "Página 11"
        },
        {
            "Política": "Política de cifrado (Encryption)",
            "Descripción": "Establece tipos de datos y dispositivos que deben cifrarse.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "HIPAA", "SOC 2", "PCI DSS"],
            "Control Principal": "DCF-181",
            "Fuente": "Página 13"
        },
        {
            "Política": "Plan de Respuesta a Incidentes",
            "Descripción": "Procedimientos para detección y reacción ante brechas de seguridad.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "SOC 2", "NIST CSF"],
            "Control Principal": "DCF-159",
            "Fuente": "Página 14"
        },
        {
            "Política": "Política de Seguridad de la Información",
            "Descripción": "Reglas y procedimientos para seguridad TI mínima.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "SOC 2", "NIST CSF"],
            "Control Principal": "DCF-13",
            "Fuente": "Página 15"
        },
        {
            "Política": "Política de Contraseñas",
            "Descripción": "Procedimiento para seleccionar y gestionar contraseñas.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "PCI DSS", "SOC 2"],
            "Control Principal": "DCF-68",
            "Fuente": "Página 16"
        },
        {
            "Política": "Política de Gestión de Proveedores",
            "Descripción": "Reglas para relaciones con proveedores de TI.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "GDPR", "SOC 2"],
            "Control Principal": "DCF-168",
            "Fuente": "Página 23"
        },
         {
            "Política": "Política de Gestión de Vulnerabilidades",
            "Descripción": "Procedimientos para descubrir y remediar vulnerabilidades.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "SOC 2", "PCI DSS"],
            "Control Principal": "DCF-183",
            "Fuente": "Página 24"
        },
        {
            "Política": "Política de Control de Acceso",
            "Descripción": "Define onboarding/offboarding y minimización de riesgo de acceso.",
            "Marcos Clave": ["FedRAMP", "ISO/IEC 27001:2022", "SOC 2", "HIPAA"],
            "Control Principal": "DCF-10",
            "Fuente": "Página 21"
        }
    ]
    return pd.DataFrame(data)

df = load_data()

# --- SIDEBAR ---
st.sidebar.title("🛡️ Centro de Auditoría")
st.sidebar.info("Basado en el 'Resumen de políticas del marco' de Drata.")
page = st.sidebar.radio("Navegación", ["Explorador de Políticas", "Auditoría de Empresa", "Análisis de Marcos"])

# --- PÁGINA 1: EXPLORADOR ---
if page == "Explorador de Políticas":
    st.title("📂 Explorador de Políticas y Controles")
    [span_4](start_span)[span_5](start_span)st.markdown("Base de datos extraída del documento de políticas[span_4](end_span)[span_5](end_span).")
    
    # Filtros
    all_frameworks = sorted(list(set([item for sublist in df['Marcos Clave'] for item in sublist])))
    selected_framework = st.selectbox("Filtrar por Marco Normativo (Framework):", ["Todos"] + all_frameworks)
    
    if selected_framework != "Todos":
        filtered_df = df[df['Marcos Clave'].apply(lambda x: selected_framework in x)]
    else:
        filtered_df = df
    
    st.write(f"Mostrando **{len(filtered_df)}** políticas aplicables para **{selected_framework}**.")
    
    # Mostrar tabla interactiva
    st.dataframe(
        filtered_df[['Política', 'Descripción', 'Control Principal', 'Marcos Clave']],
        use_container_width=True,
        hide_index=True
    )
    
    [span_6](start_span)st.caption("Los controles 'DCF' refieren a los controles internos del marco común definidos en el documento fuente[span_6](end_span).")

# --- PÁGINA 2: AUDITORÍA ---
elif page == "Auditoría de Empresa":
    st.title("✅ Simulación de Auditoría de Cumplimiento")
    st.markdown("Seleccione las políticas que su empresa ya tiene implementadas para calcular su brecha de cumplimiento.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Lista de Verificación")
        # Checkbox para cada política
        selected_policies = []
        for index, row in df.iterrows():
            if st.checkbox(f"{row['Política']} ({row['Control Principal']})", key=index):
                selected_policies.append(row['Política'])
    
    with col2:
        st.subheader("Resultados")
        total_policies = len(df)
        implemented = len(selected_policies)
        score = (implemented / total_policies) * 100
        
        st.metric(label="Puntaje de Cumplimiento Global", value=f"{score:.1f}%")
        
        # Gráfico de progreso
        fig = px.pie(values=[implemented, total_policies - implemented], names=['Implementado', 'Pendiente'], 
                     title="Estado de Implementación", hole=0.5, color_discrete_sequence=['#00CC96', '#EF553B'])
        st.plotly_chart(fig, use_container_width=True)
        
        if score < 100:
            st.warning("⚠️ Faltan políticas críticas para el cumplimiento total.")
        else:
            st.success("🎉 ¡Todas las políticas del marco están cubiertas!")

    # Análisis de Brechas (Gap Analysis)
    if implemented < total_policies:
        st.divider()
        st.subheader("🚨 Análisis de Brechas (Gap Analysis)")
        missing_policies = df[~df['Política'].isin(selected_policies)]
        st.write("Las siguientes políticas son requeridas pero no están marcadas:")
        for idx, row in missing_policies.iterrows():
            st.error(f"**{row['Política']}**: {row['Descripción']} (Requerido para: {', '.join(row['Marcos Clave'][:3])}...)")

# --- PÁGINA 3: ANÁLISIS DE MARCOS ---
elif page == "Análisis de Marcos":
    st.title("📊 Análisis por Normativa")
    st.markdown("Visualización de la carga de cumplimiento por cada marco regulatorio.")
    
    # Calcular cuántas políticas requiere cada marco
    framework_counts = {}
    for frameworks in df['Marcos Clave']:
        for f in frameworks:
            framework_counts[f] = framework_counts.get(f, 0) + 1
            
    df_counts = pd.DataFrame(list(framework_counts.items()), columns=['Marco', 'Cantidad de Políticas'])
    df_counts = df_counts.sort_values(by='Cantidad de Políticas', ascending=False)
    
    fig_bar = px.bar(df_counts, x='Marco', y='Cantidad de Políticas', 
                     title="Complejidad Regulatoria: Cantidad de Políticas por Marco",
                     text='Cantidad de Políticas', color='Cantidad de Políticas')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.markdown("""
    **Interpretación del Gráfico:**
    * Los marcos con barras más altas (ej. **[span_7](start_span)[span_8](start_span)ISO/IEC 27001:2022**, **SOC 2**) requieren un mayor número de políticas documentadas según el análisis del documento fuente[span_7](end_span)[span_8](end_span).
    * Si su empresa busca certificación en estos marcos, la carga documental será mayor.
    """)

# --- FOOTER ---
st.divider()
[span_9](start_span)[span_10](start_span)st.caption("Generado por Gemini AI | Datos extraídos de: 'Resumen de políticas del marco _ Centro de ayuda de Drata.pdf'[span_9](end_span)[span_10](end_span).")
