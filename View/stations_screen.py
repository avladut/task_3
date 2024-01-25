import PySimpleGUI as sg

from Controller.zone_conroller import ZoneController

class StationsScreen(sg.Window):

     def __init__(self, zones_provider: ZoneController):

        self.zone_provider = zones_provider
        zones = zones_provider.get_zone_names()
        stations = zones_provider.get_formatted_stations()

        sg.theme('DarkAmber')   # Add a little color to your windows

        sg.set_options(font=("Arial Bold", 14))

        tbl1 = sg.Table(values=stations, 
        headings= zones,
        auto_size_columns=True,
        display_row_numbers=False,
        justification='center', key='-TABLE-',
        selected_row_colors='red on yellow',
        enable_events=True,
        expand_x=True,
        expand_y=True,
        enable_click_events=True,
        row_height= 50,
        vertical_scroll_only = False)

        next_button = sg.Button('Next')

        layout = [[tbl1, next_button]]
        window = sg.Window('Station_table', layout, size=(715, 350), resizable=True)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Next':
                print('Hello, World!')

        window.close()