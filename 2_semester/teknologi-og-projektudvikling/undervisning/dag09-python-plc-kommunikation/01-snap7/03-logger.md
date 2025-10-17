# 03 – Simpel PLC-logger med snap7 og pandas

Lav et Python-program, der i et main loop læser fire værdier fra PLC'en (BOOL, INT, REAL, WORD) og gemmer dem i en CSV-fil med tidsstempel. Brug pandas til at skrive til CSV.

---

## Eksempel på løsning

```python
import time
import pandas as pd
from datetime import datetime
import snap7
from snap7.util import get_bool, get_int, get_real, get_word

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1
DB = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

csv_file = "log.csv"

try:
    while True:
        data = client.db_read(DB, 0, 10)  # Læs 10 bytes fra DB1
        my_bool = get_bool(data, 0, 0)   # DBX0.0
        my_int = get_int(data, 2)        # DBW2
        my_real = get_real(data, 4)      # DBD4
        my_word = get_word(data, 8)      # DBW6
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = pd.DataFrame([[timestamp, my_bool, my_int, my_real, my_word]],
                           columns=["timestamp", "my_bool", "my_int", "my_real", "my_word"])
        row.to_csv(csv_file, mode='a', header=not pd.io.common.file_exists(csv_file), index=False)
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopper logger og lukker forbindelsen...")
    client.disconnect()
```

---

**Tip:**
- Du kan ændre PLC_IP, DB og filnavn hvis nødvendigt.
- Stop loggeren med Ctrl+C.
