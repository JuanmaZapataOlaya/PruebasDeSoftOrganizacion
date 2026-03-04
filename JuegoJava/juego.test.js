// juego.test.js
const { verificarIntento, calcularPuntaje } = require('./juego');
// ── verificarIntento ──────────────────────────────────────
test('intento correcto', () => {
expect(verificarIntento(42, 42)).toBe("correcto");
});
test('intento es muy bajo, pista dice mayor', () => {
expect(verificarIntento(70, 60)).toBe("mayor"); // completar
});
test('intento es muy alto, pista dice menor', () => {
expect(verificarIntento(40, 60)).toBe("menor"); // completar
});
test('intento fuera de rango lanza excepción', () => {
expect(() => verificarIntento(50, 101)).toThrow("El intento debe estar entre 100 y 1");
});
test('intento no numérico lanza excepción', () => {
expect(() => verificarIntento(50, "ochenta")).toThrow("El intento debe ser un numero");
});
// ── calcularPuntaje ───────────────────────────────────────
test('3 intentos o menos dan puntaje 100', () => {
expect(calcularPuntaje(3)).toBe(100); // completar
});
test('entre 4 y 6 intentos dan puntaje 75', () => {
    expect(calcularPuntaje(5)).toBe(75);
// escribir la prueba completa aquí
});
test('entre 7 y 10 intentos dan puntaje 50', () => {
    expect(calcularPuntaje(8)).toBe(50);
// escribir la prueba completa aquí
});
test('más de 10 intentos dan puntaje 25', () => {
    expect(calcularPuntaje(11)).toBe(25);
// escribir la prueba completa aquí
});