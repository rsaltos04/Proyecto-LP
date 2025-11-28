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

       # === 2. Área del Editor de Código (MODIFICADO PARA LINE NUMBERS) ===
        self.editor_font = ctk.CTkFont(family="Consolas", size=14)

        # ### NUEVO: Frame contenedor para agrupar números y editor
        self.editor_container = ctk.CTkFrame(self)
        self.editor_container.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        # Configurar el grid del contenedor
        self.editor_container.grid_columnconfigure(0, weight=0) # Columna de números (fija)
        self.editor_container.grid_columnconfigure(1, weight=1) # Columna de código (expandible)
        self.editor_container.grid_rowconfigure(0, weight=1)

        # ### NUEVO: Textbox para los números de línea
        # Desactivamos scrollbar propio, color de fondo diferente, texto gris
        self.line_numbers = ctk.CTkTextbox(
            self.editor_container, 
            width=40, 
            font=self.editor_font,
            fg_color="#2b2b2b", # Un poco más claro o diferente que el editor
            text_color="#888888",
            activate_scrollbars=False 
        )
        self.line_numbers.grid(row=0, column=0, sticky="ns")
        self.line_numbers.insert("0.0", "1")
        self.line_numbers.configure(state="disabled") # Solo lectura

        # Editor principal
        self.editor_textbox = ctk.CTkTextbox(
            self.editor_container, 
            font=self.editor_font, 
            activate_scrollbars=True
        )
        self.editor_textbox.grid(row=0, column=1, sticky="nsew")

        # ### NUEVO: Sincronización de eventos
        # 1. Cuando escribimos, actualizamos los números
        self.editor_textbox.bind("<KeyRelease>", self.actualizar_numeros_linea)
        self.editor_textbox.bind("<Return>", self.actualizar_numeros_linea)
        self.editor_textbox.bind("<BackSpace>", self.actualizar_numeros_linea)
        self.editor_textbox.bind("<<Paste>>", self.actualizar_numeros_linea)
        self.editor_textbox.bind("<Button-1>", self.actualizar_numeros_linea) # Click

        # 2. Sincronizar el Scroll (Esto es un poco avanzado, accedemos al widget interno de tkinter)
        # Obtenemos la función de scroll original del CTKTextbox
        self._orig_yview_command = self.editor_textbox._textbox['yscrollcommand']
        
        # Configuramos una función proxy que mueva ambos
        self.editor_textbox._textbox.configure(yscrollcommand=self._on_scroll_text)
        
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
        self.actualizar_numeros_linea() # Llamada inicial

        # === 3. Área de Resultados ===
        self.resultados_frame = ctk.CTkFrame(self)
        self.resultados_frame.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")
        
        self.label_resultados = ctk.CTkLabel(self.resultados_frame, text="Resultados del Análisis (Consola / Errores)", anchor="w")
        self.label_resultados.pack(fill="x", padx=10, pady=5)

        self.consola_textbox = ctk.CTkTextbox(self, font=self.editor_font, activate_scrollbars=True, height=150)
        self.consola_textbox.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.consola_textbox.configure(state="disabled")

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
        syntax_errors_list, semantic_errors_list, symbol_table=resultado
        print( syntax_errors_list, semantic_errors_list, symbol_table)
        lexic_errors_list=Analizador_Lexico.lexic_errors_list
        Analizador_Lexico.lexic_errors_list=[]

       
        salida = "\n"
        
        if len(lexic_errors_list)>0:
            salida+= "--- Errores Lexicos ---\n"
            for errores in lexic_errors_list:
                salida+= f"{errores} \n"
        if len(syntax_errors_list)>0:
            salida+= "--- Errores Sintacticos ---\n"
            for errores in syntax_errors_list:
                salida+= f"{errores} \n"
        if len(semantic_errors_list)>0:
            salida+= "--- Errores Semanticos ---\n"
            for errores in semantic_errors_list:
                salida+= f"{errores} \n"
        if len(semantic_errors_list)==0 and len(syntax_errors_list)==0 and len(lexic_errors_list)==0:
            salida+= "El codigo se encuentra sin errores lexicos, sintaticos y semanticos \n"  
        
        self.mostrar_en_consola(salida)
        print("Ejecutando análisis...")



    def _on_scroll_text(self, *args):
        """
        Función Proxy para sincronizar el scroll.
        Mueve la barra de números cuando se mueve el editor.
        """
        # 1. Mover la vista de los números
        self.line_numbers._textbox.yview_moveto(args[0])
        
        # 2. Ejecutar el scroll original del editor
        if self._orig_yview_command:
            # CORRECCIÓN: Verificar si es una cadena (comando Tcl) o una función
            if isinstance(self._orig_yview_command, str):
                # Si es string, usamos tk.call para ejecutar el comando interno de Tcl
                self.editor_textbox._textbox.tk.call(self._orig_yview_command, *args)
            else:
                # Si es función, la llamamos normalmente
                self._orig_yview_command(*args)



    def actualizar_numeros_linea(self, event=None):
        """
        ### NUEVO: Recalcula las líneas y actualiza la columna izquierda.
        """
        # Obtener el contenido
        codigo = self.editor_textbox.get("0.0", "end")
        
        # Contar líneas (la última línea siempre es vacía en tkinter, restamos 1 si es necesario visualmente)
        # Usamos int(self.editor_textbox.index('end-1c').split('.')[0]) para obtener el índice real de la última línea
        try:
            numero_lineas = int(self.editor_textbox.index('end-1c').split('.')[0])
        except:
            numero_lineas = 1

        # Generar string de números "1\n2\n3..."
        line_string = "\n".join(str(i) for i in range(1, numero_lineas + 1))
        
        # Actualizar widget de números
        self.line_numbers.configure(state="normal")
        self.line_numbers.delete("0.0", "end")
        self.line_numbers.insert("0.0", line_string)
        self.line_numbers.configure(state="disabled")
        
        # Asegurar que la vista esté sincronizada después de actualizar
        # (Por si se agregaron líneas y el scroll cambió)
        self.line_numbers._textbox.yview_moveto(self.editor_textbox._textbox.yview()[0])

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