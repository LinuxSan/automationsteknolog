## 🍏 Trin for trin: Brug af GitHub i macOS (Terminal-version)

Denne guide viser, hvordan du bruger **Git** og **GitHub** via **Terminal** på macOS. Du lærer at oprette repositories (offentlige, private og delte), samt hvordan du uploader og henter kode fra GitHub via kommandolinjen.

---

### 🟢 Trin 1: Installer Git (hvis nødvendigt)

De fleste macOS-versioner har Git forudinstalleret. Tjek det med:

```bash
git --version
```

Hvis det ikke er installeret, bliver du bedt om at installere Xcode Command Line Tools. Følg blot anvisningerne.

Alternativt:

```bash
xcode-select --install
```

---

### 🟡 Trin 2: Konfigurer Git første gang

Indtast dine GitHub-oplysninger:

```bash
git config --global user.name "DIT_NAVN"
git config --global user.email "din@email.com"
```

---

### 🔵 Trin 3: Opret GitHub-repository

1. Gå til [https://github.com](https://github.com) og log ind
2. Klik på **"New repository"**
3. Udfyld:

   * Navn og beskrivelse
   * Vælg **Public** eller **Private**
   * Klik på **Create repository**

> 🟩 **Private:** Kun du (og evt. inviterede) kan se repoet.
> 🟨 **Public:** Alle kan se det.
> 🟦 **Internal:** Kun i organisationer.

---

### 🟣 Trin 4: Klon repository til din Mac (download)

```bash
cd ~/Documents

git clone https://github.com/brugernavn/repo-navn.git
cd repo-navn
```

---

### 🟠 Trin 5: Upload ændringer til GitHub

1. Redigér eller tilføj filer i mappen
2. Udfør:

```bash
git add .
git commit -m "Mit commit"
git push origin main
```

> Hvis du ikke bruger "main" som branch, tjek dit branchnavn:

```bash
git branch
```

---

### 🧑‍🤝‍🧑 Trin 6: Del repository med andre

1. Gå til repoet på GitHub
2. Klik **Settings** → **Collaborators**
3. Søg efter brugernavn og klik **Add**

---

### 🔄 Trin 7: Hent seneste ændringer (pull)

Hvis der er lavet ændringer på GitHub:

```bash
git pull origin main
```

---

### 🛠️ Nyttige Git-kommandoer

```bash
# Se status
git status

# Se commit-historik
git log

# Opret og skift branch
git checkout -b ny-feature

# Skift tilbage til main
git checkout main
```

---

### ✅ Klar til GitHub i Terminal

Du kan nu:

* Oprette og håndtere GitHub-repositories
* Uploade og hente kode
* Arbejde professionelt med versionsstyring via din Mac

> Tip: macOS-brugere kan også benytte GitHub Desktop eller Visual Studio Code med Git-integration for GUI.
