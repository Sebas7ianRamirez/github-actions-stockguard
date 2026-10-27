def clasificar_stock (stock_actual: int, stock_minimo: int) -> str:
    """Clasifica el stock de un producto en función de su cantidad actual y su stock mínimo."""
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo.")
    if stock_minimo <= 0:
        raise ValueError("El stock mínimo debe ser mayor que cero.")
    if stock_actual == 0:
        return "AGOTADO"
    if stock_actual <= stock_minimo * 0.5:
        return "CRITICO"
    if stock_actual <= stock_minimo:
        return "BAJO"
    return "NORMAL"
