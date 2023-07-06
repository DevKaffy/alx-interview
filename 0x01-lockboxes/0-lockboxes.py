def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
