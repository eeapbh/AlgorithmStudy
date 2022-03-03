const combi = function (arr, selectNumber) {
  const results = [];

  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, arr) => {
    const new_arr = arr.slice(index + 1);
    const combination = combi(new_arr, selectNumber - 1);

    const attached = combination.map((el) => [fixed, ...el]);
    results.push(...attached);
  });
  return results;
};

function solution(arr, k, t) {
  let combiArr = [];
  let answer = 0;
  for (let i = k; i <= arr.length; i++) {
    combiArr.push(combi(arr, i));
  }
  for (let i = 0; i < combiArr.length; i++) {
    if (sum(combiArr[i]) <= t) {
      answer += 1;
    }
  }
  return answer;
}
