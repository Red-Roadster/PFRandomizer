import random
import time
print("Loading... please wait")
print("*Please comment any bugs/errors you find*")
time.sleep(0.1)
print('--------------------')
#this is just importing stuff from the other files
from universal_list import universal_optics 
from universal_list import universal_barrels
from universal_list import universal_underbarrels
from universal_list import universal_other
from universal_list import universal_ammo
from universal_list import universalshotgun_ammo
from universal_list import universalshotgun_barrels
from universal_list import universalsniper_optics
from universal_list import universalpistol_optics
from universal_list import universalrevolver_barrels
from universal_list import universalpistol_other
from universal_list import universalmachinepistol_other
from gun_list import Primary_gun
from gun_list import Secondary_gun


#this defines the random primary and secondary that were randomly selected.
rand_primary = random.choice(Primary_gun)
rand_secondary = random.choice(Secondary_gun)
print("Primary: " + rand_primary)




#this code selects the random attachments. There's a lot of it, but I don't think it's possible to shorten.
  
if rand_primary == 'AK12':
  from special_list import AK12AN94_other, AK12_ammo , ak12_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + ak12_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + AK12AN94_other))
  print("Ammo: " + random.choice(universal_ammo + AK12_ammo))

if rand_primary == 'AN-94':
  from special_list import AN94_ammo
  from special_list import AK12AN94_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + AK12AN94_other))
  print("Ammo: " + random.choice(universal_ammo + AN94_ammo))

if rand_primary == 'AS VAL':
  from special_list import ASVAL_ammo, ASVAL_other , val_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(val_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + ASVAL_other))
  print("Ammo: " + random.choice(universal_ammo + ASVAL_ammo))

if rand_primary == 'Scar-L':
  from special_list import ScarL_ammo, ScarL_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + ScarL_other))
  print("Ammo: " + random.choice(universal_ammo + ScarL_ammo))

if rand_primary == 'AUG A1':
  from special_list import AUGA1_ammo, AUG_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AUG_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + AUGA1_ammo))

if rand_primary == 'M16A4':
  from special_list import M16_ammo, M16AK_other, M16_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + M16_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + M16AK_other))
  print("Ammo: " + random.choice(universal_ammo + M16_ammo))

if rand_primary == 'M16A3':
  from special_list import M16_ammo, M16AK_other, M16_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + M16_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + M16AK_other))
  print("Ammo: " + random.choice(universal_ammo + M16_ammo))

if rand_primary == 'G36':
  from special_list import AK12AN94_other, G36_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + AK12AN94_other))
  print("Ammo: " + random.choice(universal_ammo + G36_ammo))

if rand_primary == 'M16A1':
  from special_list import a1_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + a1_ammo))



if rand_primary == 'Type 20':
  from special_list import Type20_ammo, Type20_optic, Type20_barrel, Type20_other
  print("Optic: " + random.choice(universal_optics + Type20_optic))
  print("Barrel: "+ random.choice(universal_barrels + Type20_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Type20_other))
  print("Ammo: " + random.choice(universal_ammo + Type20_ammo))

if rand_primary == 'AUG A2':
  from special_list import AUGA2_ammo, AUG_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AUG_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + AUGA2_ammo))


if rand_primary == 'K2':
  from special_list import K2_other, K2_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + K2_other))
  print("Ammo: " + random.choice(universal_ammo + K2_ammo))

if rand_primary == 'FAMAS F1':
  from special_list import AK_underbarrel, Famas_other, Famas_ammo, CSbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + CSbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + Famas_other))
  print("Ammo: " + random.choice(universal_ammo + Famas_ammo))

if rand_primary == 'AK47':
  from special_list import M16AK_other , AK_underbarrel , AK_ammo, Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + M16AK_other))
  print("Ammo: " + random.choice(universal_ammo + AK_ammo))

if rand_primary == 'AUG A3':
  from special_list import AUGA3_ammo , AUG_underbarrel, Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AUG_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + AUGA3_ammo))

if rand_primary == 'L85A2':
  from special_list import AK_underbarrel , Famas_ammo , Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + Famas_ammo))

if rand_primary == 'HK416':
  from special_list import K2_other , AUGA3_ammo , CSbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + CSbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + K2_other))
  print("Ammo: " + random.choice(universal_ammo + AUGA3_ammo))

if rand_primary == 'AK74':
  from special_list import AK74_ammo , M16AK_other , Carbinebarrel, AK_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + M16AK_other))
  print("Ammo: " + random.choice(universal_ammo + AK74_ammo))

