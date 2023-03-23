import customtkinter as ctk
import tkinter as tk
import tkintermapview

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x650")
        self.master.title("SNGF CONNEKT")
        ctk.set_appearance_mode("Dark")

        self.gares = {
            "Paris Gare du Nord": (48.8809, 2.3553),
            "Paris Gare de Lyon": (48.8448, 2.3741),
            "Lyon Part-Dieu": (45.7605, 4.8596),
            "Marseille Saint-Charles": (43.3027, 5.3806),
            "Bordeaux Saint-Jean": (44.8261, -0.5567),
        }

        self.create_widgets_home()

    def create_widgets_home(self):
        #creation de la carte
        self.map_widget = tkintermapview.TkinterMapView(self.master, width=800, height=600, corner_radius=0)
        self.map_widget.place(x=0, y=50)

        self.map_widget.set_position(47.1221, 2.3200)  # Center of France
        self.map_widget.set_zoom(6)

        #creation des marqueurs
        self.markerlist = []
        root.bind("<MouseWheel>", lambda x : self.show_markers(self.map_widget.zoom, self.markerlist))


        depart_label = ctk.CTkLabel(master=self.master, text="Départ:")
        depart_label.place(x=10, y=10)
        self.depart_var = tk.StringVar(master=self.master)
        depart_entry = ctk.CTkEntry(master=self.master, textvariable=self.depart_var, width=150)
        depart_entry.place(x=60, y=10)

        arrivee_label = ctk.CTkLabel(master=self.master, text="Arrivée:")
        arrivee_label.place(x=350, y=10)
        self.arrivee_var = tk.StringVar(master=self.master)
        arrivee_entry = ctk.CTkEntry(master=self.master, textvariable=self.arrivee_var, width=150)
        arrivee_entry.place(x=400, y=10)

        calculate_button = ctk.CTkButton(master=self.master, text="Calculer", command=self.on_calculate_path)
        calculate_button.place(x=650, y=10)

    
        #Panneau lattéral
        side_panel = ctk.CTkFrame(self.master, width=200, height=650)
        side_panel.place(x=800, y=0)

        self.premiere_classe_var = tk.BooleanVar(master=self.master)
        premiere_classe_CheckBox = ctk.CTkCheckBox(master=side_panel, variable=self.premiere_classe_var, text="Première classe")
        premiere_classe_CheckBox.place(x=10, y=10)

        train_types_label = ctk.CTkLabel(master=side_panel, text="Type de train")
        train_types_label.place(x=10, y=50)

        self.TER_var = tk.BooleanVar(master=self.master)
        ter_radiobutton = ctk.CTkCheckBox(master=side_panel, text="TER", variable=self.TER_var)
        ter_radiobutton.place(x=10, y=80)

        self.TGV_var = tk.BooleanVar(master=self.master)
        tgv_radiobutton = ctk.CTkCheckBox(master=side_panel, text="TGV", variable=self.TGV_var)
        tgv_radiobutton.place(x=10, y=110)

        self.OUIGO_var = tk.BooleanVar(master=self.master)
        ouigo_radiobutton = ctk.CTkCheckBox(master=side_panel, text="OUIGO", variable=self.OUIGO_var)
        ouigo_radiobutton.place(x=10, y=140)

    def show_markers(self,zoom, markerlist):
        if zoom < 9:
            for marker in markerlist:
                marker.delete()
        else:     
            for gare, coords in self.gares.items():
                markerlist.append(self.map_widget.set_marker(coords[0], coords[1], text=gare, command=self.on_marker_click))


    def create_widgets_resultat(self):
        # on detruit la carte pour laisser place au resultat
        self.map_widget.destroy()

        # On setup le layout resultat
        resultat_label = ctk.CTkLabel(master=self.master, text="Résultat")
        resultat_label.place(anchor="center", relx=0.5, rely=0.1)

        retour_button = ctk.CTkButton(master=self.master, text="Retour", command=self.create_widgets_home)
        retour_button.place(x=650, y=10)

    def on_marker_click(self, marker):
        print(f"Clicked on {marker.text}")

        if not self.depart_var.get():
            self.depart_var.set(marker.text)
        elif not self.arrivee_var.get():
            self.arrivee_var.set(marker.text)
        else:
            self.depart_var.set(marker.text)
            self.arrivee_var.set("")

    def on_calculate_path(self):
        depart_gare = self.depart_var.get()
        arrivee_gare = self.arrivee_var.get()
        print(f"Calculer le trajet entre {depart_gare} et {arrivee_gare}")
        # ICI SUITE DE L'APPLI
        # Switch to the example widget setup
        self.create_widgets_resultat()


if __name__ == "__main__":
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()