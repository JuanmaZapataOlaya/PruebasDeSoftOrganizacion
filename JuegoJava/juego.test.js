// juego.test.js
const { verificarIntento, calcularPuntaje } = require('./juego');
// ── verificarIntento ──────────────────────────────────────
test('intento correcto', () => {
expect(verificarIntento(42, 42)).toBe("correcto");
});
test('intento es muy bajo, pista dice mayor', () => {
expect(verificarIntento(???, ???)).toBe("mayor"); // completar
});
test('intento es muy alto, pista dice menor', () => {
expect(verificarIntento(???, ???)).toBe("menor"); // completar
});
test('intento fuera de rango lanza excepción', () => {
expect(() => verificarIntento(50, ???)).toThrow("El número debe estar entre
1 y 100");
});
test('intento no numérico lanza excepción', () => {
expect(() => verificarIntento(50, ???)).toThrow("El intento debe ser un
número");
});
// ── calcularPuntaje ───────────────────────────────────────
test('3 intentos o menos dan puntaje 100', () => {
expect(calcularPuntaje(???)).toBe(???); // completar
});
test('entre 4 y 6 intentos dan puntaje 75', () => {
// escribir la prueba completa aquí
});
test('entre 7 y 10 intentos dan puntaje 50', () => {
// escribir la prueba completa aquí
});
test('más de 10 intentos dan puntaje 25', () => {
// escribir la prueba completa aquí
});