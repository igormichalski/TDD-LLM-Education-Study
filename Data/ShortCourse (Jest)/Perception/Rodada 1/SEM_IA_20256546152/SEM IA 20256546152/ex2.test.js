const exer2 = require('./ex2.js');
 describe('testes da funcao exer2',()=>{
    test('entrada (senha123).saida esperada= tudocerto',()=>{
        expect(exer2('senha123')).toBe('tudocerto')
    })
    test('entrada(senha123).saida esperada= tudocerto',()=>{
        expect(exer2('senha123')).toBe('tudocerto')
    })
 })