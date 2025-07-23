#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
    console.log('Missing number of occurrences');
} else {
    const count = parseInt(args[0]);
    for (let i = 0; i < count; i++) {
        console.log('C is fun');
    }
}
