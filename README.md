# TDD & Generative AI in Introductory Programming – Research Artifacts

This repository contains the research artifacts generated during a study on the
use of **generative AI tools (e.g., ChatGPT)** to support **introductory programming**
activities grounded in **Test-Driven Development (TDD)**.  
The study was conducted with undergraduate students from the *Universidade Estadual
de Mato Grosso do Sul (UEMS)* in collaboration with the *Universidad Nacional de Colombia (UNAL)*.

The repository is organized to ensure **reproducibility**, **transparency**, and easy
access to all analysis materials, datasets (fully anonymized), forms, problem
statements, and test suites.

---

## 📂 Repository Structure

Below is an overview of the directory organization and the purpose of each folder.

---

### **`Analysis/`**
Contains all code and outputs related to the **quantitative and qualitative analyses**.

#### `Analysis/scripts/`
Python scripts, notebooks, or helper utilities used to:
- clean and transform datasets  
- apply the rubric  
- run descriptive statistics  
- generate graphs and tables for the paper  
- export results

#### `Analysis/results/`
Final outputs of the analyses, including:
- statistical summaries  
- tables in CSV/LaTeX  
- generated figures (Likert plots, bar charts, etc.)  
- exported material used directly in the paper or presentation  

---

### **`Data/`**
Contains all anonymized datasets collected during the study.

#### `Data/Data Google Colab (Applied Rubric)/`
Results obtained through rubric application performed in Google Colab:
- coded scores per problem  
- correctness, robustness, and TDD usage evaluations  
- merged datasets across rounds  
- evaluator comparisons (if applicable)

#### `Data/Perception/`
Includes perception-related responses:
- Likert-scale questionnaires  
- attitude toward TDD  
- perceived usefulness of AI  
- confidence, difficulty, and self-evaluation metrics  

#### `Data/Survey/`
General survey datasets:
- demographic and characterization questionnaire  
- prior programming experience  
- familiarity with AI tools  
- metadata used to contextualize the sample  

All data in this directory is **fully anonymized**.

---

### **`Forms/`**
Original research instruments:
- questionnaires used in the study  
- perception forms (Likert)  
- characterization surveys  
- rubrics (PDF/MD)  
- prompt protocols and instructions given to participants  

These are the documents used by students during each round of activities.

---

### **`src/`**
Source code used throughout the study.

#### `src/problems/`
Programming problem statements and reference solutions used in:
- Round 1  
- Round 2  
- Rubric-based code evaluation  

Each subproblem contains:
- description  
- expected behavior  
- examples  
- reference implementation (if provided)

#### `src/tests/`
Test suites used to evaluate student code submissions:
- correctness tests  
- edge-case tests  
- robustness tests  
- TDD-related checks when applicable  

These tests represent the “ground truth” for the rubric evaluation.

---

## 🔍 Purpose

This repository provides everything needed to understand and reproduce the study:
- datasets (anonymous)  
- instruments  
- analysis code  
- outputs  
- problem statements and test harnesses

It is suitable for:
- replication studies  
- teaching purposes  
- transparency in AI-in-education research  
- artifact submission for academic venues  

---

## 🔐 Ethics and Anonymization

All data undergoes strict anonymization:
- no names, emails, or personal identifiers  
- all participants coded as `S01`, `S02`, …  
- free-text answers reviewed to avoid indirect identification  

This repository is intended **solely for research and education**.
