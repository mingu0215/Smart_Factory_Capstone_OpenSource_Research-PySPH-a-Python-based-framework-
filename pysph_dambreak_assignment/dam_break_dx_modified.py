from dam_break_baseline import DamBreakBaseline
from pysph.base.utils import get_particle_array_wcsph
from pysph.tools import geometry as G


class DamBreakDXModified(DamBreakBaseline):
    def create_particles(self):
        dx, hdx, rho = 0.05, 1.2, 1000.0

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

        print("[DX Modified] dx = 0.05")
        print("[DX Modified] Number of fluid particles:", fluid.get_number_of_particles())
        print("[DX Modified] Number of solid particles:", solid.get_number_of_particles())

        return [fluid, solid]


if __name__ == '__main__':
    app = DamBreakDXModified()
    app.run()