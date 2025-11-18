val PI: Double = 3.14159
var contador: Long = 0
var mensaje: String = "Inicializando..."

var x: Long = 10 + 5 * 2
var y: Long = x / 3
var z: Long = 10 % 3

var estaListo: Boolean = true
var puedeProcesar: Boolean = x > 10 && !estaListo || y == 3

if (puedeProcesar) {
    println("Procesando...")
    contador = contador + 1
} else if (y == 3) {
    println("Esperando...")
} else {
    println("Error.")
}

while (contador < 5) {
    print(contador)
    contador = contador + 1
}

for (i in 0 .. 10) {
    println(i)
}

fun sumarNumeros(a: Long, b: Long) {
    var resultado: Long = a + b
    return resultado
}

var suma: Long = sumarNumeros(x, y)
println(suma)

print("Test print")
println() 

class Usuario(val username: String, var nivel: Long) {
    
    // Propiedades dentro de la clase
    var estaActivo: Boolean = true
    
    // Método dentro de la clase
    fun promover() {
        nivel = nivel + 1
        println("¡Promovido!")
    }
}

var admin: Usuario = Usuario("admin_user", 99)

var listaUsuarios: MutableList<Usuario> = obtenerUsuarios()
var puntajes: MutableMap<String, Long> = obtenerPuntajes()
var numero : Long = 10

for (usuario in listaUsuarios) {
    println(usuario) // Asume que 'usuario' se puede imprimir
}

println("Ingresa tu nombre:")
var nombre: String = readln()
println("Hola, ", "chao")
println(nombre)
print(a)
print("Hola", "chao")