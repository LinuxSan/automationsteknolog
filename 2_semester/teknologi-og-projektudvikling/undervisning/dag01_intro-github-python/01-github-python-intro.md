# 📘 README – Dag 01: GitHub + Python Intro

Velkommen til første undervisningsdag i faget **Teknologi og Projektudvikling**.

Denne dag introducerer jer til:

* Projektopstart med GitHub
* Grundlæggende Python-programmering
* Brug af `.gitignore`
* Installation af GitHub CLI og Visual Studio Code

---

## 📁 Find installationsvejledninger

Inden du kan arbejde videre, skal du have de nødvendige værktøjer installeret.

Navigér til følgende mappe i projektstrukturen:

```
automationsteknolog/2_semester/teknologi-og-projektudvikling/hardware-og-software/
```

Her vælger du den installationsvejledning (.md-fil), der passer til dit operativsystem:

| Platform | Filnavn                                                                  |
| -------- | ------------------------------------------------------------------------ |
| Windows  | `installation-vscode-windows.md` og `installation-github-cli-windows.md` |
| Linux    | `installation-vscode-linux.md` og `installation-github-cli-linux.md`     |
| macOS    | `installation-vscode-macos.md` og `installation-github-cli-macos.md`     |

Følg vejledningerne trin for trin. Hvis du sidder fast, så spørg underviseren eller en medstuderende.

---

## 🛠️ Arbejdsopgaver

### 1. Opret GitHub repository og klon det

1. Log ind på [https://github.com](https://github.com)
2. Opret et nyt **privat** repository med navnet:

   ```
   gruppe-XX-projekt
   ```
3. Åbn terminal og kør:

   ```bash
   gh repo clone brugernavn/gruppe-XX-projekt
   cd gruppe-XX-projekt
   ```

### 2. Tilføj en README og `.gitignore`

1. Opret en tom `README.md` i roden:

   ```bash
   echo "# Gruppe XX – Teknologi og Projektudvikling" > README.md
   ```
2. Opret en `.gitignore`:

   ```bash
   echo "__pycache__/
   ```

\*.csv
.vscode/" > .gitignore

````
3. Commit og push:
```bash
git add .
git commit -m "Init: README og .gitignore"
git push
````

### 3. Opret mappestruktur til projektet

```bash
mkdir python
mkdir esp32
data
mkdir docs
```

> Sørg for at din struktur svarer til den officielle template (udleveres af underviser)

---

## 🧪 Afprøvning

* Åbn dit repo på GitHub og tjek at:

  * Mappestrukturen er korrekt
  * `.gitignore` og `README.md` er med
  * Du kan pushe ændringer uden fejl

---

## 📚 Opgaver for GitHub

* ✅ Du har oprettet og clonet dit repo
* ✅ Du har struktureret mapperne korrekt
* ✅ Du har committed og pushed en README og .gitignore
* 🔁 Du ved hvordan man bruger `git add`, `commit`, `push` og `status`
* 🔍 Du har forstået hvordan `.gitignore` fungerer

> Næste trin: Python-intro og `basis.py`, som du arbejder videre med efter GitHub-setup er færdigt.
