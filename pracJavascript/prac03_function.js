function myFunction(p1, p2){
    //여러가지 프로그래밍
    return p1 + p2;
};

const plus = (p1, p2) => { //Arrow function
    return p1 + p2;
};

//실습 | minus, multi, div => 빼기, 곱하기, 나누기 기능 추가
function minus(p1, p2) {
    return p1-p2;
}

function multi(p1, p2) {
    return p1*p2;
}

function div(p1, p2) {
    return p1/p2;
}

const minus = (p1, p2) => {
  return p1 - p2;
};

const multi = (p1, p2) => {
  return p1 * p2;
};

const div = (p1, p2) => {
  return p1 / p2;
};

console.log(myFunction(5,5));
console.log(plus(5,9));
console.log(minus(5,9));
console.log(multi(5,9));
console.log(div(5,9));