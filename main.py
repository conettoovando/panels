def check_with_orientation(pw, ph, rw, rh):
    # Calculo de cuantos paneles caben por horizontalmente por fila y la cantidad de filas completas de panel
    full_rows = rw // pw 
    full_cols = rh // ph 
    total = full_rows * full_cols 

    # Revisar si sobre espacio horizontal para revisar si cabe otro panel pero rotado
    leftover_w = rw % pw
    extra_by_width = (leftover_w // ph) * (rh // pw)

    # Se revisa si existe espacio vertical para meter otro panel rotado
    leftover_h = rh % ph
    extra_by_height = (leftover_h // pw) * (rw // ph)

    # Retornar el total de paneles con la mejor opcion de paneles extras
    return total + max(extra_by_width, extra_by_height)

def maxPanels(panel: str, roof: str):
    pw, ph = map(int, panel.lower().split("x"))
    rw, rh = map(int, roof.lower().split("x"))
    
    # obtener el maximo de paneles en las direcciones horizontal y vertical
    optionH = check_with_orientation(pw, ph, rw, rh)
    optionV = check_with_orientation(ph, pw, rw, rh)

    return max(optionH, optionV)

# Test
print(maxPanels("1x2", "3x5")) # 7
print(maxPanels("3x5", "12x15")) # 12
print(maxPanels("1x2", "1x2")) # 1
print(maxPanels("1x2", "2x1")) # 1
print(maxPanels("4x4", "3x8")) # 0
print(maxPanels("4x4", "4x8")) # 2
print(maxPanels("3x2", "5x8")) # 6

