print("=== Beam Load Calculator ===")

length = float(input("Beam Length (ft): "))
load = float(input("Point Load (lb): "))
position = float(input("Load Position from Left Support (ft): "))

reaction_a = load * (length - position) / length
reaction_b = load * position / length

print("\nResults")
print("------------------")
print(f"Reaction A = {reaction_a:.2f} lb")
print(f"Reaction B = {reaction_b:.2f} lb")

print("\nBeam Diagram")
print("----------------------------")
print("A=========================B")
print(f"↑ {reaction_a:.1f} lb")
print(f"↓ {load:.1f} lb @ {position:.1f} ft")
print(f"↑ {reaction_b:.1f} lb")
# Shear and Bending Moment Calculations
x_load = position #9.0 ft 
b_distance = length - x_load # 15.0 ft
# Shear force just to the and right of the point load
shear_left = reaction_a
shear_right = reaction_a - load
max_shear = max(abs(shear_left), abs(shear_right))
# maximum bending moment occurs directly under the point load
max_moment = reaction_a * x_load 
print("\nShear and Bending Analysis")
print("----------------------------")
print(f"Maximum Shear Force = {max_shear:.1f} lb")
print(f"Maximum Bending Moment = {max_moment:.1f} lb-ft")