if rand_primary == 'AKM':
  from special_list import AKM_ammo , M16AK_other, AK_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + M16AK_other))
  print("Ammo: " + random.choice(universal_ammo + AKM_ammo))

if rand_primary == 'AK103':
  from special_list import AK_underbarrel , AK103_barrel , AK103_ammo, ScarL_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + AK103_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + ScarL_other))
  print("Ammo: " + random.choice(universal_ammo + AK103_ammo))

if rand_primary == 'TAR-21':
  from special_list import TAR21_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + TAR21_ammo))

if rand_primary == 'Type 88':
  from special_list import AK_underbarrel , Type88_other , Type88_ammo, CSbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + CSbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + Type88_other))
  print("Ammo: " + random.choice(universal_ammo + Type88_ammo))

if rand_primary == 'M231':
  from special_list import M231_other , M231_ammo , Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + M231_other))
  print("Ammo: " + random.choice(universal_ammo + M231_ammo))

if rand_primary == 'C7A2':
  from special_list import C7_other , C7_ammo , Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + C7_other))
  print("Ammo: " + random.choice(universal_ammo + C7_ammo))

if rand_primary == 'STG-44':
  from special_list import STG_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + STG_ammo))

if rand_primary == 'G11K2':
  from special_list import AK_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'M14':
  from special_list import M14_optic , AK_underbarrel , M14_ammo
  print("Optic: " + random.choice(M14_optic))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + M14_ammo))

if rand_primary == 'Beowulf ECR':
  from special_list import AK_underbarrel , M16AK_other , ECR_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + ECR_ammo))

if rand_primary == 'Scar-H':
  from special_list import Carbinebarrel , RR_other , ScarH_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RR_other))
  print("Ammo: " + random.choice(universal_ammo + ScarH_ammo))

if rand_primary == 'AK12BR':
  from special_list import R_other , AK12BR_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + AK12BR_ammo))

if rand_primary == 'G3A3':
  from special_list import uG3_ammo, g3_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + g3_other))
  print("Ammo: " + random.choice(universal_ammo + uG3_ammo))

if rand_primary == 'AG-3':
  from special_list import R_other , G3_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + G3_ammo))

if rand_primary == 'HK417':
  from special_list import HK417_barrel , RF_other , G3_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + HK417_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RF_other))
  print("Ammo: " + random.choice(universal_ammo + G3_ammo))

if rand_primary == 'Henry 45-70':
  from special_list import Henry_other , Henry_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Henry_other))
  print("Ammo: " + random.choice(Henry_ammo))

if rand_primary == 'FAL 50.00':
  from special_list import AK_underbarrel , FAL50_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + FAL50_ammo))

if rand_primary == 'M4A1':
  from special_list import Carbinebarrel , RRF_other , M16_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + M16_ammo))

if rand_primary == 'G36K':
  from special_list import R_other , SB_Barrel , G36_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SB_Barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + G36_ammo))

if rand_primary == 'M4':
  from special_list import Carbinebarrel , RRF_other , M16_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + M16_ammo))

if rand_primary == 'L22':
  from special_list import SB_Barrel , Famas_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SB_Barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + Famas_ammo))

if rand_primary == 'Scar PDW':
  from special_list import SB_Barrel , RRF_other , ScarPDW_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SB_Barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + ScarPDW_ammo))

if rand_primary == 'AKU12':
  from special_list import CSbarrel , RF_other, AKU_ammo  
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + CSbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RF_other))
  print("Ammo: " + random.choice(universal_ammo + AKU_ammo))


if rand_primary == 'Groza-1':
  from special_list import Groza_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + Groza_ammo))

if rand_primary == 'OTS-126':
  from special_list import OTS_barrel , OTS_other , OTS_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + OTS_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + OTS_other))
  print("Ammo: " + random.choice(universal_ammo + OTS_ammo))

if rand_primary == 'AK12C':
  from special_list import R_other , CSbarrel , AK12C_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + CSbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + AK12C_ammo))

if rand_primary == 'Honey Badger':
  from special_list import Badger_barrel , RRF_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Badger_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'K1A':
  from special_list import K1A_ammo , R_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + K1A_ammo))

if rand_primary == 'SR-3M':
  from special_list import RF_other , SR3M_ammo , SR3M_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SR3M_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RF_other))
  print("Ammo: " + random.choice(universal_ammo + SR3M_ammo))

if rand_primary == 'Groza-4':
  from special_list import Groza4_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(Groza4_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'MC51':
  from special_list import MC51_barrel, MC51_other, MC51_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MC51_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + MC51_other))
  print("Ammo: " + random.choice(universal_ammo + MC51_ammo))

