import tkinter
import tkintermapview

# Train station coordinates
stations = {
    "Paris Gare du Nord": (48.8809, 2.3553),
    "Paris Gare de Lyon": (48.8448, 2.3741),
    "Lyon Part-Dieu": (45.7605, 4.8596),
    "Marseille Saint-Charles": (43.3027, 5.3806),
    "Bordeaux Saint-Jean": (44.8261, -0.5567),
}

def on_marker_click(marker):
    global start_var, goal_var
    print(f"Clicked on {marker.text}")

    if not start_var.get():
        start_var.set(marker.text)
    elif not goal_var.get():
        goal_var.set(marker.text)
    else:
        start_var.set(marker.text)
        goal_var.set("")

def on_calculate_path():
    start_station = start_var.get()
    goal_station = goal_var.get()
    print(f"Calculating path from {start_station} to {goal_station}")
    # You can implement your pathfinding algorithm here

# Create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry("800x650")
root_tk.title("French Train Stations Map")

# Create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(x=0, y=50)

# Set map position and zoom
map_widget.set_position(47.1221, 2.3200)  # Center of France
map_widget.set_zoom(6)

# Add markers for train stations
for station, coords in stations.items():
    map_widget.set_marker(coords[0], coords[1], text=station, command=on_marker_click)

# Start and goal station entry boxes
start_label = tkinter.Label(root_tk, text="Start Station:")
start_label.place(x=10, y=10)
start_var = tkinter.StringVar(root_tk)
start_entry = tkinter.Entry(root_tk, textvariable=start_var, width=30)
start_entry.place(x=100, y=10)

goal_label = tkinter.Label(root_tk, text="Goal Station:")
goal_label.place(x=400, y=10)
goal_var = tkinter.StringVar(root_tk)
goal_entry = tkinter.Entry(root_tk, textvariable=goal_var, width=30)
goal_entry.place(x=490, y=10)

# Calculate path button
calculate_button = tkinter.Button(root_tk, text="Calculate Path", command=on_calculate_path)
calculate_button.place(x=750, y=10)

# Start the main loop
root_tk.mainloop()
