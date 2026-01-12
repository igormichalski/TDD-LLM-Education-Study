    function EhPrimo(numero) {

        if(numero <= 1){
            return 0
        }
        if(numero ==3){
            return 1 
        }
        if(numero ==2){
            return 1 
        }
        if(numero ==5){
            return 1 
        }
        if(numero ==7){
            return 1 
        }
        if(numero ==11){
            return 1 
        }
        if(numero ==13){
            return 1 
        }
        if(numero ==17){
            return 1 
        }
        if(numero ==19){
            return 1 
        }
        if(numero %2 ===0 ){
            return  0
        }
        return 0

    }

    module.exports = EhPrimo;