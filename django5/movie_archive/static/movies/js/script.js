// 1
let start = Number(prompt("Введіть початок діапазону:"));
let end = Number(prompt("Введіть кінець діапазону:"));
if (start > end) {
  let temp = start;
  start = end;
  end = temp;
}
let product = 1;
for (let i = start; i <= end; i++) {
  product *= i;
}
console.log(`Добуток чисел у діапазоні від ${start} до ${end}: ${product}`);
// 2
let a = Number(prompt("Введіть перше натуральне число:"));
let b = Number(prompt("Введіть друге натуральне число:"));
let nsk = Math.max(a, b);

while (nsk % a !== 0 || nsk % b !== 0) {
  nsk++;
}
console.log(`НСК чисел ${a} та ${b} дорівнює: ${nsk}`);
// 3
let num = Number(prompt("Введіть число:"));

console.log(`Числа, кратні ${num} у діапазоні від 1 до 100:`);
for (let i = 1; i <= 100; i++) {
  if (i % num === 0) {
    console.log(i);
  }
}
// 4
let number = Math.abs(Number(prompt("Введіть число:")));
let sum = 0;

while (number > 0) {
  sum += number % 10;
  number = Math.floor(number / 10);
}

console.log(`Сума цифр введеного числа: ${sum}`);
// 5
let positiveCount = 0;
let negativeCount = 0;
let zeroCount = 0;
let mult3Count = 0;
let mult5Count = 0;

for (let i = 1; i <= 15; i++) {
  let num = Number(prompt(`Введіть число ${i} з 15:`));
  if (num > 0) positiveCount++;
  else if (num < 0) negativeCount++;
  else zeroCount++;
  if (num !== 0 && num % 3 === 0) mult3Count++;
  if (num !== 0 && num % 5 === 0) mult5Count++;
}

console.log(`Додатних: ${positiveCount}`);
console.log(`Від'ємних: ${negativeCount}`);
console.log(`Нулів: ${zeroCount}`);
console.log(`Кратних 3: ${mult3Count}`);
console.log(`Кратних 5: ${mult5Count}`);
// 6
let repeat;

do {
  let temp = Number(prompt("Введіть температуру:"));
  let choice = prompt("Оберіть напрямок:\n1 — з °C у °F\n2 — з °F у °C");

  if (choice === "1") {
    let result = (temp * 9 / 5) + 32;
    alert(`${temp}°C = ${result.toFixed(2)}°F`);
  } else if (choice === "2") {
    let result = (temp - 32) * 5 / 9;
    alert(`${temp}°F = ${result.toFixed(2)}°C`);
  } else {
    alert("Некоректний вибір напрямку!");
  }

  repeat = confirm("Бажаєте виконати ще одне переведення?");
} while (repeat);

alert("Роботу конвертера завершено.");