import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd

receipt_dict_df = pd.DataFrame()
receipt_dict = {}

st.title('Lecteur de ticket de caisse')
st.write('**Etape 1 : charger les images:**', )
# Créer un uploader pour charger une ou plusieurs images
uploaded_files = st.file_uploader("Sélectionnez un dossier ou des fichiers", accept_multiple_files=True, type=["png", "jpg", "jpeg", "tif"])
st.markdown(uploaded_files)
# st.markdown(uploaded_files.name)
# st.markdown(uploaded_files[4])
# st.markdown(len(uploaded_files))

if uploaded_files:
    # st.write("l'opération peut prendre plusieurs minutes", color='grey')

    for index, uploaded_file in enumerate(uploaded_files):
       # Utiliser PIL pour ouvrir l'image et l'afficher
        image = Image.open(uploaded_file)
        test = st.image(image, caption='Image chargée', use_column_width=True)
        test.empty()

        # Exécuter la fonction get_text sur l'image chargée
        text = pytesseract.image_to_string(image)
        receipt_dict_df['image']=image
        receipt_dict_df['lien'] = uploaded_file. _file_urls
        receipt_dict_df['text']=text

    # ajouter l'inférence de BERT.
    st.success("Traitement terminé")

    for i in receipt_dict_df.items():
        # Créer deux colonnes
        col1, col2 = st.columns(2)

        # Afficher l'image dans la colonne de gauche
        with col1:
            image = Image.open(receipt_dict_df['image'])  # Assurez-vous que ce chemin est correct
            st.image(image, use_column_width=True)

        # Afficher le texte extrait dans la colonne de droite avec la possibilité de le modifier
        with col2:
            edited_text = st.text_area("Modifiez le texte si nécessaire", value=receipt_dict_df['text'], height=300)
        



