import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import io
import folium
import base64

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x650")
        self.master.title("SNGF CONNEKT")

        self.gares = {
            "Paris Gare du Nord": (48.8809, 2.3553),
            "Paris Gare de Lyon": (48.8448, 2.3741),
            "Lyon Part-Dieu": (45.7605, 4.8596),
            "Marseille Saint-Charles": (43.3027, 5.3806),
            "Bordeaux Saint-Jean": (44.8261, -0.5567),
        }

        self.create_widgets_home()

    def create_widgets_home(self):
        self.map_widget = self.create_map()
        self.map_widget.pack()

        depart_label = ttk.Label(master=self.master, text="Départ:")
        depart_label.place(x=10, y=10)
        self.depart_var = tk.StringVar(master=self.master)
        depart_entry = ttk.Entry(master=self.master, textvariable=self.depart_var, width=20)
        depart_entry.place(x=60, y=10)

        arrivee_label = ttk.Label(master=self.master, text="Arrivée:")
        arrivee_label.place(x=350, y=10)
        self.arrivee_var = tk.StringVar(master=self.master)
        arrivee_entry = ttk.Entry(master=self.master, textvariable=self.arrivee_var, width=20)
        arrivee_entry.place(x=400, y=10)

        calculate_button = ttk.Button(master=self.master, text="Calculer", command=self.on_calculate_path)
        calculate_button.place(x=650, y=10)

        side_panel = ttk.Frame(self.master, width=200, height=650)
        side_panel.place(x=800, y=0)

        self.premiere_classe_var = tk.BooleanVar(master=self.master)
        premiere_classe_CheckBox = ttk.Checkbutton(master=side_panel, variable=self.premiere_classe_var, text="Première classe")
        premiere_classe_CheckBox.place(x=10, y=10)

        train_types_label = ttk.Label(master=side_panel, text="Type de train")
        train_types_label.place(x=10, y=50)

        self.TER_var = tk.BooleanVar(master=self.master)
        ter_radiobutton = ttk.Checkbutton(master=side_panel, text="TER", variable=self.TER_var)
        ter_radiobutton.place(x=10, y=80)

        self.TGV_var = tk.BooleanVar(master=self.master)
        tgv_radiobutton = ttk.Checkbutton(master=side_panel, text="TGV", variable=self.TGV_var)
        tgv_radiobutton.place(x=10, y=110)

        self.OUIGO_var = tk.BooleanVar(master=self.master)
        ouigo_radiobutton = ttk.Checkbutton(master=side_panel, text="OUIGO", variable=self.OUIGO_var)
        ouigo_radiobutton.place(x=10, y=140)

    def create_map(self):
        map_frame = tk.Frame(self.master)
        m = folium.Map(location=[47.1221, 2.3200], zoom_start=6, control_scale=True)

        for gare, coords in self.gares.items():
            folium.Marker(coords, popup=gare, tooltip=gare).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        data.seek(0)
        img = Image.open(data)
        img.thumbnail((800, 600))

        map_image = ImageTk.PhotoImage(img)
        map_label = tk.Label(map_frame, image=map_image)
        map_label.image = map_image
        map_label.pack()

        return map_frame

    def on_calculate_path(self):
        depart_gare = self.depart_var.get()
        arrivee_gare = self.arrivee_var.get()
        print(f"Calculer le trajet entre {depart_gare} et {arrivee_gare}")
        # You can implement the rest of the app as needed

if __name__ == "main":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()