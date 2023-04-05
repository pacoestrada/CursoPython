import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GastosApp(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Registro de Gastos")
        self.set_default_size(400, 300)

        # Crear una caja vertical para contener los elementos de la ventana
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)

        # Etiqueta de título
        self.label = Gtk.Label(label="Registro de Gastos")
        self.label.set_markup("<big><b>Registro de Gastos</b></big>")
        self.box.pack_start(self.label, False, False, 0)

        # Botón para agregar gastos
        self.button = Gtk.Button(label="Agregar Gastos")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, False, False, 0)

        # Lista de gastos
        self.liststore = Gtk.ListStore(str, str, float)
        self.treeview = Gtk.TreeView(model=self.liststore)

        for i, column_title in enumerate(["Motivo", "Lugar", "Cantidad"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        self.box.pack_start(self.treeview, True, True, 0)

        # Etiqueta para la cantidad total
        self.total_label = Gtk.Label(label="Cantidad Total: 0 euros")
        self.box.pack_start(self.total_label, False, False, 0)

    def on_button_clicked(self, widget):
        dialog = Gtk.Dialog(title="Agregar Gasto", parent=self, flags=0)
        dialog.add_button("Cancelar", Gtk.ResponseType.CANCEL)
        dialog.add_button("Agregar", Gtk.ResponseType.OK)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        dialog.get_content_area().add(grid)

        motivo_label = Gtk.Label(label="Motivo:")
        lugar_label = Gtk.Label(label="Lugar:")
        cantidad_label = Gtk.Label(label="Cantidad:")

        motivo_entry = Gtk.Entry()
        lugar_entry = Gtk.Entry()
        cantidad_entry = Gtk.Entry()

        grid.attach(motivo_label, 0, 0, 1, 1)
        grid.attach(motivo_entry, 1, 0, 1, 1)
        grid.attach(lugar_label, 0, 1, 1, 1)
        grid.attach(lugar_entry, 1, 1, 1, 1)
        grid.attach(cantidad_label, 0, 2, 1, 1)
        grid.attach(cantidad_entry, 1, 2, 1, 1)

        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.liststore.append([motivo_entry.get_text(), lugar_entry.get_text(), float(cantidad_entry.get_text())])
            cantidad_total = sum([row[2] for row in self.liststore])
            self.total_label.set_text("Cantidad Total: {} euros".format(cantidad_total))

        dialog.destroy()

win = GastosApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
