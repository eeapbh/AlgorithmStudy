let arr = [];
for (let i = 1; i < 10000; i++) {
  let num = i;
  let tmp = String(i);
  for (let j = 0; j < tmp.length; j++) {
    num += Number(tmp[j]);
  }
  arr.push(num);
}
for (let k = 1; k < 10000; k++) {
  if (arr.includes(k) === false) {
    console.log(k);
  }
}
