# 06 – **Live-plot** + **Write via tastatur** (FuncAnimation, én fil)

> **Mål:**  
> - Live-plot af `MyReal` med **FuncAnimation** (ingen `while True`).  
> - Skriv til PLC ved at trykke **taster** (fx toggle `MyBool`, justér `MyReal`).  
> - **Ingen tråde**. Vi lægger “skriv-ønsker” i en lille liste, som `update()` udfører.

**Krav fra 01–03:**  
Du kan forbinde til din CompactLogix / ControlLogix / Echo, og du har `MyBool` (BOOL), `MyInt` (INT), `MyReal` (REAL).

**Installér:**
```bash
pip install pycomm3 matplotlib
````

---

## Opgave – Plot & tastatur-skriv (begynder-venlig)

**Taster under kørslen:**

* `t` → toggle `MyBool`
* `+` → læg **trin** til `MyReal` (fx +0.5)
* `-` → træk **trin** fra `MyReal` (fx −0.5)
* `r` → læs og print alle tre tags i terminalen
* `q` → luk plottet (stop programmet)

```python
# gem som: opg6_plot_write_keys.py
# kør: python opg6_plot_write_keys.py

from pycomm3 import LogixDriver
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1) Vælg din PLC-sti (ÉN af disse)
PLC = "192.168.1.50"      # CompactLogix (kun IP)
# PLC = "192.168.1.60/0"  # ControlLogix / Echo (ENxT-IP / CPU-slot)

# 2) Forbind til PLC én gang
plc = LogixDriver(PLC)
plc.open()

# 3) Plot-forberedelse
fig, ax = plt.subplots()
line, = ax.plot([], [])     # tom linje i starten
ax.set_xlabel("måling #")
ax.set_ylabel("MyReal (REAL)")
vindue = 100                # vis de seneste 100 målinger
x_data = []
y_data = []
tæller = 0

# 4) Skriv-indstillinger
trin = 0.5                  # hvor meget +/− der skrives til MyReal
ventetekst = "Tryk: t=toggle MyBool, +=+0.5, -=-0.5, r=read, q=quit"
sidste_handling = "Klar."

# 5) Liste til “ventende” handlinger (ingen tråde)
#    Vi lægger kun små “kommandoer” her, og udfører dem i update()
ventende = []  # fx ("toggle", "MyBool") eller ("add", "MyReal", 0.5) eller ("read_print",)

# 6) Tastatur-håndtering (meget enkel)
def on_key(event):
    k = (event.key or "").lower()
    if k == "t":
        ventende.append(("toggle", "MyBool"))
    elif k == "+":
        ventende.append(("add", "MyReal", +trin))
    elif k == "-":
        ventende.append(("add", "MyReal", -trin))
    elif k == "r":
        ventende.append(("read_print",))
    elif k == "q":
        plt.close(fig)  # luk vinduet = stop

fig.canvas.mpl_connect("key_press_event", on_key)

# 7) Luk forbindelsen pænt når vinduet lukkes
def on_close(_e):
    try:
        plc.close()
    except:
        pass
    print("Lukket pænt.")

fig.canvas.mpl_connect("close_event", on_close)

# 8) Animationens opdaterings-funktion
def update(_frame):
    global tæller, sidste_handling

    # 8a) Udfør eventuelle ventende handlinger først (én ad gangen eller alle – her tager vi alle)
    while ventende:
        cmd = ventende.pop(0)
        if cmd[0] == "toggle":
            tag = cmd[1]           # "MyBool"
            før = plc.read(tag).value
            plc.write(tag, not før)
            efter = plc.read(tag).value
            print("Toggle", tag, "->", efter)
            sidste_handling = f"Toggle {tag} -> {efter}"

        elif cmd[0] == "add":
            tag, delta = cmd[1], cmd[2]   # "MyReal", ±trin
            før = float(plc.read(tag).value)
            ny = før + float(delta)
            plc.write(tag, ny)
            print(tag, "=", ny)
            sidste_handling = f"{tag} = {ny:.3f}"

        elif cmd[0] == "read_print":
            vb = plc.read("MyBool").value
            vi = plc.read("MyInt").value
            vr = plc.read("MyReal").value
            print("Læsning -> MyBool:", vb, " MyInt:", vi, " MyReal:", vr)
            sidste_handling = "Læsning vist i terminal."

    # 8b) Læs værdien til plot (MyReal)
    val = plc.read("MyReal").value

    # 8c) Opdater dataserier
    x_data.append(tæller)
    y_data.append(val)
    if len(x_data) > vindue:
        x_data.pop(0)
        y_data.pop(0)

    # 8d) Tegn linjen og hold akser fornuftige
    line.set_data(range(len(x_data)), y_data)
    ax.set_xlim(0, vindue)

    if len(y_data) > 1:
        ymin = min(y_data)
        ymax = max(y_data)
        if ymin == ymax:
            ymin -= 1.0
            ymax += 1.0
        margin = 0.1 * (abs(ymin) + abs(ymax) + 1.0)
        ax.set_ylim(ymin - margin, ymax + margin)

    # 8e) Vis hjælpetekst i titel
    ax.set_title(ventetekst + "   |   " + sidste_handling)

    tæller += 1
    return line,

# 9) Start animationen (opdater f.eks. hver 500 ms)
ani = FuncAnimation(fig, update, interval=500)
plt.title("Plot + tastatur-write (FuncAnimation)")
plt.show()

# Ekstra oprydning hvis close-event ikke kom
try:
    plc.close()
except:
    pass
```

### Hvad sker der – roligt og i rækkefølge

1. Vi åbner **én** forbindelse til PLC.
2. **FuncAnimation** kalder `update()` med faste intervaller (fx hver 500 ms).
3. Når du trykker en tast, lægger `on_key()` en **lille kommando** i `ventende`.
4. I starten af `update()` kører vi alle ventende kommandoer (fx toggle af `MyBool` eller +/− på `MyReal`).
5. Så læser vi `MyReal`, opdaterer grafen og viser en enkel status-tekst.
6. Når du lukker plottet (eller trykker `q`), lukkes forbindelsen pænt.

### Små øvelser

* Skift `trin = 0.5` til `0.1` for finere justering.
* Tilføj en tast `i` der sætter `MyInt` til et fast tal (fx 1000): `ventende.append(("write_const", "MyInt", 1000))` og håndter i `update()`.
* Plot også `MyInt` som **anden linje** (lav `line2` og opdater den).
* Kombinér med CSV-log (fra kapitel 04): skriv én række i `update()` hver gang, mens du stadig kan trykke taster.

> Pointen: Du kan **læse, tegne og skrive** i samme `update()` – én fil, ingen tråde. FuncAnimation er din “main-løkke”.
