function converteTemperatura(valor, unidade) {
    if (typeof valor !== 'number' || (unidade !== 'C' && unidade !== 'F')) {
        return 'Erro';
    }

    if (unidade === 'C') {
        // Celsius → Fahrenheit
        return (valor * 9/5) + 32;
    } else {
        // Fahrenheit → Celsius
        return (valor - 32) * 5/9;
    }
}

module.exports = converteTemperatura;
