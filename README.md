# blackscholes
Options Pricing Using Black Scholes Model For Indian Market

# How to Use The Function
Option Premium Calculator Using Black Scholes Model:

https://unofficed.com/black-scholes-model-options-calculator-google-sheet/

## Inputs in Black-Scholes Option Pricing Model Formula

* S0 = underlying price
* X = strike price
* σ = volatility
* r = continuously compounded risk-free interest rate
* q = continuously compounded dividend yield
* t = time to expiration
* td = number of trading days.

Usage:

`black_scholes_dexter(S0,X,t,σ="",r=10,q=0.0,td=365)`

Default Value:

For,

* σ = Volatility = India VIX has been taken. Keep it blank and it will automatically use India Vix's latest value.
* r = 10% (As per NSE Website, it is fixed.)
* q = 0.00% (Assumed No Dividend)
* td = Zerodha uses `365` in their calculator. You can use anything you want.

**Usage:**


```
S0 = 34950.60
X = 35000.00
σ = 14.72
t = 3
call_theta,put_theta,call_premium,put_premium,call_delta,put_delta,gamma,vega,call_rho,put_rho=black_scholes_dexter(S0,X,t,σ="",r=10,q=0.0,td=365)
print(call_theta)
print(put_theta)
print(call_premium)
print(put_premium)
print(call_delta)
print(put_delta)
print(gamma)
print(vega)
print(call_rho)
print(put_rho)
```
**Output:**

```
-35.57594968706057
-25.994786756764814
175.92468507293597
196.56938065246504
0.4850057898780081
-0.514994210121992
0.0008543132102275919
12.621618527502404
1.378793315723619
-1.495555563365108
```
