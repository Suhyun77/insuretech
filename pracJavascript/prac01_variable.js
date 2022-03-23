// var : 중복 선언 가능
var a = "hello";
var a = "bye";


// let, const : 중복 선언 불가능
let b = "test";
let c = "test2";
b = "test3"; // var, let : 값의 재할당 가능

const d = "test";   // const : 값의 재할당 불가능
let name = "name";
let age = 15;
let height = 144.32;

const method = () => {
    console.log("hello");
};

const array = [a, b, c];

const obj = {
    name : "test"
    age : 14
}


console.log(b);

