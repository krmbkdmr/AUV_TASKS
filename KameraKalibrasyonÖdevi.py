from pathlib import Path
import cv2
import numpy as np

camera_matrix = np.array([
    [714.285714, 0.0, 319.5],
    [0.0, 714.285714, 239.5],
    [0.0, 0.0, 1.0],
])

dist_coeffs = np.array([-0.22, 0.04, 0.001, -0.001, 0.0])

def undistort_image(image, camera_matrix, dist_coeffs):
    duzeltilmis = cv2.undistort(image, camera_matrix, dist_coeffs)
    return duzeltilmis

def rotate_image(image, angle_deg):
    yukseklik, genislik = image.shape[:2]
    merkez = ((genislik - 1) / 2, (yukseklik - 1) / 2)
    
    # Pozitif açı ile saat yönünün tersine döndürüyorum.
    donusum = cv2.getRotationMatrix2D(merkez, angle_deg, 1.0)
    
    dondurulmus = cv2.warpAffine(image, donusum, (genislik, yukseklik), borderMode=cv2.BORDER_REPLICATE)
    return dondurulmus

if __name__ == "__main__":
    image_path = Path(__file__).with_name("havuz_26_haziran_bozuk.jpg")
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError("Görüntü okunamadı; dosya yolunu kontrol edin.")
        
    undistorted = undistort_image(image, camera_matrix, dist_coeffs)
    
    # Açıyı negatif bir değerle döndürüyorum.
    corrected = rotate_image(undistorted, -15.0)
    
    output_path = image_path.with_name("havuz_26_haziran_duzeltilmisfinal.jpg")
    cv2.imwrite(str(output_path), corrected)