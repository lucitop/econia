# city_identity.py

import random
from collections import defaultdict

# CLASES Y EFECTOS DEFINIDOS

CITY_CLASSES = {
    "Guerrera": {
        "bonos": {"reservas": 20, "empleo": 10},
        "efectos": ["mejor desempeño en eventos bélicos"],
        "penalizacion": {"felicidad": -10}
    },
    "Diplomática": {
        "bonos": {"felicidad": 15, "reservas": 15},
        "efectos": ["alianzas generan beneficios"],
        "penalizacion": {"empleo": -10}
    },
    "Liberal": {
        "bonos": {"dinero": 20},
        "efectos": ["acceso a privatizaciones y desregulación anticipada"],
        "penalizacion": {"salud": -10}
    },
    "Colectivista": {
        "bonos": {"salud": 15, "felicidad": 15},
        "efectos": ["menor costo de políticas sociales"],
        "penalizacion": {"dinero": -10}
    },
    "Pragmática": {
        "bonos": {"dinero": 10, "salud": 10, "felicidad": 10, "empleo": 10, "reservas": 10},
        "efectos": ["menor impacto de efectos negativos"],
        "penalizacion": {"especial": "no accede a reformas extremas"}
    },
    "Aislacionista": {
        "bonos": {"produccion": 15},
        "efectos": ["menor impacto de shocks externos"],
        "penalizacion": {"reservas": -15}
    },
    "Tecno-Productivista": {
        "bonos": {"empleo": 20},
        "efectos": ["acceso a políticas de inversión y educación avanzada"],
        "penalizacion": {"felicidad": -10}
    },
    "Tradicionalista": {
        "bonos": {"felicidad": 15, "salud": 10},
        "efectos": ["resistencia cultural a eventos"],
        "penalizacion": {"empleo": -10}
    },
    "Teocrática": {
        "bonos": {"felicidad": 20},
        "efectos": ["menor efecto de políticas impopulares"],
        "penalizacion": {"reservas": -15}
    }
    # Las mixtas se agregan al vuelo más adelante
}

# PREGUNTAS Y RESPUESTAS

