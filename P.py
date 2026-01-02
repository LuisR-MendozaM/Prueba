import flet as ft

def main(page: ft.Page):
    # Si tu rango es -30 a 0 y quieres espacio "abajo" (más negativo)
    data = [-25, -20, -18, -12, -8]
    
    chart = ft.LineChart(
        data_series=[
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(i, data[i]) for i in range(len(data))
                ],
                stroke_width=3,
                color=ft.colors.PURPLE,
            )
        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=-35, label=ft.Text("")),  # Etiqueta vacía para espacio
                ft.ChartAxisLabel(value=-30, label=ft.Text("-30")),
                ft.ChartAxisLabel(value=-20, label=ft.Text("-20")),
                ft.ChartAxisLabel(value=-10, label=ft.Text("-10")),
                ft.ChartAxisLabel(value=0, label=ft.Text("0")),
            ],
            labels_size=40,
        ),
        # Espacio de -35 a -30 antes de que empiecen los valores
        min_y=-35,
        max_y=5,  # Un poco de espacio arriba del 0
        expand=True,
    )
    
    page.add(
        ft.Column([
            ft.Text("Espacio en eje Y negativo", size=20),
            ft.Text("min_y=-35 crea espacio de -35 a -30", size=14),
            chart
        ])
    )

ft.app(main)
