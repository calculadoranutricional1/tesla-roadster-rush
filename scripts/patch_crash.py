with open("public/assets/game.bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

target1 = "this.audio?.say?.(`crash`,{force:`always`}),this.crashWhat=e||`traffic`}"
repl1 = "this.crashWhat=e||`traffic`,this.audio?.say?.((e===`sign`||(this.player?.position?.y||0)>2.2)?`crashSign`:`crash`,{force:`always`})}"

target2 = "this.hud?.showGameOver({score:e,best:this.best,isBest:t,distance:this.distance,bolts:this.bolts,bestCombo:this.bestCombo})"
repl2 = "this.hud?.showGameOver({score:e,best:this.best,isBest:t,distance:this.distance,bolts:this.bolts,bestCombo:this.bestCombo,crashWhat:this.crashWhat})"

target3 = "t.querySelector(`.go-quip`).textContent=Vg[Math.floor(Math.random()*Vg.length)]"
repl3 = "let q=(e&&e.crashWhat===`sign`)?[`¡Uf, eso era un cartel!`,`Resulta que los carteles no se apartan.`,`Al seguro le va a encantar esto.`]:Vg;t.querySelector(`.go-quip`).textContent=q[Math.floor(Math.random()*q.length)]"

if target1 in text:
    text = text.replace(target1, repl1, 1)
    print("target1 replaced!")
else:
    print("target1 NOT found")

if target2 in text:
    text = text.replace(target2, repl2, 1)
    print("target2 replaced!")
else:
    print("target2 NOT found")

if target3 in text:
    text = text.replace(target3, repl3, 1)
    print("target3 replaced!")
else:
    print("target3 NOT found")

with open("public/assets/game.bundle.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved patch successfully!")
