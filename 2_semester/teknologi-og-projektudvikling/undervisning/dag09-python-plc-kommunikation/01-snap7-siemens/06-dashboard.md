## 14A) Opgave 14A – FuncAnimation + skriv til CSV **hver gang** (ingen buffer)

**Mål:**  
- Plot `REAL` fra `DBD4` live med `FuncAnimation`.  
- Skriv **én** CSV-række pr. opdatering (ingen batch).  

**Installér:**
```bash
pip install python-snap7 pandas matplotlib
```

```python

# gem som: opg14a_funcanimation_log_each_row.py
# kør: python opg14a_funcanimation_log_each_row.py

import os
import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import snap7
from snap7.util import get_bool, get_int, get_real, get_word

# 1) Udfyld disse (fra TIA)
ip = "192.168.1.100"
rack = 0
slot = 1            # S7-1500: 0
db_number = 1

# 2) Vi læser 10 bytes (dækker DBX0.0, DBW2, DBD4, DBW8)
start_byte = 0
length = 10

# 3) Plot og CSV
vindue = 100            # hvor mange punkter vises ad gangen
interval_ms = 500       # opdater hver 500 ms
csv_fil = "plc_log.csv"

# 4) Forbind til PLC
client = snap7.client.Client()
client.connect(ip, rack, slot)
print("Forbundet. Live-plot + CSV (én række pr. opdatering).")

# 5) Forbered plot
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel("måling #")
ax.set_ylabel("REAL @ DBD4")
ax.set_xlim(0, vindue)
ax.set_ylim(-1, 1)      # justeres automatisk løbende
x_data = []
y_data = []
måling_nr = 0

# 6) Skriv kolonnenavne kun hvis filen ikke findes i forvejen
første_skriv = not os.path.exists(csv_fil)

def on_close(event):
    # Luk PLC pænt hvis vinduet lukkes
    try:
        client.disconnect()
        client.destroy()
    except:
        pass
    print("Lukket. Forbindelse lukket.")

fig.canvas.mpl_connect("close_event", on_close)

def update(_frame):
    """
    Kaldes automatisk af FuncAnimation.
    - læs 10 bytes fra DB
    - pak BOOL/INT/REAL/WORD ud
    - opdater plot (REAL)
    - skriv ÉN række til CSV (med header kun første gang)
    """
    nonlocal_vars = update.__dict__  # lille trick så vi kan ændre 'første_skriv' indeni funktionen
    global første_skriv
    # 1) Læs fra PLC
    data = client.db_read(db_number, start_byte, length)

    # 2) Pak værdier ud
    v_bool = get_bool(data, 0, 0)  # DBX0.0
    v_int  = get_int(data, 2)      # DBW2
    v_real = get_real(data, 4)     # DBD4
    v_word = get_word(data, 8)     # DBW8

    # 3) Opdater dataserier (plotter REAL)
    nonlocal_vars.setdefault("måling_nr", 0)
    idx = nonlocal_vars["måling_nr"]
    x_data.append(idx)
    y_data.append(v_real)
    if len(x_data) > vindue:
        x_data.pop(0)
        y_data.pop(0)
    line.set_data(range(len(x_data)), y_data)

    # auto-y så kurven kan ses
    if len(y_data) > 1:
        ymin = min(y_data)
        ymax = max(y_data)
        if ymin == ymax:
            ymin -= 1
            ymax += 1
        margen = 0.1 * (abs(ymin) + abs(ymax) + 1)
        ax.set_ylim(ymin - margen, ymax + margen)

    # 4) Skriv ÉN række til CSV
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    df = pd.DataFrame([{
        "timestamp": ts,
        "bool": bool(v_bool),
        "int": int(v_int),
        "real": float(v_real),
        "word": int(v_word)
    }])
    df.to_csv(csv_fil, mode="a", index=False, header=første_skriv)
    første_skriv = False  # fra nu af skriver vi uden header

    nonlocal_vars["måling_nr"] = idx + 1
    return line,

ani = FuncAnimation(fig, update, interval=interval_ms)
plt.title("FuncAnimation – skriv til CSV for hver måling")
plt.show()

# Hvis miljøet ikke udløser close_event korrekt, så ryd op her også:
try:
    client.disconnect()
    client.destroy()
except:
    pass
print("Færdig.")

````

### Hvad sker der – trin for trin

1. Vi forbinder til PLC én gang.
2. `FuncAnimation` kalder `update()` hver `interval_ms` millisekund.
3. `update()` læser 10 bytes, pakker `BOOL/INT/REAL/WORD` ud, **opdaterer grafen**, og **skriver én CSV-række** med `pandas`.
4. Header skrives kun første gang (hvis filen ikke fandtes).
5. Når du lukker figuren, lukkes PLC-forbindelsen pænt.

> Bemærk: At hvis du skal plotte hurtigt så bruges en buffer som engang imellem skubbes ned i csv. I undervisning hvor vi henter data hver 2 sec. så er det fint at lave ny linje for hver opdatering men skal vi plotte hurtigere så bruges en buffer.
