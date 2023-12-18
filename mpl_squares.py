import  matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4 ,9, 16, 25]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chat title and lavel axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squre of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()