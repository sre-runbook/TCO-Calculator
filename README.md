# GreenOps & FinOps Calculatiemodule (v1.0)

## 1. Doelstelling & Context
Deze command-line module is ontwikkeld voor de geautomatiseerde en reproduceerbare berekening van CO2-uitstoot (GreenOps) en resource-kosten (FinOps). De tool is gebouwd met een sterke focus op auditability, traceerbaarheid en compliance, geschikt voor hoog-beveiligde en gereguleerde enterprise/overheidsomgevingen.

## 2. Architectuur & Beveiligingsprincipes
Om de integriteit van het host-systeem te waarborgen, wordt gewerkt volgens het *Immutable Infrastructure* principe:
- **Host OS:** Fedora Silverblue (Container-first, read-only root).
- **Runtime:** Isolatie via Toolbx containers.
- **Dependencies:** Strikte scheiding via Python Virtual Environments (`venv`).
- **Validatie:** 100% Test-Driven Development (TDD) via `pytest`.

## 3. Installatie & Validatie (Audit Trail)
Volg deze stappen voor een geïsoleerde executie:
1. Activeer de omgeving: `source venv/bin/activate`
2. Voer de unit-tests uit: `pytest test_greenops.py -v`

## 4. Incident Logboek (Post-Mortem)
**Incident:** TDD-001 (Syntax & Parsing Error in testfase)
**Symptoom:** Testmodule kon niet worden geïnitialiseerd (`collected 0 items`).
**Root Cause:** Handmatige interactie met een grafische teksteditor (`nano`) leidde tot corrupte bestandsnamen en ongeoorloofde Bash-syntax (`cat << EOF`) binnen de Python runtime.
**Resolutie & Preventie:** Menselijke interactie geminimaliseerd. Implementatie van directe CLI-gebaseerde file-injection (Infrastructure as Code principes) ter voorkoming van toekomstige syntax-corruptie.
