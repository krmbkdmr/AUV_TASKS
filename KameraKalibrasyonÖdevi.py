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
# TODO: Mercek bozulmasını düzeltip yeni görüntüyü döndürün.
raise NotImplementedError("undistort_image tamamlanmalı")
def rotate_image(image, angle_deg):
# TODO: Görüntü merkezini ((width-1)/2, (height-1)/2) bulun.
# TODO: Dönüş matrisini oluşturup dönüşü uygulayın.
# TODO: Döndürülmüş görüntüyü döndürün.
raise NotImplementedError("rotate_image tamamlanmalı")
if __name__ == "__main__":
image_path = Path(__file__).with_name("havuz_26_haziran_bozuk.jpg")
image = cv2.imread(str(image_path))
if image is None:
raise ValueError("Görüntü okunamadı; dosya yolunu kontrol edin.")
undistorted = undistort_image(image, camera_matrix, dist_coeffs)
corrected = rotate_image(undistorted, -15.0)
output_path = image_path.with_name("havuz_26_haziran_duzeltilmis.jpg")
cv2.imwrite(str(output_path), corrected)