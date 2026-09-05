import time
import flet as ft

COOLDOWN_SECONDS = 24 * 3600

def main(page: ft.Page):
    page.title = "Energy Tracker"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Твоя коллекция банок
    collection_items = [
        {"name": "BURN Сочная Энергия", "volume": "0.449 л", "caffeine": 135},
        {"name": "Adrenaline Rush", "volume": "0.449 л", "caffeine": 135},
    ]

    last_drink_time = 0

    status_text = ft.Text("🟢 Можно пить энергос!", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_400)
    timer_text = ft.Text("24:00:00", size=36, weight=ft.FontWeight.BOLD)

    def drink_click(e):
        nonlocal last_drink_time
        last_drink_time = time.time()
        status_text.value = "🔴 Кулдаун 24 часа!"
        status_text.color = ft.colors.RED_400
        page.update()

    drink_btn = ft.ElevatedButton(
        text="🍺 Выпил энергос!",
        style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.RED_600),
        on_click=drink_click,
        height=50,
    )

    coll_controls = []
    for item in collection_items:
        coll_controls.append(
            ft.ListTile(
                leading=ft.Icon(ft.icons.LOCAL_DRINK, color=ft.colors.AMBER_400),
                title=ft.Text(item["name"]),
                subtitle=ft.Text(f"Объем: {item['volume']} | Кофеин: {item['caffeine']} мг"),
            )
        )

    page.add(
        ft.Text("⚡ Energy Tracker", size=26, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        status_text,
        timer_text,
        drink_btn,
        ft.Divider(),
        ft.Text("📦 Коллекция:", size=18, weight=ft.FontWeight.BOLD),
        ft.Column(controls=coll_controls, scroll=ft.ScrollMode.AUTO, expand=True)
    )

ft.app(target=main)
