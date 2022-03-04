



// Square

console.group("Square");


function square_perimeter(side){
    return side *4;
}

square_perimeter ();

function square_area(side){
    return side *side;
}

square_area ();


console.groupEnd();

// Triangle

console.group("Triangles");


function triangle_perimeter(base,side_1,side_2){
    return (base + side_1 + side_2);
}

triangle_perimeter ();

function triangle_area(base,height){
    return base * height;
}


triangle_area ();


console.groupEnd()

// Circle


console.group("Circle");

const pi = Math.PI;

function circle_perimeter(diameter){
    return (diameter*pi);
}

function radius(diameter){
    return diameter/2;
}

circle_perimeter ();

function circle_area(radius){
    return (radius*radius*pi);

}
console.groupEnd()

// integration with HTML

function buttonA(){
    const input = document.getElementById("input_square");
    const value = input.value;

    const perimeter =square_perimeter(value);
    alert(perimeter);
}

function buttonB(){
    const input = document.getElementById("input_square");
    const value = input.value;

    const area =square_area(value);
    alert(area);
}