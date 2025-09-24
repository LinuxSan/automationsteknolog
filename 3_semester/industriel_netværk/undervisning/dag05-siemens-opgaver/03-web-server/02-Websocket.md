# Opsætning af Webserver

<a name="subsec:webserver_simulated_physical_plc"></a>

**Mål:** Målet med denne opgave er at opsætte og konfigurere en webserver på en fysisk SIMATIC S7-1200 PLC og en simuleret S7-1500 PLC ved hjælp af Siemens PLCSIM Advanced. Opgaven giver praktisk erfaring med webserverfunktionalitet på en PLC og dens anvendelse til overvågning og kontrol af industrielle processer.

**Opgavebeskrivelse:**

1. **Konfiguration af PLC A (S7-1200 som Webserver):**

   * Opret et nyt projekt i TIA Portal og tilføj en fysisk S7-1200 PLC.
   * Tildel en IP-adresse til PLC'en, fx `192.168.0.1`, og konfigurer de nødvendige netværksparametre.
   * Aktiver webserveren i PLC-indstillingerne under `Properties`.
   * Opret en simpel webside ved hjælp af TIA Portal, der viser vigtige procesdata som sensordata og maskinstatus.

2. **Konfiguration af PLC B (S7-1500 som Simuleret Webserver):**

   * Tilføj en S7-1500 PLC i TIA Portal og opsæt en simulering med PLCSIM Advanced.
   * Tildel en IP-adresse til den simulerede PLC, fx `192.168.0.2`.
   * Aktivér webserveren på S7-1500 under `Properties`, og opret brugerdefinerede websider for at vise og styre procesdata.
   * Start simuleringen og verificer, at webserveren på den simulerede PLC er tilgængelig via en webbrowser ved at bruge IP-adressen.

3. **Test og Verifikation:**

   * Brug en webbrowser til at tilgå PLC'ernes webservere ved hjælp af deres IP-adresser.
   * Test, at procesdata opdateres i realtid, og at kontrolfunktioner på websiden fungerer korrekt.

4. **Dokumentation:**

   * Dokumentér alle konfigurationsindstillinger med skærmbilleder og opsætninger af websiderne.
   * Udarbejd en kort teknisk rapport med skærmbilleder af webserver-konfigurationerne og testresultater.

**Krav:**

* Grundlæggende forståelse af webservere og deres anvendelse i industriel kommunikation.
* Erfaring med TIA Portal og PLCSIM Advanced.

---

# WebSocket-Kommunikation via Webserver

<a name="subsec:websocket_communication_plc"></a>

**Mål:** Denne opgave fokuserer på at opsætte en WebSocket-kommunikation mellem to SIMATIC S7-1500 PLC'er ved hjælp af en webserver.

**Opgavebeskrivelse:**

1. **Konfiguration af WebSocket-forbindelse:**

   * Aktiver webserveren på begge PLC'er og implementér en WebSocket-klient i HTML:

```html
<script type="text/javascript">
var ws = new WebSocket('ws://PLC_SERVER_ADRESSE');
ws.onopen = function() { /* Håndter forbindelse */ };
ws.onmessage = function(evt) { /* Håndter besked */ };
ws.onclose = function() { /* Håndter lukning */ };
</script>
```

2. **Simulering og Test:**

   * Simulér begge PLC'er og test WebSocket-kommunikationen.

3. **Dokumentation:**

   * Dokumentér opsætningen, kodeeksempler og testresultater for WebSocket-forbindelsen.

**Krav:**

* Grundlæggende forståelse af WebSockets og JavaScript.
* Erfaring med TIA Portal og PLCSIM Advanced.

---

## Manglende elementer for at få eksemplet til at virke (MVP)

> Den oprindelige snippet er kun et **script** (klient). For at køre end-to-end mangler **HTML-inputfelter/knapper** og en **server** at forbinde til. PLC’ens indbyggede webserver kan hoste brugerdefinerede HTML-sider (klient), men er **ikke** en generel WebSocket-server.

