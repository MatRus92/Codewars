def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2

    if you_speed == 0:
        return "Shark Bait!"

    if shark_speed == 0:
        return "Alive!"

    you_to_pon = pontoon_distance / you_speed
    shark_to_pon = shark_distance / shark_speed

    if you_to_pon < shark_to_pon:
        return "Alive!"

    return "Shark Bait!"