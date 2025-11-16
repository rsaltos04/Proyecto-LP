fun main() {
    var nombre : String = "Reynaldo"        
    println("Hola, $nombre !")        
    print("Conteo:")
    for (i in 0..10) {           
        print(" $i")
        if (i%2==0){
          println(" Par")
        }else {
          println(" Impar")
        }
    }
    val sum: (Int) -> Int = { x: Int, y: Int -> x }
}
// Prueba de Jefferson Saltos

