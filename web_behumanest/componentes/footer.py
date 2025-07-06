import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src="/SALUD.png", width="auto", height="40px"),  # Asegurate de tener el logo en assets/
            rx.text("© 2025 Behumanest. Proyecto piloto de humanización al paciente.", font_size="sm"),
            spacing="2",
            align="center",
        ),
        position="fixed",
        bottom="0",
        width="100%",
        bg="gray.100",
        padding="1em",
        box_shadow="md",
        z_index="100",
    )