if rand_primary == 'FAL 50.63 Para':
  from special_list import AK_underbarrel , RF_other , FAL63_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + RF_other))
  print("Ammo: " + random.choice(universal_ammo + FAL63_ammo))

if rand_primary == '1858 Carbine':
  from special_list import c1858_barrel , c1858_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(c1858_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(c1858_ammo))

if rand_primary == 'AK105':
  from special_list import AK103_barrel , AK_underbarrel , AK105_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + AK103_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + AK105_ammo))

if rand_primary == 'Jury':
  from special_list import c1858_barrel, Jury_other , Jury_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(c1858_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Jury_other))
  print("Ammo: " + random.choice(Jury_ammo))

if rand_primary == 'KAC SRR':
  from special_list import Groza4_barrel , Jury_other , KAC_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: None")
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Jury_other))
  print("Ammo: " + random.choice(KAC_ammo))


if rand_primary == 'Gyrojet Carbine':
  from special_list import Gyro_other , Gyro_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: "  + random.choice(universal_other + Gyro_other))
  print("Ammo: " + random.choice(Gyro_ammo))

if rand_primary == 'C8A2':
  from special_list import C7_other , C7_ammo , Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + C7_other))
  print("Ammo: " + random.choice(universal_ammo + C7_ammo))

if rand_primary == 'X95R':
  from special_list import X95R_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + X95R_ammo))

if rand_primary == 'HK51B':
  from special_list import HKB_barrel , HKB_other , G3_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + HKB_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + HKB_other))
  print("Ammo: " + random.choice(universal_ammo + G3_ammo))

if rand_primary == 'Can Cannon':
  from special_list import ccannon_barrel , ccannon_other , ccannon_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(ccannon_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + ccannon_other))
  print("Ammo: " + random.choice(ccannon_ammo))
  
if rand_primary == 'KSG-12':
  from special_list import KSG_barrel , r870_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + KSG_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + r870_ammo))

if rand_primary == 'Model 870':
  from special_list import fchoke_barrel , AK_underbarrel , r870_other , r870_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + fchoke_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + r870_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + r870_ammo))

if rand_primary == 'DBV12':
  from special_list import R_other , DBV_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + DBV_ammo))

if rand_primary == 'KS-23M':
  from special_list import KS23M_barrel , ref_other , KS23M_ammo , AK_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + KS23M_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + ref_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + KS23M_ammo))

if rand_primary == 'Saiga-12':
  from special_list import Saiga_barrel , AK_underbarrel , Saiga_ammo , RR_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + Saiga_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + RR_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + Saiga_ammo))

if rand_primary == 'Stevens DB':
  from special_list import Re_other , db_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(db_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other  + Re_other))
  print("Ammo: " + random.choice(universalshotgun_ammo))

if rand_primary == 'E Gun':
  from special_list import Egun_barrel , Egun_other , Egun_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(Egun_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Egun_other))
  print("Ammo: " + random.choice(Egun_ammo))

if rand_primary == 'AA-12':
  from special_list import KS23M_barrel , AK_underbarrel , AA12_other , AA12_ammo 
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + KS23M_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + AA12_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + AA12_ammo))

if rand_primary == 'SPAS-12':
  from special_list import AK_underbarrel , Spas_other , Spas_optics
  print("Optic: " + random.choice(universal_optics + Spas_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + Spas_other))
  print("Ammo: " + random.choice(universalshotgun_ammo))

if rand_primary == 'DT11 Pro':
  from special_list import Dt11_optics , Dt11_barrel , Dt11_other, dt11_ammo
  print("Optic: " + random.choice(universal_optics + Dt11_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + Dt11_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Dt11_other))
  print("Ammo: " + random.choice(dt11_ammo))

if rand_primary == 'USAS-12':
  from special_list import AA12_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + AA12_other))
  print("Ammo: " + random.choice(universalshotgun_ammo))

if rand_primary == 'MP5K':
  from special_list import MP5K_ammo , MP5K_barrel , MP5K_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + MP5K_other))
  print("Ammo: " + random.choice(universal_ammo + MP5K_ammo))

if rand_primary == 'UMP45':
  from special_list import MP5K_barrel , UMP_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + UMP_ammo))

if rand_primary == 'G36C':
  from special_list import SB_Barrel , R_other , G36c_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SB_Barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + G36c_ammo))

if rand_primary == 'MP7':
  from special_list import Osprey_barrel , MP7_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + MP7_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'Mac10':
  from special_list import mac_barrel , mac_other , mac_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + mac_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + mac_other))
  print("Ammo: " + random.choice(universal_ammo + mac_ammo))

