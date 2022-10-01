const Rectangle = require('./3-rectangle')

const r1 = new Rectangle(10,4);
// console.log(r1.height * 10)
// console.log(r1.width + 4)
console.log(r1.width, r1.height)
r1.print()
r1.rotate()
console.log(r1.width, r1.height)
r1.print()
r1.double()
console.log(r1.width, r1.height)