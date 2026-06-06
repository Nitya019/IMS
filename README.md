# VN Jewellers — Inventory Management System

A web-based inventory and catalogue application built for **VN Jewellers**, an extension of Munna Lal Verma Jewellers, a family jewellery business with 50+ years of legacy in Lucknow, India.

Built using **Python** and **Streamlit**, the app digitizes the jewellery inventory and makes it accessible as a clean, browsable catalogue.

🔗 **Live App:** [vnjewellers.streamlit.app](https://vnjewellers.streamlit.app)

---

## Features

### Public View
- Browse the full jewellery catalogue organized by category
- Categories include: Earrings, Sets, Bracelets, Mangalsutra, Bangles, Tika, and Pendants
- Each item displays its **photo**, **purity** (e.g. 18k), **weight**, and **unique ID**
- Clean dark-themed UI designed for easy browsing

### Admin Panel
- Secure admin interface for managing inventory
- Add, update, or remove jewellery items
- Upload product images directly through the app

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web framework and deployment |
| Pandas | Data handling |
| GitHub | Version control |

---

## Project Structure

```
vnjewellers/
│
├── home.py               # Landing page with business introduction
├── pages/
│   ├── view.py           # Public catalogue view
│   └── admin.py          # Admin inventory management panel
├── data/                 # Inventory data files
├── images/               # Product images
└── requirements.txt      # Dependencies
```

---

## Getting Started

### Prerequisites
```
Python 3.8+
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/vnjewellers.git

# Navigate into the project
cd vnjewellers

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run home.py
```

---

## Background

This application was built to solve a real problem — the business previously managed its entire inventory manually, making it difficult to track stock, check item details quickly, or present the catalogue to customers digitally.

This system replaced the manual process with a structured, visual, and easy-to-use web application accessible from any device.

---

## Developer

**Nitya Verma**  
B.Sc Applied Statistics and Analytics — NMIMS Mumbai  
[LinkedIn](#) | [GitHub](#) | [Kaggle](#)