if rand_primary == 'P90':
  from special_list import MP5K_barrel , P90_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + P90_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'Colt MARS':
  from special_list import SB_Barrel, RRF_other, mars_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SB_Barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + mars_ammo))

if rand_primary == 'MP5':
  from special_list import MP5K_barrel , AK_underbarrel , MP5_other , plusp_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + MP5_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_primary == 'Colt SMG 633':
  from special_list import MP5K_barrel , AK_underbarrel , RRF_other ,  Coltsmg_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + Coltsmg_ammo))

if rand_primary == 'L2A3':
  from special_list import L2A3_barrel , L2A3_ammo , RR_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + L2A3_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RR_other))
  print("Ammo: " + random.choice(universal_ammo + L2A3_ammo))

if rand_primary == 'MP5SD':
  from special_list import AK_underbarrel , MP5_other , plusp_ammo , MP5SD_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5SD_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + MP5_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_primary == 'MP10':
  from special_list import MP5K_barrel , plusp_ammo , MP10
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + MP10))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_primary == 'M3A1':
  from special_list import Osprey_barrel , R_other, M3A1
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + M3A1))

if rand_primary == 'MP5/10':
  from special_list import MP5K_barrel , AK_underbarrel , MP510_other , MP510_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + MP510_other))
  print("Ammo: " + random.choice(universal_ammo + MP510_ammo))

if rand_primary == 'Uzi':
  from special_list import MP5K_barrel , Uzi_other , Uzi_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Uzi_other))
  print("Ammo: " + random.choice(universal_ammo + Uzi_ammo))

if rand_primary == 'AUG A3 Para XS':
  from special_list import MP510_ammo , MP5K_barrel 
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + MP510_ammo))

if rand_primary == 'K7':
  from special_list import K7_ammo , R_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: None")
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + K7_ammo))

if rand_primary == 'AKS74U':
  from special_list import SB_Barrel , RRF_other , aks_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + SB_Barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + aks_ammo))

if rand_primary == 'PPSH-41':
  from special_list import ppsh_barrel , ppsh_ubarrel , Re_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + ppsh_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + ppsh_ubarrel))
  print("Other: " + random.choice(universal_other + Re_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'FAL Para Shorty':
  from special_list import FAL50_ammo , fals_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + fals_other))
  print("Ammo: " + random.choice(universal_ammo + FAL50_ammo))

if rand_primary == 'Kriss Vector':
  from special_list import MP5K_barrel , RR_other , kriss_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RR_other))
  print("Ammo: " + random.choice(universal_ammo + kriss_ammo))

if rand_primary == 'PP-19 Bizon':
  from special_list import Osprey_barrel , RRF_other , bizon_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + bizon_ammo))

if rand_primary == 'MP40':
  from special_list import Osprey_barrel , plusp_ammo , R_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_primary == 'X95 SMG':
  from special_list import Osprey_barrel , x95_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + x95_ammo))

if rand_primary == 'Tommy Gun':
  from special_list import tommy_optic , tommy_barrel , tommy_ubarrel , tommy_other , tommy_ammo
  print("Optic: " + random.choice(universal_optics + tommy_optic))
  print("Barrel: "+ random.choice(universal_barrels + tommy_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + tommy_ubarrel))
  print("Other: " + random.choice(universal_other + tommy_other))
  print("Ammo: " + random.choice(universal_ammo + tommy_ammo))

if rand_primary == 'Rama 1130':
  from special_list import MP5K_barrel , rama_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + rama_ammo))

if rand_primary == 'BWC9 A':
  from special_list import bwc_barrel , bwc_other, bwc_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + bwc_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + bwc_other))
  print("Ammo: " + random.choice(universal_ammo + bwc_ammo))

if rand_primary == 'Five-0':
  from special_list import five_other, five_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + five_other))
  print("Ammo: " + random.choice(universal_ammo + five_ammo))

if rand_primary == 'MK11':
  from special_list import assbarrel , mk11_other , mk11_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + assbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + mk11_other))
  print("Ammo: " + random.choice(universal_ammo + mk11_ammo))

if rand_primary == 'SKS':
  from special_list import RF_other , assbarrel , AK_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + assbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RF_other))
  print("Ammo: " + random.choice(universal_ammo + AK_ammo))

if rand_primary == 'SL-8':
  from special_list import AK_underbarrel , mmanbarrel , sl8_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + mmanbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + sl8_ammo))

