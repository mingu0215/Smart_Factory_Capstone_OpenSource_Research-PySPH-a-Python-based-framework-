from pysph.solver.application import Application
from pysph.base.utils import get_particle_array_wcsph
from pysph.tools import geometry as G
from pysph.sph.equation import Equation, Group
from pysph.solver.solver import Solver
from pysph.base.kernels import CubicSpline
from pysph.sph.integrator import EulerIntegrator
from pysph.sph.integrator_step import EulerStep


class EOS(Equation):
    def __init__(self, dest, sources, rho0, c0, gamma=7.0):
        self.rho0 = rho0
        self.gamma = gamma
        self.B = rho0 * c0 * c0 / gamma
        super(EOS, self).__init__(dest, sources)

    def initialize(self, d_idx, d_p, d_rho):
        tmp = (d_rho[d_idx] / self.rho0) ** self.gamma
        d_p[d_idx] = self.B * (tmp - 1.0)


class ContinuityEquation(Equation):
    def initialize(self, d_idx, d_arho):
        d_arho[d_idx] = 0.0

    def loop(self, d_idx, s_idx, d_arho, s_m, DWIJ, VIJ):
        vijdotdwij = DWIJ[0] * VIJ[0] + DWIJ[1] * VIJ[1] + DWIJ[2] * VIJ[2]
        d_arho[d_idx] += s_m[s_idx] * vijdotdwij


class MomentumEquation(Equation):
    def __init__(self, dest, sources, gy=-9.81):
        self.gy = gy
        super(MomentumEquation, self).__init__(dest, sources)

    def initialize(self, d_idx, d_au, d_av, d_aw):
        d_au[d_idx] = 0.0
        d_av[d_idx] = self.gy
        d_aw[d_idx] = 0.0

    def loop(self, d_idx, s_idx, d_rho, s_rho, d_p, s_p,
             d_au, d_av, d_aw, s_m, DWIJ):
        tmp = d_p[d_idx] / (d_rho[d_idx] ** 2) + s_p[s_idx] / (s_rho[s_idx] ** 2)
        d_au[d_idx] += -s_m[s_idx] * tmp * DWIJ[0]
        d_av[d_idx] += -s_m[s_idx] * tmp * DWIJ[1]
        d_aw[d_idx] += -s_m[s_idx] * tmp * DWIJ[2]


class DamBreakBaseline(Application):
    def create_particles(self):
        dx, hdx, rho = 0.1, 1.2, 1000.0

        xf, yf = G.get_2d_block(
            dx=dx,
            length=1.0,
            height=2.0,
            center=[-1.5 + dx, 1.0 + dx]
        )

        m = dx * dx * rho

        fluid = get_particle_array_wcsph(
            name='fluid',
            x=xf,
            y=yf,
            h=hdx * dx,
            m=m,
            rho=rho
        )

        xt, yt = G.get_2d_tank(
            dx=dx,
            length=4.0,
            height=4.0,
            num_layers=3
        )

        solid = get_particle_array_wcsph(
            name='solid',
            x=xt,
            y=yt,
            h=hdx * dx,
            m=m,
            rho=rho
        )

        print("[Baseline] Number of fluid particles:", fluid.get_number_of_particles())
        print("[Baseline] Number of solid particles:", solid.get_number_of_particles())

        return [fluid, solid]

    def create_equations(self):
        return [
            Group(equations=[
                EOS(dest='fluid', sources=None, rho0=1000.0, c0=10.0),
                EOS(dest='solid', sources=None, rho0=1000.0, c0=10.0),
            ]),
            Group(equations=[
                ContinuityEquation(dest='fluid', sources=['fluid', 'solid']),
                ContinuityEquation(dest='solid', sources=['fluid']),
                MomentumEquation(dest='fluid', sources=['fluid', 'solid'], gy=-9.81),
            ])
        ]

    def create_solver(self):
        kernel = CubicSpline(dim=2)

        integrator = EulerIntegrator(
            fluid=EulerStep(),
            solid=EulerStep()
        )

        solver = Solver(
            kernel=kernel,
            dim=2,
            integrator=integrator,
            dt=2e-4,
            tf=0.2,
            pfreq=10
        )

        return solver


if __name__ == '__main__':
    app = DamBreakBaseline()
    app.run()