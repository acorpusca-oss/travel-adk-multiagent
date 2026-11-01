"""Tool with basic local culture information for the LocalCultureAgent."""

_CULTURE_DATA: dict[str, dict] = {
    "cusco": {
        "dishes": ["Cuy al horno", "Chiri uchu", "Sopa de quinua", "Chicha morada"],
        "customs": [
            "Pide permiso antes de fotografiar a personas de comunidades locales.",
            "El mate de coca es común para la altura; consúmelo con moderación.",
            "Respeta los sitios sagrados: no tocar muros incas ni salirse de los senderos.",
        ],
        "phrases": [
            "Allillanchu? - ¿Cómo estás? (quechua)",
            "Sulpayki - Gracias (quechua)",
            "¿Cuánto cuesta? - Para preguntar precios en mercados",
        ],
    },
    "arequipa": {
        "dishes": ["Rocoto relleno", "Adobo arequipeño", "Chupe de camarones", "Queso helado"],
        "customs": [
            "El almuerzo es la comida principal y se disfruta sin prisa en las picanterías.",
            "Es común saludar con un apretón de manos o beso en la mejilla entre conocidos.",
            "El pan y los dulces tradicionales suelen comprarse en mercados y conventos.",
        ],
        "phrases": [
            "Buenos días - Saludo formal",
            "Por favor / Gracias - Cortesía básica",
            "¿Dónde queda...? - Para pedir direcciones",
        ],
    },
    "buenos aires": {
        "dishes": ["Asado", "Empanadas", "Milanesa", "Alfajores con dulce de leche"],
        "customs": [
            "La cena suele empezar tarde, alrededor de las 9 o 10 p. m.",
            "Es habitual saludar con un beso en la mejilla.",
            "El mate se comparte: no lo pases ni lo muevas con la bombilla sin necesidad.",
            "La propina habitual en restaurantes ronda el 10 %.",
        ],
        "phrases": [
            "Che - Interjección informal para llamar la atención",
            "¿Qué hacés? - ¿Cómo estás?",
            "Muchas gracias - Agradecimiento general",
        ],
    },
    "paris": {
        "dishes": ["Croissant", "Baguette con queso", "Coq au vin", "Crêpes", "Sopa de cebolla"],
        "customs": [
            "Saluda con 'Bonjour' al entrar a tiendas y restaurantes.",
            "El servicio suele estar incluido en la cuenta; la propina es opcional.",
            "Evita hablar muy fuerte en transporte público y restaurantes.",
        ],
        "phrases": [
            "Bonjour - Buenos días",
            "Merci / S'il vous plaît - Gracias / Por favor",
            "Parlez-vous anglais ? - ¿Habla inglés?",
        ],
    },
}


def get_local_culture_info(destination: str) -> dict:
    """Return typical dishes, local customs and useful phrases for a destination.

    This is intentionally simple for an introductory laboratory.

    Args:
        destination: Travel destination (for example, "Cusco" or "París").

    Returns:
        Dictionary with dishes, customs and phrases, or a not_found status.
    """
    destination_normalized = (
        destination.lower().strip().replace("í", "i").replace("é", "e").replace("á", "a")
    )

    if not destination_normalized:
        return {
            "status": "error",
            "message": "The destination must not be empty.",
        }

    for key, data in _CULTURE_DATA.items():
        if key in destination_normalized:
            return {
                "status": "success",
                "destination": destination,
                "dishes": data["dishes"],
                "customs": data["customs"],
                "phrases": data["phrases"],
            }

    return {
        "status": "not_found",
        "destination": destination,
        "message": "No local data for this destination. Use general knowledge or web search.",
    }
