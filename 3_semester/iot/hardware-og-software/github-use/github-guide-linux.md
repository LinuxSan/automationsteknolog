## 🐧 Trin for trin: Brug af GitHub i Linux (CLI-version)

Denne guide hjælper dig med at bruge **Git** og **GitHub** via terminalen i Linux. Vi gennemgår, hvordan du opretter repositories (private, public og delte), samt hvordan du uploader og henter kode til og fra GitHub.

---

### 🟢 Trin 1: Installer Git

Åbn terminalen og kør:

```bash
sudo apt update
sudo apt install git -y
```

Tjek at Git er installeret:

```bash
git --version
```

---

### 🟡 Trin 2: Konfigurer Git (første gang)

Indtast dine brugeroplysninger:

```bash
git config --global user.name "DIT_NAVN"
git config --global user.email "din@email.com"
```

---

### 🔵 Trin 3: Opret GitHub-konto og repository

1. Gå til [https://github.com](https://github.com)
2. Opret eller log ind på din konto
3. Klik på **"New repository"**
4. Udfyld:

   * Repository name
   * Vælg **Public** eller **Private**
   * (Valgfrit) Tilføj README
   * Klik "Create repository"

> 🟨 **Public:** Alle kan se dit repo.
> 🟩 **Private:** Kun du (og evt. inviterede) kan se repoet.

---

### 🟣 Trin 4: Klon repository (hent til lokal maskine)

```bash
cd ~

git clone https://github.com/brugernavn/repo-navn.git
cd repo-navn
```

---

### 🟠 Trin 5: Upload ændringer til GitHub

1. Tilføj eller redigér filer i mappen
2. Udfør disse kommandoer:

```bash
git add .
git commit -m "Tilføjet nye filer"
git push origin main
```

> Hvis branch ikke er "main", tjek med:

```bash
git branch
```

---

### 🧑‍🤝‍🧑 Trin 6: Del repository med andre

1. Gå til dit repository på GitHub
2. Klik på **Settings** → **Collaborators**
3. Inviter brugere ved GitHub-brugernavn

---

### 🔄 Trin 7: Hent nyeste ændringer (pull)

Hvis andre (eller du selv) har lavet ændringer i repoet:

```bash
git pull origin main
```

---

### 🛠️ Nyttige Git-kommandoer

```bash
# Tjek status for ændringer
git status

# Se commit-historik
git log

# Opret ny branch
git checkout -b ny-feature

# Skift branch
git checkout main
```

---

### ✅ Klar til GitHub på Linux!

Du er nu klar til at:

* Administrere dine GitHub-projekter
* Arbejde med versionsstyring
* Samarbejde med andre via Git og terminal

Ønsker du GUI? Prøv GitKraken, GitHub Desktop (via Wine), eller brug Visual Studio Code med Git-integration.
