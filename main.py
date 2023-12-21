import streamlit as st
from PIL import Image
import numpy as np
import pickle as pkl
import sklearn


class_list = {'0': 'Benign', '1': 'Malicious'}

st.title('PDF Malwware Detection')

input = open('xgb_model.pkl', 'rb')
model = pkl.load(input)

st.header('Upload an image')

image = st.file_uploader('Choose an image', type=(['png', 'jpg', 'jpeg']))

if image is not None:
  image = Image.open(image)
  st.image(image, caption='Test image')

  if st.button('Predict'):
    image = image.resize((227*227*3, 1))
    vector = np.array(image)
    label = str((model.predict(vector))[0])

    st.header('Result')
    st.text(class_list[label])
