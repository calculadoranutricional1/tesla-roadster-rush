import os

bundle_path = "public/assets/game.bundle.js"

with open(bundle_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    # Title & Tagline
    ("Bg=`Traffic is a ground-level problem.`", "Bg=`El tráfico es un problema terrestre.`"),
    ("Tap to start", "Toca para empezar"),
    ("Press space to start", "Pulsa espacio para empezar"),
    ("<b>W / ↑ / Shift</b> accelerate<i></i><b>A/D</b> lanes<i></i><b>Space</b> hop and fly<i></i><b>Q/E</b> barrel roll",
     "<b>W / ↑ / Shift</b> acelerar<i></i><b>A/D</b> carriles<i></i><b>Espacio</b> saltar y volar<i></i><b>Q/E</b> giro de barril"),
    ("`Best ${Wg(e)}`", "`Récord ${Wg(e)}`"),
    ("`Best ${Wg(e.best)}`", "`Récord ${Wg(e.best)}`"),

    # HUD & Touch controls
    ("<span class=\"micro\">Score</span>", "<span class=\"micro\">Puntos</span>"),
    ("<div class=\"air-label\">Air</div>", "<div class=\"air-label\">Aire</div>"),
    ("Hold Accelerate to fire rear thrusters · hold Fly to climb · double-tap to roll",
     "Mantén Acelerar para propulsores · mantén Volar para ascender · doble toque para girar"),
    ("aria-label=\"Barrel roll left\">Roll L</button>", "aria-label=\"Giro barril izquierda\">Giro I</button>"),
    ("aria-label=\"Steer left\">&#9664;</button>", "aria-label=\"Girar izquierda\">&#9664;</button>"),
    ("aria-label=\"Steer right\">&#9654;</button>", "aria-label=\"Girar derecha\">&#9654;</button>"),
    ("aria-label=\"Barrel roll right\">Roll R</button>", "aria-label=\"Giro barril derecha\">Giro D</button>"),
    ("data-action=\"dive\" data-hold=\"1\" aria-label=\"Hold to dive\">Dive</button>",
     "data-action=\"dive\" data-hold=\"1\" aria-label=\"Mantén para descender\">Bajar</button>"),
    ("data-action=\"boost\" data-hold=\"1\" aria-label=\"Hold to accelerate forward with rear thrusters\"><span class=\"accel-ico\" aria-hidden=\"true\">${Ng}</span><span>Accelerate</span></button>",
     "data-action=\"boost\" data-hold=\"1\" aria-label=\"Mantén para acelerar con propulsores traseros\"><span class=\"accel-ico\" aria-hidden=\"true\">${Ng}</span><span>Acelerar</span></button>"),
    ("data-action=\"thrust\" data-hold=\"1\" aria-label=\"Tap to hop or hold to fly\">Fly</button>",
     "data-action=\"thrust\" data-hold=\"1\" aria-label=\"Toca para saltar o mantén para volar\">Volar</button>"),
    ("setAttribute(`aria-label`,`Pause game`)", "setAttribute(`aria-label`,`Pausar juego`)"),
    ("setAttribute(`aria-label`,`Toggle sound`)", "setAttribute(`aria-label`,`Activar/desactivar sonido`)"),

    # Pause screen
    ("<h2>Paused</h2>", "<h2>En Pausa</h2>"),
    ("<div class=\"quip\">The traffic will wait. It always does.</div>", "<div class=\"quip\">El tráfico esperará. Siempre lo hace.</div>"),
    ("<button class=\"btn\">Resume</button>", "<button class=\"btn\">Reanudar</button>"),
    ("Tap to resume", "Toca para reanudar"),
    ("Press P to resume", "Pulsa P para reanudar"),

    # Game Over screen
    ("<h2 class=\"go-head\">Wrecked!</h2>", "<h2 class=\"go-head\">¡Destrozado!</h2>"),
    ("<span class=\"new-best\">New best</span>", "<span class=\"new-best\">Nuevo récord</span>"),
    ("<span>Distance m</span>", "<span>Distancia m</span>"),
    ("<span>Bolts</span>", "<span>Rayos</span>"),
    ("<span>Best combo</span>", "<span>Mejor combo</span>"),
    ("<button class=\"btn go-retry\">Retry</button>", "<button class=\"btn go-retry\">Reintentar</button>"),
    ("Tap retry to go again", "Toca para reintentar"),
    ("Space to go again", "Espacio para reintentar"),

    # Quips & crash heads
    ("`That was a car.`", "`Eso era un coche.`"),
    ("`Insurance is going to love this.`", "`Al seguro le va a encantar esto.`"),
    ("`Turns out the sky has traffic too.`", "`Resulta que el cielo también tiene tráfico.`"),
    ("`Exit only means exit only.`", "`Salida obligatoria significa salida obligatoria.`"),
    ("`Gravity: 1. You: still pretty cool.`", "`Gravedad: 1. Tú: sigues teniendo estilo.`"),
    ("`Somebody honked. Probably at you.`", "`Alguien ha tocado el claxon. Seguro que a ti.`"),
    ("`Maybe try going over next time.`", "`Quizás la próxima vez intenta pasar por encima.`"),
    ("Hg=[`Wrecked`,`Fender bender`,`Total loss`,`End of the line`]",
     "Hg=[`¡Destrozado!`,`Golpe lateral`,`Siniestro total`,`Fin del trayecto`]"),

    # Tricks & powerups
    ("t_=[`Barrel roll!`,`Double roll!`,`Triple roll!`,`Quad roll!`]",
     "t_=[`¡Giro de barril!`,`¡Doble giro!`,`¡Triple giro!`,`¡Giro cuádruple!`]" ),
    ("`${e}× roll combo!`", "`${e}× combo de giros!`"),
    ("n_={magnet:`Bolt magnet`,rocket:`Rocket!`,shield:`Shield up`,multiplier:`Double points`,air:`Air refill`}",
     "n_={magnet:`Imán de rayos`,rocket:`¡Cohete!`,shield:`Escudo activo`,multiplier:`Doble puntuación`,air:`Recarga de aire`}"),
    ("`Welcome to the sky lane`", "`¡Bienvenido al carril aéreo!`"),
    ("`Power up!`", "`¡Potenciador!`"),
    ("`Roof runner`", "`Corredor de tejados`"),
    ("`Ramp launch!`", "`¡Salto de rampa!`"),
    ("`Big air ${e.toFixed(1)}s`", "`¡Gran salto ${e.toFixed(1)}s!`"),
    ("e?`Sky dodge!`:`Close call!`", "e?`¡Esquiva aérea!`:`¡Por los pelos!`"),

    # Boot failure
    ("`The freeway is closed for repairs. Try reloading.`", "`La autopista está cerrada por obras. Prueba a recargar.`")
]

count = 0
for orig, repl in replacements:
    if orig in text:
        text = text.replace(orig, repl)
        count += 1
    else:
        print(f"NOT FOUND: {orig[:40]}")

print(f"Applied {count}/{len(replacements)} localization replacements.")

with open(bundle_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Saved localized game.bundle.js!")
