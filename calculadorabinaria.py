import tkinter as tk #importa a biblioteca

#cria a janela principal
janela = tk.Tk()
janela.title('Calculadora Binário ⇄ Decimal')
janela.geometry("300x200") #largura x altura

#cria o campo de entrada
entrada = tk.Entry(janela)
entrada.pack(pady=10)

#cria o campo onde o resultado vai aparecer
resultado = tk.Label(janela,text="")
resultado.pack(pady=10)

#binário -> decimal
def binario_para_decimal():
    try:
        numero_binario = entrada.get()
        decimal = int(numero_binario,2)
        resultado.config(text=f'Decimal: {decimal}')
    except ValueError:
        resultado.config(text="Entrada Invalida.")


#decimal -> binário
def decimal_para_binario():
    try:
        numero_decimal = int(entrada.get())
        binario = bin(numero_decimal)[2:]
        resultado.config(text=F'Binário: {binario}')
    except ValueError:
        resultado.config(text='Entrada inválida')

#cria os botões que chamam as funções
botao_bin_para_dec = tk.Button(janela, text="Binário → Decimal", command=binario_para_decimal)
botao_bin_para_dec.pack(pady=5)

botao_dec_para_bin = tk.Button(janela, text="Decimal → Binário", command=decimal_para_binario)
botao_dec_para_bin.pack(pady=5)

janela.mainloop()