const MDC =require('./Ex1')

describe("Teste de MDC", () => {

   test("Entrada(12,18) Saida esperada = 6", ()=>{
      expect(MDC(12,18)).toBe(6)
   });

   test("Entrada(-4,-2) Saida = 2", ()=>{
      expect(MDC(-4,-2)).toBe(2)
   });

   test("Entra(25,30) Saida(5)", ()=>{
      expect(MDC(25,30)).toBe(5)
   });

   test("Entra(10.2,10.2) Saida(ERRO)", ()=>{
      expect(MDC(10.2,10.2)).toBe('ERRO')
   });

   test("Entra(100,200) Saida(100)", ()=>{
      expect(MDC(100,200)).toBe(100)
   });

   test("Entra('a',10) Saida(ERRO)", ()=>{
      expect(MDC('a',10)).toBe('ERRO')
   });
   test("Entra(10,'a') Saida(ERRO)", ()=>{
      expect(MDC(10,'a')).toBe('ERRO')
   });

});
