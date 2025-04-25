
import numpy as np

def accelerate_postprocessing(detections, conf_thresh=0.5, iou_thresh=0.5):
    boxes = []
    scores = []

    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        if conf >= conf_thresh:
            boxes.append((int(x1), int(y1), int(x2), int(y2)))
            scores.append(conf)

    indices = nms(boxes, scores, iou_thresh)
    final_boxes = [(boxes[i][0], boxes[i][1], boxes[i][2]-boxes[i][0], boxes[i][3]-boxes[i][1]) for i in indices]
    return final_boxes

def nms(boxes, scores, iou_threshold):
    indices = []
    boxes = np.array(boxes)
    scores = np.array(scores)
    order = scores.argsort()[::-1]

    while order.size > 0:
        i = order[0]
        indices.append(i)
        if order.size == 1:
            break
        xx1 = np.maximum(boxes[i, 0], boxes[order[1:], 0])
        yy1 = np.maximum(boxes[i, 1], boxes[order[1:], 1])
        xx2 = np.minimum(boxes[i, 2], boxes[order[1:], 2])
        yy2 = np.minimum(boxes[i, 3], boxes[order[1:], 3])

        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        inter = w * h
        iou = inter / ((boxes[i,2]-boxes[i,0]) * (boxes[i,3]-boxes[i,1]) + 
                       (boxes[order[1:],2]-boxes[order[1:],0]) * (boxes[order[1:],3]-boxes[order[1:],1]) - inter)

        order = order[1:][iou <= iou_threshold]

    return indices