if rand_primary == 'VSS Vintorez':
  from special_list import val_barrel , val_other , val_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(val_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + val_other))
  print("Ammo: " + random.choice(universal_ammo + val_ammo))

if rand_primary == 'MSG90':
  from special_list import AK_underbarrel , msg_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + msg_ammo))

if rand_primary == 'M21':
  from special_list import M14_optic , M14_ammo , AK_underbarrel
  print("Optic: " + random.choice(M14_optic))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + M14_ammo))

if rand_primary == 'Beowulf TCR':
  from special_list import RRF_other , tcr_barrel , tcr_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + tcr_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + tcr_ammo))

if rand_primary == 'SA58 SPR':
  from special_list import FAL50_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + FAL50_ammo))

if rand_primary == 'Scar SSR':
  from special_list import M14_ammo , ssr_barrel , RR_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + ssr_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RR_other))
  print("Ammo: " + random.choice(universal_ammo + M14_ammo))

if rand_primary == 'Colt LMG':
  from special_list import Carbinebarrel , coltl_other , M16_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + coltl_other))
  print("Ammo: " + random.choice(universal_ammo + M16_ammo))

if rand_primary == 'M60':
  from special_list import G3_ammo , m60_optic , Re_other
  print("Optic: " + random.choice(universal_optics + m60_optic))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Re_other))
  print("Ammo: " + random.choice(universal_ammo + G3_ammo))

if rand_primary == 'AUG HBAR':
  from special_list import hbar_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + hbar_ammo))

if rand_primary == 'MG36':
  from special_list import AK12AN94_other, G36_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + AK12AN94_other))
  print("Ammo: " + random.choice(universal_ammo + G36_ammo))

if rand_primary == 'RPK12':
  from special_list import Carbinebarrel , R_other , rpk1_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + R_other))
  print("Ammo: " + random.choice(universal_ammo + rpk1_ammo))

if rand_primary == 'L86 LSW':
  from special_list import AK_underbarrel , Famas_ammo , Carbinebarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + Carbinebarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + Famas_ammo))

if rand_primary == 'RPK':
  from special_list import AK_ammo , AK_underbarrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + AK_ammo))

if rand_primary == 'HK21E':
  from special_list import G3_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + G3_ammo))

if rand_primary == 'HAMR IAR':
  from special_list import CSbarrel , RR_other , hamr_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + CSbarrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + RR_other))
  print("Ammo: " + random.choice(universal_ammo + hamr_ammo))

if rand_primary == 'RPK74':
  from special_list import AK_underbarrel , rpk7_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + rpk7_ammo))

if rand_primary == 'MG3KWS':
  from special_list import m60_optic , mg3_other , mg3_ammo
  print("Optic: " + random.choice(universal_optics + m60_optic))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + mg3_other))
  print("Ammo: " + random.choice(universal_ammo + mg3_ammo))

if rand_primary == 'MGV-176':
  from special_list import mgv_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + mgv_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'Stoner 96':
  from special_list import stoner_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + stoner_ammo))

if rand_primary == 'ChainSAW':
  from special_list import stoner_ammo, saw_underbarrel
  print("Optic: None")
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(saw_underbarrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + stoner_ammo))

if rand_primary == 'MG42':
  from special_list import mg4_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + mg4_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_primary == 'Intervention':
  from special_list import cqb_barrel , inter_other , inter_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + cqb_barrel ))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(inter_ammo))

if rand_primary == 'Model 700':
  from special_list import r700_barrel , inter_other , r700_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + r700_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(r700_ammo))

if rand_primary == 'Dragonuv SVU':
  from special_list import svu_optic , svu_barrel , svu_other , svu_ammo
  print("Optic: " + random.choice(universalsniper_optics + svu_optic))
  print("Barrel: "+ random.choice(universal_barrels + svu_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + svu_other))
  print("Ammo: " + random.choice(svu_ammo))

if rand_primary == 'AWS':
  from special_list import r700_ammo , aws_other
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: None")
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other +  aws_other))
  print("Ammo: " + random.choice(r700_ammo))

if rand_primary == 'AWM':
  from special_list import awm_ammo , awm_other
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + awm_other))
  print("Ammo: " + random.choice(awm_ammo))

if rand_primary == 'TRG-42':
  from special_list import r700_barrel , inter_other , trg_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + r700_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(trg_ammo))

if rand_primary == 'Mosin Nagant':
  from special_list import inter_other , mosin_barrel , mosin_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + mosin_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(mosin_ammo))

