# GreenOps & FinOps Calculation Module (v1.0)

## 1. Objective & Context
This command-line module has been developed for the automated and reproducible calculation of CO2 emissions (GreenOps) and resource costs (FinOps). The tool is built with a strong focus on auditability, traceability and compliance, suitable for high-security and regulated enterprise/government environments.

## 2. Architecture & Security Principles
To ensure the integrity of the host system, the *Immutable Infrastructure* principle is used
- **Host OS:** Fedora Silverblue (Container-first, read-only root).
- **Runtime:** Insulation via Toolbx containers.
- **Dependencies:** Strict separation via Python Virtual Environments (`venv`).
- **Validation:** 100% Test-Driven Development (TDD) via `pytest`.

## 3. Installation & Validation (Audit Trail)
Follow these steps for an isolated execution:
1. Activate the environment: `source venv/bin/activate`
2. Run the unit tests: `pytest test_greenops.py-v`
   
## 4. Incident Logbook (Post-Mortem)
**Incident:** TDD-001 (Syntax & Parsing Error in Test Phase)
**Symptom:** Test module could not be initialized (`collected 0 items`).
**Root Cause:** Manual interaction with a graphical text editor (`) led to corrupt filenames and unauthorized Bash syntax (` << EOF`) within the Python runtime.
**Resolution & Prevention:** Human interaction minimized. Implementation of direct CLI-based file injection (Infrastructure as Code principles) to prevent future syntax corruption.
