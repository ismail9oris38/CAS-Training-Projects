# 🚗 Lane Detection and Tracking with OpenCV

Bu proje, **OpenCV** ve **NumPy** kullanarak video üzerinden yol çizgilerinin tespit edilmesi ve takip edilmesini sağlar.  
Kod, Hough Transform, Canny Edge Detection ve ROI (Region of Interest) maskeleri ile çalışır.  
Ayrıca belirli bölgelerde sapma (offset) hesaplayarak yolun merkezine göre çizgi konumunu görselleştirir.

---

## ✨ Özellikler
- Video akışı üzerinden kareleri işleme
- Gri tonlama ve ikili eşikleme (thresholding)
- Kenar tespiti (**Canny Edge Detection**)
- Doğru tespiti (**HoughLinesP**)
- Farklı bölgelerde çizgi merkezlerini bulma ve sapmayı hesaplama
- Sonuçların anlık olarak gösterimi

---

## 🛠️ Kullanılan Teknolojiler
- Python 3
- OpenCV (cv2)
- NumPy
