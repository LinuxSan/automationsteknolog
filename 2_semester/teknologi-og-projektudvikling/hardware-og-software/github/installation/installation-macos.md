# 🍎 Installation af GitHub CLI på macOS

Denne guide hjælper dig med at installere og konfigurere GitHub CLI (`gh`) på en Mac via Homebrew.

---

## 🧰 Forudsætninger

* macOS 11 eller nyere
* Terminal-adgang (Cmd + Space → "Terminal")
* En GitHub-konto ([https://github.com](https://github.com))

---

## 1️⃣ Installer Homebrew (hvis nødvendigt)

Homebrew bruges til at installere programmer på macOS:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Tjek at det virker:

```bash
brew --version
```

---

## 2️⃣ Installer GitHub CLI med Homebrew

```bash
brew install gh
```

---

## 3️⃣ Bekræft installation

Tjek at kommandoen virker:

```bash
gh --version
```

Du bør se `gh version 2.x.x`

---

## 4️⃣ Log ind på GitHub

Kør:

```bash
gh auth login
```

Svar på følgende:

* GitHub.com eller Enterprise? → **GitHub.com**
* Protokol? → **HTTPS**
* Login-metode? → **Login via browser**

Følg linket i terminalen og giv tilladelse via din browser. Når det er bekræftet, vender du tilbage til terminalen.

---

## ✅ Klar til brug!

GitHub CLI er nu installeret og koblet til din GitHub-konto.

### Eksempler:

```bash
gh repo clone brugernavn/projektnavn

gh repo create

gh issue list
```

> Brug `gh help` eller `gh <kommando> --help` for at se muligheder og syntaks.

Kontakt underviser hvis du får fejl under installationen eller login.
