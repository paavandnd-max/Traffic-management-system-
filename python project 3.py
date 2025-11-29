import time
from collections import deque
import cv2

t_s = input("Enter current signal (red/yellow/green): ")
vehicle_queue = []
signal_timer = {"red": 10, "yellow": 5, "green": 10}

def show_signal():
    print("\nCurrent signal:", t_s)
    if t_s == "red":
        print("Red signal - STOP")
    elif t_s == "yellow":
        print("Yellow signal - WAIT")
    else:
        print("Green signal - GO")

def add_vehicle():
    global t_s
    if t_s in ["red", "yellow"]:
        vehicle = input("Enter vehicle number: ")
        vehicle_queue.append(vehicle)
        print(f"ADDED: {vehicle}")
    else:
        print("Signal is green! No vehicles added.")

def view_vehicle():
    if vehicle_queue:
        print("Vehicles waiting:", ", ".join(vehicle_queue))
    else:
        print("No vehicles waiting.")

def count_vehicle():
    print("Total vehicles waiting:", len(vehicle_queue))

signal_durations = {"red": 10, "yellow": 5, "green": 10}
signal_order = ["red", "yellow", "green"]

def traffic_s():
    global t_s
    t_s = input("Enter current signal (red/yellow/green): ")

def change_signal():
    for signal in signal_order:
        print(signal.upper(), "-- LIGHT ON --")
        duration = signal_durations[signal]
        for sec in range(duration, 0, -1):
            print(f"{signal}: {sec} sec remaining")
            time.sleep(1)

def allow_vehicle():
    global t_s
    if t_s != "green":
        print("Signal is NOT green. Vehicles cannot pass.")
        return
    if vehicle_queue:
        passed = vehicle_queue.pop(0)
        print(f"Vehicle {passed} has passed.")
    else:
        print("No vehicles waiting.")

def detect_lane_violation(x_position, lane_boundary):
    if x_position > lane_boundary:
        print("Lane violation detected!")
        return True
    print("No lane violation.")
    return False

def capture_violation_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    print("Press SPACE to capture frame, ESC to exit...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.imshow("Violation Capture", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
        if key == 32:
            cv2.imwrite("violation_frame.jpg", frame)
            print("Violation frame saved as 'violation_frame.jpg'")
            break
    cap.release()
    cv2.destroyAllWindows()

def emergency_mode():
    global t_s
    print("Emergency Vehicle Detected!")
    print("Switching ALL signals to GREEN!")
    
    t_s = "green"     
    
    time.sleep(5)
    print("Signal is now GREEN for emergency vehicle.")
    print("Emergency Mode Completed.")
while True:
    print("\n=== TRAFFIC MANAGEMENT SYSTEM ===")
    print("1. Show signal")
    print("2. Add Vehicle")
    print("3. View waiting vehicles")
    print("4. Count waiting vehicles")
    print("5. Change signals")
    print("6. Allow vehicles to pass")
    print("7. Detect lane violation")
    print("8. Capture violation frame (Webcam)")
    print("9. Emergency vehicle detected")
    print("10. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        show_signal()
    elif ch == 2:
        add_vehicle()
    elif ch == 3:
        view_vehicle()
    elif ch == 4:
        count_vehicle()
    elif ch == 5:
        traffic_s()
        change_signal()
    elif ch == 6:
        allow_vehicle()
    elif ch == 7:
        detect_lane_violation(70, 50)
    elif ch == 8:
        capture_violation_frame()
    elif ch == 9:
        print("Emergency mode completed")
        emergency_mode()
    elif ch == 10:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
