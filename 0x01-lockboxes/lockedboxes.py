#!/usr/bin/python3

def can_unlock_all(boxes):
    unlocked_boxes = [0]
    total_boxes = len(boxes)

    for box_index, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < total_boxes and key not in unlocked_boxes and key != box_index:
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == total_boxes
