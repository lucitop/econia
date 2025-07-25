OBJETIVOS_POR_CLASE = {
    "Liberal": {
        "objetivos_principales": [
            "Lograr superávit fiscal durante al menos 3 eventos económicos negativos consecutivos",
            "Convertirse en el centro financiero de la región firmando acuerdos de libre comercio con 3 ciudades distintas"
        ],
        "objetivos_secundarios": [
            "Evitar subsidios por 10 días consecutivos",
            "Reducir el desempleo por debajo del 5%",
            "Acumular más de $5000 sin recibir ayuda externa",
            "Aumentar el comercio exterior en un 30%",
            "Privatizar al menos 3 sectores de la ciudad"
        ]
    },

    "Colectivista": {
        "objetivos_principales": [
            "Establecer un sistema universal de salud y educación con satisfacción ciudadana ≥ 90%",
            "Formar una federación de ayuda mutua con 2 ciudades afines"
        ],
        "objetivos_secundarios": [
            "Reducir la desigualdad a menos de 10%",
            "Crear 3 programas sociales exitosos",
            "Aumentar la felicidad por encima del 80% con impuestos progresivos",
            "Eliminar el desempleo estructural",
            "Redistribuir tierras o recursos productivos en al menos un sector"
        ]
    },

    "Diplomática": {
        "objetivos_principales": [
            "Firmar tratados de paz o cooperación con 4 ciudades distintas",
            "Evitar todo conflicto bélico durante 30 decisiones relevantes"
        ],
        "objetivos_secundarios": [
            "Resolver 3 eventos por vía diplomática",
            "Establecer embajadas con al menos 2 ciudades",
            "Obtener una reputación positiva con el 90% de los vecinos",
            "Participar en una mediación exitosa entre otras dos ciudades",
            "Firmar 2 tratados comerciales o de salud multilaterales"
        ]
    },

    "Guerrera": {
        "objetivos_principales": [
            "Conquistar o dominar al menos 2 ciudades vecinas",
            "Mantener la superioridad militar durante 10 turnos sin perder batallas"
        ],
        "objetivos_secundarios": [
            "Entrenar al ejército al 100% de su capacidad",
            "Responder con éxito a 3 ataques enemigos",
            "Desarrollar una tecnología militar avanzada",
            "Controlar estratégicamente 3 recursos clave",
            "Imponer condiciones en un tratado de paz"
        ]
    },

    "Pragmática": {
        "objetivos_principales": [
            "Resolver 5 crisis optimizando el bienestar general sin dañar ninguna variable clave",
            "Establecer un sistema adaptable de políticas según los indicadores sociales"
        ],
        "objetivos_secundarios": [
            "Tener al menos 3 sectores públicos y 3 privados funcionando eficazmente",
            "Alcanzar 70% de satisfacción en 5 áreas clave simultáneamente",
            "Modificar 2 políticas contradictorias al contexto y acertar",
            "Superar 2 crisis con políticas inesperadas",
            "Reducir la deuda sin sacrificar empleo ni felicidad"
        ]
    },

    "Tradicionalista": {
        "objetivos_principales": [
            "Preservar las costumbres y estructura social durante 20 decisiones sin alterar políticas básicas",
            "Reinstaurar una forma de gobierno o valores culturales antiguos reconocidos por otras ciudades"
        ],
        "objetivos_secundarios": [
            "Evitar cambios estructurales por 15 turnos",
            "Lograr satisfacción ≥ 85% manteniendo costumbres",
            "Impedir reformas externas 3 veces",
            "Fundar una celebración tradicional reconocida",
            "Restaurar un monumento o valor simbólico perdido"
        ]
    },

    "Tecno-Productivista": {
        "objetivos_principales": [
            "Automatizar al menos el 70% de los procesos productivos",
            "Convertirse en centro de innovación exportando 3 tecnologías únicas"
        ],
        "objetivos_secundarios": [
            "Implementar un plan de I+D exitoso",
            "Construir 2 zonas industriales avanzadas",
            "Aumentar productividad en un 50%",
            "Eliminar cuellos de botella logísticos",
            "Atraer inversión tecnológica extranjera"
        ]
    },

    "Populista": {
        "objetivos_principales": [
            "Obtener aprobación ciudadana ≥ 90% en decisiones clave sin importar los datos técnicos",
            "Controlar una crisis redistribuyendo recursos de forma espectacular"
        ],
        "objetivos_secundarios": [
            "Realizar 3 reformas populares sin resistencia",
            "Ganar 2 votaciones o referendos internos",
            "Imponer una narrativa nacional exitosa",
            "Aumentar felicidad a pesar de déficit fiscal",
            "Eliminar oposición en al menos 1 sector"
        ]
    },

    "Teocrática": {
        "objetivos_principales": [
            "Convertirse en un centro espiritual reconocido por otras ciudades",
            "Evangelizar a 2 ciudades vecinas por medios no bélicos"
        ],
        "objetivos_secundarios": [
            "Construir 3 templos o centros de fe",
            "Alcanzar pureza moral ≥ 90%",
            "Evitar la corrupción durante 15 turnos",
            "Responder a un desastre con fe",
            "Impedir 2 reformas que contradigan la doctrina"
        ]
    },

    "Aislacionista": {
        "objetivos_principales": [
            "Mantener la soberanía total sin influencias externas por 20 eventos",
            "Alcanzar autosuficiencia económica y energética"
        ],
        "objetivos_secundarios": [
            "Rechazar 5 tratados internacionales",
            "Proteger todas las fronteras durante una década",
            "Construir reservas estratégicas altas",
            "Eliminar espionaje externo",
            "Reducir dependencias en un 80%"
        ]
    }
}

def obtener_objetivos_para_clase(nombre_clase):
    from city_config import COMBINACIONES_VALIDAS
    if nombre_clase in OBJETIVOS_POR_CLASE:
        objetivos_crudos = OBJETIVOS_POR_CLASE[nombre_clase]
        return {
            "principales": objetivos_crudos["objetivos_principales"],
            "secundarios": objetivos_crudos["objetivos_secundarios"]
        }

    for combinacion, nombre_mixto in COMBINACIONES_VALIDAS.items():
        if nombre_mixto == nombre_clase:
            clases_puras = list(combinacion)
            objetivos = {
                "principales": [],
                "secundarios": []
            }

            for clase in clases_puras:
                if clase in OBJETIVOS_POR_CLASE:
                    objetivos["principales"].extend(OBJETIVOS_POR_CLASE[clase]["objetivos_principales"])
                    objetivos["secundarios"].extend(OBJETIVOS_POR_CLASE[clase]["objetivos_secundarios"])
            
            objetivos["principales"] = objetivos["principales"][:2]
            objetivos["secundarios"] = objetivos["secundarios"][:5]
            return objetivos

    return {
        "principales": ["Objetivo no definido."],
        "secundarios": []
    }
