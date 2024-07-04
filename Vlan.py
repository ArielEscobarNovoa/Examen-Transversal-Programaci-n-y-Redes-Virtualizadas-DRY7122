# vlan_checker.py
def verificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN de rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN de rango extendido"
    else:
        return "Número de VLAN fuera de rango"

vlan_id = int(input("Ingrese el número de VLAN: "))
resultado = verificar_vlan(vlan_id)
print(resultado)
