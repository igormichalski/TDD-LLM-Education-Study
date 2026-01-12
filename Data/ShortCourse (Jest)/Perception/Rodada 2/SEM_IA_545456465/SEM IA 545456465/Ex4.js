function cnp (a){
    cont=1
    div=0
    while(cont<=a){
        if(a%cont){
            div=div+1;
        }
        cont=cont+1;
    }
    if(a==2){
        return 1;
    }
    if(div!=2){
        return 0;
    }
    if(div==2){
        return 1;
    }
    
}
module.exports = cnp;