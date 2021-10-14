const ordinaryLeastSquare = (X, y) =>{
  let x_sum = 0;
  let y_sum = 0;
  for (let i = 0; i < X.length; i++) {
    x_sum += X[i];
    y_sum += y[i];
  }

  let x_mean = x_sum / X.length;
  let y_mean = y_sum / y.length;
  let multiplier = 0;
  let divider = 0;
  for (let i = 0; i < X.length; i++) {
    multiplier += (X[i] - x_mean)*(y[i] - y_mean);
    divider += (X[i] - x_mean) * (X[i] - x_mean);
  }

  let theta1 = multiplier / divider;
  let theta0 = y_mean - theta1 * x_mean;
  
  console.log('theta1: ' + theta1)
  console.log('theta0: ' + theta0)
}

var X = [1, 2, 3, 4, 5], y = [1, 3, 5, 7, 9];
ordinaryLeastSquare(X, y);
