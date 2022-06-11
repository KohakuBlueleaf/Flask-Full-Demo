def parse_object_id(id: str) -> list[int]:
    time = id[:8]
    pid = id[8:18]
    count = id[18:]
    return int(time, 16), int(pid, 16), int(count, 16)