if rand_primary == 'Dragonuv SVDS':
  from special_list import mosin_barrel , RRF_other , svu_ammo , AK_underbarrel
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + mosin_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + AK_underbarrel))
  print("Other: " + random.choice(universal_other + RRF_other))
  print("Ammo: " + random.choice(universal_ammo + svu_ammo))

if rand_primary == 'M1903':
  from special_list import inter_other , m19_barrel , m19_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + m19_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(m19_ammo))

if rand_primary == 'K14':
  from special_list import k14_ammo , mosin_barrel , inter_other
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + mosin_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(k14_ammo))

if rand_primary == 'Hecate II':
  from special_list import inter_other , hecate_barrel , hecate_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + hecate_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + inter_other))
  print("Ammo: " + random.choice(hecate_ammo))

if rand_primary == 'FT300':
  from special_list import r700_barrel , ft_ubarrel , ft_other , ft_ammo , ft_optic
  print("Optic: " + random.choice(universalsniper_optics + ft_optic))
  print("Barrel: "+ random.choice(universal_barrels + r700_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + ft_ubarrel))
  print("Other: " + random.choice(universal_other + ft_other))
  print("Ammo: " + random.choice(ft_ammo))

if rand_primary == 'M107':
  from special_list import cqb_barrel , m107_other , hecate_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + cqb_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + m107_other))
  print("Ammo: " + random.choice(hecate_ammo))

if rand_primary == 'Steyr Scout':
  from special_list import r700_barrel , aws_other , scout_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels + r700_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + aws_other))
  print("Ammo: " + random.choice(scout_ammo))

if rand_primary == 'NTW-20':
  from special_list import ntw_barrel , aws_other , ntw_ammo, ntw_optic
  print("Optic: " + random.choice(ntw_optic))
  print("Barrel: " + random.choice(universal_barrels + ntw_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels + ntw_ammo))
  print("Other: " + random.choice(universal_other + aws_other))
  print("Ammo: " + random.choice(ntw_ammo))

if rand_primary == 'WA2000':
  from special_list import wa_ammo
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(wa_ammo))




#this prints a line that seperates the different weapons, making it easier to read.
print("--------------------")







print("Secondary: " + rand_secondary)
if rand_secondary == 'M9': 
  from special_list import m9_other, MP5K_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Other: " + random.choice(universalpistol_other + m9_other))
  print("Ammo: " + random.choice(universal_ammo))


if rand_secondary == 'Glock 17':
  from special_list import MP5K_barrel , g17_other , g17_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + MP5K_barrel))
  print("Other: " + random.choice(universalpistol_other + g17_other))
  print("Ammo: " + random.choice(universal_ammo + g17_ammo))

if rand_secondary == 'M1911A1':
  from special_list import m1911_other , m1911_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Other: " + random.choice(universalpistol_other + m1911_other))
  print("Ammo: " + random.choice(universal_ammo + m1911_ammo))

if rand_secondary == 'M17':
  from special_list import m17_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo + m17_ammo))

if rand_secondary == 'Desert Eagle L5':
  from special_list import deagle_barrel , deagle_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + deagle_barrel))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo + deagle_ammo))

if rand_secondary == 'G21':
  from special_list import g17_barrel , g17_other, g21_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g17_barrel))
  print("Other: " + random.choice(universalpistol_other + g17_other))
  print("Ammo: " + random.choice(universal_ammo + g21_ammo))

if rand_secondary == 'G23':
  from special_list import g17_barrel , g17_other, g23_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g17_barrel))
  print("Other: " + random.choice(universalpistol_other + g17_other))
  print("Ammo: " + random.choice(universal_ammo + g23_ammo))

if rand_secondary == 'M45A1':
  from special_list import m45_other , Osprey_barrel , m45_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other + m45_other))
  print("Ammo: " + random.choice(universal_ammo + m45_ammo))

if rand_secondary == 'G40':
  from special_list import g17_other , g40_barrel , g40_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g40_barrel))
  print("Other: " + random.choice(universalpistol_other + g17_other))
  print("Ammo: " + random.choice(universal_ammo + g40_ammo))

if rand_secondary == 'KG-99':
  from special_list import g17_barrel , kg_other , kg_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g17_barrel))
  print("Other: " + random.choice(universalpistol_other +kg_other ))
  print("Ammo: " + random.choice(universal_ammo + kg_ammo))

if rand_secondary == 'G50':
  from special_list import g50_barrel , g50_other
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g50_barrel))
  print("Other: " + random.choice(universalpistol_other+ g50_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_secondary == 'Five Seven':
  from special_list import Osprey_barrel , five7_other
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other+ five7_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_secondary == 'Zip 22':
  from special_list import Osprey_barrel , zip_other , zip_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other + zip_other))
  print("Ammo: " + random.choice(universal_ammo + zip_ammo))

