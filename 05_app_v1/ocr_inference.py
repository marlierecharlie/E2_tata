import keras_ocr
from PIL import Image
import io

def get_text(image_file):
    pipeline = keras_ocr.pipeline.Pipeline()
    image = Image.open(image_file)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')  # Enregistrer l'image dans un buffer en format PNG
    image_bytes.seek(0)
    images = [keras_ocr.tools.read(image_bytes)]


    prediction_groups = pipeline.recognize(images)
    text_list=[]
    predicted_image = prediction_groups[0]
    for text, box in predicted_image:
        print(text)
        text_list.append(text)
    return text_list
