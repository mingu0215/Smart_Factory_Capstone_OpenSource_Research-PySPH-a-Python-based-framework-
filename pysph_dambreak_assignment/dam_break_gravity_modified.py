from dam_break_baseline import DamBreakBaseline, EOS, ContinuityEquation, MomentumEquation
from pysph.sph.equation import Group


class DamBreakGravityModified(DamBreakBaseline):
    def create_equations(self):
        return [
            Group(equations=[
                EOS(dest='fluid', sources=None, rho0=1000.0, c0=10.0),
                EOS(dest='solid', sources=None, rho0=1000.0, c0=10.0),
            ]),
            Group(equations=[
                ContinuityEquation(dest='fluid', sources=['fluid', 'solid']),
                ContinuityEquation(dest='solid', sources=['fluid']),
                MomentumEquation(dest='fluid', sources=['fluid', 'solid'], gy=-19.62),
            ])
        ]


if __name__ == '__main__':
    print("[Gravity Modified] gravity = -19.62")
    app = DamBreakGravityModified()
    app.run()