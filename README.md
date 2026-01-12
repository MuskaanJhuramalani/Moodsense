# MoodSense

**MoodSense** is a Python-based mood tracking and analysis system that records user emotions and visualizes patterns over time. It helps users monitor their emotional trends and gain insights into their mental well-being.

## Features

- Record daily moods and notes
- Visualize mood patterns with graphs
- Lightweight, easy-to-use Python interface
- Extensible for future analytics or ML features

## Folder Structure
moodsense/
├── src/ # Main Python scripts
│ ├── main.py
│ └── graphs.py
├── data_sample/ # Example data for testing
├── data/ # Your real data (ignored by Git)
├── .gitignore
└── README.md


> **Note:** The `data/` folder is ignored to protect privacy. Use `data_sample/` for testing.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/moodsense.git
cd moodsense

**## 2. Install dependencies:**
pip install -r requirements.txt

**##3. Run the main program:**
python src/main.py
