# 💻 Installation af GitHub CLI på Windows

Denne guide hjælper dig med at installere og konfigurere GitHub CLI (`gh`) på en Windows-computer, så du kan bruge GitHub fra kommandolinjen.

---

## 🧰 Forudsætninger

* Windows 10 eller 11
* Git installeret (kan hentes fra [https://git-scm.com](https://git-scm.com))
* En GitHub-konto (opret på [https://github.com](https://github.com) hvis du ikke har én)

---

## 1️⃣ Download GitHub CLI

1. Gå til den officielle side:
   👉 [https://cli.github.com/](https://cli.github.com/)
2. Klik på **Download for Windows**
   Eller brug direkte link:
   👉 [https://github.com/cli/cli/releases](https://github.com/cli/cli/releases)
3. Vælg `.msi` installationsfilen (f.eks. `gh_*_windows_amd64.msi`)
4. Download og kør installationsfilen

---

## 2️⃣ Installer GitHub CLI

1. Følg installationsguiden (næste/næste/finish)
2. Sørg for at sætte flueben i “Add to PATH” (normalt standard)
3. Når installationen er færdig, åbnes evt. en terminal — du kan lukke den

---

## 3️⃣ Test installationen

Åbn en ny Kommandoprompt (`cmd`) eller PowerShell og skriv:

```cmd
gh --version
```

Du bør få vist versionsnummer og at kommandoen virker.

---

## 4️⃣ Log ind på GitHub

For at bruge GitHub CLI med din konto:

```cmd
gh auth login
```

Svar på følgende spørgsmål:

* GitHub.com eller Enterprise? → **GitHub.com**
* Metode? → **HTTPS**
* Hvordan vil du logge ind? → Vælg **Login via browser**

En browser åbner, hvor du logger ind og tillader adgangen. Terminalen vil bekræfte når det lykkes.

---

## ✅ Klar til brug!

Du har nu GitHub CLI (`gh`) installeret og forbundet til din GitHub-konto.

### Eksempler:

```cmd
gh repo clone brugernavn/projektnavn

gh repo create

gh issue list
```

> Brug `gh help` eller `gh <kommando> --help` for hjælp til specifikke kommandoer.

Spørg underviser ved problemer eller spørgsmål.
