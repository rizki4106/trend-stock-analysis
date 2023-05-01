def calculate_trend_slope(x1, y1, x2, y2) -> float:
    """
    Calculates the slope of a line between two points

    Args:
        x1 : int -> x1 coordinate
        y1 : int -> y1 coordinate
        x2 : int -> x2 coordinate
        y2 : int -> y2 coordinate

    Returns:
        float -> slope of the line
    """
    return (y2 - y1) / (x2 - x1)