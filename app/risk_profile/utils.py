def deduct_point(field_value, point):
    if isinstance(field_value, str):
        return field_value
    return field_value - point if field_value > point else 0


def append_point(field_value, point):
    if isinstance(field_value, str):
        return field_value
    return field_value + point
