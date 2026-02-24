# 🛡️ DevSecure API

Une petite API Python (Flask) conçue avec une approche **DevSecOps** : sécurisée dès le développement, containerisée et livrée via une pipeline CI/CD automatisée.

![CI/CD](https://github.com/Daniween/ci-cd-secure/actions/workflows/ci-cd.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![Security](https://img.shields.io/badge/Security-Scanned-brightgreen)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fb08c8cefab641ccb3040926126d05db)](https://app.codacy.com/gh/daniween/ci-cd-secure/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

---

## 🔧 Fonctionnalités

- ✅ **API Python légère** (Flask ou FastAPI)
- 🐳 **Dockerisation** complète
- ⚙️ **Pipeline CI/CD GitHub Actions**
  - Build & test de l’image Docker
  - Scan de sécurité :
    - [Trivy](https://github.com/aquasecurity/trivy) (vulnérabilités)
    - [Snyk](https://snyk.io/) (dépendances & container)
    - [GitLeaks](https://github.com/zricethezav/gitleaks) (secrets dans le code)
  - Push automatique vers [Docker Hub](https://hub.docker.com/)
- 🧾 Génération de rapport HTML de vulnérabilités

---

## 🚀 Lancer en local

### 1. Cloner le projet

```bash
git clone https://github.com/Daniween/ci-cd-secure.git
cd ci-cd-secure
docker build -t devsecure-api .
docker run -p 3000:3000 devsecure-api
```

## 🧪 Tester l'API (Exemple Flask)

```bash
curl http://localhost:3000/
```

## 🔐 Sécurité & Scans

| Outil    | Objectifs                                           |
| -------- | --------------------------------------------------- |
| Trivy    | Scan des vulnérabilités dans l'image Docker         |
| Snyk     | Analyse des dépendances Python et du container      |
| GitLeaks | Détection de secrets (clés, tokens...) dans le code |

## 📦 Déploiement Docker Hub

- Une fois la branche dev poussée :
- L’image est construite automatiquement
- Elle est scannée avec Trivy & Snyk
- Puis poussée en latest sur Docker Hub :

```bash
docker pull <ton_user>/devsecure-api:latest
```

## 📁 Structure du projet

```
├── app.py # Application Flask principale
├── Dockerfile # Configuration de l’image
├── requirements.txt # Dépendances Python
├── .github/
│ └── workflows/
│ └── ci.yml # Pipeline CI/CD GitHub Actions
└── README.md # Documentation
```

### 🗺️ Architecture CI/CD

<p align="center">
  <img src="https://raw.githubusercontent.com/Daniween/ci-cd-secure/main/.github/assets/architecture.svg" alt="Architecture Diagram" width="800"/>
</p>
Test workflow 