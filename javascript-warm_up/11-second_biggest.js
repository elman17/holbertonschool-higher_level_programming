#!/usr/bin/node
const args = ProcessingInstruction.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
