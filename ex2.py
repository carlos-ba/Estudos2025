import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Calculadora de Carga Térmica", layout="wide")

# Título principal
st.title("Calculadora de Carga Térmica")

# Criando abas para organizar melhor os inputs
tab1, tab2, tab3 = st.tabs(["Dados do Ambiente (texte)", "Características Construtivas", "Resultados"])

with tab1:
    st.header("Dados do Ambiente")

    col1, col2 = st.columns(2)

    with col1:
        # Inputs para dimensões
        area = st.number_input("Área do ambiente (m²)", min_value=0.0, value=20.0)
        pe_direito = st.number_input("Pé direito (m)", min_value=0.0, value=2.8)
        n_pessoas = st.number_input("Número de pessoas", min_value=0, value=1)

    with col2:
        # Inputs para temperatura
        temp_interna = st.number_input("Temperatura interna desejada (°C)", min_value=0.0, value=24.0)
        temp_externa = st.number_input("Temperatura externa máxima (°C)", min_value=0.0, value=35.0)
        umidade_relativa = st.number_input("Umidade relativa do ar (%)", min_value=0.0, max_value=100.0, value=60.0)

with tab2:
    st.header("Características Construtivas")

    # Seleção do tipo de parede
    tipo_parede = st.selectbox(
        "Tipo de parede",
        ["Alvenaria 15cm", "Alvenaria 20cm", "Drywall", "Concreto"]
    )

    # Seleção do tipo de vidro
    tipo_vidro = st.selectbox(
        "Tipo de vidro",
        ["Vidro simples", "Vidro duplo", "Vidro low-e", "Sem vidro"]
    )

    # Área de janelas
    area_vidro = st.number_input("Área total de vidros (m²)", min_value=0.0, value=0.0)

    # Orientação solar principal
    orientacao = st.selectbox(
        "Orientação solar principal",
        ["Norte", "Sul", "Leste", "Oeste"]
    )

with tab3:
    st.header("Resultados do Cálculo")

    if st.button("Calcular Carga Térmica"):
        # Cálculos básicos (exemplo simplificado)
        volume = area * pe_direito
        diferenca_temp = temp_externa - temp_interna

        # Fatores de cálculo (exemplo - ajuste conforme necessário)
        fator_solar = {
            "Norte": 1.0,
            "Sul": 0.8,
            "Leste": 1.2,
            "Oeste": 1.3
        }

        fator_parede = {
            "Alvenaria 15cm": 2.5,
            "Alvenaria 20cm": 2.0,
            "Drywall": 3.0,
            "Concreto": 2.8
        }

        # Cálculo simplificado
        carga_pessoas = n_pessoas * 115  # Watts por pessoa (exemplo)
        carga_solar = area_vidro * fator_solar[orientacao] * 800  # Exemplo simplificado
        carga_conducao = (area - area_vidro) * fator_parede[tipo_parede] * diferenca_temp

        carga_total = carga_pessoas + carga_solar + carga_conducao

        # Exibição dos resultados
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Carga Térmica Total", f"{carga_total:.2f} W")
            st.metric("Carga por m²", f"{(carga_total / area):.2f} W/m²")

        with col2:
            st.metric("BTUs necessários", f"{(carga_total * 3.412):.0f} BTU/h")

        # Tabela detalhada
        st.subheader("Detalhamento da Carga Térmica")
        detalhamento = pd.DataFrame({
            'Componente': ['Pessoas', 'Radiação Solar', 'Condução Térmica', 'Total'],
            'Carga (W)': [carga_pessoas, carga_solar, carga_conducao, carga_total]
        })
        st.dataframe(detalhamento)

        # Recomendações
        st.subheader("Recomendações")
        if carga_total / area > 600:
            st.warning("Carga térmica por m² está alta. Considere medidas de redução.")
        else:
            st.success("Carga térmica por m² está dentro de valores aceitáveis.")

# Adiciona informações no rodapé
st.markdown("---")
st.markdown("""
    **Observações:**
    - Os cálculos apresentados são simplificados e devem ser utilizados apenas como referência
    - Para um dimensionamento preciso, consulte um profissional qualificado
    - Valores podem variar de acordo com outros fatores não considerados neste cálculo
""")