from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# ...existing code...
class_labels = ['Amoxicillin 500 MG', 'Atomoxetine 25 MG', 'Calcitriol 0.00025 MG', 'Oseltamivir 45 MG', 'Ramipril 5 MG', 'apixaban 2.5 MG', 'aprepitant 80 MG', 'benzonatate 100 MG', 'carvedilol 3.125 MG', 'celecoxib 200 MG', 'duloxetine 30 MG', 'eltrombopag 25 MG', 'montelukast 10 MG', 'mycophenolate mofetil 250 MG', 'pantoprazole 40 MG', 'pitavastatin 1 MG', 'prasugrel 10 MG', 'saxagliptin 5 MG', 'sitagliptin 50 MG', 'tadalafil 5 MG']
# ...existing code...

app = Flask(__name__)
model = load_model(r'C:\Users\asus\Downloads\Pill Identification Flask\pill_identifier_model.keras')

IMG_SIZE = 128

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None
#     confidence = None

#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return 'No file part'
        
#         file = request.files['file']
        
#         if file.filename == '':
#             return 'No selected file'
        
#         if file:
#             img_path = os.path.join('static/uploads', file.filename)
#             file.save(img_path)
#             prediction, confidence = predict_pill(img_path)
    
#     return render_template('index.html', prediction=prediction, confidence=confidence)

# 

# THIS IS CORRECTED CODE
# ...existing code...
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None

#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return 'No file part'
        
#         file = request.files['file']
        
#         if file.filename == '':
#             return 'No selected file'
        
#         if file:
#             upload_folder = os.path.join('static', 'uploads')
#             os.makedirs(upload_folder, exist_ok=True)  # Ensure the folder exists
#             img_path = os.path.join(upload_folder, file.filename)
#             file.save(img_path)
#             pred_class, confidence = predict_pill(img_path)
#             prediction = {'class': pred_class, 'confidence': confidence}
    
#     return render_template('index.html', prediction=prediction)
# ...existing code...

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        if file:
            upload_folder = os.path.join('static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            img_path = os.path.join(upload_folder, file.filename)
            file.save(img_path)
            pred_class, confidence = predict_pill(img_path)
            # Build the image URL for the template
            image_url = f"/static/uploads/{file.filename}"
            prediction = {'class': pred_class, 'confidence': confidence, 'image_url': image_url}
    
    return render_template('index.html', prediction=prediction)


# def predict_pill(img_path):
#     img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
#     img_array = image.img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     prediction = model.predict(img_array)
#     class_idx = np.argmax(prediction)
    
#     class_labels = list(model.class_indices.keys())
#     return class_labels[class_idx], prediction[0][class_idx]

def predict_pill(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    return class_labels[class_idx], float(prediction[0][class_idx])

# def predict_pill(img_path):
#     img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
#     img_array = image.img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     prediction = model.predict(img_array)
#     class_idx = np.argmax(prediction)
    
#     class_labels = list(train_generator.class_indices.keys())
#     return class_labels[class_idx], prediction[0][class_idx]

if __name__ == '__main__':
    app.run(debug=True)