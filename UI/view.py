import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.btn_analizzaVendite = None
        self.btn_topVendite = None
        self.dd_retailer = None
        self.dd_brand = None
        self.dd_anno = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW with some controls

        self.dd_anno = ft.Dropdown(label="anno",
                                   hint_text="anno")

        self._controller.fillAnni()

        self.dd_brand = ft.Dropdown(label="brand",
                                    hint_text="brand")
        self._controller.fillBrand()

        self.dd_retailer = ft.Dropdown(label="retailer",
                                       hint_text="retailer")
        self._controller.fillRetailer()

        # button for the "hello" reply

        self.btn_topVendite = ft.ElevatedButton(text="Top Vendite",
                                                on_click=self._controller.handle_topVendite)
        self.btn_analizzaVendite = ft.ElevatedButton(text="Analizza Vendite",
                                                     on_click=self._controller.handle_analizzaVendite)

        row1 = ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)

        row2 = ft.Row([self.btn_topVendite, self.btn_analizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
