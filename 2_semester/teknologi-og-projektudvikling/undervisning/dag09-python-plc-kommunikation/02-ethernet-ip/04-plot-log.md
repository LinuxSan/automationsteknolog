# 04 – **Live-plot** & **CSV-log** med FuncAnimation  
*(CompactLogix, ControlLogix og Logix Echo, via `pycomm3`)*

> For begyndere: én fil, én tråd, ingen “while True”.  
> Matplotlibs **FuncAnimation** kalder din `update()` med faste intervaller.  
> I `update()` læser vi **tags**, opdaterer **grafen**, og gemmer **CSV**.

---

## Hvad skal være klar (fra “01” og “02”)

- PLC-IP (f.eks. `192.168.1.50` for CompactLogix, eller ENxT-IP for ControlLogix/Echo).  
- **ControlLogix/Echo:** CPU **slot** (ofte `0`) → forbindelsesstreng: `"IP/slot"` (eksempel `"192.168.1.60/0"`).  
- Controller-tags (Controller Scope) med External Access = Read/Write:
  - `MyBool` (BOOL), `MyInt` (INT), `MyReal` (REAL)

Installer pakker (én gang):
```bash
pip install pycomm3 matplotlib pandas
````

---

## 1) Opgave 1 – Vælg din PLC-sti (hurtig sanity-check)

**Vælg kun én** af de tre PLC-linjer og kør scriptet. Der sker ikke andet end “åbn/luk forbindelse”.

```python
# gem som: opg1_pick_plc_plot.py
from pycomm3 import LogixDriver

# VÆLG KUN ÉN:
PLC = "192.168.1.50"     # CompactLogix (kun IP)
# PLC = "192.168.1.60/0" # ControlLogix (ENxT-IP / CPU-slot)
# PLC = "192.168.1.70/0" # Logix Echo (ENxT-IP / CPU-slot)

with LogixDriver(PLC) as plc:
    pass

print("Forbindelse OK:", PLC)
```

Kør:

```bash
python opg1_pick_plc_plot.py
```

---

## 2) Opgave 2 – **Live-plot** af `MyReal` (uden CSV)

**Idé:** Vi viser de **seneste 100 målinger** af `MyReal`.
Ingen `try/except` endnu – bare det enkleste, så I kan se det virke.

```python
# gem som: opg2_liveplot_real.py
from pycomm3 import LogixDriver
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1) Vælg din PLC-sti
PLC = "192.168.1.50"      # eller "192.168.1.60/0" for ControlLogix/Echo

# 2) Forbundet én gang før vi starter animationen
plc = LogixDriver(PLC)
plc.open()

# 3) Forbered figur og dataserier
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel("måling #")
ax.set_ylabel("MyReal (REAL)")
vindue = 100                 # vis de seneste 100 punkter
x_data = []
y_data = []
count = 0                    # tæller målinger

# 4) Sørg for at lukke PLC pænt, når vinduet lukkes
def on_close(_event):
    try:
        plc.close()
    except:
        pass
    print("Lukket: forbindelse lukket.")

fig.canvas.mpl_connect("close_event", on_close)

# 5) Denne funktion kaldes af FuncAnimation med faste intervaller
def update(_frame):
    global count
    # læs tag
    val = plc.read("MyReal").value

    # opdater dataserier
    x_data.append(count)
    y_data.append(val)
    if len(x_data) > vindue:
        x_data.pop(0)
        y_data.pop(0)

    line.set_data(range(len(x_data)), y_data)
    ax.set_xlim(0, vindue)

    # enkel auto-y så kurven kan ses
    if len(y_data) > 1:
        ymin = min(y_data)
        ymax = max(y_data)
        if ymin == ymax:
            ymin = ymin - 1.0
            ymax = ymax + 1.0
        margin = 0.1 * (abs(ymin) + abs(ymax) + 1.0)
        ax.set_ylim(ymin - margin, ymax + margin)

    count = count + 1
    return line,

ani = FuncAnimation(fig, update, interval=500)   # 500 ms mellem opdateringer
plt.title("Live-plot af MyReal (FuncAnimation)")
plt.show()

# ekstra oprydning hvis close-event ikke kom
try:
    plc.close()
except:
    pass
```

Kør:

```bash
python opg2_liveplot_real.py
```

---

## 3) Opgave 3 – Live-plot **og** CSV-log (én række pr. opdatering)

**Mål:** Samme plot som før, men nu skriver vi **én** række i CSV **hver gang** `update()` kører.
Kolonne-navne skrives første gang.

```python
# gem som: opg3_liveplot_real_csv_each.py
from pycomm3 import LogixDriver
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import datetime
import os

PLC = "192.168.1.50"      # eller "192.168.1.60/0"

plc = LogixDriver(PLC)
plc.open()

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel("måling #")
ax.set_ylabel("MyReal (REAL)")

vindue = 100
x_data = []
y_data = []
count = 0

