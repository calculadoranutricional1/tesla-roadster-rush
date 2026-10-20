with open("public/assets/game.bundle.js", "r", encoding="utf-8") as f:
    text = f.read()

old_crash = "_crash(e){this.mode===`playing`&&(this.player.alive!==!1&&this.player.crash?.(),this.mode=`crashed`,this.crashT=0,this.chase?.setMode?.(`crash`),this.audio?.sfx?.(`crash`),this.audio?.music?.(null),this.audio?.quiet?.(),this.crashWhat=e||`traffic`,this.audio?.say?.(e===`sign`?`crashSign`:`crashCar`,{force:`always`}))}"

# Set mode to crashed and crashWhat FIRST, so player.crash() cannot re-enter or trigger a second _crash call
new_crash = "_crash(e){if(this.mode!==`playing`)return;this.mode=`crashed`,this.crashWhat=e||`traffic`,this.crashT=0,this.chase?.setMode?.(`crash`),this.audio?.sfx?.(`crash`),this.audio?.music?.(null),this.audio?.quiet?.(),this.audio?.say?.((this.crashWhat===`sign`||e===`sign`)?`crashSign`:`crashCar`,{force:`always`}),this.player.alive!==!1&&this.player.crash?.()}"

assert old_crash in text, "old_crash pattern not found in game.bundle.js"
text = text.replace(old_crash, new_crash, 1)

with open("public/assets/game.bundle.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated _crash order!")
