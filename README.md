# Bubble Farming

> Scaling gas bubble injection for energy-efficient mass transfer in agricultural and water systems.

---

## 🔬 Overview

Bubble Farming is a simulation-first research project exploring how **bubble fields can be treated as controllable mass-transfer operators** rather than passive aeration artifacts.

The core goal is to understand and quantify how spatially and temporally structured bubble injection can:

- Improve nutrient and oxygen dispersion
- Reduce concentration dead zones
- Lower energy per unit effective gas transfer
- Enable control-oriented design of aeration systems

Hydroponics is the initial motivating application, but the methods generalize to aquaculture, wastewater treatment, and bioreactors.

---

## 🧠 Core idea

Instead of asking:

> “How much air should we inject?”

this project asks:

> **“Where and when should gas transfer occur to achieve uniformity with minimal energy?”**

Mathematically, bubble plumes are modeled as **distributed source terms** in diffusion–uptake systems and optimized using explicit dispersion and efficiency metrics.

---

## 🧪 Repository structure

```

docs/
proposal/          # NSF-style research framing and technical plan

src/
physics/           # bubble source models + transport equations
metrics/           # dispersion + efficiency metrics
run_simulation.py  # CLI simulation runner

experiments/
baseline_vs_bubbles.py

notebooks/
(visualization + analysis, optional)

requirements.txt

````

---

## 🚀 Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/run_simulation.py --plot
python experiments/baseline_vs_bubbles.py
````

---

## 📊 Current capabilities

* 2D diffusion + uptake transport model
* Gaussian bubble source abstraction
* Multi-source injection
* Spatial variance and dispersion metrics
* Baseline vs bubble-assisted comparison experiments

---

## 📈 Metrics of interest

The project focuses on:

* Spatial variance of concentration fields
* Coefficient of variation
* Time-to-uniformity
* Energy proxy per unit effective transfer

These are chosen to map directly to **efficiency-driven system design** rather than qualitative visualization alone.

---

## 🗺 Roadmap

* [x] Reduced-order diffusion + bubble source model
* [x] Baseline vs bubble comparison experiment
* [ ] Energy efficiency modeling (pump / pressure proxies)
* [ ] Spatial source optimization
* [ ] Feedback control strategies
* [ ] Parameter sweeps + phase diagrams
* [ ] Reproducible figure gallery

---

## 📚 Research framing

Formal problem statements and technical aims are documented in:

```
docs/proposal/
```

These mirror transport-phenomena and control-systems research programs (e.g., NSF CBET / CPS style work).

---

## ⚖ License

MIT

