# Friction Caused by a Fluid Flowing Through a Pipe

As a fluid flows through a pipe, it encounters resistance according to several factors, including the
diameter and wall roughness of the pipe, the velocity and viscosity of the fluid, and whether the
fluid is in a laminar or turbulent state. However, the relationship between these variables is typically
complex and nonlinear, meaning that we require computational techniques to predict pressure losses
– a requirement in a range of engineering design scenarios.

## Theory - The Darcy-Weisbach Equation

Consider a circular pipe of diameter D and length $L$, through which a fluid of density ρ is flowing at a
mean flow velocity $U$. The pressure loss  $\Delta p$ per unit length is given by the Darcy-Weisbach equation:

$$ \frac{\Delta p}{L}=f_{D} \frac{\rho U^{2}}{2D} $$

And the equations for the Reynolds number is:
$$ Re = \frac{\rho U D}{\mu} $$
where µ is the dynamic viscosity of the fluid.
The Reynolds Number dictates whether the fluid is in a turbulent or laminar state: if $Re < 2040$ the flow can be assumed to be laminar, or if $Re ≥ 2040$ we assume
it is turbulent.

If the flow is laminar, then the relationship for the friction factor is straightforward and can be derived
from the Poiseuille (laminar) flow profile, giving:

$$ f_{D} =\frac{64}{Re} $$

On the other hand, if the flow is turbulent, the relationship is more complex. In this case, fD can only
be found by solving the nonlinear Colebrook-White equation:

$$ \frac{1}{\sqrt{f_{D}}} =-2 log_{10} \left ( \frac{2.51}{Re \sqrt{f_{D}}} + \frac{\epsilon / D}{3.72} \right ) $$

Clearly, this relationship cannot be solved analytically. However, by rearranging this equation, we
can see that it can instead be turned into a root-finding problem; i.e. find $f_{D}$ such that the function
$C(f_{D}) = 0$, where:

$$ C(f_{D})= \frac{1}{\sqrt{f_{D}}} + 2 log_{10} \left ( \frac{2.51}{Re \sqrt{f_{D}}} + \frac{\epsilon / D}{3.72} \right ) $$

## Newton-Ralphson Algorithm for Root Finding

The Newton-Raphson algorthim can be used to solve this root finding problem.

In order to find the root of a function f(x) using the Newton-Raphson algorithm, we first require
the function’s derivative f'(x) and an initial starting point x0, we can approximate roots of the
function by applying the iterative relationship:

$$ x_{n+1} = x_{n} - \frac{f(x_{n})}{{f}'(x_{n})} $$

## Moody Chart

The Moody Chart or Moody Diagram is used to visualise the change in Darcy Friction Factor as the Reynolds Number changes. The Moody Chart includes plotted lines of several relative roughnesses. The relative roughness of the pipe is the surface roughness devided by the diameter of the pipe.

### Engineer's Application

Different lines on the moody chart represent different relitive roughnesses. The engineer may know the specifiaction of their pipe but not know the darcy friction factor. The Engineer can therefore use the chart to read off the approximate friction factor for different velocities of fluid flow, and from that, calcualte the pressure loss across the legnth of their pipe.
