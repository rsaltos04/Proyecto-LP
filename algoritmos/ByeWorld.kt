/*
Prueba hecha por Steve Robinson
Lenguaje de programación de Kotlin
*/
fun funcion() {
    var hola : Boolean = true  
    
    // Comentario
    if( 1 >= 10+10 && 10 < 10-9 || 9*2 == 10/11 && 10 != 9 || 10<=9 && false || 9>0){
        print("
              hola
        ")
    }
    
    while(hola){
        var numero : Double = 10.05
        val mutableList: MutableList<Long> = mutableListOf(12, 10, 20)
        
        for(elemento in mutableList){
			val mapa : MutableMap<String, Long> = mutableMapOf(1, 2)
            print(elemento)
        }
        
        var hola : Boolean = !hola
        var bool: Boolean = hola && hola || hola
       
    }
}
