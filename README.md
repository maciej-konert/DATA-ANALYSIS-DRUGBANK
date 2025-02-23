# **DrugBank Data Analysis - Python Project**  

## **Project Overview**  
This project is a part of my Python course and focuses on analyzing drug-related data from DrugBank. The tasks were originally given in another language and have been automatically translated into English. You can find the translated task description in the `project_task.pdf` file.  

## **How to Run the Project**  
To execute the project, follow these steps:  

1. **Set up a virtual environment (recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
2. **Open the Jupyter Notebook**  
   The main analysis is in the following notebooks:  
   - `Main.ipynb` → Contains most of the tasks.  
   - `Randomized_Simulation.ipynb` → Generates a random DrugBank database of a specified size.  

   To start Jupyter Notebook, run:  
   ```bash
   jupyter notebook
   ```

## **Running the Tests**  
Tests are located in the `tests/` folder. To run them, use:  
```bash
pytest tests/test_drugbank_parser.py
```

## **Dataset Information**  
This project uses a **downloaded subset of 100 drugs** from DrugBank. If you want access to the full dataset, you can find it at:  
👉 **[DrugBank Official Website](https://www.drugbank.com/)**  

## **Project Structure**  
```
├── Main.ipynb                   # Main analysis notebook  
├── Randomized_Simulation.ipynb   # Generates random DrugBank data  
├── project_task.pdf              # Auto-translated project task description  
├── dataframes/                   # Contains processed dataframes  
├── drugbank_partial.xml          # DrugBank dataset (100 drugs)  
├── tests/                         # Folder with test scripts  
│   ├── test_drugbank_parser.py    # Unit tests for the parser  
├── .gitignore                     # Ignored files (cache, venv, etc.)  
├── README.md                      # Project documentation  
```

## **License**  
This project is for educational purposes as part of a Python course.  

