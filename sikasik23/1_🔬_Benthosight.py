import streamlit as st
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

dic = {0: 'Clams', 
       1: 'Crabs', 
       2: 'Jelly_Fish', 
       3: 'Lobster', 
       4: 'Nudibranchs', 
       5: 'Octopus', 
       6: 'Sea_Urchins', 
       7: 'Shrimp', 
       8: 'Squid', 
       9: 'Starfish'}

model = load_model('Asik23-BenthosException101-82.38.h5')

def predict_label(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    pred_prob = model.predict(img_array)[0]
    pred_class = int(np.argmax(pred_prob))
    accuracy = pred_prob[pred_class] * 100  # Akurasi dalam persentase
    return dic[pred_class], accuracy

def main():
    st.set_page_config(page_icon="🌊")
    st.sidebar.success("Select Page Above.")
    st.title("Benthos Species Classification")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Membuat folder "upload" jika belum ada
        if not os.path.exists("upload"):
            os.makedirs("upload")

        img_path = os.path.join("upload", "temp.jpg")
        with open(img_path, "wb") as f:
            f.write(uploaded_file.read())

        st.image(img_path, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        predicted_class, accuracy = predict_label(img_path)
        st.success(f"The predicted species is: {predicted_class}")
        st.info(f"Accuracy: {accuracy:.2f}%")

if __name__ == '__main__':
    main()
