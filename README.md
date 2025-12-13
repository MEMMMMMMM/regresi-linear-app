## 📥 Installation
- Download 'app.exe' here :
> https://github.com/MEMMMMMMM/regresi-linear-app/releases/download/2.0/app.exe


- Run the 'app.exe'
- (Optional) Download 'dataset_example.csv' for testing 

## 📊 Multiple Linear Regression Application
A desktop application built in Python that performs Multiple Linear Regression (MLR) with a clean interface (GUI). The tool is designed for students, researchers, and analysts who want a simple way to run regression without writing code. MLR is a statistical method used to model the relationship between one dependent variable and two or more independent variables. MLR is commonly used for predicting outcomes (e.g., income, revenue, performance scores), measuring variable influence (e.g., how work hours affect income), testing hypotheses using t-tests and F-tests, and identifying significant predictors in a model.

## 🚀 Key Features
> 📁 CSV File Upload
- Load dataset (.csv) directly from your computer
- Automatically detects and displays all column names
> 🔽 Dynamic Variable Selection
- Choose Y (dependent variable) from a dropdown
- Select one or more X variables from a multi-select listbox
> 📐 Optional Transformations
- Apply natural logarithm ln(Y) and ln(X variables)
- Useful for handling skewed data or exponential relationships.
> 🧪 Statistical Controls
- Input custom alpha (α) for significance testing
- p-value evaluation shown as Good (if p < α) and Bad (if p ≥ α)
> 📈 Complete Regression Output
- Output includes Intercept, Regression coefficients, t-values, p-values, R², Adjusted R², F-statistic, F p-value, Sample size (n), and Indicators of variable significance

## 📝 Dataset Requirements
To avoid errors, the dataset should:
- Be in .csv format
- Include column headers
- Contain numeric values for Y and X variables
- Not contain missing values (NaN)
If the dataset contains invalid or missing data, the regression may fail.

## 🛠️ Technologies Used
| Library          | Function                 |
| ---------------- | ------------------------ |
| **pandas**       | Load & process CSV files |
| **scikit-learn** | Regression model         |
| **tkinter**      | Base GUI framework       |
| **ttkbootstrap** | Modern UI styling        |
| **numpy**		   | mathematical operations  |
| **scipy**		   | t-test & F-test		  |


## 📊 Example Regression Output


<img width="418" height="389" alt="Screenshot 2025-12-13 101735" src="https://github.com/user-attachments/assets/4c312e9d-ccd4-4af9-82b9-845d13c9796d" />


	
## 👤 Author
- Imam Nuur Wahid
- Developed for academic and learning purposes.