csv_fil = "log_myreal.csv"
first_write = not os.path.exists(csv_fil)   # skriv header hvis filen ikke findes

def on_close(_event):
    try:
        plc.close()
    except:
        pass
    print("Lukket: CSV lukket og forbindelse lukket.")

fig.canvas.mpl_connect("close_event", on_close)

def update(_frame):
    global count, first_write

    # 1) læs MyReal
    val = plc.read("MyReal").value

    # 2) opdater plot-data
    x_data.append(count)
    y_data.append(val)
    if len(x_data) > vindue:
        x_data.pop(0)
        y_data.pop(0)
    line.set_data(range(len(x_data)), y_data)
    ax.set_xlim(0, vindue)

    if len(y_data) > 1:
        ymin = min(y_data); ymax = max(y_data)
        if ymin == ymax:
            ymin -= 1.0; ymax += 1.0
        margin = 0.1 * (abs(ymin) + abs(ymax) + 1.0)
        ax.set_ylim(ymin - margin, ymax + margin)

    # 3) skriv ÉN række til CSV
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    df = pd.DataFrame([{"timestamp": ts, "MyReal": float(val)}])
    df.to_csv(csv_fil, mode="a", index=False, header=first_write)
    first_write = False

    count = count + 1
    return line,

ani = FuncAnimation(fig, update, interval=500)
plt.title("Live-plot + CSV (én række pr. opdatering)")
plt.show()

try:
    plc.close()
except:
    pass
```

Kør:

```bash
python opg3_liveplot_real_csv_each.py
```

---

## 4) Opgave 4 – Læs **flere tags** og log dem alle, men plot kun `MyReal`

**Idé:** `update()` kan læse *flere* tags. Vi plotter `MyReal`, men skriver **MyBool, MyInt, MyReal** til CSV.
Fint som skabelon til jeres egne tags.

```python
# gem som: opg4_liveplot_multi_csv.py
from pycomm3 import LogixDriver
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import datetime
import os

PLC = "192.168.1.50"      # eller "192.168.1.60/0"

plc = LogixDriver(PLC)
plc.open()

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel("måling #")
ax.set_ylabel("MyReal (REAL)")

vindue = 100
x_data = []
y_data = []
count = 0

csv_fil = "log_multi.csv"
first_write = not os.path.exists(csv_fil)

def on_close(_event):
    try:
        plc.close()
    except:
        pass
    print("Lukket: CSV lukket og forbindelse lukket.")

fig.canvas.mpl_connect("close_event", on_close)

def update(_frame):
    global count, first_write

    # 1) læs tre tags
    v_bool = plc.read("MyBool").value
    v_int  = plc.read("MyInt").value
    v_real = plc.read("MyReal").value

    # 2) plot kun REAL
    x_data.append(count)
    y_data.append(v_real)
    if len(x_data) > vindue:
        x_data.pop(0); y_data.pop(0)
    line.set_data(range(len(x_data)), y_data)
    ax.set_xlim(0, vindue)

    if len(y_data) > 1:
        ymin = min(y_data); ymax = max(y_data)
        if ymin == ymax:
            ymin -= 1.0; ymax += 1.0
        margin = 0.1 * (abs(ymin) + abs(ymax) + 1.0)
        ax.set_ylim(ymin - margin, ymax + margin)

    # 3) skriv alle tre værdier i CSV
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    row = {"timestamp": ts, "MyBool": bool(v_bool), "MyInt": int(v_int), "MyReal": float(v_real)}
    pd.DataFrame([row]).to_csv(csv_fil, mode="a", index=False, header=first_write)
    first_write = False

    count = count + 1
    return line,

ani = FuncAnimation(fig, update, interval=500)
plt.title("Live-plot (MyReal) + CSV (MyBool, MyInt, MyReal)")
plt.show()

try:
    plc.close()
except:
    pass
```

---

## Fejlfinding (kort)

* **Ingen forbindelse / timeout**

  * Kan du `ping`e IP?
  * **ControlLogix/Echo:** Er **slot** korrekt i stien `"IP/slot"`?
* **Grafen flad / “skæv” skala**

  * Tjek at `MyReal` faktisk ændrer sig.
  * Sæt `interval=200` for hurtigere opdatering.
  * Justér `vindue` større/mindre.
* **CSV bliver meget stor**

  * Øg `interval` eller log færre felter.
  * Alternativ: batch-skriv (se jeres S7-opgave for “buffer”-udgave).

---

## Bonus-øvelser (når 2–4 virker)

* Plot **både** `MyReal` og `MyInt` som to linjer.
* Tilføj en **toggle-knap** i koden der skriver til `MyBool` hvert X sekund.
* Lav en udgave med `try/except/finally`, så forbindelsen **altid** lukkes (samme stil som i S7-opgaverne).

> Pointen i dette kapitel: **FuncAnimation** er jeres “main-løkke”. I `update()` kan I roligt både læse, tegne og skrive til CSV – alt i **én fil** uden ekstra tråde.
