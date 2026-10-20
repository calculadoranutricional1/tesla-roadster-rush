with open("public/assets/game.bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update _crash to play crashSign for signs, and crashCar for all cars (flying or ground)
old_crash = "this.audio?.say?.((e===`sign`||(this.player?.position?.y||0)>2.2)?`crashSign`:`crash`,{force:`always`})"
new_crash = "this.audio?.say?.(e===`sign`?`crashSign`:`crashCar`,{force:`always`})"

assert old_crash in text, "old_crash not found in bundle"
text = text.replace(old_crash, new_crash, 1)

# 2. Update showGameOver quip logic
old_quip = "let q=(e&&e.crashWhat===`sign`)?[`¡Uf, eso era un cartel!`,`Resulta que los carteles no se apartan.`,`Al seguro le va a encantar esto.`]:Vg;"
new_quip = "let q=(e&&e.crashWhat===`sign`)?[`¡Uf, chocaste contra un cartel!`,`Resulta que los carteles no se apartan.`,`Al seguro le va a encantar esto.`]:(e&&e.crashWhat===`skyRoadster`)?[`¡Uf, chocaste contra un auto volador!`,`Resulta que el cielo también tiene tráfico.`,`Al seguro le va a encantar esto.`]:[`¡Uf, chocaste contra un auto!`,`Al seguro le va a encantar esto.`,`Quizás la próxima vez intenta pasar por encima.`];"

assert old_quip in text, "old_quip not found in bundle"
text = text.replace(old_quip, new_quip, 1)

with open("public/assets/game.bundle.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated crash logic and quips successfully!")
