function exer(numero1, numero2) {
        var R;
  while ((numero1 % numero2) > 0)  {
    R = numero1 % numero2;
    numero1= numero2;
    numero2= R;
  }
  return numero2;
  
}
module.exports= exer;