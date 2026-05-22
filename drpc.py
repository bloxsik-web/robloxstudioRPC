import time
import pygetwindow as gw
from pypresence import Presence

rpc = Presence("1507491124733022229")
rpc.connect()

while True:
    state = "Idle"

    for w in gw.getWindowsWithTitle("Roblox Studio"):
        title = w.title.strip()

        if " - Roblox Studio" in title:
            place = title.split(" - Roblox Studio")[0].strip()
            state = f'Editing {place}'
            break

    rpc.update(
        state=state,
        large_image="logo"
    )

    print("select", state)

    time.sleep(1)