let x = 10;
let y = x++;
let z = ++x;
console.log(x, y, z);//12,10,12

let a = 5;
let b = a-- + ++a;
console.log(a, b);//5,10

let m = 7;
let n = --m + m++;
console.log(m, n);//7,12

let p = 3;
let q = p++ + ++p + p;
console.log(p, q);//5,13

let val = 0;
val = val++ + ++val;
console.log(val);//2