# 🐧 Installation af GitHub CLI på Linux (Ubuntu/Debian)

Denne guide hjælper dig med at installere og konfigurere GitHub CLI (`gh`) på en Linux-maskine (især Ubuntu/Debian-baseret).

---

## 🧰 Forudsætninger

* Terminaladgang med `sudo`-rettigheder
* Git installeret (`sudo apt install git` hvis nødvendigt)
* En GitHub-konto ([https://github.com](https://github.com))

---

## 1️⃣ Tilføj GitHub CLI repository

Kør følgende kommandoer:

```bash
sudo apt update
sudo apt install curl -y

curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
  https://cli.github.com/packages stable main" | \
  sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
```

---

## 2️⃣ Installer GitHub CLI

```bash
sudo apt update
sudo apt install gh -y
```

---

## 3️⃣ Bekræft installationen

```bash
gh --version
```

Du bør se noget i stil med `gh version 2.x.x`

---

## 4️⃣ Log ind på GitHub

Kør:

```bash
gh auth login
```

Følg vejledningen:

* Vælg **GitHub.com**
* Vælg **HTTPS** som protokol
* Vælg **Login via browser**
* Følg linket der vises i terminalen for at logge ind

Når login er gennemført, vender du tilbage til terminalen og får bekræftelse.

---

## ✅ Klar til brug!

Du har nu GitHub CLI installeret og koblet til din GitHub-konto.

### Eksempler på kommandoer:

```bash
gh repo clone brugernavn/projektnavn

gh repo create

gh issue list
```

> Brug `gh help` eller `gh <kommando> --help` for at se muligheder og detaljer.

Spørg underviser hvis du har problemer med installationen.
