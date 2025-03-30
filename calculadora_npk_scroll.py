import tkinter as tk
from tkinter import ttk, messagebox, Scrollbar, Canvas, Frame

def calcular():
    try:
        n_recomendado = float(entry_n.get() or 0)
        p_recomendado = float(entry_p.get() or 0)
        k_recomendado = float(entry_k.get() or 0)

        n_fert = float(entry_n_fert.get() or 0) / 100
        p_fert = float(entry_p_fert.get() or 0) / 100
        k_fert = float(entry_k_fert.get() or 0) / 100

        if n_fert == 0 or p_fert == 0 or k_fert == 0:
            messagebox.showerror("Erro", "A composição do fertilizante não pode ter 0% em nenhum nutriente!")
            return

        qtd_n = n_recomendado / n_fert
        qtd_p = (p_recomendado / 0.437) / p_fert
        qtd_k = (k_recomendado / 0.830) / k_fert

        if any(qtd < 0 for qtd in [qtd_n, qtd_p, qtd_k]):
            messagebox.showerror("Erro", "Valores negativos não são permitidos!")
            return

        qtd_fertilizante = max(qtd_n, qtd_p, qtd_k)
        
        resultado_label.config(text=f"Quantidade total: {qtd_fertilizante:.2f} kg/ha")
        resultado_individual_n.config(text=f"{qtd_n:.2f} kg/ha")
        resultado_individual_p.config(text=f"{qtd_p:.2f} kg/ha")
        resultado_individual_k.config(text=f"{qtd_k:.2f} kg/ha")

        valor_n = float(entry_n_fert.get())
        if valor_n < 4:
            resultado_nitrogenio.config(text="Baixo", fg="red")
        elif 4 <= valor_n <= 9:
            resultado_nitrogenio.config(text="Médio", fg="orange")
        else:
            resultado_nitrogenio.config(text="Alto", fg="green")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos!")

