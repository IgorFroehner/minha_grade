
from model import Schedule, schedule
from model import Phase
from model import Subject

from decouple import config
from mongoengine import connect


def create_computacao():
    computacao = Schedule(2, 'Ciência da Computação 2012/2')

    fase1 = Phase(1)

    cdi1 = Subject('CDI0001', 'CÁLCULO DIFERENCIAL E INTEGRAL I', 108)
    cdi1.save()
    alg1 = Subject('ALG1001', 'ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA I', 72)
    alg1.save()
    agt = Subject('AGT0001', 'ALGORITMOS', 72)
    agt.save()
    lma = Subject('LMA0001', 'LÓGICA MATEMÁTICA', 72)
    lma.save()
    mci = Subject('MCI0001', 'METODOLOGIA CIENTIFICA', 36)
    mci.save()
    tgs = Subject('TGS0001', 'TEORIA GERAL DE SISTEMAS', 72)
    tgs.save()

    fase1.add_subjects([cdi1, alg1, agt, lma, mci, tgs])
    fase1.save()

    fase2 = Phase(2)

    alg2 = Subject('ALG2002', 'ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA II', 72, ids_requirements=['ALG1001'])
    alg2.save()
    cdi2 = Subject('CDI2001', 'CÁLCULO DIFERENCIAL E INTEGRAL II', 72, ids_requirements=['ALG1001', 'CDI1001'])
    cdi2.save()
    est = Subject('EST0007', 'PROBABILIDADE E ESTATÍSTICA', 72, ids_requirements=['CDI1001'])
    est.save()
    fcc = Subject('FCC0002', 'FÍSICA PARA CIÊNCIA DA COMPUTAÇÃO', 72, ids_requirements=['CDI1001'])
    fcc.save()
    lpg = Subject('LPG0001', 'LINGUAGEM DE PROGRAMAÇÃO', 72, ids_requirements=['AGT0001'])
    lpg.save()
    mdi = Subject('MDI0001', 'MATEMÁTICA DISCRETA', 72, ids_requirements=['ALG1002'])
    mdi.save()
    sna = Subject('SNA0001', 'SISTEMAS DE NUMERAÇÃO E ÁLGEBRA DE BOOLE', 32)
    sna.save()

    fase2.add_subjects([alg2, cdi2, est, fcc, lpg, mdi, sna])
    fase2.save()

    computacao.add_phase(fase1)
    computacao.add_phase(fase2)

    computacao.save()


if __name__ == '__main__':

    connect(host=f"mongodb+srv://{config('DB_USER')}:{config('DB_PASS')}@cluster0.ogn2b.mongodb.net/myFirstDatabase"
            f"?retryWrites=true&w=majority")

    for schedule in Schedule.objects:
        print(schedule.content)
