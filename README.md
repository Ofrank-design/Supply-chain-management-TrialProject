# 📊 SCM Projects  Python & JavaScript

> Two practical supply chain projects built from scratch a KPI dashboard in Python and a procurement quiz game in JavaScript.

**By [Frank Oduro](https://ofrank-design.github.io/scm-projects) · KSTU BSc Procurement & Supply Chain Management · Ghana 🇬🇭**


## About the Author

**Frank Oduro** *BSc Procurement & Supply Chain Management at Kumasi Technical University (KSTU), Ghana. Building a real portfolio 

- 🌐 [Portfolio](https://ofrank-design.github.io)
- 🛠️ [Procurement Toolkit](https://ofrank-design.github.io/procurement-logistics-toolkit)
- 🐙 [GitHub](https://github.com/Ofrank-design)

![Student](https://img.shields.io/badge/KSTU-BSc%20Procurement%20%26%20-0d2149?style=flat-square&logo=graduation-cap&logoColor=d4a843)
![Year](https://img.shields.io/badge/Enrolled-October%202026-d4a843?style=flat-square)
![Location](https://img.shields.io/badge/📍-Kumasi%2C%20Ghana-006B3F?style=flat-square)
![Portfolio](https://img.shields.io/badge/Portfolio-Live-brightgreen?style=flat-square&logo=github)
![Ghana PPA](https://img.shields.io/badge/Ghana%20PPA%20Acts%20663%20%26%20914-0a4d2e?style=for-the-badge&logoColor=white)
![Ghana e-GP](https://img.shields.io/badge/Ghana%20e--GP%20Portal-1a6b3c?style=for-the-badge&logoColor=white)
![EOQ Modelling](https://img.shields.io/badge/EOQ%20Modelling-16a34a?style=for-the-badge&logoColor=white)
![ABC Analysis](https://img.shields.io/badge/ABC%20Analysis-15803d?style=for-the-badge&logoColor=white)
![Contract Management](https://img.shields.io/badge/Contract%20Management-166534?style=for-the-badge&logoColor=white)
![Strategic Sourcing](https://img.shields.io/badge/Strategic%20Sourcing-14532d?style=for-the-badge&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![SAP MM](https://img.shields.io/badge/SAP%20MM-0FAAFF?style=for-the-badge&logo=sap&logoColor=white)
![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle%20Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![MS Dynamics 365](https://img.shields.io/badge/MS%20Dynamics%20365-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Microsoft Learn](https://img.shields.io/badge/Microsoft%20Learn-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)




## Projects

### 1. 📈 Supply Chain KPI Dashboard  Python

A fully coded KPI dashboard built with Python and matplotlib, visualising six key supply chain metrics for a Ghana public sector context.

**Charts included:**
- On-Time Delivery Rate vs target (line chart)
- Purchase Order Cycle Time (bar chart)
- Supplier Quality Rate (line + fill)
- Cost Savings vs Budget — GHS (bar chart, green/red)
- Inventory Turnover Ratio (line chart)
- Annual Spend by Category (pie chart)

**KPI Scorecard** at the bottom summarises December performance at a glance — green for on target, red for below.

![SCM KPI Dashboard](scm_kpi_dashboard.png)



### 2. 🎮 Ghana Procurement Quiz Game  JavaScript

An interactive browser-based quiz testing knowledge of Ghana's Public Procurement Acts 663 & 914, EOQ calculations, logistics, and supply chain management fundamentals.

**Features:**
- 15 questions across 5 categories
- 30-second countdown timer per question
- Score system — faster correct answers earn more points
- Detailed explanation after every answer
- Final grade (A/B/C/D) with personalised study feedback
- Zero dependencies — pure HTML, CSS, JavaScript

**[▶ Play the Quiz →](https://ofrank-design.github.io/procurement-logistics-toolkit)**



## Tech Stack

| Project | Language | Libraries |
|---|---|---|
| KPI Dashboard | Python | matplotlib, numpy |
| Quiz Game | JavaScript | Vanilla JS — no frameworks |



## How to Run

### Python Dashboard
```bash
# Clone the repo
git clone https://github.com/Ofrank-design/scm-projects.git
cd scm-projects

# Install dependencies
pip install matplotlib numpy

# Run the dashboard
python scm_kpi_dashboard.py

# Output: scm_kpi_dashboard.png saved in the same folder


### Quiz Game
```bash
# Just open the file in any browser
open procurement-quiz.html
```
No server needed. Works completely offline.



## Sample KPIs Used

| KPI | Target | Dec Actual |
|---|---|---|
| On-Time Delivery Rate | 90% | 96% ✅ |
| PO Cycle Time | 14 days | 10 days ✅ |
| Supplier Quality Rate | 95% | 97% ✅ |
| Inventory Turnover | 5.0x | 6.0x ✅ |

Data represents a typical Ghana public sector supply chain. Replace with your own CSV data to customise.



## Quiz Categories

- 🏛️ Ghana PPA Act 663 — procurement methods, RFQ rules, PPA mandate
- 📋 Ghana PPA Act 914 — e-GP platform, sole source approvals, amendments
- 📦 EOQ & Inventory — calculations, safety stock, reorder point
- 🚚 Logistics — Incoterms 2020, CIF, FOB, EXW
- 🔗 Supply Chain Management — Bullwhip Effect, SCOR model, ABC analysis



## What's Next

- [ ] Connect dashboard to real Ghana e-GP CSV data
- [ ] Add Power BI version of the KPI dashboard
- [ ] Expand quiz to 30 questions with difficulty levels
- [ ] Add leaderboard to the quiz using localStorage


## License

MIT  free to use, fork, and adapt. A star is appreciated if this helped you.



*Made in Kumasi, Ghana 🇬🇭*