PREGUNTAS_POOL = [
    {
        "texto": "Un grupo poderoso amenaza tu ciudad si no adoptás sus valores. ¿Qué hacés?",
        "opciones": {
            "Resistir y reforzar nuestras fuerzas": ["Guerrera"],
            "Negociar una salida pacífica": ["Diplomática"],
            "Aceptar si es conveniente económicamente": ["Liberal"],
            "Reunir al pueblo y decidir en conjunto": ["Colectivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Se descubre una nueva tecnología agrícola, pero cara. ¿Qué hacés?",
        "opciones": {
            "La adoptamos rápidamente, mejorará nuestra producción.": ["Tecno-Productivista"],
            "Esperamos a que baje el precio, no arriesgamos.": ["Tradicionalista"],
            "La subvencionamos para que todos puedan usarla.": ["Colectivista"],
            "Solo la usan quienes puedan pagarla.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una minoría cultural exige reconocimiento. ¿Cómo respondés?",
        "opciones": {
            "Escuchamos y generamos canales de diálogo.": ["Diplomática"],
            "Mantenemos los valores tradicionales.": ["Tradicionalista"],
            "Aplicamos una consulta popular.": ["Pragmática"],
            "Ignoramos el pedido para no dividir a la población.": ["Teocrática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "¿Qué política priorizarías en una crisis económica?",
        "opciones": {
            "Recortes fiscales urgentes.": ["Liberal"],
            "Subsidios inmediatos a los sectores vulnerables.": ["Populista"],
            "Fomentar inversión tecnológica.": ["Tecno-Productivista"],
            "Reunir un consejo de sectores para coordinar medidas.": ["Pragmática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una potencia extranjera propone un tratado desigual. ¿Firmás?",
        "opciones": {
            "Jamás. Nuestra soberanía es lo primero.": ["Guerrera"],
            "Negociamos mejores términos.": ["Diplomática"],
            "Aceptamos si trae beneficios a corto plazo.": ["Populista"],
            "Solo si permite acceso a nuevos mercados.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Tu pueblo exige más participación política. ¿Cómo actuás?",
        "opciones": {
            "Implemento mecanismos de democracia directa.": ["Colectivista"],
            "Promuevo debates amplios sin ceder el control.": ["Tradicionalista"],
            "Respondo con mayor transparencia y datos.": ["Tecno-Productivista"],
            "Redacto una nueva constitución con participación ciudadana.": ["Pragmática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Se detecta una pandemia en países vecinos. ¿Qué hacés?",
        "opciones": {
            "Cierro completamente las fronteras.": ["Aislacionista"],
            "Coordinamos con países vecinos para una estrategia común.": ["Diplomática"],
            "Reforzamos el sistema de salud con inversión estatal.": ["Colectivista"],
            "Compramos vacunas con urgencia, sin importar el costo.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Tu población se polariza ideológicamente. ¿Qué estrategia seguís?",
        "opciones": {
            "Unificamos con valores religiosos y éticos.": ["Teocrática"],
            "Promovemos diálogo nacional abierto.": ["Diplomática"],
            "Fortalecemos un liderazgo firme.": ["Populista"],
            "Educación cívica para todos.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Se descubre una enorme reserva de recursos naturales. ¿Cómo la usás?",
        "opciones": {
            "Explotación inmediata vía empresas nacionales.": ["Colectivista"],
            "Licencias privadas con impuestos bajos.": ["Liberal"],
            "Plan de uso a largo plazo con supervisión.": ["Pragmática"],
            "Se protege como patrimonio espiritual.": ["Teocrática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un escándalo de corrupción sacude a tu gobierno. ¿Qué hacés?",
        "opciones": {
            "Desplazo a todos los involucrados y convoco elecciones.": ["Pragmática"],
            "Culpo a fuerzas externas y cierro filas.": ["Guerrera"],
            "Consulto con líderes religiosos para una respuesta moral.": ["Teocrática"],
            "Implemento auditorías con inteligencia artificial.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Tus ciudadanos reclaman un sistema educativo más justo. ¿Qué priorizás?",
        "opciones": {
            "Gratuidad y acceso universal.": ["Colectivista"],
            "Mejorar calidad con competencia entre escuelas.": ["Liberal"],
            "Educación en valores patrióticos.": ["Tradicionalista"],
            "Mayor inversión en ciencia y tecnología.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una comunidad aislada pide autonomía total. ¿Cómo respondés?",
        "opciones": {
            "Respetamos su decisión y los dejamos autogestionarse.": ["Aislacionista"],
            "Dialogamos y buscamos integración.": ["Diplomática"],
            "Aplicamos la ley con firmeza.": ["Guerrera"],
            "Aceptamos si reducen nuestra carga fiscal.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Hay una fuerte caída de empleo joven. ¿Qué hacés?",
        "opciones": {
            "Fomentamos industrias de alta tecnología.": ["Tecno-Productivista"],
            "Plan de empleo estatal temporal.": ["Colectivista"],
            "Reducción de impuestos al empleo juvenil.": ["Liberal"],
            "Movilizamos la comunidad religiosa para contención social.": ["Teocrática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Cae la natalidad. ¿Qué política adoptás?",
        "opciones": {
            "Incentivos económicos por hijo.": ["Populista"],
            "Educación y salud reproductiva.": ["Pragmática"],
            "Campañas culturales sobre el valor de la familia.": ["Tradicionalista"],
            "No hacemos nada, es parte del progreso.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El transporte público está colapsado. ¿Qué hacés?",
        "opciones": {
            "Inversión pública masiva.": ["Colectivista"],
            "Privatización con regulaciones.": ["Liberal"],
            "Cooperativas barriales de transporte.": ["Tradicionalista"],
            "Desarrollo de tecnología autónoma.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "La inflación aumenta rápidamente. ¿Qué medida tomás primero?",
        "opciones": {
            "Control de precios y subsidios.": ["Populista"],
            "Política monetaria restrictiva.": ["Liberal"],
            "Diálogo social y acuerdo de precios.": ["Diplomática"],
            "Auditoría técnica del gasto público.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una empresa extranjera quiere instalar una megafactoría. ¿Qué hacés?",
        "opciones": {
            "Autorizamos con impuestos bajos.": ["Liberal"],
            "Solo si cumple normas ambientales y laborales estrictas.": ["Pragmática"],
            "Impulsamos una empresa estatal alternativa.": ["Colectivista"],
            "La rechazamos, no queremos depender de otros.": ["Aislacionista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Tus reservas internacionales bajan peligrosamente. ¿Qué hacés?",
        "opciones": {
            "Buscamos acuerdos diplomáticos y préstamos.": ["Diplomática"],
            "Ajuste fiscal urgente.": ["Liberal"],
            "Movilizamos el aparato productivo estatal.": ["Colectivista"],
            "Emitimos dinero para frenar la recesión.": ["Populista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Los jóvenes rechazan el sistema político actual. ¿Qué hacés?",
        "opciones": {
            "Abrimos un canal de diálogo y reformas.": ["Pragmática"],
            "Creamos un Ministerio de Juventud y Cultura.": ["Populista"],
            "Fortalecemos los valores religiosos.": ["Teocrática"],
            "Fomentamos participación mediante plataformas digitales.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una crisis climática global golpea al país. ¿Qué priorizás?",
        "opciones": {
            "Autonomía alimentaria y energética.": ["Aislacionista"],
            "Alianzas internacionales para cooperación.": ["Diplomática"],
            "Política científica y tecnológica ambiental.": ["Tecno-Productivista"],
            "Regulación ambiental estricta y redistributiva.": ["Colectivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una sociedad funciona mejor cuando hay un liderazgo fuerte que mantenga el orden.",
        "opciones": {
            "Estoy completamente de acuerdo.": ["Guerrera"],
            "Estoy de acuerdo solo si se respeta la democracia.": ["Pragmática"],
            "Prefiero una sociedad basada en la deliberación y el consenso.": ["Diplomática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El rol del Estado debe ser garantizar el bienestar social aunque eso implique altos impuestos.",
        "opciones": {
            "Totalmente de acuerdo.": ["Colectivista"],
            "Solo en casos extremos.": ["Pragmática"],
            "El Estado debe intervenir lo menos posible.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "La cultura nacional debe preservarse aunque eso limite ciertas libertades individuales.",
        "opciones": {
            "Sí, la tradición debe respetarse.": ["Tradicionalista"],
            "Solo si no se vulneran derechos fundamentales.": ["Pragmática"],
            "No, la cultura debe adaptarse a los tiempos.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un desarrollo económico sostenible depende del avance científico y tecnológico.",
        "opciones": {
            "Absolutamente cierto.": ["Tecno-Productivista"],
            "Solo si se regula con fines sociales.": ["Colectivista"],
            "Debe estar guiado por valores espirituales.": ["Teocrática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "La autodeterminación de un país está por encima de cualquier tratado internacional.",
        "opciones": {
            "Siempre.": ["Guerrera"],
            "Depende del contexto.": ["Diplomática"],
            "Es una excusa para el aislamiento.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El populismo es una herramienta útil para conectar con las masas.",
        "opciones": {
            "Sí, es necesario en democracia.": ["Populista"],
            "Solo si se usa con responsabilidad.": ["Pragmática"],
            "No, lleva a decisiones impulsivas.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "La economía debe ser planificada por técnicos y expertos.",
        "opciones": {
            "Sí, el conocimiento debe guiar las decisiones.": ["Tecno-Productivista"],
            "Solo si hay control ciudadano.": ["Colectivista"],
            "Prefiero el mercado como guía.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "La espiritualidad debe tener un rol central en la vida pública.",
        "opciones": {
            "Sí, la fe unifica a la sociedad.": ["Teocrática"],
            "Solo como parte del debate cultural.": ["Tradicionalista"],
            "No, debe separarse de la política.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "La apertura comercial beneficia a todos en el largo plazo.",
        "opciones": {
            "Sí, hay que integrarse al mundo.": ["Diplomática"],
            "Depende de la protección a la industria nacional.": ["Pragmática"],
            "No, priorizo la autosuficiencia.": ["Aislacionista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un país fuerte necesita capacidad militar.",
        "opciones": {
            "Sí, es esencial para la defensa.": ["Guerrera"],
            "Solo como disuasión.": ["Pragmática"],
            "No, hay que invertir más en cooperación.": ["Diplomática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El progreso tecnológico sin guía moral es tan peligroso como la ignorancia organizada.",
        "opciones": {
            "La moral debe liderar la ciencia.": ["Teocrática"],
            "Necesitamos equilibrio y regulación.": ["Pragmática"],
            "El conocimiento se justifica por sí mismo.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un sabio dijo: 'Para alimentar a todos, a veces hay que expropiar a unos pocos'.",
        "opciones": {
            "Tiene razón.": ["Colectivista"],
            "Solo si hay consenso democrático.": ["Pragmática"],
            "Eso justifica autoritarismos peligrosos.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una estatua de un héroe nacional es derribada en una protesta.",
        "opciones": {
            "Reinstalo la estatua como símbolo de unidad.": ["Tradicionalista"],
            "Abro un debate público sobre su legado.": ["Diplomática"],
            "No intervengo, que el pueblo decida.": ["Populista"],
            "Construyo un museo donde todos los símbolos convivan.": ["Pragmática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El enemigo está en las puertas, pero el pueblo está dividido.",
        "opciones": {
            "Unifico con un discurso de identidad nacional.": ["Guerrera"],
            "Busco un frente político amplio.": ["Diplomática"],
            "Genero lealtad a través del fervor religioso.": ["Teocrática"],
            "Lanzo una campaña educativa masiva.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El conocimiento debe ser un bien común, no un privilegio.",
        "opciones": {
            "Coincido plenamente.": ["Colectivista"],
            "Sí, pero con incentivos al mérito.": ["Pragmática"],
            "Solo si no frena la innovación privada.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una generación entera quiere abandonar el país.",
        "opciones": {
            "Refuerzo los lazos culturales y espirituales.": ["Tradicionalista"],
            "Genero incentivos laborales y académicos.": ["Tecno-Productivista"],
            "Escucho sus razones y promuevo reformas.": ["Pragmática"],
            "Los dejo ir, nadie está obligado a quedarse.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un país no es una empresa. No todo se puede medir en rentabilidad.",
        "opciones": {
            "Totalmente de acuerdo.": ["Colectivista"],
            "Depende del área: algunas cosas sí.": ["Pragmática"],
            "Es un error pensar así. La eficiencia importa.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Tus ancestros dejaron un legado de sangre, tierra y fe.",
        "opciones": {
            "Debemos honrar ese legado.": ["Tradicionalista"],
            "Hay que reinterpretarlo para el presente.": ["Diplomática"],
            "Solo debemos conservar lo útil.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Hay algo sagrado en cada comunidad que la ley no puede definir.",
        "opciones": {
            "Eso debe protegerse.": ["Teocrática"],
            "Puede inspirar políticas públicas.": ["Tradicionalista"],
            "El Estado no debe legislar sobre lo sagrado.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Si no hay justicia para todos, no habrá paz para nadie.",
        "opciones": {
            "Hay que redistribuir poder y recursos.": ["Colectivista"],
            "Hay que asegurar reglas claras e iguales.": ["Liberal"],
            "Hay que educar para la paz.": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El pueblo canta el himno bajo la lluvia, mientras el país atraviesa una crisis.",
        "opciones": {
            "Eso demuestra su fuerza espiritual.": ["Teocrática"],
            "Es tiempo de convertir esa emoción en políticas concretas.": ["Pragmática"],
            "Me conmueve, pero también me preocupa el fanatismo.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una gran empresa ofrece regalar computadoras a cambio de instalar antenas de datos en cada escuela.",
        "opciones": {
            "Acepto, es progreso.": ["Tecno-Productivista"],
            "Solo si hay regulación y control social.": ["Pragmática"],
            "Rechazo. La educación no se negocia.": ["Tradicionalista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Durante una visita oficial, el embajador extranjero critica la historia de tu país.",
        "opciones": {
            "Lo expulso de inmediato.": ["Guerrera"],
            "Contesto con datos y diplomacia.": ["Diplomática"],
            "Le agradezco su sinceridad y abro debate.": ["Liberal"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El mercado colapsa. La población exige respuestas urgentes.",
        "opciones": {
            "Controlo precios y emito dinero para estabilizar.": ["Populista"],
            "Lanzo un plan de estímulo científico-productivo.": ["Tecno-Productivista"],
            "Convoco a todos los sectores a una mesa de crisis.": ["Pragmática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un ministro quiere incluir programación en la educación primaria.",
        "opciones": {
            "Apoyo sin reservas.": ["Tecno-Productivista"],
            "Solo si no desplaza materias humanísticas.": ["Tradicionalista"],
            "Eso debe decidirlo cada comunidad.": ["Colectivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Las redes sociales difunden noticias falsas que generan caos.",
        "opciones": {
            "Regulamos las plataformas con fuerza.": ["Guerrera"],
            "Educamos a la población en alfabetización digital.": ["Tecno-Productivista"],
            "Apelamos a la ética de las empresas tecnológicas.": ["Diplomática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "El Ministerio de Finanzas propone reemplazar al de Cultura por uno de Blockchain.",
        "opciones": {
            "Una barbaridad, la cultura es esencial.": ["Tradicionalista"],
            "Modernización sin alma es vacía.": ["Teocrática"],
            "Es polémico, pero vale analizarlo.": ["Pragmática"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un terremoto destruye varias ciudades. La población quiere milagros.",
        "opciones": {
            "Movilizo recursos de emergencia y fe colectiva.": ["Teocrática"],
            "Diseño un plan técnico de reconstrucción.": ["Tecno-Productivista"],
            "Llamo a la unidad nacional y la solidaridad.": ["Colectivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Una generación entera pide vivir con mascotas en edificios públicos.",
        "opciones": {
            "Adaptamos las normativas, la convivencia evoluciona.": ["Diplomática"],
            "Solo si no molesta a nadie. Orden ante todo.": ["Tradicionalista"],
            "Permitido. ¿Y si entrenamos perros para tareas estatales?": ["Tecno-Productivista"],
            "Ninguna de las anteriores": None
        }
    },
    {
        "texto": "Un poeta callejero dice que gobernás como un algoritmo sin alma.",
        "opciones": {
            "Me río. Le invito a debatir públicamente.": ["Liberal"],
            "Lo ignoro. Hay cosas más importantes.": ["Tecno-Productivista"],
            "Lo escucho. Tal vez tenga algo que enseñarme.": ["Pragmática"],
            "Ninguna de las anteriores": None
        }
    }   
]

# SISTEMA DE CLASIFICACION

def seleccionar_preguntas(pool, cantidad=10):
    return random.sample(pool, cantidad)

def clasificar_ciudad(respuestas):
    puntajes = defaultdict(int)
    for clases in respuestas:
        if clases is None:
            continue
        for clase in clases:
            puntajes[clase] += 1

    top = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    if len(top) < 2:
        return top[0][0]

    c1, p1 = top[0]
    c2, p2 = top[1]

    if respuestas.count(None) >= 9:
        return "Pragmática"

    compatibles = frozenset([c1, c2]) in COMBINACIONES_VALIDAS
    if compatibles and abs(p1 - p2) <= 2:
        return COMBINACIONES_VALIDAS[frozenset([c1, c2])]
    return c1

COMBINACIONES_VALIDAS = {
    frozenset(["Liberal", "Diplomática"]): "República Comercial Global",
    frozenset(["Liberal", "Tecno-Productivista"]): "Capitalismo Innovador",
    frozenset(["Diplomática", "Tradicionalista"]): "Reino Moderado",
    frozenset(["Colectivista", "Tradicionalista"]): "Socialismo Moral",
    frozenset(["Tecno-Productivista", "Guerrera"]): "Nación Industrial Militarizada",
    frozenset(["Colectivista", "Populista"]): "Estado Asistencialista Reactivo",
    frozenset(["Populista", "Guerrera"]): "Autocracia Emocional",
    frozenset(["Tecno-Productivista", "Colectivista"]): "Planificación Científica",
    frozenset(["Teocrática", "Tradicionalista"]): "Teocracia Conservadora",
    frozenset(["Liberal", "Pragmática"]): "Democracia Económica Mixta",
    frozenset(["Diplomática", "Pragmática"]): "Estado Cooperativo Racional",
    frozenset(["Colectivista", "Pragmática"]): "Estado Solidario Eficiente",
    frozenset(["Aislacionista", "Tradicionalista"]): "Nación Autónoma Histórica"
}

# INICIO DE LA CIUDAD

def aplicar_bonos_ciudad(city, clase, solo_devolver=False):
    datos = CITY_CLASSES.get(clase, {})
    bonos = datos.get("bonos", {})
    penalizacion = datos.get("penalizacion", {})
    efectos = datos.get("efectos", [])

    descripcion = datos.get("descripcion", "Sin descripción disponible.")

    if solo_devolver:
        return {
            "bonos": bonos,
            "penalizacion": penalizacion,
            "efectos": efectos,
            "descripcion": descripcion
        }

    for var, val in bonos.items():
        if hasattr(city, var):
            setattr(city, var, getattr(city, var) + val)

    for var, val in penalizacion.items():
        if hasattr(city, var):
            setattr(city, var, max(0, getattr(city, var) + val))

    print(f"\nTu ciudad ha sido clasificada como: {clase}")
    print(f"Bonificaciones iniciales: {bonos}")
    print(f"Penalización inicial: {penalizacion}")
    print(f"Efectos especiales: {', '.join(efectos) if efectos else 'Ninguno'}")
