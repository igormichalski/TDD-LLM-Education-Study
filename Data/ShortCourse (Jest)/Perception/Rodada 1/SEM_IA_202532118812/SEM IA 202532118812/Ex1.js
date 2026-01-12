function MDC(a,b) {
    let y = 1

        if(a%1 !== 0 || b%1 !== 0){
            return 'ERRO'
        }
        if(typeof(a) !==  "number" && typeof(b) !== "number"){
            return 'ERRO'
        }
        do {
            if ( a%2 === 0 || b%2 === 0){
                if (a%2 === 0) {
                    a = a/2
                }
                if (b%2 === 0) {
                    b = b/2
                }
                if( a%2 === 0 && b%2 === 0) {
                    y = y*2
                }
                if ( a%3 === 0 || b%3 === 0){
                if (a%3 === 0) {
                    a = a/3
                }
                if (b%3 === 0) {
                    b = b/3
                }
                if( a%3 === 0 && b%3 === 0) {
                    y = y*3
                }
                if ( a%5 === 0 || b%5 === 0){
                if (a%5 === 0) {
                    a = a/5
                }
                if (b%5 === 0) {
                    b = b/5
                }
                if( a%5 === 0 && b%5 === 0) {
                    y = y*5
                }

            
        }while(a>=2 && b>=2)
                
    return y
}
module.exports = MDC;