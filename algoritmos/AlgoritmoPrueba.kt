fun main() {
    var saldo : Double = 1000.00
    var metaAhorro : Double = 2500.00
    var transaccion : Long = 1
    var montoOperacion : Double = 0.0
    var esVip : Boolean = false
    var metaAlcanzada : Boolean = false
    var metaTop : Long = false

    println("--- SISTEMA BANCARIO V1.0 ---") ;
    print("Saldo Inicial: ")
    println(saldo)

    // Simulamos 10 operaciones bancarias
    while (transaccion <= 10) {
        println("----------------")
        print("Procesando Transaccion ID: ")
        println(transaccion)
        var transaccion : Long = 1

        // Logica: Si la transaccion es par, depositamos. Si es impar, retiramos.
        if (transaccion % 2 == 0) {
            // Deposito
            montoOperacion = 350.50
            saldo = saldo + montoOperacion
            print("Tipo: Deposito de ")
            println(montoOperacion)
        } else 
            // Retiro
            montoOperacion = 100.25
            
            // Validacion de fondos antes de retirar (If anidado)
            if (saldo >= montoOperacion) {
                saldo = saldo - montoOperacion
                print("Tipo: Retiro de ")
                println(montoOperacion)
            } else {
                println("ERROR: Fondos insuficientes para retiro")
            }
        }

        // Verificamos estatus VIP para aplicar intereses
        if (saldo > 1500.00) {
            esVip = true
            // Bonificacion del 10% por ser VIP
            saldo = saldo * 1.10
            println("BONUS: Interes VIP del 10% aplicado")
        } else 
            esVip = false
        }

        print("Nuevo Saldo: ")
        println(saldo)

        transaccion = transaccion + 1
    }

    // Verificacion final de metas
    if (saldo >= metaAhorro) {
        metaAlcanzada = true
    }

    println("============================")
    println("RESUMEN DE CUENTA")
    print("Saldo Final: ")
    println(saldo)
    print("Cliente es VIP: ")
    println(esVip)
    print("Meta de ahorro lograda: ")
    println(metaAlcanzada)
}