import pandas as pd

def otherRegression(input_feature, output):
  x_mean = input_feature.mean()
  y_mean = output.mean()

  temp_1 =input_feature * output
  product = temp_1.mean()

  temp_2 = input_feature * input_feature
  square = temp_2.mean()

  num = product - y_mean * x_mean
  den = square - x_mean * x_mean

  slope = num/den
  intercept = y_mean - slope * x_mean

  return (intercept, slope)

def get_regression_predictions(input_feature, intercept, slope):
  # calculate the predicted values:
  # take the x value multiply by slope and add intercept to find y value
  predicted_values = input_feature * slope + intercept

  return predicted_values

X =  pd.DataFrame([0, 1, 2, 3, 4])
Y = pd.DataFrame([1, 3, 7, 13, 21])

otherRegression(X, Y)
pred = get_regression_predictions(X, -1, 5)
print(pred)
print()