

def conversion_kg_lbs(kg):
    lbs = kg *  2.20462
    return lbs 

kg = float(input("enter weight into kilograms: "))
pounds = conversion_kg_lbs(kg)
print(f"{kg} kg is equal to {pounds} lbs")