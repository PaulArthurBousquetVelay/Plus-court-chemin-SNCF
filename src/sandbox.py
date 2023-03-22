import tkinter
import tkintermapview


class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x650")
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
        self.map_widget.place(x=0, y=50)

        self.map_widget.set_position(47.1221, 2.3200)  # Center of France
        self.map_widget.set_zoom(6)

        for gare, coords in self.gares.items():
            self.map_widget.set_marker(coords[0], coords[1], text=gare, command=self.on_marker_click)

        depart_label = tkinter.Label(self.master, text="Départ:")
        depart_label.place(x=10, y=10)
        self.depart_var = tkinter.StringVar(self.master)
        depart_entry = tkinter.Entry(self.master, textvariable=self.depart_var, width=30)
        depart_entry.place(x=100, y=10)

        arrivee_label = tkinter.Label(self.master, text="Arrivée:")
        arrivee_label.place(x=400, y=10)
        self.arrivee_var = tkinter.StringVar(self.master)
        arrivee_entry = tkinter.Entry(self.master, textvariable=self.arrivee_var, width=30)
        arrivee_entry.place(x=490, y=10)

        calculate_button = tkinter.Button(self.master, text="Calculer", command=self.on_calculate_path)
        calculate_button.place(x=700, y=5)

    def create_widgets_resultat(self):
        # Remove previous widgets
        self.map_widget.destroy()

        # Example widget setup
        resultat_label = tkinter.Label(self.master, text="Résultat")
        resultat_label.place(anchor=tkinter.CENTER, relx=0.5, rely=0.1)

        retour_button = tkinter.Button(self.master, text="Retour", command=self.create_widgets_home)
        retour_button.place(x=700, y=5)

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
        # ICI SUITE DE L'APPLI genre disjrka et afficher resultats

        # Switch to the example widget setup
        self.create_widgets_resultat()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()
