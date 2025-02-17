from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

class Expression(BaseModel):
    expression: str

class Calculator:
    def __init__(self):
        self.current_expression = ""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def add_to_expression(self, expression: str):
        self.current_expression += expression
        return self.current_expression

    def evaluate_expression(self, expression: str) -> float:
        try:
            expression = re.sub(r'\s+', '', expression)
            return eval(expression)
        except Exception as e:
            return f"Error: {str(e)}"

    def get_current_expression(self) -> str:
        return self.current_expression

calculator = Calculator()

@app.post("/add")
def add(operation: Operation):
    return {"result": calculator.add(operation.a, operation.b)}

@app.post("/subtract")
def subtract(operation: Operation):
    return {"result": calculator.subtract(operation.a, operation.b)}

@app.post("/multiply")
def multiply(operation: Operation):
    return {"result": calculator.multiply(operation.a, operation.b)}

@app.post("/divide")
def divide(operation: Operation):
    return {"result": calculator.divide(operation.a, operation.b)}

@app.post("/add_to_expression")
def add_to_expression(expression: Expression):
    return {"current_expression": calculator.add_to_expression(expression.expression)}

@app.post("/evaluate_expression")
def evaluate_expression(expression: Expression):
    return {"result": calculator.evaluate_expression(expression.expression)}

@app.get("/get_current_expression")
def get_current_expression():
    return {"current_expression": calculator.get_current_expression()}
