let car = {
    carname : "bmw",
    ph : 140,
    start : function () {
        console.log("engine start")
    },
    stop : function() {
        console.log("engine stop")
    },
};

console.log(car.carname);
console.log(car.start);
car.start();

//const carname = car.carname;
//const carph = car.ph;

const {carname, ph} = car; // 구조 분해 할당 : object의 구조를 분해해 변수에 할당
console.log(carname);
console.log(ph);