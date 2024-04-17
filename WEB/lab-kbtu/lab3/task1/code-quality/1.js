function pow(x,n)
{
  let result = 1;
  for(let i=0;i<n;i++) {result*=x;}
  return result;
}

// let x=prompt("x?",''), n=prompt("n?",'')
if (n<=0)
{
  alert(`Степень ${n} не поддерживается, введите целую степень, большую 0`);
}
else
{
  alert(pow(x,n))
}

function pow(x, n) {
    let result = 1;
  
    for (let i = 0; i < n; i++) {
      result *= x;
    }
  
    return result;
  }
  
  let x = prompt("x?", "");
  let n = prompt("n?", "");
  
  if (n <= 0) {
    alert(`Степень ${n} не поддерживается,
      введите целую степень, большую 0`);
  } else {
    alert( pow(x, n) );
  }

  it("Возводит x в степень n", function() {
    let x = 5;
  
    let result = x;
    assert.equal(pow(x, 1), result);
  
    result *= x;
    assert.equal(pow(x, 2), result);
  
    result *= x;
    assert.equal(pow(x, 3), result);
  });