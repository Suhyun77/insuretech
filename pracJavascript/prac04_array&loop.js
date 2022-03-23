//array

// 데이터 크기, 타입에 대한 문제 발생 x
const array = [1, 'test', {name:"test"}, 123.42351];
console.log(array);
//in java
// public String [] StringArray = new String[5];
// public arrayList [String] arrayListString = new ArrayList(String);

//접근 방법 : index
console.log(array[0]);
console.log(array[2].name);
console.log(array[3]+2);



// 루프

// 익숙한 방식
for (let i = 0; i < array.length; i++){
    let element = array[i];
    console.log(element);
}

//es6
for(element of array){
    console.log(element);
}

//array map
array.map((data) => {
    console.log(data);
});