### 1) Fuld HTML-side (med inputfelter)

Gem som `index.html` og host den som *user-defined web page* på PLC’ens webserver **eller** åbn den lokalt i en browser.

```html
<!doctype html>
<html lang="da">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>PLC WebSocket Client</title>
  <style>
    body{font-family:system-ui,Arial,sans-serif;max-width:900px;margin:24px auto;padding:0 12px}
    fieldset{margin:12px 0;padding:12px;border:1px solid #ddd;border-radius:8px}
    label{display:block;margin:6px 0 2px}
    input,select,button,textarea{padding:8px;font-size:14px}
    .row{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
    #log{height:240px;overflow:auto;background:#111;color:#0f0;padding:12px;border-radius:8px}
  </style>
</head>
<body>
  <h1>WebSocket testklient</h1>

  <fieldset>
    <legend>Forbindelse</legend>
    <div class="row">
      <div>
        <label for="proto">Protocol</label>
        <select id="proto"><option>ws</option><option>wss</option></select>
      </div>
      <div>
        <label for="host">Host/IP</label>
        <input id="host" value="192.168.0.100" />
      </div>
      <div>
        <label for="port">Port</label>
        <input id="port" value="8080" />
      </div>
      <div>
        <label for="path">Path</label>
        <input id="path" value="/" />
      </div>
    </div>
    <div style="margin-top:8px">
      <button id="connect">Connect</button>
      <button id="disconnect" disabled>Disconnect</button>
    </div>
  </fieldset>

  <fieldset>
    <legend>Besked</legend>
    <label for="message">Payload</label>
    <input id="message" value="Hello from PLC client" style="width:100%" />
    <div style="margin-top:8px">
      <button id="send" disabled>Send</button>
    </div>
  </fieldset>

  <fieldset>
    <legend>Log</legend>
    <pre id="log"></pre>
  </fieldset>

  <script>
    let ws;
    const $ = (id)=>document.getElementById(id);
    const log = (m)=>{ const el=$('log'); el.textContent += m + "\n"; el.scrollTop = el.scrollHeight; };

    $('connect').addEventListener('click', (e)=>{
      e.preventDefault();
      const url = `${$('proto').value}://${$('host').value}:${$('port').value}${$('path').value}`;
      log('CONNECT ' + url);
      ws = new WebSocket(url);
      ws.onopen = ()=>{ log('OPEN'); $('send').disabled=false; $('disconnect').disabled=false; };
      ws.onmessage = (evt)=> log('RX: ' + evt.data);
      ws.onerror = (err)=> log('ERR: ' + (err?.message || 'unknown'));
      ws.onclose = ()=>{ log('CLOSED'); $('send').disabled=true; $('disconnect').disabled=true; };
    });

    $('disconnect').addEventListener('click', (e)=>{ e.preventDefault(); if(ws){ ws.close(); } });
    $('send').addEventListener('click', (e)=>{
      e.preventDefault();
      const msg = $('message').value;
      if(ws && ws.readyState === WebSocket.OPEN){ ws.send(msg); log('TX: ' + msg); }
      else { log('Not connected'); }
    });
  </script>
</body>
</html>
```

### 2) Minimal WebSocket-server til test/bridge

Kør på en PC/edge-enhed i samme subnet. Denne server echos tilbage (ACK) og kan agere midtpunkt mellem PLC A & B.

`server.js`

```js
// npm init -y && npm i ws
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (socket, req) => {
  console.log('Client connected:', req.socket.remoteAddress);
  socket.send('Welcome – WS online');

  socket.on('message', (msg) => {
    const text = msg.toString();
    console.log('RX:', text);
    socket.send('ACK: ' + text);
  });

  socket.on('close', () => console.log('Client disconnected'));
});

