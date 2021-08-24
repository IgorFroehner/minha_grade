from model import Schedule, schedule_dao
from model import Phase
from model import Subject


def create_computacao_2012():
    computacao_2012 = Schedule('Ciência da Computação 2012')

    fase1 = Phase(1)

    cdi1 = Subject('CDI0001', 'CÁLCULO DIFERENCIAL E INTEGRAL I', 108)
    alg1 = Subject('ALG1001', 'ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA I', 72)
    agt = Subject('AGT0001', 'ALGORITMOS', 72)
    lma = Subject('LMA0001', 'LÓGICA MATEMÁTICA', 72)
    mci = Subject('MCI0001', 'METODOLOGIA CIENTIFICA', 36)
    tgs = Subject('TGS0001', 'TEORIA GERAL DE SISTEMAS', 72)

    fase1.add_subjects([cdi1, alg1, agt, lma, mci, tgs])

    fase2 = Phase(2)

    alg2 = Subject('ALG2002', 'ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA II',
                   72, ids_requirements=['ALG1001'])
    cdi2 = Subject('CDI2001', 'CÁLCULO DIFERENCIAL E INTEGRAL II',
                   72, ids_requirements=['ALG1001', 'CDI1001'])
    est = Subject('EST0007', 'PROBABILIDADE E ESTATÍSTICA',
                  72, ids_requirements=['CDI1001'])
    fcc = Subject('FCC0002', 'FÍSICA PARA CIÊNCIA DA COMPUTAÇÃO',
                  72, ids_requirements=['CDI1001'])
    lpg = Subject('LPG0001', 'LINGUAGEM DE PROGRAMAÇÃO',
                  72, ids_requirements=['AGT0001'])
    mdi = Subject('MDI0001', 'MATEMÁTICA DISCRETA',
                  72, ids_requirements=['ALG1002'])
    sna = Subject('SNA0001', 'SISTEMAS DE NUMERAÇÃO E ÁLGEBRA DE BOOLE', 32)

    fase2.add_subjects([alg2, cdi2, est, fcc, lpg, mdi, sna])

    fase3 = Phase(3)

    ann = Subject('ANN0001', 'ANÁLISE NUMÉRICA',
                  72, ids_requirements=['CDI2001', 'AGT0001'])
    aoc = Subject('AOC0003', 'ARQUITETURA E ORG. DE COMPUTADORES',
                  72, ids_requirements=['FCC0002', 'SNA0001'])
    eda = Subject('EDA0001', 'ESTRUTURA DE DADOS',
                  72, ids_requirements=['LPG0001'])
    lfa = Subject('LFA0001', 'LINGUAGENS FORMAIS E AUTÔMATOS',
                  72, ids_requirements=['AGT0001', 'MDI0001'])
    mep = Subject('MEP0003', 'METODOLOGIA DA PESQUISA',
                  36, ids_requirements=['MCI0001'])
    poo = Subject('POO00011', 'PROGRAMAÇÃO ORIENTADA A OBJETOS',
                  72, ids_requirements=['AGT0001'])
    ppr = Subject('PPR0001', 'PROJETO DE PROGRAMAS',
                  32, ids_requirements=['LPG0001'])

    fase3.add_subjects([ann, aoc, eda, lfa, mep, poo, ppr])

    fase4 = Phase(4)

    ams = Subject('AMS0001', 'ANÁLISE E MODELAGEM DE SISTEMAS',
                  36, ids_requirements=['TGS0001'])
    ban = Subject('BAN1001', 'BANCO DE DADOS I',
                  72, ids_requirements=['LPG0001', 'MDI0001'])
    com = Subject('COM0002', 'COMPILADORES',
                  72, ids_requirements=['LFA0001', 'EDA0001'])
    pra = Subject('PRA0001', 'PROJETO DE ARQUIVOS',
                  72, ids_requirements=['EDA0001'])
    rec = Subject('REC0001', '	REDES DE COMPUTADORES',
                  36, ids_requirements=['EDA0001', 'AOC0003'])
    soft = Subject('SOFT001', 'ENGENHARIA DE SOFTWARE',
                   72, ids_requirements=['PPR0001'])
    sop = Subject('SOP0001', 'SISTEMAS OPERACIONAIS',
                  72, ids_requirements=['EDA0001', 'AOC0003'])
    teg = Subject('TEG0001', 'TEORIA DOS GRAFOS',
                  72, ids_requirements=['EDA0001'])

    fase4.add_subjects([ams, ban, com, pra, rec, soft, sop, teg])

    fase5 = Phase(5)

    ban2 = Subject('BAN2001', 'BANCO DE DADOS II',
                   72, ids_requirements=['BAN1001'])
    cal = Subject('CAL0001', 'COMPLEXIDADE DE ALGORITMOS',
                  72, ids_requirements=['AGT0001', 'TEG0001'])
    cgr = Subject('CGR0001', 'COMPUTAÇÃO GRÁFICA',
                  72, ids_requirements=['EDA0001', 'ALG2002'])
    pap = Subject('PAP0002', 'PARADIGMAS DE PROGRAMAÇÃO',
                  72, ids_requirements=['LPG0001', 'POO0001'])
    pes = Subject('PES0001', '	PESQUISA OPERACIONAL',
                  72, ids_requirements=['TEG0001'])
    sdi = Subject('SDI0001', 'SISTEMAS DISTRIBUIDOS',
                  72, ids_requirements=['REC0001'])
    tec = Subject('TEC0001', 'TEORIA DA COMPUTAÇÃO',
                  72, ids_requirements=['LFA0001'])

    fase5.add_subjects([ban2, cal, cgr, pap, pes, sdi, tec])

    fase6 = Phase(6)

    act = Subject('ACT0001', 'AUTOMAÇÃO E CONTROLE',
                  72, ids_requirements=['CGR0001', 'AOC0003'])
    emi = Subject('EMI0001', 'EMPREENDEDORISMO EM INFORMÁTICA',
                  72)
    iar = Subject('IAR0001', 'INTELIGÊNCIA ARTIFICIAL',
                  72, ids_requirements=['CAL0001', 'TEC0001'])
    ihc = Subject('IHC0001', '	INTERAÇÃO HOMEM COMPUTADOR',
                  72, ids_requirements=['EDA0001'])
    mfo = Subject('MFO0001', 'MÉTODOS FORMAIS',
                  72, ids_requirements=['LMA0001', 'LFA0001'])
    op1 = Subject('OPI', '	OPTATIVA I',
                  72)

    fase6.add_subjects([act, emi, iar, ihc, mfo, op1])

    fase7 = Phase(7)

    op2 = Subject('OPII', 'OPTATIVA II',
                  72)
    op3 = Subject('OPIII', 'OPTATIVA III',
                  72)
    op4 = Subject('OPIV', 'OPTATIVA IV',
                  72)
    pim = Subject('PIM0001', 'PROCESSAMENTO DE IMAGENS',
                  72, ids_requirements=['EDA0001', 'ALG2002', 'CDI1001'])

    tcc1 = Subject('TCC1003', 'TRABALHO DE CONCLUSÃO DE CURSO I',
                   36, ids_requirements=['SOFT001', 'CAL0001', 'REC0001', 'CGR0001', 'BAN2001', 'MEP0003'])

    fase7.add_subjects([op2, op3, op4, pim, tcc1])

    fase8 = Phase(8)

    atc = Subject('ATC0007', 'ATIVIDADES COMPLEMENTARES',
                  72)
    eti = Subject('ETI0001', '	ÉTICA EM INFORMÁTICA',
                  72)
    op5 = Subject('OPV', 'OPTATIVA V',
                  72)
    op6 = Subject('OPVI', 'OPTATIVA VI',
                  72)
    tcc2 = Subject('TCC2003', 'TRABALHO DE CONCLUSÃO DE CURSO II',
                   36, ids_requirements=['TCC1003'])

    fase8.add_subjects([atc, eti, op5, op6, tcc2])

    # ----------------

    computacao_2012.add_phase(fase1)
    computacao_2012.add_phase(fase2)
    computacao_2012.add_phase(fase3)
    computacao_2012.add_phase(fase4)
    computacao_2012.add_phase(fase5)
    computacao_2012.add_phase(fase6)
    computacao_2012.add_phase(fase7)
    computacao_2012.add_phase(fase8)

    computacao_2012.save()


