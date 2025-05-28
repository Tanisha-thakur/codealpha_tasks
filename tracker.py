import numpy as np

def compute_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1g, y1g, x2g, y2g = box2

    xi1 = max(x1, x1g)
    yi1 = max(y1, y1g)
    xi2 = min(x2, x2g)
    yi2 = min(y2, y2g)

    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2g - x1g) * (y2g - y1g)
    union_area = box1_area + box2_area - inter_area

    if union_area == 0:
        return 0
    return inter_area / union_area


class SimpleTracker:
    def __init__(self, iou_threshold=0.5):
        self.tracks = []  # Each track: {'id': int, 'bbox': [x1,y1,x2,y2]}
        self.track_id = 0
        self.iou_threshold = iou_threshold

    def update(self, detections):
        updated_tracks = []
        unmatched_detections = [det for det in detections]  # Copy the list

        for track in self.tracks:
            best_match = None
            best_iou = 0

            for det in unmatched_detections:
                iou = compute_iou(track['bbox'], det[:4])
                if iou > best_iou and iou > self.iou_threshold:
                    best_iou = iou
                    best_match = det

            if best_match is not None:
                updated_tracks.append({'id': track['id'], 'bbox': best_match[:4]})
                unmatched_detections = [det for det in unmatched_detections if not np.array_equal(det, best_match)]

        # Add new tracks for unmatched detections
        for det in unmatched_detections:
            updated_tracks.append({'id': self.track_id, 'bbox': det[:4]})
            self.track_id += 1

        self.tracks = updated_tracks
        return [(track['id'], track['bbox']) for track in self.tracks]
