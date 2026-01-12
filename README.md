# TDD & Generative AI in Introductory Programming — Research Artifacts

![GitHub repo size](https://img.shields.io/github/repo-size/igormichalski/TDD-LLM-Education-Study?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/igormichalski/TDD-LLM-Education-Study?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/igormichalski/TDD-LLM-Education-Study?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/igormichalski/TDD-LLM-Education-Study?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/igormichalski/TDD-LLM-Education-Study?style=for-the-badge)

This repository contains anonymized datasets, analysis scripts, forms, and programming materials used in a study investigating **Test-Driven Development (TDD)** and the role of **generative AI tools** in **introductory programming education**.

The study materials are organized into **two instructional contexts**:

- **ShortCourse (Assert)**: C programming tasks using `assert`-based tests.
- **ShortCourse (Jest)**: JavaScript programming tasks using Jest.

---

## 📦 Repository structure (high level)

```text
.
├── Analysis/                      # Analysis scripts + exported results
├── Data/                          # Fully anonymized datasets (CSV + derived outputs)
├── Forms/                         # PDF forms used in the study
├── src/                           # Programming tasks + reference tests + utilities
├── Rubric Table                   # Rubric table used for scoring (see note below)
├── LICENSE
└── README.md
```

---

## 📂 Detailed structure

### `Analysis/`
Analysis content is separated by instructional context:

- `Analysis/ShortCourse (Assert)/`
  - `scripts/` — data cleaning, rubric aggregation, and figure/table generation
  - `results/` — exported plots/tables used in the study

- `Analysis/ShortCourse (Jest)/`
  - `scripts/` — data cleaning, rubric aggregation, and figure/table generation
  - `results/` — exported plots/tables used in the study

> Tip: If you add a `requirements.txt` (or similar) in the future, you can document the exact reproduction steps here.

---

### `Data/`
All data is fully anonymized and separated by context:

- `Data/ShortCourse (Assert)/`
  - `Characterization Responses Form.csv` — participant characterization responses
  - `Post-Round Response Form.csv` — post-round responses
  - `Survey/` — characterization / general survey data
  - `Perception/` — perception-related data/materials
  - `Data Google Colab (Applied Rubric)/` — rubric scoring outputs

- `Data/ShortCourse (Jest)/`
  - `Characterization Responses Form.csv`
  - `Post-Round Response Form.csv`
  - `Perception/`
  - `Data Google Colab (Applied Rubric)/`

---

### `Forms/`
PDF instruments used during data collection:

- `Forms/ShortCourse (Assert)/`
  - `Characterization Form.pdf`
  - `Post-Round Form.pdf`

- `Forms/ShortCourse (Jest)/`
  - `Characterization Form.pdf`
  - `Post-Round Form.pdf`

---

### `src/`
Programming tasks and reference tests used for the activities:

- `src/ShortCourse (Assert)/`
  - `problems/` — programming tasks + statements
  - `tests/` — reference tests (assert-based) for evaluation

- `src/ShortCourse (Jest)/`
  - `problems/` — programming tasks + statements
  - `tests/` — reference tests (Jest) for evaluation

- `src/utils/server (used for participants to upload files)/`
  - simple upload server utility used during the study (participant submissions)

---

## 🔎 Rubric
The scoring rubric used in the study is included as **`Rubric Table`**.

> Note: Consider renaming this file to something explicit like `Rubric-Table.pdf` or `Rubric-Table.xlsx` (and avoiding spaces) to improve portability.

---

## ♻️ Reproducibility (recommended workflow)
If you want to run the analysis locally:

1. Inspect the scripts under:
   - `Analysis/ShortCourse (Assert)/scripts/`
   - `Analysis/ShortCourse (Jest)/scripts/`

2. Ensure the scripts point to the correct input paths under `Data/`.

3. Run scripts to generate outputs into each `results/` folder.

> If you tell me what language/tools you used in `scripts/` (Python? R? notebooks?), I can add an exact “How to run” section with commands and environment setup.

---

## 📣 How to cite
If you are using these artifacts in academic work, please cite the associated paper:

```bibtex
@article{TODO,
  title   = {TODO: Paper Title},
  author  = {TODO: Authors},
  journal = {TODO},
  year    = {TODO},
  note    = {Artifacts available at: https://github.com/igormichalski/TDD-LLM-Education-Study}
}
```

---

## 🤝 Collaborators

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/igormichalski" title="Igor Michalski">
        <img src="https://avatars.githubusercontent.com/u/100472292?v=4" width="100px;" alt="Photo of Igor Michalski"/><br>
        <sub><b>Igor Roberto Michalski</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Kauandugi" title="Kauan Henrique">
        <img src="https://avatars.githubusercontent.com/u/80713347?v=4" width="100px;" alt="Photo of Kauan Henrique"/><br>
        <sub><b>Kauan Henrique Teixeira</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/jorge-m-prates/" title="Jorge Marques Prates">
        <img src="https://media.licdn.com/dms/image/v2/C4D03AQGm9ernj1GktA/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1609435619639" width="100px;" alt="Photo of Jorge Marques Prates"/><br>
        <sub><b>Dr. Jorge Marques Prates</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ferestrepoca" title="Felipe Restrepo Calle">
        <img src="https://avatars.githubusercontent.com/u/11912846?v=4" width="100px;" alt="Photo of Felipe Restrepo Calle"/><br>
        <sub><b>Dr. Felipe Restrepo Calle</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/VictorVendruscolo" title="Victor Rech Vendruscolo">
        <img src="https://avatars.githubusercontent.com/u/71718834?v=4" width="100px;" alt="Photo of Victor Rech Vendruscolo"/><br>
        <sub><b>Victor Rech Vendruscolo</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## 🔐 Ethics
All participant data has been anonymized.

---

## 📝 License
This project is under the **CC0-1.0 License**.  
See **LICENSE** for details.
