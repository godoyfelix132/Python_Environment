# Take information from .op file to calculate gain of 3 source follower configurations
from Analog.Examen.src.read import Read

root = "D:\\Respaldo\\Maestria\\2 - Cuatrimestre\\Analog\\1er Parcial\\Simulaciones\\practica\\Source follower\\Source follower.op"
read = Read(root)


def get_a(gmp1, gdsp1, gmp2, gdsp2, gmn3, gdsn3, conf):
    conf = conf
    g_mn3 = gmn3
    g_dsn3 = gdsn3
    g_mp1 = gmp1
    g_dsp1 = gdsp1
    g_mp2 = gmp2
    g_dsp2 = gdsp2
    if conf == '00':
        r = g_dsn3 * g_mp2 / (g_dsn3 * g_dsp1 + g_dsn3 * g_dsp2 + g_dsn3 * g_mp2 + g_dsp1 * g_dsp2)
    if conf == '01':
        r = g_mp2 * (g_dsn3 + g_mn3) / (
                g_dsn3 * g_dsp1 + g_dsn3 * g_dsp2 + g_dsn3 * g_mp2 + g_dsp1 * g_dsp2 + g_dsp1 * g_mn3 + g_dsp2 * g_mn3 + g_mn3 * g_mp2)
    if conf == '10':
        r = g_dsn3 * g_mp2 / (
                g_dsn3 * g_dsp1 + g_dsn3 * g_dsp2 + g_dsn3 * g_mp1 + g_dsn3 * g_mp2 + g_dsp1 * g_dsp2 + g_dsp2 * g_mp1)
    if conf == '11':
        r = g_mp2 * (g_dsn3 + g_mn3) / (
                g_dsn3 * g_dsp1 + g_dsn3 * g_dsp2 + g_dsn3 * g_mp1 + g_dsn3 * g_mp2 + g_dsp1 * g_dsp2 + g_dsp1 * g_mn3 + g_dsp2 * g_mn3 + g_dsp2 * g_mp1 + g_mn3 * g_mp1 + g_mn3 * g_mp2)
    return r


for m in read.mosfets:
    if m.name == 'Mpa1':
        Mpa1 = m
    if m.name == 'Mpa2':
        Mpa2 = m
    if m.name == 'Mna3':
        Mna3 = m

    if m.name == 'Mpb1':
        Mpb1 = m
    if m.name == 'Mpb2':
        Mpb2 = m
    if m.name == 'Mnb3':
        Mnb3 = m

    if m.name == 'Mpc1':
        Mpc1 = m
    if m.name == 'Mpc2':
        Mpc2 = m
    if m.name == 'Mnc3':
        Mnc3 = m

    if m.name == 'Mpd1':
        Mpd1 = m
    if m.name == 'Mpd2':
        Mpd2 = m
    if m.name == 'Mnd3':
        Mnd3 = m

    if m.name == 'Mpe1':
        Mpe1 = m
    if m.name == 'Mpe2':
        Mpe2 = m
    if m.name == 'Mne3':
        Mne3 = m

Vdd = 2.5
Vss = -2.5

Rpb1 = 1/Mpb1.gds
Rnb3 = 1/Mnb3.gds

Rpc1 = 1/Mpc1.gds
Rnc3 = 1/Mnc3.gm

Rpd1 = 1/Mpd1.gm
Rnd3 = 1/Mnd3.gds

Rpe1 = 1/Mpe1.gm
Rne3 = 1/Mne3.gm

A_b = get_a(Mpb1.gm, Mpb1.gds, Mpb2.gm, Mpb2.gds, Mnb3.gm, Mnb3.gds, '00')
A_c = get_a(Mpc1.gm, Mpc1.gds, Mpc2.gm, Mpc2.gds, Mnc3.gm, Mnc3.gds, '01')
A_d = get_a(Mpd1.gm, Mpd1.gds, Mpd2.gm, Mpd2.gds, Mnd3.gm, Mnd3.gds, '10')
A_e = get_a(Mpe1.gm, Mpe1.gds, Mpe2.gm, Mpe2.gds, Mne3.gm, Mne3.gds, '11')

print('Ab', A_b)
print('Ac', A_c)
print('Ad', A_d)
print('Ae', A_e)

