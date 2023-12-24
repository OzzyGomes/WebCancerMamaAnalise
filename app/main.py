import streamlit as st
import pickle
import pandas as pd

def get_clean_data():
    data = pd.read_csv('data/data.csv')
    
    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({ 'M': 1, 'B': 0})
    return data


def add_sidebar():
    st.sidebar.header('Cell Nuclei Measurements')

    data = get_clean_data()

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    input_dict = {}  


    for label, key in slider_labels:
         st.sidebar.slider(
             label=label,
             min_value=float(0),
             max_value=float(data[key].max()),
             value=float(data[key].mean())

         )

def main():
    st.set_page_config(
        page_title="Preditor de Cancer de Mama",
        page_icon=":female-doctor:",
        layout='wide',
        initial_sidebar_state='expanded'
        )
    
    add_sidebar()

    with st.container():
        st.title('Preditor de Cancer de Mama')
        st.write('Por favor, conecte este aplicativo ao seu laboratório de citologia\
                para ajudar no diagnóstico do câncer de mama a partir da amostra de tecido.\
                Este aplicativo prevê, usando um modelo de aprendizado de máquina, se um tumor \
                mamário é benigno ou maligno com base nas medidas que ele recebe do seu laboratório de citologia. \
                Você também pode atualizar as medidas manualmente usando os controles deslizantes na barra lateral.')
    
    col1, col2 = st.columns([4,1])

    with col1:
        st.write('this is colum 1')

    with col2:
        st.write('this is colum 2') 

if __name__ == '__main__':
    main()