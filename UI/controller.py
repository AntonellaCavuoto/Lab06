import flet as ft
import self as self

from model import retailer


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._retailer = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillAnni(self):
        self._view.dd_anno.options.append(ft.dropdown.Option("Nessun filtro"))

        for anno in self._model.getAnni():
            self._view.dd_anno.options.append(ft.dropdown.Option(anno))

        self._view.update_page()

    def fillBrand(self):
        self._view.dd_brand.options.append(ft.dropdown.Option("Nessun filtro"))

        for brand in self._model.getBrand():
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))

        self._view.update_page()

    def read_retailer(self, e):
        self._retailer = e.control.data
    def fillRetailer(self):
        self._view.dd_retailer.options.append(ft.dropdown.Option("Nessun filtro"))
        for ret in self._model.getRetailer():
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=ret.name,
                                                                         text=ret.name,
                                                                         data=ret,
                                                                         on_click=self.read_retailer))
        self._view.update_page()

    def handle_topVendite(self, e):
        self._view.txt_result.controls.clear()

        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        ret = self._view.dd_retailer.value

        if anno == "Nessun filtro":
            anno = None

        if brand == "Nessun filtro":
            brand = None

        if ret == "Nessun filtro":
            ret = None

        top_vendite = self._model.getTopVendite(anno, brand, ret)

        for top in top_vendite:
            self._view.txt_result.controls.append(ft.Text(top))

        self._view.update_page()


    def handle_analizzaVendite(self, e):
        self._view.txt_result.controls.clear()

        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        ret = self._view.dd_retailer.value

        if anno == "Nessun filtro":
            anno = None

        if brand == "Nessun filtro":
            brand = None

        if ret == "Nessun filtro":
            ret = None

        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        analisi = self._model.getAnalisiVendite(anno, brand, ret)
        self._view.txt_result.controls.append(ft.Text(analisi))

        self._view.update_page()






