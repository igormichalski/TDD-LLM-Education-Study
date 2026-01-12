function ccf(g, a){
    if(ccf=='celcius'){
        if(a==0){
            return 32;
        }
        a=a*1.8+32
    }
    if(ccf=='fahrenheit'){
        if(a==32){
            return 0;
        }
        a=(a-32)/1.8
    }
}