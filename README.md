📊 Multiple Linear Regression Application
This application is a Python-based Multiple Linear Regression tool equipped with simple GUI. It allows users to:
- Upload datasets in CSV format
- Select the dependent variable (Y)
- Select one or more independent variables (X)
- Run a Multiple Linear Regression model
- View results including Intercept, Regression coefficients, and R-Squared (R²) value
- The interface is designed with a clean, modern, rounded UI using tkinter and ttkbootstrap.

🚀 Features
- CSV File Upload, Users can upload a .csv dataset directly from their computer.
- Dynamic Variable Selection, After uploading all column names are automatically detected
- Y variable can be selected from a dropdown and X variables can be selected from a multi-select listbox
- Multiple Linear Regression implemented using:
from sklearn.linear_model import LinearRegression
- Result Display shown in a popup message box, including Intercept (constant), Each X variable’s coefficient, and R-Squared value

📝 Dataset Requirements
To avoid errors, the dataset should:
- Be in .csv format
- Include column headers
- Contain numeric values for Y and X variables
- Not contain missing values (NaN)
If the dataset contains invalid or missing data, the regression may fail.

🛠️ Technologies Used
| Library          | Function                 |
| ---------------- | ------------------------ |
| **pandas**       | Load & process CSV files |
| **scikit-learn** | Regression model         |
| **tkinter**      | Base GUI framework       |
| **ttkbootstrap** | Modern UI styling        |
| **PyInstaller**  | Optional: build `.exe`   |

📊 Example Regression Output


<img width="550" height="400" alt="Screenshot 2025-12-12 082809" src="https://github.com/user-attachments/assets/9826cb45-60a4-4225-9da1-43bc0efcce3c" />


📥 Installation
- Clone this repository
- Install the requirements (run on CMD)
> pip install -r requirements.txt

- Running the app (run on CMD)
> python source/app.py

- (Optional) Making the .exe
> pyinstaller --onefile --windowed source/app.py

your .exe will be generated inside "dist/"

	
👤 Author
- Imam Nuur Wahid
- Developed for academic and learning purposes.