console.log('WebSocket server listening on ws://0.0.0.0:8080');
```

**Kørsel:**

```bash
node server.js
# Forbind fra index.html: ws://<server-ip>:8080/
```

---

# WebSocket-Kommunikation via Webserver (S7‑1500‑kompatibel)

**Mål:** Justeret til S7‑1500’s webserver-model hvor læs/skriv til PLC-tags sker via **AWP** (Automation Web Programming), mens WebSocket bruges som **ekstern** event-kanal.

## Fuld HTML med AWP (deploy som *User-defined page*)

```html
<!doctype html>
<html lang="da">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>PLC WebSocket + AWP (S7‑1500)</title>
  <style>
    body{font-family:system-ui,Arial,sans-serif;max-width:900px;margin:24px auto;padding:0 12px}
    fieldset{margin:12px 0;padding:12px;border:1px solid #ddd;border-radius:8px}
    label{display:block;margin:6px 0 2px}
    input,button{padding:8px;font-size:14px}
    #log{height:180px;overflow:auto;background:#111;color:#0f0;padding:12px;border-radius:8px}
  </style>
</head>
<body>
  <!-- AWP_In_Variable Name='Setpoint' Use='"DB1".Setpoint' -->
  <!-- AWP_In_Variable Name='Message'  Use='"DB1".Message'  -->

  <h1>WebSocket + AWP (S7‑1500)</h1>

  <fieldset>
    <legend>Aktuelle værdier</legend>
    <p>Setpoint: <strong>:=Setpoint:</strong></p>
    <p>Message:  <strong>:=Message:</strong></p>
  </fieldset>

  <fieldset>
    <legend>Skriv til PLC (AWP POST)</legend>
    <form id="awpForm" method="post">
      <label for="sp">Setpoint</label>
      <input id="sp" name='Setpoint' type="number" step="1"/>

      <label for="msg" style="margin-top:8px">Message</label>
      <input id="msg" name='Message' type="text"/>

      <div style="margin-top:8px">
        <button type="submit">Skriv</button>
      </div>
    </form>
  </fieldset>

  <fieldset>
    <legend>WebSocket (ekstern)</legend>
    <input id="wsurl" value="ws://192.168.0.100:8080/" style="width:100%"/>
    <div style="margin-top:8px">
      <button id="connect">Connect</button>
      <button id="disconnect" disabled>Disconnect</button>
    </div>
    <pre id="log"></pre>
  </fieldset>

  <script>
    let ws;
    const $ = (id)=>document.getElementById(id);
    const log = (m)=>{ const el=$('log'); el.textContent += m + "\n"; el.scrollTop = el.scrollHeight; };

    $('connect').addEventListener('click', ()=>{
      ws = new WebSocket($('wsurl').value);
      ws.onopen    = ()=>{ log('OPEN'); $('disconnect').disabled=false; };
      ws.onclose   = ()=>{ log('CLOSED'); $('disconnect').disabled=true; };
      ws.onerror   = (e)=> log('ERR ' + (e?.message || ''));
      ws.onmessage = (evt)=>{
        log('RX ' + evt.data);
        // Forvent fx JSON: { "setpoint": 42, "message": "Hello" }
        try{
          const d = JSON.parse(evt.data);
          if(typeof d.setpoint !== 'undefined') $('sp').value = d.setpoint;
          if(typeof d.message  !== 'undefined') $('msg').value = d.message;
          document.getElementById('awpForm').submit();
        }catch{}
      };
    });

    $('disconnect').addEventListener('click', ()=>{ if(ws) ws.close(); });
  </script>
</body>
</html>
```

**Noter:**

* **Read** i AWP: `:=Alias:` erstattes server‑side af webserveren med aktuelle værdier.
* **Write** i AWP: `<form method="post">` sender felter med navne, der matcher AWP‑aliaser.
* PLC‑webserveren er **ikke** en WS‑server; brug ekstern endpoint (fx Node.js) til WS‑events.

---

## Krav (S7‑kompatibilitet)

* Webserver aktiveret og *User‑defined pages* deployet i TIA.
* Korrekte runtime‑rettigheder for skriveadgang.
* Ekstern WS‑endpoint i samme subnet for realtids‑events/telemetri.
