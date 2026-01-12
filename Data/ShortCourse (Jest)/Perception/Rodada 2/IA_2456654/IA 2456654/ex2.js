function contaVogais(str) {
    if (typeof str !== 'string') return 'Erro';

    const vogais = ['a', 'e', 'i', 'o', 'u'];
    let count = 0;

    for (let char of str.toLowerCase()) {
        if (vogais.includes(char)) {
            count++;
        }
    }

    return count;
}

module.exports = contaVogais;
