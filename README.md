# Pill Identifier App

This project is a Flask web application that allows users to upload images of pills and receive predictions on their identity using a trained machine learning model.

## Project Structure

```
pill-identifier-app
├── app.py                  # Main application file for the Flask server
|
├── model                   # Directory containing the trained model
│   └── pill_identifier_model.h5
├── static                  # Directory for static files
│   └── uploads             # Directory for temporarily storing uploaded images
├── templates               # Directory for HTML templates
│   └── index.html         # Frontend template for user interaction

```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clonehttps://github.com/Shubham-741/Pill-Identification-System
   run the pill_identification.ipynb code
   This will create a pill_identifier_model.h5 model. Use it in your app.py
   cd pill-identifier-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- On the homepage, you can upload an image of a pill.
  
- Here is an example of the app in use:

  ![Pill Identifier App Screenshot](static/images/Pill_Test_Screen.jpg)

- After uploading, the application will display the predicted class of the pill along with the confidence level of the prediction.