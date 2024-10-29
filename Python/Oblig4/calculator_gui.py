import tkinter as tk
from calculator import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.calculator = Calculator()
        
        # Configure window
        root.title("Calculator")
        root.geometry("300x380")
        
        # Operand 1
        operand1_label = tk.Label(root, text="Operand 1")
        operand1_label.place(x=10, y=10)
        self.operand1_entry = tk.Entry(root, width=25)
        self.operand1_entry.place(x=100, y=10)

        # Operator
        operator_label = tk.Label(root, text="Operator")
        operator_label.place(x=10, y=40)
        self.operator_entry = tk.Entry(root, width=25)
        self.operator_entry.place(x=100, y=40)

        # Operand 2
        operand2_label = tk.Label(root, text="Operand 2")
        operand2_label.place(x=10, y=70)
        self.operand2_entry = tk.Entry(root, width=25)
        self.operand2_entry.place(x=100, y=70)

        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.place(x=10, y=100)

        # Clear log button
        self.clear_log_button = tk.Button(root, text="Clear log", command=self.clear_log)
        self.clear_log_button.place(x=100, y=100)

        # Quit button
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.place(x=200, y=100)

        # Result Label
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.place(x=10, y=130)

        # Log Text Box
        self.log_label = tk.Label(root, text="Log")
        self.log_label.place(x=10, y=160)
        self.log_text = tk.Text(root, height=10, width=30)
        self.log_text.place(x=10, y=180)

    def calculate(self):
        try:
            operand1 = float(self.operand1_entry.get())
            operand2 = float(self.operand2_entry.get())
            operator = self.operator_entry.get()
            result = self.calculator.calculate(operand1, operand2, operator)
            self.result_label.config(text=f"Result: {result}")

            # Update log display
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "\n".join(self.calculator.get_log()))
        except ValueError:
            self.result_label.config(text="Please enter valid numbers.")
        self.operand1_entry.delete(0, tk.END)
        self.operand2_entry.delete(0, tk.END)
        self.operator_entry.delete(0, tk.END)


    def clear_log(self):
        self.calculator.clear_log()
        self.log_text.delete(1.0, tk.END)
        self.result_label.config(text="Result:")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
