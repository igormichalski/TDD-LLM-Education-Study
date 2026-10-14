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

## 📄 Paper

These artifacts accompany the paper **"Exploring AI-Assisted Test-Driven Development in Introductory Programming Education"**, accepted at the Brazilian Symposium on Software Quality (SBQS 2026).

- Author version: [`Paper/SBQS2026_Exploring_AI-Assisted_TDD.pdf`](Paper/SBQS2026_Exploring_AI-Assisted_TDD.pdf)

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

## ⚙️ Requirements

All commands below were tested on macOS with:

| Component | Used by | Tested version |
|---|---|---|
| Python | analysis scripts, upload server | 3.11 |
| pandas, numpy, matplotlib, seaborn | analysis scripts | see `requirements.txt` |
| Flask, gunicorn, gevent | upload server | see `requirements.txt` |
| GCC or Clang (any C99 compiler) | C reference tests | Apple Clang (`gcc`) |
| Node.js + npm | Jest reference tests | Node 25, Jest 29.7 |

Clone the repository and install the Python dependencies in a virtual environment:

```bash
git clone https://github.com/igormichalski/TDD-LLM-Education-Study.git
cd TDD-LLM-Education-Study
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ How to run

All commands assume you start from the repository root, with the virtual environment active.

### 1. Rubric analysis (descriptive statistics and figures)

The scripts were exported from Google Colab and read the CSV files from the current directory, so run them **from inside the data folder**. They print the descriptive statistics tables to the terminal and open the figures (Likert distribution and boxplots) in a window.

**ShortCourse (Assert)**

```bash
cd "Data/ShortCourse (Assert)/Data Google Colab (Applied Rubric)"
python "../../../Analysis/ShortCourse (Assert)/scripts/rubric.py"
cd -
```

**ShortCourse (Jest)**

```bash
cd "Data/ShortCourse (Jest)/Data Google Colab (Applied Rubric)"
python "../../../Analysis/ShortCourse (Jest)/scripts/rubric_ifms.py"
cd -
```

Columns in the rubric CSVs: `participant`, `group`, `rater`, `code` (exercise), and the scores (0–3) for `correction`, `design` and `style`, plus `total` (0–9). The figures reported in the study are in `Analysis/*/results/`.

> On a machine without a display, prefix the command with `MPLBACKEND=Agg` to skip the figure windows and print only the tables.

### 2. C reference tests (ShortCourse Assert)

Each file in `src/ShortCourse (Assert)/tests/` holds the headers/macros and the `assert` calls for one problem. The function under test is not included, because participants wrote it. To run a test against an implementation (for example, a participant's solution in `Data/ShortCourse (Assert)/Perception/` or your own), put the function in a file and build a test program around it:

```bash
TEST="src/ShortCourse (Assert)/tests/Test Problem 1.c"   # Problems 1–4
SOLUTION=my_solution.c                                     # file containing mdc(...)

{ grep -vE '^[[:space:]]*(assert|ASSERT_NEAR)\(' "$TEST"
  cat "$SOLUTION"
  echo 'int main(void){'
  grep -E '^[[:space:]]*(assert|ASSERT_NEAR)\(' "$TEST"
  echo '  puts("All tests passed"); return 0; }'
} > run_test.c

gcc -o run_test run_test.c -lm && ./run_test
```

Functions expected by each test: Problem 1 `int mdc(int, int)`; Problem 2 `soma_digitos(long long)`; Problem 3 `int conta_vogais(const char *)`; Problem 4 `double convCtoF(double)` and `double convFtoC(double)`. Invalid inputs must return `-1` (`EXPECT_ERR`). The problem statements are in `src/ShortCourse (Assert)/problems/`.

### 3. Jest reference tests (ShortCourse Jest)

The `.test.js` files in `src/ShortCourse (Jest)/tests/` call the functions directly (the `require` line is commented out). The simplest way to run them is to put the implementation and the test in one file:

```bash
mkdir jest-run && cd jest-run
npm init -y
npm install --save-dev jest@29

# my_solution.js contains: function mdc(a, b) { ... }
cat my_solution.js "../src/ShortCourse (Jest)/tests/Round 1/Testes Ex1.test.js" > ex1.test.js
npx jest
```

Functions expected by each test: Ex1 `mdc`, Ex2 `validaSenha`, Ex3 `soma_digitos` (receives `BigInt` for large values), Ex4 `ehPrimo`, Ex5 `conta_vogais`, Ex6 `convCtoF` / `convFtoC`.

### 4. Upload server (optional)

The Flask application that participants used to submit their files during the short courses. See `src/utils/server (used for participants to upload files)/README.md` for details.

```bash
cd "src/utils/server (used for participants to upload files)"
python server.py                                  # development server on http://localhost:5000
# or, as used during the study:
gunicorn -c gunicorn_config.py server:app
```

Uploaded files are saved in `uploads/` inside that folder.

### ⚠️ Known issues in the reference tests

The tests are kept exactly as they were used in the study. Running them with correct implementations shows two problems in the test oracles:

- **Problem 2 (C), `soma_digitos(98765432109876543210)`**: the literal does not fit in any C integer type, so compilation fails with *"integer literal is too large"*. Remove that line to run the remaining asserts. The Jest version (Ex3) uses `BigInt` and works.
- **Problem 3 (C) / Ex5 (Jest), `conta_vogais`**: the expected values are inconsistent about accented vowels. `"Inteligência Artificial" == 10` only holds if accented vowels are **not** counted, while `"Olá, mundo!" == 4` and `"àéîõü café CAÇÃO" == 8` require counting them (and the last one gives 10 when accented vowels are counted). No single implementation passes all asserts.

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
        <img src="https://avatars.githubusercontent.com/u/71718834?v=4" width="100px;" alt="Photo of Jorge Marques Prates"/><br>
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
      <td align="center">
      <a href="https://orcid.org/0000-0001-5934-2564" title="Silvana Morita Melo">
        <img src="https://avatars.githubusercontent.com/u/71718834?v=4" width="100px;" alt="Photo of Silvana Morita Melo"/><br>
        <sub><b>Dra. Silvana Morita Melo</b></sub>
      </a>
  </tr>
</table>

---

## 🔐 Ethics
All participant data has been anonymized.

---

## 📝 License
This project is under the **CC0-1.0 License**.  
See **LICENSE** for details.
