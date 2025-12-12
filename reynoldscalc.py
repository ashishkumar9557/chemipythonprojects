def reynolds_number(rho, v, d, mu):
    Re = (rho * v * d) / mu
    if Re < 2300:
        flow = "Laminar Flow"
    elif Re < 4000:
        flow = "Transient Flow"
    else:
        flow = "Turbulent Flow"
    return Re, flow

rho = float(input("Density (kg/m3): "))
v = float(input("Velocity (m/s): "))
d = float(input("Diameter (m): "))
mu = float(input("Viscosity (Pa.s): "))

Re, flow = reynolds_number(rho, v, d, mu)
print("Reynolds Number =", Re)
print("Flow Regime =", flow)
