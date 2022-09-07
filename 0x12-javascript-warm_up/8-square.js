#!/usr/bin/node
const argument = parseInt(process.argv[2])
if (Number.isNaN(argument)) {
    console.log('Missing size')
} else {
    for (let i = 0, size; i < argument; i++ ) {
        size = ' '
        for (let j = 0; j < argument; j++) {
            size += 'X'
        }
        console.log(size)
    }
}
