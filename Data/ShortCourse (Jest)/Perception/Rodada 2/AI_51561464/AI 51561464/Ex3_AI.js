function fahrenheitParaCelsius(f) {
  return (f - 32) / 1.8;
}

console.log(fahrenheitParaCelsius(98.6)); // 37°C (temperatura corporal normal)

module.exports = fahrenheitParaCelsius