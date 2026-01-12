const exer = require('./ex1.js');
 describe('testes da funcao exer',()=>{
    test('Entrada (12,18). Saida esperada = 6',()=>{
        expect(exer(12,18)).toBe(6);
    })
 })