import streamlit as st
from PIL import Image
from ocr_inference import get_text



st.title('Lecteur de ticket de caisse')
st.write('**Etape 1 : charger les images:**', )
# Créer un uploader pour charger une ou plusieurs images
uploaded_files = st.file_uploader("Sélectionnez un dossier ou des fichiers", accept_multiple_files=True, type=["png", "jpg", "jpeg", "tif"])

if uploaded_files:
    st.write("l'opération peut prendre plusieurs minutes", color='grey')
    # Initialiser la barre de progression
    progress_bar = st.progress(0)
    total_files = len(uploaded_files)
    receipt_dict = {}

    for index, uploaded_file in enumerate(uploaded_files):
        # Mise à jour de la barre de progression
        progress_percentage = int((index / total_files) * 100)
        progress_bar.progress(progress_percentage)

        # Utiliser PIL pour ouvrir l'image et l'afficher
        image = Image.open(uploaded_file)
        test = st.image(image, caption='Image chargée', use_column_width=True)
        test.empty()

        # Exécuter la fonction get_text sur l'image chargée
        text_list = get_text(uploaded_file)
        receipt_dict[uploaded_file.name] = text_list

        # Mise à jour finale de la barre de progression
        progress_bar.progress(progress_percentage + int(1 / total_files * 100))

    # Traitement terminé
    progress_bar.empty()  # Optionnel: cacher la barre de progression à la fin

    # ajouter l'inférence de BERT.
    st.success("Traitement terminé")
    st.button(pages="test")
