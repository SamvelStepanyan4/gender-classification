# Gender Classification with MobileNetV2 🚀

This project implements a gender classification system using a MobileNetV2-based deep learning model trained on facial images 📸. The model predicts whether a person is male 👨 or female 👩 based on input images, and a real-time camera application displays the prediction with confidence scores 🎥.

## Table of Contents 📋
- [Project Overview](#project-overview) 🌟
- [Features](#features) ✨
- [Dataset](#dataset) 📊
- [Installation](#installation) 🛠️
- [Usage](#usage) 🚀
- [File Structure](#file-structure) 📁
- [Training the Model](#training-the-model) 🧠
- [Running the Camera Application](#running-the-camera-application) 🎬
- [Contributing](#contributing) 🤝
- [License](#license) 📜

## Project Overview 🌟
This project leverages a pre-trained MobileNetV2 model, fine-tuned for binary gender classification (Male/Female) 👥. The training is performed on a dataset of facial images, and the model is saved for use in a real-time camera application that processes video feed to predict gender with confidence scores 📈.

## Features ✨
- **Deep Learning Model** 🧠: Utilizes MobileNetV2 for efficient and accurate gender classification.
- **Real-Time Prediction** 🎥: Processes webcam feed to predict gender in real time.
- **Visualization** 📉: Plots training and validation accuracy/loss for performance analysis.
- **Pre-trained Model** ✅: Includes a saved model for immediate use.
- **Lightweight** ⚡: Optimized for fast inference using MobileNetV2.

## Dataset 📊
The dataset is expected to be organized in the `data` directory with `train` and `val` subdirectories, each containing `male` and `female` folders with facial images. The provided code assumes:
- Training set: ~47,009 images
- Validation set: ~11,649 images
- Image size: 128x128 pixels 🖼️

*Note*: The dataset is not included in this repository due to its size. You can use any gender classification dataset (e.g., UTKFace, CelebA) with a similar structure.

## Installation 🛠️
To set up the project, follow these steps:

1. **Clone the Repository** 📥:
   ```bash
   git clone https://github.com/SamvelStepanyan4/gender-classification.git
   cd gender-classification
   ```

2. **Install Dependencies** 🐍:
   Ensure you have Python 3.8+ installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with:
   ```
   tensorflow==2.10.0
   numpy
   pandas
   seaborn
   matplotlib
   opencv-python
   ```

3. **Prepare the Dataset** 📂:
   - Place your dataset in a `data` directory with the following structure:
     ```
     data/
     ├── train/
     │   ├── male/
     │   └── female/
     └── val/
         ├── male/
         └── female/
     ```

## Usage 🚀
The project includes two main components:
- A Jupyter Notebook (`Gender_classification.ipynb`) for training the model 📓.
- A Python script (`camera.py`) for real-time gender classification using a webcam 🎥.

### Training the Model 🧠
1. Open `Gender_classification.ipynb` in Jupyter Notebook or JupyterLab.
2. Ensure the dataset is in the `data` directory as described above.
3. Run all cells to:
   - Load and preprocess the dataset 📊.
   - Train the MobileNetV2 model for 3 epochs initially, followed by fine-tuning for 2 epochs 🔧.
   - Save the trained model as `gender_classification_mobilenetv2_fast_training.h5` 💾.
   - Generate accuracy and loss plots 📈.

### Running the Camera Application 🎬
1. Ensure a webcam is connected to your device.
2. Run the `camera.py` script:
   ```bash
   python camera.py
   ```
3. The application will:
   - Capture video feed from your webcam 📷.
   - Display the predicted gender (Male/Female) and confidence score on the video feed 🎥.
   - Press `q` to quit the application 🚪.

## File Structure 📁
```
gender-classification/
├── data/                    # Dataset directory (not included)
├── Gender_classification.ipynb  # Jupyter Notebook for training
├── camera.py                # Script for real-time camera prediction
├── gender_classification_mobilenetv2_fast_training.h5  # Trained model
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Contributing 🤝
Contributions are welcome! 🎉 To contribute:
1. Fork the repository 🍴.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request 📬.

Please ensure your code follows PEP 8 guidelines and includes appropriate comments.

## License 📜
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding, SamvelStepanyan4! 🎉 If you have any questions, feel free to open an issue or contact me. 😊