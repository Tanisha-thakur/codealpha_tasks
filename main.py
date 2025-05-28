import cv2
from detector import ObjectDetector
from tracker import SimpleTracker

def main():
    cap = cv2.VideoCapture(0)
    detector = ObjectDetector()
    tracker = SimpleTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections, annotated_frame = detector.detect(frame)
        tracks = tracker.update(detections)

        for track_id, bbox in tracks:
         x1, y1, x2, y2 = map(int, bbox)
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(annotated_frame, f'ID {track_id}', (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)



        cv2.imshow("Object Detection & Tracking", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
