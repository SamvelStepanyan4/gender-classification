import tensorflow as tf
import cv2
import numpy as np

labels = ["Female", "Male"]

model = tf.keras.models.load_model('gender_classification_mobilenetv2_fast_training.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Не удалось получить кадр")
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # changed from GRAY to RGB
    image = cv2.resize(image, (128, 128))  # changed from 48x48 to 224x224
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    y_pred = model.predict(image, verbose=0)[0][0]
    gender = "Male" if y_pred > 0.5 else "Female"
    prob = y_pred if y_pred > 0.5 else 1 - y_pred

    text = f"{gender} ({prob*100:.1f}%)"
    cv2.putText(frame, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()