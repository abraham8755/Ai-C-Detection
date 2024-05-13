#for lung segmentation
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras import backend as K
from tensorflow.keras.utils import get_custom_objects
from tensorflow.keras.layers import Layer
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import pydicom
#import tensorflow_addons as tfa

def tversky_index( y_true, y_pred):
        y_true_pos = K.flatten(y_true)
        y_pred_pos = K.flatten(y_pred)
        true_pos = K.sum(y_true_pos * y_pred_pos)
        false_neg = K.sum(y_true_pos * (1 - y_pred_pos))
        false_pos = K.sum((1 - y_true_pos) * y_pred_pos)
        alpha = 0.6

        return (true_pos + 1) / (true_pos + alpha * false_neg + (
                1 - alpha) * false_pos + 1)

def tversky_loss( y_true, y_pred):
    return 1 - tversky_index(y_true, y_pred)

def focal_tversky( y_true, y_pred):
    pt_1 = tversky_index(y_true, y_pred)
    gamma = 0.75
    return K.pow((1 - pt_1), gamma)

def sensitivity( y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    return true_positives / (possible_positives + K.epsilon())

def specificity(y_true, y_pred):
    true_negatives = K.sum(
        K.round(K.clip((1 - y_true) * (1 - y_pred), 0, 1)))
    possible_negatives = K.sum(K.round(K.clip(1 - y_true, 0, 1)))
    return true_negatives / (possible_negatives + K.epsilon())

def iou(y_true, y_pred):
    y_true_pos = K.flatten(y_true)
    y_pred_pos = K.flatten(y_pred)
    true_pos = K.sum(y_true_pos * y_pred_pos)
    false_neg = K.sum(y_true_pos * (1 - y_pred_pos))
    false_pos = K.sum((1 - y_true_pos) * y_pred_pos)

    jac = (true_pos+1) / (true_pos+false_neg+false_pos+1)
    return jac

def iou_loss(y_true, y_pred):
    return 1-iou(y_true,y_pred)

def transform_to_hu(dicom_file, image):
    intercept = dicom_file.RescaleIntercept
    slope = dicom_file.RescaleSlope
    hu_image = image * slope + intercept

    return hu_image

def normalize(image):
    min=image.min()
    return (image-min)/(image.max()-min)


def load_and_predict_image(image_path, model_path, img_size=(256, 256)):
    # Modeli yükle
    model = load_model(model_path, custom_objects={'focal_tversky': focal_tversky, 'iou': iou, 'sensitivity': sensitivity, 'specificity': specificity}, compile=False)
    model.compile(optimizer=Adam(), loss=focal_tversky, metrics=[iou, 'binary_accuracy', sensitivity, specificity])

    # Görüntü dosyasını yükle
    dicom_file = pydicom.read_file(image_path)
    if dicom_file is None:
        print("Görüntü yüklenemedi: ", image_path)
        return

    dicom_image = dicom_file.pixel_array
    original_size = dicom_image.shape
    dicom_image = transform_to_hu(dicom_file, dicom_image)
    dicom_image = cv2.resize(dicom_image, img_size, interpolation=cv2.INTER_AREA)
    dicom_image = normalize(dicom_image)
    dicom_image = dicom_image[..., np.newaxis]
    dicom_image = dicom_image.squeeze()

    # Model ile tahmin yap
    dicom_image_batch = np.expand_dims(dicom_image, axis=0)
    predicted_mask = model.predict(dicom_image_batch)
    predicted_mask = predicted_mask.squeeze()
    predicted_mask = (predicted_mask > 0.5).astype(np.float32)
    # Ensure the predicted mask is resized to the img_size used for the model input
    predicted_mask_resized = cv2.resize(predicted_mask, img_size, interpolation=cv2.INTER_NEAREST)

    # Create the overlay image by multiplying the original DICOM image (first channel) with the resized predicted mask
    overlay_image = dicom_image * predicted_mask_resized


    # Görüntüyü ve maskeyi görselleştir
    plt.figure(figsize=(18, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(dicom_image, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 3, 2)
    plt.imshow(predicted_mask, cmap='gray')
    plt.title('Predicted Mask')
    plt.subplot(1, 3, 3)
    plt.imshow(overlay_image, cmap='gray')
    plt.title('Overlay Image')
    plt.show()



# Model dosya yolu
model_path = "lung_unet_256px_focaltversky_alpha=0.6_dicomformat.keras"


# Tahmin yapılacak görüntü dosyalarının bulunduğu dizin
image_path = "1-031.dcm"
# Dizindeki tüm görüntüler üzerinde tahmin yap
load_and_predict_image(image_path, model_path)