if rand_secondary == 'GI M1':
  from special_list import g50_barrel , m1911_other  
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g50_barrel))
  print("Other: " + random.choice(universalpistol_other + m1911_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_secondary == 'Hardballer':
  from special_list import g40_barrel , m1911_other , plusp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g40_barrel))
  print("Other: " + random.choice(universalpistol_other + m1911_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_secondary == 'Izhevsk PB':
  from special_list import makarov_optic , makarov_other , makarov_ammo
  print("Optic: " + random.choice(makarov_optic))
  print("Barrel: None")
  print("Other: " + random.choice(universalpistol_other + makarov_other))
  print("Ammo: " + random.choice(universal_ammo + makarov_ammo))

if rand_secondary == 'Makarov PM':
  from special_list import makarov_optic , makarov_other , makarov_ammo
  print("Optic: " + random.choice(makarov_optic))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Other: " + random.choice(universalpistol_other + makarov_other))
  print("Ammo: " + random.choice(universal_ammo + makarov_ammo))

if rand_secondary == 'GB-22':
  from special_list import gb_barrel , gb_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + gb_barrel))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo + gb_ammo))

if rand_secondary == 'Desert Eagle XIX':
  from special_list import deaglex_barrel , deaglex_other , deagle_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + deaglex_barrel))
  print("Other: " + random.choice(universalpistol_other + deaglex_other))
  print("Ammo: " + random.choice(universal_ammo + deagle_ammo))

if rand_secondary == 'Automag III':
  from special_list import automag_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo + automag_ammo))

if rand_secondary == 'Gyrojet Mark I':
  from special_list import Gyro_ammo , Gyro_other , Gyro_barrel
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(Gyro_barrel))
  print("Other: " + random.choice(universalpistol_other + Gyro_other))
  print("Ammo: " + random.choice(universal_ammo + Gyro_ammo))

if rand_secondary == 'GSP':
  from special_list import gsp_barrel , gsp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + gsp_barrel))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo + gsp_ammo))

if rand_secondary == 'Grizzly':
  from special_list import grizzly_barrel
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + grizzly_barrel))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_secondary == 'M2011':
  from special_list import m1911_other , g17_barrel , plusp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g17_barrel))
  print("Other: " + random.choice(universalpistol_other + m1911_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_secondary == 'Alien':
  from special_list import Osprey_barrel , plusp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_secondary == 'AF2011-A1':
  from special_list import m1911_other , Osprey_barrel , af2011_ammo 
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other + m1911_other))
  print("Ammo: " + random.choice(universal_ammo + af2011_ammo))

if rand_secondary == 'G18C':
  from special_list import g17_barrel , g18_other , g18_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g17_barrel))
  print("Other: " + random.choice(universalpistol_other + g18_other))
  print("Ammo: " + random.choice(universal_ammo + g18_ammo))

if rand_secondary == '93R':
  from special_list import m9_other , Osprey_barrel , plusp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other + m9_other ))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_secondary == 'PP-2000':
  from special_list import pp_other , Osprey_barrel , pp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalmachinepistol_other+ pp_other))
  print("Ammo: " + random.choice(universal_ammo + pp_ammo))

if rand_secondary == 'TEC-9':
  from special_list import kg_other , tec_barrel , kg_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + tec_barrel))
  print("Other: " + random.choice(universalpistol_other + kg_other))
  print("Ammo: " + random.choice(universal_ammo + kg_ammo))

if rand_secondary == 'Micro Uzi':
  from special_list import kg_other , Osprey_barrel , microu_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalpistol_other + kg_other))
  print("Ammo: " + random.choice(universal_ammo + microu_ammo))

if rand_secondary == 'Škorpion VZ.61':
  from special_list import g17_barrel , skorp_other , skorp_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + g17_barrel))
  print("Other: " + random.choice(universalpistol_other + skorp_other))
  print("Ammo: " + random.choice(universal_ammo + skorp_ammo))

if rand_secondary == 'ASMI':
  from special_list import plusp_ammo , Osprey_barrel , asmi_other
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + Osprey_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + asmi_other))
  print("Ammo: " + random.choice(universal_ammo + plusp_ammo))

if rand_secondary == 'MP1911':
  from special_list import mp1911_barrel , mp1911_other , mp1911_ammo
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels + mp1911_barrel))
  print("Other: " + random.choice(universalpistol_other + mp1911_other))
  print("Ammo: " + random.choice(universal_ammo + mp1911_ammo))

