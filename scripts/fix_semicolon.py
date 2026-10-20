with open("public/assets/game.bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

# Restore original if needed
target_bad = ",let q=(e&&e.crashWhat===`sign`)?[`¡Uf, eso era un cartel!`,`Resulta que los carteles no se apartan.`,`Al seguro le va a encantar esto.`]:Vg;t.querySelector(`.go-quip`).textContent=q[Math.floor(Math.random()*q.length)]"
if target_bad in text:
    text = text.replace(target_bad, ";let q=(e&&e.crashWhat===`sign`)?[`¡Uf, eso era un cartel!`,`Resulta que los carteles no se apartan.`,`Al seguro le va a encantar esto.`]:Vg;t.querySelector(`.go-quip`).textContent=q[Math.floor(Math.random()*q.length)]")

with open("public/assets/game.bundle.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed semicolon in patch!")
