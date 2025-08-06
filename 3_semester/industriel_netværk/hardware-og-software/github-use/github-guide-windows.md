## 🚀 Trin for trin: Brug af GitHub i Windows (CMD-version)

Denne guide hjælper dig med at bruge **Git** og **GitHub** via **kommandoprompt (CMD)** i Windows. Vi gennemgår, hvordan du opretter repositories (private, public og delte), og hvordan du uploader og downloader kode til/fra dit repository.

---

### 🟢 Trin 1: Installer Git

1. Gå til [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Kør installationsfilen
3. Vælg standardindstillinger (med mindre du har særlige ønsker)
4. Bekræft at Git virker:

```bash
git --version
```

---

### 🟡 Trin 2: Opret GitHub-konto og repository

1. Gå til [https://github.com](https://github.com)
2. Log ind eller opret en konto
3. Klik på **"New repository"**
4. Udfyld:

   * **Repository name**
   * **Description** (valgfrit)
   * Vælg **Public**, **Private**, eller **Internal**
   * Tilføj README (valgfrit)
   * Klik **Create repository**

> 🟨 **Public:** Alle kan se dit repo.
> 🟩 **Private:** Kun du (og evt. inviterede) kan se repoet.
> 🟦 **Internal (kun organisationer):** Synlig for org-medlemmer.

---

### 🔵 Trin 3: Klon et repository (download)

```bash
# Navigér til ønsket mappe
cd C:\Bruger\Projekter

# Klon repository (erstat med dit eget)
git clone https://github.com/brugernavn/repo-navn.git
```

---

### 🟣 Trin 4: Upload filer til dit repository (commit & push)

1. Navigér ind i mappen:

```bash
cd repo-navn
```

2. Tilføj dine filer (eller redigér eksisterende)

3. Kør følgende:

```bash
# Føj alle nye/ændrede filer til Git
git add .

# Commit dine ændringer med en besked
git commit -m "Tilføjet nye filer"

# Skub ændringer til GitHub
git push origin main
```

> 💡 Hvis "main" ikke virker, brug `git branch` for at se dit branch-navn.

---

### 🧑‍🤝‍🧑 Trin 5: Del repository med andre

1. Gå til dit repository på GitHub
2. Klik på **Settings** → **Collaborators**
3. Søg efter brugernavnet på GitHub
4. Vælg person og klik **Add**

> Personen får en invitation via e-mail/GitHub-notifikation.

---

### 🔄 Trin 6: Træk seneste ændringer fra GitHub (pull)

Hvis du eller andre har ændret noget i repoet:

```bash
git pull origin main
```

---

### 🛠️ Ekstra Git-kommandoer

```bash
# Tjek status på ændringer
git status

# Se commit-historik
git log

# Opret ny branch
git checkout -b ny-feature

# Skift branch
git checkout main
```

---

### 🎯 Klar til GitHub!

Du er nu i stand til at:

* Oprette og dele repositories
* Arbejde med versionsstyring lokalt
* Uploade og hente kode via CMD på Windows

Har du brug for GUI? Prøv GitHub Desktop. Du kan også integrere Git med Visual Studio Code.
