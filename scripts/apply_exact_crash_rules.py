with open("public/assets/game.bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update _crash audio selection
old_audio = "this.audio?.say?.((this.crashWhat===`sign`||e===`sign`)?`crashSign`:`crashCar`,{force:`always`})"
new_audio = "this.audio?.say?.((this.crashWhat===`sign`||e===`sign`)?`crashSign`:(this.crashWhat===`skyRoadster`||e===`skyRoadster`)?`crashSky`:`crashRoad`,{force:`always`})"

assert old_audio in text, "old_audio not found"
text = text.replace(old_audio, new_audio, 1)

# 2. Update showGameOver quip logic
old_quip = "let q=(e&&e.crashWhat===`sign`)?[`¡Uf, chocaste contra un cartel!`,`Resulta que los carteles no se apartan.`,`Al seguro le va a encantar esto.`]:(e&&e.crashWhat===`skyRoadster`)?[`¡Uf, chocaste contra un auto volador!`,`Resulta que el cielo también tiene tráfico.`,`Al seguro le va a encantar esto.`]:[`¡Uf, chocaste contra un Tesla!`,`¡Uf, chocaste contra un auto volador!`,`Al seguro le va a encantar esto.`,`Quizás la próxima vez intenta pasar por encima.`];"
new_quip = "let q=(e&&e.crashWhat===`sign`)?[`Chocaste contra un cartel`,`Uh, esto al seguro le va a encantar`]:(e&&e.crashWhat===`skyRoadster`)?[`Uh, chocaste contra un Tesla`,`Uh, esto al seguro le va a encantar`]:[`Chocaste contra un auto`,`Uh, esto al seguro le va a encantar`];"

assert old_quip in text, "old_quip not found"
text = text.replace(old_quip, new_quip, 1)

with open("public/assets/game.bundle.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated _crash and showGameOver to match exact user specifications!")
