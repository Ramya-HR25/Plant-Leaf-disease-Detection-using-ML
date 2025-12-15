# Plant Disease Detection Web App

A modern web application for detecting plant diseases from leaf images using deep learning and transfer learning (MobileNetV2). Trained on the PlantVillage dataset with 38 classes (Tomato, Potato, Pepper, healthy and diseased).

## Features
- Upload a leaf image and get instant disease prediction
- Shows disease name, confidence, treatment recommendation, and the analyzed image
- Uses transfer learning for high accuracy
- Supports 38 classes from PlantVillage
- Camera integration for real-time leaf detection and capture

## Project Structure
```
plant-disease-detection/
├─ .git/
├─ app.py
├─ class_indices.json
├─ create_reliable_from_unreliable.py
├─ disease_info.json
├─ evaluate_model.py
├─ move_reliable_images.py
├─ move_unreliable_images.py
├─ PlantVillage/ (not tracked by Git - see Dataset section)
├─ README.md
├─ requirements.txt
├─ train_model.py
├─ static/
│  └─ css/
│     ├─ style.css
│     └─ script.js
└─ templates/
   ├─ index.html
   ├─ result.html
   └─ welcome.html
```

## Dataset
The PlantVillage dataset is used for training the model. It contains thousands of images of healthy and diseased plant leaves across multiple species. Due to its large size (several GBs), the dataset is not included in this repository and must be downloaded separately.

**Download Instructions:**
1. Visit the PlantVillage dataset on Kaggle: https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset
2. Download the dataset
3. Extract the contents to the `PlantVillage/` directory in your project folder

**Note:** The `PlantVillage/` directory is intentionally excluded from version control via `.gitignore` due to the large size of the dataset.

## Data Preparation Scripts
The repository includes several utility scripts for organizing the dataset:
- `create_reliable_from_unreliable.py`: Creates a reliable dataset by filtering out corrupted or low-quality images
- `move_reliable_images.py`: Moves verified good images to a separate directory
- `move_unreliable_images.py`: Separates potentially problematic images for manual review

## Setup
1. **Clone the repository and navigate to the folder:**
   ```bash
   git clone <repo-url>
   cd plant-disease-detection
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download and prepare the PlantVillage dataset:**
   - Follow the dataset instructions above to download and extract the dataset to the `PlantVillage/` directory

## Training the Model
1. **Edit `train_model.py` if needed (e.g., change epochs, batch size).**
2. **Run the training script:**
   ```bash
   python train_model.py
   ```
   - This will train a MobileNetV2-based model and save `plant_disease_model.h5` and `class_indices.json`.

## Running the Web App
1. **Start the Flask app:**
   ```bash
   python app.py
   ```
2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```
3. **Upload a leaf image or use the camera feature to capture a photo and view the prediction and treatment.**

## Troubleshooting
- **Import errors:**
  - Make sure you have activated your virtual environment and installed all requirements.
  - In VS Code, select the correct Python interpreter (from your venv).
- **Model not accurate?**
  - Try increasing epochs in `train_model.py`.
  - Use more images per class if possible.
  - Try unfreezing some layers of MobileNetV2 for fine-tuning.
- **Blank result page?**
  - Check your terminal for errors and ensure all template variables are passed.

## Credits
- PlantVillage dataset: https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset
- Built with TensorFlow, Keras, Flask, and Bootstrap