def create_computacao_2019():
    computacao_2019 = Schedule('Ciência da Computação 2019/2')

    fase1 = Phase(1)

    agt_ = Subject('AGT0001', 'ALGORITMOS', 72)
    gan_ = Subject('GAN0001', 'GEOMETRIA ANALÍTICA', 72)
    icd_ = Subject(
        'ICD0001', 'INTRODUÇÃO AO CÁLCULO DIFERENCIAL E INTEGRAL', 72)
    lma_ = Subject('LMA0001', '	LÓGICA MATEMÁTICA', 72)
    pfn_ = Subject('PFN0001', 'PROGRAMAÇÃO FUNCIONAL', 72)
    tgs_ = Subject('TGS0001', 'TEORIA GERAL DE SISTEMAS', 72)

    fase1.add_subjects([agt_, gan_, icd_, lma_, pfn_, tgs_])

    fase2 = Phase(2)

    ali_ = Subject('ALI0001', 'ÁLGEBRA LINEAR',
                   72, ids_requirements=['GAN0001'])
    cdi1_ = Subject('CDI1001', 'CÁLCULO DIFERENCIAL E INTEGRAL I',
                    108, ids_requirements=['ICD0001'])
    ecc_ = Subject('ECC0001', 'ELETRÔNICA PARA CIÊNCIA DA COMPUTAÇÃO',
                   72)
    lpg_ = Subject('LPG0001', 'LINGUAGEM DE PROGRAMAÇÃO',
                   72, ids_requirements=['AGT0001'])
    mdi_ = Subject('MDI0002', 'MATEMÁTICA DISCRETA',
                   72, ids_requirements=['LMA0001'])

    fase2.add_subjects([ali_, cdi1_, ecc_, lpg_, mdi_])

    fase3 = Phase(3)

    ams_ = Subject('AMS0002	', 'ANÁLISE E MODELAGEM DE SISTEMAS',
                   72, ids_requirements=['LPG0001'])
    cdi2_ = Subject('CDI2001', 'CÁLCULO DIFERENCIAL E INTEGRAL II',
                    72, ids_requirements=['CDI1001', 'GAN0001'])
    eda_ = Subject('EDA1001', 'ESTRUTURA DE DADOS I',
                   72, ids_requirements=['LPG0001'])
    est_ = Subject('EST0008', 'PROBABILIDADE E ESTATÍSTICA',
                   36, ids_requirements=['CDI1001'])
    poo_ = Subject('POO0001', 'PROGRAMAÇÃO ORIENTADA A OBJETOS',
                   72, ids_requirements=['AGT0001'])
    sid_ = Subject('SID0001', 'SISTEMAS DIGITAIS',
                   72, ids_requirements=['ECC0001'])

    fase3.add_subjects([ams_, cdi2_, eda_, est_, poo_, sid_])

    fase4 = Phase(4)

    ann_ = Subject('ANN0001', 'ANÁLISE NUMÉRICA',
                   36, ids_requirements=['CDI2001', 'LPG0001'])
    aoc_ = Subject('AOC0004', '	ARQUITETURA E ORG. DE COMPUTADORES',
                   72, ids_requirements=['SID0001'])
    eda2_ = Subject('EDA2001', 'ESTRUTURA DE DADOS II',
                    72, ids_requirements=['EDA1001'])
    lfa_ = Subject('LFA0001', 'LINGUAGENS FORMAIS E AUTÔMATOS',
                   72, ids_requirements=['MDI0002', 'LPG0001'])
    mep_ = Subject('MEP0004', 'METODOLOGIA DA PESQUISA',
                   36, ids_requirements=['TGS0001'])
    teg_ = Subject('TEG0002', 'TEORIA DOS GRAFOS',
                   72, ids_requirements=['EDA1001'])

    fase4.add_subjects([ann_, aoc_, eda2_, lfa_, mep_, teg_])

    fase5 = Phase(5)

    ban_ = Subject('BAN1002', 'BANCO DE DADOS I',
                   72, ids_requirements=['MDI0002', 'MDI0002', 'LPG0001'])
    cal_ = Subject('CAL0002', 'COMPLEXIDADE DE ALGORITMOS',
                   72, ids_requirements=['TEG0002'])
    cgr_ = Subject('CGR0002', 'COMPUTAÇÃO GRÁFICA',
                   72, ids_requirements=['ALI0001', 'EDA1001'])
    com_ = Subject('COM0002', 'COMPILADORES',
                   72, ids_requirements=['EDA1001', 'LFA0001'])
    soft_ = Subject('SOFT003', 'ENGENHARIA DE SOFTWARE',
                    72, ids_requirements=['AMS0002,POO0001'])
    sop_ = Subject('SOP0003', 'SISTEMAS OPERACIONAIS',
                   72, ids_requirements=['AOC0004', 'EDA1001'])

    fase5.add_subjects([ban_, cal_, cgr_, com_, soft_, sop_])

    fase6 = Phase(6)

    ban2_ = Subject('BAN2002', 'BANCO DE DADOS II',
                    72, ids_requirements=['BAN1002'])
    ihc_ = Subject('IHC0002', 'INTERAÇÃO HOMEM COMPUTADOR',
                   72, ids_requirements=['EDA1001', 'AMS0002'])
    pes_ = Subject('PES0003', 'PESQUISA OPERACIONAL',
                   72, ids_requirements=['TEG0002'])
    pim_ = Subject('PIM0002', '	PROCESSAMENTO DE IMAGENS',
                   72, ids_requirements=['ALI0001', 'EDA1001', 'ANN0001'])
    rec_ = Subject('REC0003', 'REDES DE COMPUTADORES',
                   72, ids_requirements=['AOC0004', 'LFA0001'])
    tec_ = Subject('TEC0002', '	TEORIA DA COMPUTAÇÃO',
                   72, ids_requirements=['LFA0001'])

    fase6.add_subjects([ban2_, ihc_, pes_, pim_, rec_, tec_])

    fase7 = Phase(7)

    act_ = Subject('ACT0001', 'AUTOMAÇÃO E CONTROLE',
                   72,  ids_requirements=['AOC0004', 'CGR0002'])
    emi_ = Subject('EMI0003', 'EMPREENDEDORISMO EM INFORMÁTICA',
                   72)
    iar_ = Subject('IAR0002', 'INTELIGÊNCIA ARTIFICIAL',
                   72,  ids_requirements=['TEC0002', 'CAL0002'])
    mfo_ = Subject('MFO0001', 'MÉTODOS FORMAIS',
                   72, ids_requirements=['LFA0001'])
    sdi_ = Subject('SDI0002', 'SISTEMAS DISTRIBUIDOS',
                   72, ids_requirements=['REC0003'])

    fase7.add_subjects([act_, emi_, iar_, mfo_, sdi_])

    fase8 = Phase(8)

    op1_ = Subject('OPI', 'OPTATIVA I',
                   72)
    op2_ = Subject('OPII', 'OPTATIVA II',
                   72)
    op3_ = Subject('OPIII', 'OPTATIVA III',
                   72)
    op4_ = Subject('OPIV', 'OPTATIVA IV',
                   72)
    op5_ = Subject('OPV', 'OPTATIVA V',
                   72)
    tcc1_ = Subject('TCC1004', 'TRABALHO DE CONCLUSÃO DE CURSO I',
                    36, ids_requirements=['MEP0004'])

    fase8.add_subjects([op1_, op2_, op3_, op4_, op5_, tcc1_])

    fase9 = Phase(9)

    atc_ = Subject('ATC0011', 'ATIVIDADES COMPLEMENTARES',
                   72)
    eti_ = Subject('ETI0003', 'ÉTICA EM INFORMÁTICA',
                   72)
    op6_ = Subject('OPVI', '	OPTATIVA VI',
                   72)
    op7_ = Subject('OPVII', 'OPTATIVA VII',
                   72)
    tcc2_ = Subject('TCC2005', 'TRABALHO DE CONCLUSÃO DE CURSO II',
                    36, ids_requirements=['TCC1004'])

    fase9.add_subjects([atc_, eti_, op6_, op7_, tcc2_])

    # ----------------

    computacao_2019.add_phase(fase1)
    computacao_2019.add_phase(fase2)
    computacao_2019.add_phase(fase3)
    computacao_2019.add_phase(fase4)
    computacao_2019.add_phase(fase5)
    computacao_2019.add_phase(fase6)
    computacao_2019.add_phase(fase7)
    computacao_2019.add_phase(fase8)
    computacao_2019.add_phase(fase9)

    computacao_2019.save()


if __name__ == '__main__':

    create_computacao_2012()
    create_computacao_2019()

    # for schedule in Schedule.objects:
    #     print(schedule.name)