if rand_secondary == 'Arm Pistol':
  from special_list import Famas_ammo , arm_other
  print("Optic: " + random.choice(universalpistol_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Other: " + random.choice(universalmachinepistol_other + arm_other))
  print("Ammo: " + random.choice(universal_ammo + Famas_ammo))

if rand_secondary == 'MP412 Rex':
  from special_list import rex_barrel , speedl , rex_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalrevolver_barrels + rex_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + speedl))
  print("Ammo: " + random.choice(universal_ammo + rex_ammo))

if rand_secondary == 'Mateba 6':
  from special_list import rex_barrel , speedl , mateba_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalrevolver_barrels + rex_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + speedl))
  print("Ammo: " + random.choice(universal_ammo + mateba_ammo))

if rand_secondary == '1858 New Army':
  from special_list import r1858_barrel , r1858_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalrevolver_barrels + r1858_barrel))
  print("Other: " + random.choice(universalmachinepistol_other))
  print("Ammo: " + random.choice(universal_ammo + r1858_ammo))

if rand_secondary == 'Redhawk 44':
  from special_list import rex_barrel , redhawk_other , redhawk_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalrevolver_barrels + rex_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + redhawk_other))
  print("Ammo: " + random.choice(universal_ammo + redhawk_ammo))

if rand_secondary == 'Judge':
  from special_list import judge_barrel , judge_other 
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalrevolver_barrels + judge_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + judge_other))
  print("Ammo: " + random.choice(universalshotgun_ammo))

if rand_secondary == 'Executioner':
  from special_list import judge_barrel , judge_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalrevolver_barrels + judge_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + judge_other))
  print("Ammo: " + random.choice(universal_ammo))

if rand_secondary == 'Super Shorty':
  from special_list import fchoke_barrel , super_ammo, serbu_other  
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + fchoke_barrel))
  print("Other: " + random.choice(universal_other + serbu_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + super_ammo))

if rand_secondary == 'SFG 50':
  from special_list import hecate_ammo , Re_other
  print("Optic: " + random.choice(universalsniper_optics))
  print("Barrel: "+ random.choice(universal_barrels))
  print("Other: " + random.choice(universal_other + Re_other))
  print("Ammo: " + random.choice(universal_ammo + hecate_ammo))

if rand_secondary == 'M79 Thumper':
  from special_list import m79_optic , m79_barrel , Re_other , m79_ammo
  print("Optic: " + random.choice(universal_optics + m79_optic))
  print("Barrel: "+ random.choice(m79_barrel))
  print("Other: " + random.choice(universalmachinepistol_other + Re_other))
  print("Ammo: " + random.choice(universal_ammo + m79_ammo))

if rand_secondary == 'Advanced Coilgun':
  from special_list import Egun_barrel , Egun_other , Egun_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(Egun_barrel))
  print("Underbarrel: "+ random.choice(universal_underbarrels))
  print("Other: " + random.choice(universal_other + Egun_other))
  print("Ammo: " + random.choice(Egun_ammo))

if rand_secondary == 'Sawed Off':
  from special_list import db_barrel, sawed_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(db_barrel))
  print("Other: " + random.choice(universal_other + sawed_other))
  print("Ammo: " + random.choice(universalshotgun_ammo))

if rand_secondary == 'Saiga-12U':
  from special_list import saigau_other , Saiga_ammo , fchoke_barrel
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universalshotgun_barrels + fchoke_barrel))
  print("Other: " + random.choice(universal_other + saigau_other))
  print("Ammo: " + random.choice(universalshotgun_ammo + Saiga_ammo))

if rand_secondary == 'Obrez':
  from special_list import mosin_ammo , obrez_barrel , obrez_other
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + obrez_barrel))
  print("Other: " + random.choice(universal_other + obrez_other))
  print("Ammo: " + random.choice(mosin_ammo))

if rand_secondary == 'SASS 308':
  from special_list import sass_barrel , sass_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: "+ random.choice(universal_barrels + sass_barrel))
  print("Other: " + random.choice(universal_other))
  print("Ammo: " + random.choice(universal_ammo + sass_ammo))

if rand_secondary == 'Boxy Buster':
  from special_list import buster_ammo
  print("Optic: " + random.choice(universal_optics))
  print("Barrel: None")
  print("Other: " + random.choice(universalmachinepistol_other))
  print("Ammo: " + random.choice(buster_ammo))


print("--------------------")
from gun_list import Melee
print("Melee: " + random.choice(Melee))



print("--------------------")
from gun_list import Grenade
print("Grenade: " + random.choice(Grenade))


print("--------------------")
from challenge_list import Challenges
print("Extra Challenge: " + random.choice(Challenges))

print("--------------------")