def avaliar_nutrientes():
    try:
        fosforo = float(entry_fosforo.get() or 0)
        potassio = float(entry_potassio.get() or 0)
        nitrogenio = float(entry_nitrogenio.get() or 0)
        tipo_solo = combo_tipo_solo.get()

        if tipo_solo == "Solo Argiloso":
            if nitrogenio < 6:
                classificacao_n = "Baixo"
            elif 6 <= nitrogenio <= 12:
                classificacao_n = "Médio"
            else:
                classificacao_n = "Alto"
        elif tipo_solo == "Solo Arenoso":
            if nitrogenio < 3:
                classificacao_n = "Baixo"
            elif 3 <= nitrogenio <= 8:
                classificacao_n = "Médio"
            else:
                classificacao_n = "Alto"
        elif tipo_solo == "Solo Siltoso":
            if nitrogenio < 4:
                classificacao_n = "Baixo"
            elif 4 <= nitrogenio <= 9:
                classificacao_n = "Médio"
            else:
                classificacao_n = "Alto"
        else:
            classificacao_n = "Indefinido"

        if tipo_solo == "Solo Argiloso":
            if fosforo < 6:
                classificacao_p = "Baixo"
            elif 6 <= fosforo <= 10:
                classificacao_p = "Médio"
            else:
                classificacao_p = "Alto"
        elif tipo_solo == "Solo Arenoso":
            if fosforo < 4:
                classificacao_p = "Baixo"
            elif 4 <= fosforo <= 8:
                classificacao_p = "Médio"
            else:
                classificacao_p = "Alto"
        elif tipo_solo == "Solo Siltoso":
            if fosforo < 5:
                classificacao_p = "Baixo"
            elif 5 <= fosforo <= 9:
                classificacao_p = "Médio"
            else:
                classificacao_p = "Alto"
        else:
            classificacao_p = "Indefinido"

        if tipo_solo == "Solo Argiloso":
            if potassio < 15:
                classificacao_k = "Baixo"
            elif 15 <= potassio <= 25:
                classificacao_k = "Médio"
            else:
                classificacao_k = "Alto"
        elif tipo_solo == "Solo Arenoso":
            if potassio < 12:
                classificacao_k = "Baixo"
            elif 12 <= potassio <= 20:
                classificacao_k = "Médio"
            else:
                classificacao_k = "Alto"
        elif tipo_solo == "Solo Siltoso":
            if potassio < 10:
                classificacao_k = "Baixo"
            elif 10 <= potassio <= 18:
                classificacao_k = "Médio"
            else:
                classificacao_k = "Alto"
        else:
            classificacao_k = "Indefinido"

        analise_label.config(
            text=f"Fósforo: {classificacao_p}\nPotássio: {classificacao_k}\nNitrogênio: {classificacao_n}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def limpar_campos():

    entry_n.delete(0, 'end')
    entry_p.delete(0, 'end')
    entry_k.delete(0, 'end')
    entry_n_fert.delete(0, 'end')
    entry_p_fert.delete(0, 'end')
    entry_k_fert.delete(0, 'end')
    entry_fosforo.delete(0, 'end')
    entry_potassio.delete(0, 'end')
    entry_nitrogenio.delete(0, 'end')
    
    combo_tipo_solo.current(0)
    combo_adubacao_organica.current(0)
    
    resultado_label.config(text='')
    resultado_individual_n.config(text='0.00 kg/ha')
    resultado_individual_p.config(text='0.00 kg/ha')
    resultado_individual_k.config(text='0.00 kg/ha')
    resultado_nitrogenio.config(text='')
    analise_label.config(text='')

root = tk.Tk()
root.title("Calculadora de Fertilizante")
root.geometry("800x600")
root.configure(bg="#f4f4f4")

container = Frame(root)
canvas = Canvas(container, bg="#f4f4f4")
scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#f4f4f4")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

container.pack(fill="both", expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

main_frame = scrollable_frame

left_frame = tk.Frame(main_frame, bg="#f4f4f4")
left_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

right_frame = tk.Frame(main_frame, bg="#f4f4f4")
right_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

frame_tipo_solo = tk.LabelFrame(left_frame, text="Tipo de Solo", bg="white", padx=10, pady=10)
frame_tipo_solo.pack(fill="x", padx=5, pady=5)

tk.Label(frame_tipo_solo, text="Selecione o tipo de solo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
combo_tipo_solo = ttk.Combobox(frame_tipo_solo, values=["Solo Argiloso", "Solo Arenoso", "Solo Siltoso"], state="readonly")
combo_tipo_solo.grid(row=0, column=1, padx=5, pady=5)
combo_tipo_solo.current(0)

frame_adubacao_organica = tk.LabelFrame(left_frame, text="Adubação Orgânica", bg="white", padx=10, pady=10)
frame_adubacao_organica.pack(fill="x", padx=5, pady=5)

tk.Label(frame_adubacao_organica, text="Selecione o tipo de adubação orgânica:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
combo_adubacao_organica = ttk.Combobox(frame_adubacao_organica, values=[
    "Esterco bovino curtido", "Esterco de galinha", "Esterco de porco",
    "Composto de lixo", "Lodo de esgoto", "Composto com lodo de esgoto",
    "Vinhaça in natura", "Torta de mamona"
], state="readonly")
combo_adubacao_organica.grid(row=0, column=1, padx=5, pady=5)
combo_adubacao_organica.current(0)

frame_npk = tk.LabelFrame(left_frame, text="Recomendação de NPK (kg/ha)", bg="white", padx=10, pady=10)
frame_npk.pack(fill="x", padx=5, pady=5)

tk.Label(frame_npk, text="Nitrogênio (N):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_n = tk.Entry(frame_npk)
entry_n.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_npk, text="Fósforo (P):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_p = tk.Entry(frame_npk)
entry_p.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_npk, text="Potássio (K):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_k = tk.Entry(frame_npk)
entry_k.grid(row=2, column=1, padx=5, pady=5)

frame_fertilizante = tk.LabelFrame(left_frame, text="Composição do Fertilizante (%)", bg="white", padx=10, pady=10)
frame_fertilizante.pack(fill="x", padx=5, pady=5)

tk.Label(frame_fertilizante, text="Nitrogênio (N):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_n_fert = tk.Entry(frame_fertilizante)
entry_n_fert.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_fertilizante, text="Fósforo (P):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_p_fert = tk.Entry(frame_fertilizante)
entry_p_fert.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_fertilizante, text="Potássio (K):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_k_fert = tk.Entry(frame_fertilizante)
entry_k_fert.grid(row=2, column=1, padx=5, pady=5)

resultado_nitrogenio = tk.Label(frame_fertilizante, text="", font=("Arial", 10, "bold"), bg="white")
resultado_nitrogenio.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

frame_avaliacao = tk.LabelFrame(left_frame, text="Avaliação dos Nutrientes", bg="white", padx=10, pady=10)
frame_avaliacao.pack(fill="x", padx=5, pady=5)

tk.Label(frame_avaliacao, text="Fósforo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_fosforo = tk.Entry(frame_avaliacao)
entry_fosforo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_avaliacao, text="Potássio:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_potassio = tk.Entry(frame_avaliacao)
entry_potassio.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_avaliacao, text="Nitrogênio:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_nitrogenio = tk.Entry(frame_avaliacao)
entry_nitrogenio.grid(row=2, column=1, padx=5, pady=5)

analise_label = tk.Label(frame_avaliacao, text="", font=("Arial", 10, "bold"), bg="white")
analise_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

btn_frame = tk.Frame(left_frame, bg="#f4f4f4")
btn_frame.pack(fill="x", padx=5, pady=5)

btn_calcular = tk.Button(btn_frame, text="Calcular Fertilizante", command=calcular, bg="#008CBA", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(fill="x", pady=5)

btn_avaliar = tk.Button(btn_frame, text="Avaliar Nutrientes", command=avaliar_nutrientes, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_avaliar.pack(fill="x", pady=5)

btn_limpar = tk.Button(btn_frame, text="Limpar", command=limpar_campos, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
btn_limpar.pack(fill="x", pady=5)

resultado_label = tk.Label(left_frame, text="", font=("Arial", 12, "bold"), bg="#f4f4f4")
resultado_label.pack(padx=5, pady=10)

frame_calculo_individual = tk.LabelFrame(right_frame, text="Cálculo Individual de Nutrientes", bg="white", padx=10, pady=10)
frame_calculo_individual.pack(fill="both", expand=True, padx=5, pady=5)

frame_n = tk.Frame(frame_calculo_individual, bg="white")
frame_n.pack(fill="x", padx=5, pady=5)

tk.Label(frame_n, text="Nitrogênio (N):", bg="white").pack(side="left", padx=5, pady=5)
resultado_individual_n = tk.Label(frame_n, text="0.00 kg/ha", bg="white", font=("Arial", 10, "bold"))
resultado_individual_n.pack(side="right", padx=5, pady=5)

frame_p = tk.Frame(frame_calculo_individual, bg="white")
frame_p.pack(fill="x", padx=5, pady=5)

tk.Label(frame_p, text="Fósforo (P):", bg="white").pack(side="left", padx=5, pady=5)
resultado_individual_p = tk.Label(frame_p, text="0.00 kg/ha", bg="white", font=("Arial", 10, "bold"))
resultado_individual_p.pack(side="right", padx=5, pady=5)

frame_k = tk.Frame(frame_calculo_individual, bg="white")
frame_k.pack(fill="x", padx=5, pady=5)

tk.Label(frame_k, text="Potássio (K):", bg="white").pack(side="left", padx=5, pady=5)
resultado_individual_k = tk.Label(frame_k, text="0.00 kg/ha", bg="white", font=("Arial", 10, "bold"))
resultado_individual_k.pack(side="right", padx=5, pady=5)

frame_formulas = tk.LabelFrame(right_frame, text="Fórmulas Utilizadas", bg="white", padx=10, pady=10)
frame_formulas.pack(fill="x", padx=5, pady=5)

tk.Label(frame_formulas, 
        text="Nitrogênio: Qtd = N_recomendado / %N_fertilizante\n"
             "Fósforo: Qtd = (P_recomendado / 0.437) / %P_fertilizante\n"
             "Potássio: Qtd = (K_recomendado / 0.830) / %K_fertilizante",
        bg="white", justify="left").pack(anchor="w", padx=5, pady=5)

root.mainloop()