const exer3 = require('./ex3.js');
describe('testes a funcao de soma', ()=>{
    test('entrada(492). saida esperada = 15',()=>{
        expect(exer3(492)).toBe(15)
    })
})
