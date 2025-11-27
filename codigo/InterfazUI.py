import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import os
import ply.yacc as yacc
import Analizador_Sintactico
import Analizador_Lexico

# --- Configuración Inicial ---
ctk.set_appearance_mode("Dark")  # Opciones: "System" (estándar), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (estándar), "green", "dark-blue"

class InterpreteApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Intérprete de Código - Proyecto LP")
        self.geometry("1000x700")
        
        # Configuración del Grid Layout principal (2 filas, 1 columna)
        self.grid_rowconfigure(1, weight=2) # El editor ocupa más espacio
        self.grid_rowconfigure(3, weight=1) # El área de resultados ocupa menos
        self.grid_columnconfigure(0, weight=1)

        # === 1. Cabecera y Botones Superiores ===
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        self.label_titulo = ctk.CTkLabel(self.header_frame, text="Editor de Código", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.pack(side="left", padx=10)

        # Botones de acción (usando colores similares a la imagen)
        self.btn_guardar = ctk.CTkButton(self.header_frame, text="Guardar", command=self.guardar_archivo, width=80, fg_color="#333333", hover_color="#444444")
        self.btn_guardar.pack(side="right", padx=5)
        
        self.btn_cargar = ctk.CTkButton(self.header_frame, text="Cargar", command=self.cargar_archivo, width=80, fg_color="#333333", hover_color="#444444")
        self.btn_cargar.pack(side="right", padx=5)

        self.btn_limpiar = ctk.CTkButton(self.header_frame, text="Limpiar", command=self.limpiar_editor, width=80, fg_color="#333333", hover_color="#444444")
        self.btn_limpiar.pack(side="right", padx=5)

        # Botón Ejecutar destacado en azul
        self.btn_ejecutar = ctk.CTkButton(self.header_frame, text="▶ Ejecutar", command=self.ejecutar_analisis, width=100)
        self.btn_ejecutar.pack(side="right", padx=(5, 20))

        # === 2. Área del Editor de Código ===
        # Usamos una fuente monoespaciada para el código
        self.editor_font = ctk.CTkFont(family="Consolas", size=14)
        self.editor_textbox = ctk.CTkTextbox(self, font=self.editor_font, activate_scrollbars=True)
        self.editor_textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        # Texto de ejemplo inicial
        codigo_inicial = """fun main() {
    var nombre : Long = 3  
    println("Hola, $nombre !")        
    print("Conteo:")
    for (i in 0..10) {           
        print(" $i")
    }
}"""
        self.editor_textbox.insert("0.0", codigo_inicial)

        # === 3. Área de Resultados (Consola/Errores) ===
        self.resultados_frame = ctk.CTkFrame(self)
        self.resultados_frame.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")
        
        self.label_resultados = ctk.CTkLabel(self.resultados_frame, text="Resultados del Análisis (Consola / Errores)", anchor="w")
        self.label_resultados.pack(fill="x", padx=10, pady=5)

        # Textbox de solo lectura para mostrar la salida
        self.consola_textbox = ctk.CTkTextbox(self, font=self.editor_font, activate_scrollbars=True, height=150)
        self.consola_textbox.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.consola_textbox.configure(state="disabled") # Inicialmente deshabilitado para lectura


    # --- Funciones de los Botones (Stubs) ---

    def ejecutar_analisis(self):
        """
        Aquí es donde conectarías tu backend de PLY.
        1. Obtienes el texto del editor: self.editor_textbox.get("0.0", "end")
        2. Lo pasas a tu parser.parse(data)
        3. Recoges las listas syntax_errors_list y semantic_errors_list y el symbol_table.
        4. Formateas esa salida y la muestras en la consola inferior.
        """
        # Obtener código del editor
        codigo_fuente = self.editor_textbox.get("0.0", "end")
        
        print(codigo_fuente)
        
        resultado=Analizador_Sintactico.analizar_sintaxis(codigo_fuente)
        syntax_errors_list, semantic_errors_list, symbol_table,lexic_errors_list=resultado
        print( syntax_errors_list, semantic_errors_list, symbol_table,lexic_errors_list)


       
        salida = "\n"
        
        if len(lexic_errors_list)>0:
            salida+= "--- Errores Lexicos ---\n"
            for errores in lexic_errors_list:
                salida+= f"{errores} \n"
        elif len(syntax_errors_list)>0:
            salida+= "--- Errores Sintacticos ---\n"
            for errores in syntax_errors_list:
                salida+= f"{errores} \n"
        elif len(semantic_errors_list)>0:
            salida+= "--- Errores Semanticos ---\n"
            for errores in semantic_errors_list:
                salida+= f"{errores} \n"
        else:
            salida+= "El codigo se encuentra sin errores lexicos, sintaticos y semanticos \n"  
        
        self.mostrar_en_consola(salida)
        print("Ejecutando análisis...")


    def mostrar_en_consola(self, texto):
        # Habilitar temporalmente para insertar texto, luego deshabilitar de nuevo
        self.consola_textbox.configure(state="normal")
        self.consola_textbox.delete("0.0", "end") # Limpiar anterior
        self.consola_textbox.insert("0.0", texto)
        self.consola_textbox.configure(state="disabled")

    def limpiar_editor(self):
        self.editor_textbox.delete("0.0", "end")
        self.mostrar_en_consola("Editor limpiado.")

    def cargar_archivo(self):
        filepath = filedialog.askopenfilename(filetypes=[("Kotlin Files", "*.kt"), ("All Files", "*.*")])
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    content = file.read()
                    self.editor_textbox.delete("0.0", "end")
                    self.editor_textbox.insert("0.0", content)
                self.mostrar_en_consola(f"Archivo cargado: {os.path.basename(filepath)}")
            except Exception as e:
                 self.mostrar_en_consola(f"Error al cargar archivo: {e}")

    def guardar_archivo(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".kt", filetypes=[("Kotlin Files", "*.kt"), ("All Files", "*.*")])
        if filepath:
            try:
                content = self.editor_textbox.get("0.0", "end")
                with open(filepath, 'w') as file:
                    file.write(content)
                self.mostrar_en_consola(f"Archivo guardado en: {filepath}")
            except Exception as e:
                self.mostrar_en_consola(f"Error al guardar archivo: {e}")

if __name__ == "__main__":
    app = InterpreteApp()
    app.mainloop()