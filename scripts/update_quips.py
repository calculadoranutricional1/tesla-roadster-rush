with open("public/assets/game.bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

old_quip = ":[`¡Uf, chocaste contra un auto!`,`Al seguro le va a encantar esto.`,`Quizás la próxima vez intenta pasar por encima.`];"
new_quip = ":[`¡Uf, chocaste contra un Tesla!`,`¡Uf, chocaste contra un auto volador!`,`Al seguro le va a encantar esto.`,`Quizás la próxima vez intenta pasar por encima.`];"

if old_quip in text:
    text = text.replace(old_quip, new_quip, 1)
    print("Replaced old_quip successfully!")
else:
    print("old_quip not found!")

with open("public/assets/game.bundle.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved game.bundle.js!")
