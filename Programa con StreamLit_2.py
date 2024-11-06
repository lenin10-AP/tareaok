import streamlit as st
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

st.title("Resolución de Ejercicios de Programación Lineal y Entera con Streamlit")

# --- Ejercicio 8.1 ---
st.header("Ejercicio 8.1: Método de Branch and Bound")
st.write("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
4x_1 + 2x_2 + x_3 &\leq 10 \\
3x_1 + 4x_2 + 2x_3 &\leq 14 \\
2x_1 + x_2 + 3x_3 &\leq 7 \\
x_1, x_2, x_3 &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.1"):
    # Definir el problema
    prob_8_1 = LpProblem("Ejercicio_8_1", LpMaximize)
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    x3 = LpVariable("x3", lowBound=0, cat="Integer")

    # Función objetivo
    prob_8_1 += 4 * x1 + 3 * x2 + 3 * x3

    # Restricciones
    prob_8_1 += 4 * x1 + 2 * x2 + x3 <= 10
    prob_8_1 += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob_8_1 += 2 * x1 + x2 + 3 * x3 <= 7

    # Resolver el problema
    prob_8_1.solve()
    st.write("*Solución:*")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}, x3 = {x3.varValue}")
    st.write(f"Valor de la función objetivo: P = {prob_8_1.objective.value()}")

# --- Ejercicio 8.2 ---
st.header("Ejercicio 8.2: Resolución como un Problema de Programación Entera")
st.write("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
4x_1 + 2x_2 + x_3 &\leq 10 \\
3x_1 + 4x_2 + 2x_3 &\leq 14 \\
2x_1 + x_2 + 3x_3 &\leq 7 \\
x_1, x_2, x_3 &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.2"):
    # Definir el problema
    prob_8_2 = LpProblem("Ejercicio_8_2", LpMaximize)
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    x3 = LpVariable("x3", lowBound=0, cat="Integer")

    # Función objetivo
    prob_8_2 += 4 * x1 + 3 * x2 + 3 * x3

    # Restricciones
    prob_8_2 += 4 * x1 + 2 * x2 + x3 <= 10
    prob_8_2 += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob_8_2 += 2 * x1 + x2 + 3 * x3 <= 7

    # Resolver el problema
    prob_8_2.solve()
    st.write("*Solución del problema de programación entera:*")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}, x3 = {x3.varValue}")
    st.write(f"Valor de la función objetivo: P = {prob_8_2.objective.value()}")

# --- Ejercicio 8.3 ---
st.header("Ejercicio 8.3: Método de Cortes de Gomory")
st.write("Minimizar C(x, y) = x - y sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
3x + 4y &\leq 6 \\
x - y &\leq 1 \\
x, y &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.3"):
    # Definir el problema
    prob_8_3 = LpProblem("Ejercicio_8_3", LpMinimize)
    x = LpVariable("x", lowBound=0, cat="Integer")
    y = LpVariable("y", lowBound=0, cat="Integer")

    # Función objetivo
    prob_8_3 += x - y

    # Restricciones
    prob_8_3 += 3 * x + 4 * y <= 6
    prob_8_3 += x - y <= 1

    # Resolver el problema
    prob_8_3.solve()
    st.write("*Solución relajada:*")
    st.write(f"x = {x.varValue}, y = {y.varValue}")
    st.write(f"Valor de la función objetivo: C = {prob_8_3.objective.value()}")

# --- Ejercicio 8.4 ---
st.header("Ejercicio 8.4: Método de Cortes de Gomory")
st.write("Maximizar P(x1, x2, x3) = 4x1 + 3x2 + 3x3 sujeto a las restricciones:")
st.latex(r"""
\begin{align*}
4x_1 + 2x_2 + x_3 &\leq 10 \\
3x_1 + 4x_2 + 2x_3 &\leq 14 \\
2x_1 + x_2 + 3x_3 &\leq 7 \\
x_1, x_2, x_3 &\geq 0, \text{ enteros}
\end{align*}
""")

if st.button("Resolver Ejercicio 8.4"):
    # Definir el problema
    prob_8_4 = LpProblem("Ejercicio_8_4", LpMaximize)
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")
    x3 = LpVariable("x3", lowBound=0, cat="Integer")

    # Función objetivo
    prob_8_4 += 4 * x1 + 3 * x2 + 3 * x3

    # Restricciones
    prob_8_4 += 4 * x1 + 2 * x2 + x3 <= 10
    prob_8_4 += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob_8_4 += 2 * x1 + x2 + 3 * x3 <= 7

    # Resolver el problema
    prob_8_4.solve()
    st.write("*Solución relajada del ejercicio 8.4:*")
    st.write(f"x1 = {x1.varValue}, x2 = {x2.varValue}, x3 = {x3.varValue}")
    st.write(f"Valor de la función objetivo: P = {prob_8_4.objective.value()}")

# --- Ejercicio 8.5 ---
st.header("Ejercicio 8.5: Selección de Proyectos de I+D")
st.write("Maximizar el NPV sujeto a las restricciones de presupuesto para cada año.")

if st.button("Resolver Ejercicio 8.5"):
    # Definir el problema
    prob_8_5 = LpProblem("Ejercicio_8_5", LpMaximize)
    projects = ["P1", "P2", "P3", "P4", "P5", "P6"]
    npv_values = [141, 187, 121, 85, 262, 127]
    capital_requirements = [
        [75, 90, 60, 85, 100, 50],
        [25, 35, 15, 25, 30, 20],
        [20, 0, 15, 0, 20, 10],
        [15, 50, 15, 0, 20, 30],
        [10, 30, 15, 0, 20, 40]
    ]
    budgets = [250, 75, 50, 50, 50]

    # Variables binarias para seleccionar proyectos
    decision_vars = {project: LpVariable(project, cat="Binary") for project in projects}

    # Función objetivo
    prob_8_5 += lpSum([npv_values[i] * decision_vars[projects[i]] for i in range(len(projects))])

    # Restricciones de presupuesto por año
    for i in range(len(budgets)):
        prob_8_5 += lpSum([capital_requirements[i][j] * decision_vars[projects[j]] for j in range(len(projects))]) <= budgets[i]

    # Resolver el problema
    prob_8_5.solve()
    st.write("*Proyectos seleccionados:*")
    for project in projects:
        st.write(f"{project}: {'Seleccionado' if decision_vars[project].varValue == 1 else 'No seleccionado'}")

    st.write(f"**Valor total de NPV:** {prob_8_5.objective.value()}")
