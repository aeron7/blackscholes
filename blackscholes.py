from nsepython import *
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
