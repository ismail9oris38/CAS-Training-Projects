import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Line.mp4")

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    _, thresh = cv.threshold(gray, 127, 255, cv.THRESH_OTSU)

    edges = cv.Canny(thresh, 100, 150)

    lines = cv.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi/180,
        threshold=5,
        minLineLength=5,
        maxLineGap=5
    )

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv.circle(frame, (int(width / 2), int(height / 8)), 5, (0, 0, 255), -1)
    cv.circle(frame, (int(width / 2), int(height / 8 + height / 4)), 5, (0, 0, 255), -1)
    cv.circle(frame, (int(width / 2), int(height / 8 + height / 2)), 5, (0, 0, 255), -1)
    cv.circle(frame, (int(width / 2), int(height - height / 8)), 5, (0, 0, 255), -1)

    regions = [
        (int(height * 0.75), height),  # Alt
        (int(height * 0.5), int(height * 0.75)),  # Orta-alt
        (int(height * 0.25), int(height * 0.5)),  # Orta-üst
        (0, int(height * 0.25))  # Üst
    ]

    points_x_y = []

    for i, (y1, y2) in enumerate(regions):
        mask = np.zeros_like(edges)
        mask[y1:y2, :] = 255
        roi = cv.bitwise_and(edges, mask)

        points = np.column_stack(np.where(roi > 0))

        if len(points) > 0:
            center_x = int(np.mean(points[:, 1]))
            center_y = int(np.mean(points[:, 0]))

            points_x_y.append([center_x, center_y])

            cv.circle(frame, (center_x, center_y), 5, (255, 255, 255), -1)

            sapma = center_x - width // 2
            cv.putText(frame, f"{-sapma}", (center_x + 15, center_y), cv.FONT_HERSHEY_SIMPLEX, 0.8, (100, 150, 150), 2)

    points_x_y = np.array(points_x_y, dtype=np.int32)
    hull = cv.convexHull(points_x_y, returnPoints=True)
    cv.polylines(frame, [hull], isClosed=True, color=(255,0,0))

    # 10. Sonucu göster
    cv.imshow("Yol Takip", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
