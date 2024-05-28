import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# Definir el valor de k
k = np.log(5 / 3)

def solve_differential_equation():
    try:
        P0 = float(entry_P0.get())
        t_max = float(entry_t_max.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
        return
    
    def model(t, P):
        return k * P

    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, 1000)
    sol = solve_ivp(model, t_span, [P0], t_eval=t_eval)

    plt.figure(figsize=(10, 6))
    plt.plot(sol.t, sol.y[0], label='P(t)')
    plt.xlabel('Tiempo (horas)')
    plt.ylabel('cantida  de computadores')
    plt.title('Solución de la Ecuación Diferencial dP/dt = kP')
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Solución de EDO: dP/dt = kP")

# Crear y posicionar los elementos en la ventana
label_P0 = Label(root, text="Valor inicial de computadores:")
label_P0.grid(row=0, column=0, padx=10, pady=5)
entry_P0 = Entry(root)
entry_P0.grid(row=0, column=1, padx=10, pady=5)

label_t_max = Label(root, text="Tiempo máximo:")
label_t_max.grid(row=1, column=0, padx=10, pady=5)
entry_t_max = Entry(root)
entry_t_max.grid(row=1, column=1, padx=10, pady=5)

button_solve = Button(root, text="Resolver", command=solve_differential_equation)
button_solve.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
