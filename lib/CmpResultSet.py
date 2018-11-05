from lib import ConfigValues
import re

def CmpData(row1,row2, claim_list):
    OutData = []
    rowCnt1 = len(row1)
    rowCnt2 = len(row2)
    if rowCnt1 != rowCnt2:
        OutData = ('Test version records count# %d did matched with Prod version records count %d' %(rowCnt1,rowCnt2))
        return OutData
    else:
            datadic1 = {}
            datadic2 = {}
            
            for rec in row1:
                rec_key = str(rec[0]) + '|' + str(rec[1]) + '|' + str(rec[2])
                claim_rec = rec
                datadic1[rec_key] = claim_rec

            for rec in row2:
                rec_key = str(rec[0]) + '|' + str(rec[1]) + '|' + str(rec[2])
                claim_rec = rec
                datadic2[rec_key] = claim_rec

            for rec_key in datadic1:
                cmp1 = datadic1[rec_key]
                cmp2 = datadic2[rec_key]
                getCLM = re.search('[0-9A-Za-z]*|', rec_key)
                clm = getCLM.group(0)
                c = 0
                for i in ConfigValues.Tbl_Fields:
                    if cmp1[c] != cmp2[c]:
                        OutData.append('For claim: ' + clm + '  Field: '+ str(i).ljust(35) + ' Test version value: ' +str(cmp1[c]) + ' not matched to PROD version Value: ' + str(cmp2[c]))
                    c += 1
            return OutData

