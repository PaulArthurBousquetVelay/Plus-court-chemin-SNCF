#ICI ON TEST DES TRUCS POUR PAS TOUT CASSER

import customtkinter as ctk
import tkinter as tk
import tkintermapview

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
        self.map_widget = tkintermapview.TkinterMapView(self.master, width=800, height=600, corner_radius=0)
        self.map_widget.place(relx=0, rely=0.077)

        self.map_widget.set_position(47.1221, 2.3200)  # Center of France
        self.map_widget.set_zoom(6)

        for gare, coords in self.gares.items():
            self.map_widget.set_marker(coords[0], coords[1], text=gare, command=self.on_marker_click)

        depart_label = ctk.CTkLabel(master=self.master, text="Départ:")
        depart_label.place(relx=0.01, rely=0.015)
        self.depart_var = tk.StringVar(master=self.master)
        depart_entry = ctk.CTkEntry(master=self.master, textvariable=self.depart_var, width=150)
        depart_entry.place(relx=0.06, rely=0.015)

        arrivee_label = ctk.CTkLabel(master=self.master, text="Arrivée:")
        arrivee_label.place(relx=0.35, rely=0.015)
        self.arrivee_var = tk.StringVar(master=self.master)
        arrivee_entry = ctk.CTkEntry(master=self.master, textvariable=self.arrivee_var, width=150)
        arrivee_entry.place(relx=0.4, rely=0.015)

        calculate_button = ctk.CTkButton(master=self.master, text="Calculer", command=self.on_calculate_path)
        calculate_button.place(relx=0.65, rely=0.015)

        #Panneau lattéral
        side_panel = ctk.CTkFrame(self.master, width=200, height=650)
        side_panel.place(relx=0.8, rely=0)

        self.premiere_classe_var = tk.BooleanVar(master=self.master)
        premiere_classe_CheckBox = ctk.CTkCheckBox(master=side_panel, variable=self.premiere_classe_var, text="Première classe")
        premiere_classe_CheckBox.place(relx=0.05, rely=0.015)

        train_types_label = ctk.CTkLabel(master=side_panel, text="Type de train")
        train_types_label.place(relx=0.05, rely=0.077)
        self.train_type_var = tk.StringVar(master=self.master)
        ter_radiobutton = ctk.CTkRadioButton(master=side_panel, text="TER", variable=self.train_type_var, value="TER")
        ter_radiobutton.place(relx=0.05, rely=0.123)
        tgv_radiobutton = ctk.CTkRadioButton(master=side_panel, text="TGV", variable=self.train_type_var, value="TGV")
        tgv_radiobutton.place(relx=0.05, rely=0.169)
        ouigo_radiobutton = ctk.CTkRadioButton(master=side_panel, text="OUIGO", variable=self.train_type_var, value="OUIGO")
        ouigo_radiobutton.place(relx=0.05, rely=0.215)

        
    def create_widgets_resultat(self):
        # Remove previous widgets
        self.map_widget.destroy()

        # Example widget setup
        resultat_label = ctk.CTkLabel(master=self.master, text="Résultat")
        resultat_label.place(anchor="center", relx=0.5, rely=0.1)

        retour_button = ctk.CTkButton(master=self.master, text="Retour", command=self.create_widgets_home)
        retour_button.place(relx=0.65, rely=0.015)

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