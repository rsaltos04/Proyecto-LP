class Coche(val marca: String, var color: String) {
    
    val marca: String = "Toyota"
    var color: String = "Rojo"

    // Método
    fun arrancar() {
        println("El coche $marca de color $color está arrancando...")
    }

    val PI: Float = 3.14159
    var contador: Int = 0
    var mensaje: String = "Inicializando..."

    var x: Int = 10 + 5 * 2
    var y: Int = x / 3
    var z: Int = 10 % 3

    var estaListo: Boolean = true
    var puedeProcesar: Boolean = x > 10 && ! estaListo || y == 3

    fun sumarNumeros(a: Int, b: Int) {
        var resultado: Int = a + b
        return resultado
    }
}

var suma: Int = sumarNumeros(x, y)
println(suma)

print("Test print")
println() // Prueba

// Definición de clase
class Usuario(val username: String, var nivel: Int) {
    
    // Propiedades dentro de la clase
    var estaActivo: Boolean = true
    
    // Método dentro de la clase
    fun promover() {
        var nivel : Int = nivel + 1
        println("¡Promovido!")
    }
}

if (puedeProcesar) {
    println("Procesando...")
    var contador: Int = contador + 1
} else if (y == 3) {
    println("Esperando...")
} else {
    println("Error.")
}

while (contador < 5) {
    print(contador)
    var contador: Int = contador + 1
}

for (i in 0 .. 10) {
    println(i)
}

var admin: Usuario = Usuario("admin_user", 99)

var listaUsuarios: MutableList<Usuario> = obtenerUsuarios()
var puntajes: MutableMap<String, Int> = obtenerPuntajes()

for (usuario in listaUsuarios) {
    println(usuario) // Asume que 'usuario' se puede imprimir
}

println("Ingresa tu nombre:")
var nombre: String = readln()
println("Hola, ")
println(nombre)