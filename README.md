# Pill Identifier App

This project is a Flask web application that allows users to upload images of pills and receive predictions on their identity using a trained machine learning model.

## Project Structure

```
pill-identifier-app
├── app.py                  # Main application file for the Flask server
├── requirements.txt        # Lists the dependencies required for the project
├── model                   # Directory containing the trained model
│   └── pill_identifier_model.h5
├── static                  # Directory for static files
│   └── uploads             # Directory for temporarily storing uploaded images
├── templates               # Directory for HTML templates
│   └── index.html         # Frontend template for user interaction
└── README.md               # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
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
- After uploading, the application will display the predicted class of the pill along with the confidence level of the prediction.

## License

This project is licensed under the MIT License - see the LICENSE file for details.