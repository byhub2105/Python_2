// 1
console.log("Олексій"); 
console.log(42);       
console.log(`Привіт! Мені ${10 + 6} років.`); 
// 2
let username = "Артем";
let age = 16;
let email = "artem.dev@example.com";
let isOnline = true;
console.log(username);
console.log(age);
console.log(email);
console.log(isOnline);
console.log(`Користувач ${username} (${age} років, email: ${email}) зараз ${isOnline ? "онлайн" : "офлайн"}.`);
// 3
let a = 16;
let b = 5;
console.log(a + b); 
console.log(a - b);
console.log(a * b); 
console.log(a / b); 
// 4
const celsius = 25;
const fahrenheit = celsius * 9 / 5 + 32; 
console.log(`${celsius}°C — це ${fahrenheit}°F`);
// 5
let age1 = 15;
let age2 = 18;
let age3 = 22;
console.log(`Людина 1: ${age1 >= 18 ? "Повнолітня" : "Неповнолітня"}`);
console.log(`Людина 2: ${age2 >= 18 ? "Повнолітня" : "Неповнолітня"}`);
console.log(`Людина 3: ${age3 >= 18 ? "Повнолітня" : "Неповнолітня"}`);
// 6
let taskCount = 5;
taskCount += 2;
console.log(`Додано 2 завдання. Залишилось ${taskCount} завдань.`);
taskCount -= 3;
console.log(`Виконано 3 завдання. Залишилось ${taskCount} завдань.`);
// 7
let priceA = 250;
let priceB = 180;
console.log(`Товар А коштує ${priceA} грн, а товар Б — ${priceB} грн. ${priceA > priceB ? "Товар А дорожчий." : "Товар Б дорожчий."}`);