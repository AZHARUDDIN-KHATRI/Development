import math

def calculate_attendance(total_classes, attended_classes, od_granted=0):
    """
    Calculates final attendance metrics including university OD credits
    and computes the gap required to hit the 75% baseline.
    """
    adjusted_attended = attended_classes + od_granted
    
    if total_classes == 0:
        return 0.0, 0
        
    current_percentage = (adjusted_attended / total_classes) * 100
    
    # Calculate classes needed to reach the 75% boundary
    classes_needed = 0
    if current_percentage < 75.0:
        # Equation: (attended + X) / (total + X) = 0.75 => X = (0.75 * total - attended) / 0.25
        classes_needed = math.ceil((0.75 * total_classes - adjusted_attended) / 0.25)
        if classes_needed < 0:
            classes_needed = 0

    return round(current_percentage, 2), classes_needed

if __name__ == "__main__":
    print("=== Academic Attendance & OD Optimization Dashboard ===")
    
    try:
        tot = int(input("Enter total scheduled classes: "))
        att = int(input("Enter classes actually attended: "))
        od = int(input("Enter official On-Duty (OD) credits approved: "))
        
        pct, deficit = calculate_attendance(tot, att, od)
        
        print(f"\n📈 Current Calculated Attendance: {pct}%")
        
        if pct >= 75.0:
            print("✅ Status: Safe Zone. Permitted for Term-End Examination.")
        else:
            print(f"❌ Status: DEBARRED RISK. You must attend {deficit} consecutive classes without omission to reach 75%.")
            
    except ValueError:
        print("Error: Please input valid numeric data strings.")
