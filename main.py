import time
import flet as ft

def main(page: ft.Page):
    page.title = "Energy Tracker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#100914"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    last_drink_time = 0

    collection_items = [
        {"name": "BURN Сочная Энергия", "volume": "0.449 л", "caffeine": "135 мг", "color": "#800020"},
        {"name": "Adrenaline Rush", "volume": "0.449 л", "caffeine": "135 мг", "color": "#4A0E4E"},
        {"name": "Monster Energy", "volume": "0.5 л", "caffeine": "160 мг", "color": "#2A085C"},
    ]

    status_icon = ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color="#A855F7", size=32)
    status_text = ft.Text("Готов к зарядке!", size=18, weight=ft.FontWeight.BOLD, color="#A855F7")
    timer_text = ft.Text("24:00:00", size=42, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    
    drink_btn = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.FLASH_ON_ROUNDED, color=ft.Colors.WHITE),
                ft.Text("ВЫПИЛ ЭНЕРГОС", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor={"": "#8B0000", ft.ControlState.DISABLED: "#2A1A2A"},
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
        width=280,
        height=54,
    )

    def drink_action(e):
        nonlocal last_drink_time
        last_drink_time = time.time()
        status_icon.name = ft.Icons.TIMER_OUTLINED
        status_icon.color = "#FF2E93"
        status_text.value = "Кулдаун активен"
        status_text.color = "#FF2E93"
        drink_btn.disabled = True
        
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Заряд получен! Таймер запущен ⚡"),
            bgcolor="#2A0A3B"
        )
        page.snack_bar.open = True
        page.update()

    drink_btn.on_click = drink_action

    timer_card = ft.Container(
        content=ft.Column(
            [
                ft.Row([status_icon, status_text], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Container(height=10),
                timer_text,
                ft.Container(height=15),
                drink_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=24,
        border_radius=20,
        bgcolor="#1A0F24",
        border=ft.border.all(1, "#3B1459"),
    )

    coll_cards = []
    for item in collection_items:
        coll_cards.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(ft.Icons.LOCAL_DRINK_ROUNDED, color=ft.Colors.WHITE, size=24),
                            bgcolor=item["color"],
                            padding=12,
                            border_radius=12,
                        ),
                        ft.Column(
                            [
                                ft.Text(item["name"], size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Text(f"{item['volume']} • {item['caffeine']}", size=13, color="#B388FF"),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.ADD_CIRCLE_OUTLINE_ROUNDED,
                            icon_color="#A855F7",
                            tooltip="Пить этот",
                            on_click=drink_action,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=12,
                border_radius=14,
                bgcolor="#160C21",
                border=ft.border.all(1, "#2C1242"),
            )
        )

    page.add(
        ft.Container(height=10),
        ft.Row(
            [
                ft.Image(src="assets/icon.png", width=36, height=36, error_content=ft.Icon(ft.Icons.BOLT_ROUNDED, color="#A855F7", size=36)),
                ft.Text("ENERGY TRACKER", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        ft.Container(height=15),
        timer_card,
        ft.Container(height=25),
        ft.Row(
            [
                ft.Text("Моя коллекция", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(f"{len(collection_items)} банок", size=14, color="#B388FF"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Container(height=10),
        ft.Column(controls=coll_cards, spacing=10),
    )

ft.app(target=main, assets_dir="assets")
