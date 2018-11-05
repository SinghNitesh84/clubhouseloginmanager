import cx_Oracle
from lib import ConfigValues 
from lib import EnvDetails


def InputDataCopy(claim_list):
    con = cx_Oracle.connect(EnvDetails.DWEIHPRD_conn)
    cur = con.cursor()
    sql = 'select * from OUT_GROUPER.OH_GRPR_APR_CALL_3M where Claim_num in '+ str(tuple(claim_list))
    if sql.endswith(",)"):
        sql = sql.replace(",)", ")")
    cur.execute(sql)
    row1 = cur.fetchall()
    cur.close()
    con.close()
    rec = []
    for row in row1:
        rec.append(row)
    con = cx_Oracle.connect(EnvDetails.DWEIHDVX_conn)
    cur = con.cursor()
    cur.bindarraysize = len(rec)
    try :
        cur.execute('delete from OUT_GROUPER.OT_GRPR_APR_CALL_3M_ERROR')
        cur.execute('delete from OUT_GROUPER.OH_GRPR_APR_CALL_3M_ERROR')
        cur.execute('delete from OUT_GROUPER.OT_GRPR_APR_CALL_3M')
        cur.execute('delete from OUT_GROUPER.OH_GRPR_APR_CALL_3M')
        con.commit()
        cur.executemany("insert into OUT_GROUPER.OT_GRPR_APR_CALL_3M (OT_GRPR_APR_CALL_3M_SK, CLAIM_NUM, LINE_NUM, LINE_SEQUENCE_NUM, ADMIT_FROM_DT, ADMIT_DX_CD, AGE_IN_DAYS, AGE_IN_YEARS, BIRTH_DT, BIRTH_WEIGHT, BIRTH_WEIGHT_OPTION, CLAIM_TYPE, CD_VERSION_DT, CD_VERSION_MAPPING_TYPE, DX_CD, DX_PRESENT_ON_ADMISSION, DISCHARGE_TO_DT, DISCHARGE_APR_DRG_OPTION, DISCHARGE_STATUS, ENABLE_SUGGESTED_PRIN_PROC, EXT_CAUSE_OF_INJURY_DX_CD, EXT_CAUSE_OF_INJURY_DX_POA, GROUPER_ICD_VERSION_QUALIFIER, GROUPER_TYPE, GROUPER_VERSION, HAC_AGENCY_IND, HAC_VERSION, ICD_VERSION_QUALIFIER, PAYER_LOGIC_IND, PROC_CD, PROC_SERVICE_DT, REORDER, SCHEDULE_TYPE, SEX, SUPPRESS_HAC_CATEGORIES, TOTAL_CHARGES, USER_KEY_1, USER_KEY_2, LENGTH_OF_STAY, CONTENT_VERSION, FINANCIAL_PAYER, MEMBER_BENEFIT_PLAN, NON_COVERED_CHARGES, PATIENT_RESPONSIBILITY_AMT, CLAIM_EDITS, DX_HAC_CATEGORY, DX_RELATED_GROUP, DRG_FOL_HAC_ADRG_PROCESSING, SOI_FOL_HAC_ADRG_PROCESSING, MEDICAL_SURGICAL_DRG_FLG, SOI_AT_DISCHARGE, SRC_SYS_CLM_UPDATE_DTTM, INSERT_DTTM, INSERT_USER_ID, INSERT_CYCLE_ID, SOURCE_SYSTEM_CD) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53,:54,:55,:56)", rec)
        cur.executemany("insert into OUT_GROUPER.OH_GRPR_APR_CALL_3M (OH_GRPR_APR_CALL_3M_SK, CLAIM_NUM, LINE_NUM, LINE_SEQUENCE_NUM, ADMIT_FROM_DT, ADMIT_DX_CD, AGE_IN_DAYS, AGE_IN_YEARS, BIRTH_DT, BIRTH_WEIGHT, BIRTH_WEIGHT_OPTION, CLAIM_TYPE, CD_VERSION_DT, CD_VERSION_MAPPING_TYPE, DX_CD, DX_PRESENT_ON_ADMISSION, DISCHARGE_TO_DT, DISCHARGE_APR_DRG_OPTION, DISCHARGE_STATUS, ENABLE_SUGGESTED_PRIN_PROC, EXT_CAUSE_OF_INJURY_DX_CD, EXT_CAUSE_OF_INJURY_DX_POA, GROUPER_ICD_VERSION_QUALIFIER, GROUPER_TYPE, GROUPER_VERSION, HAC_AGENCY_IND, HAC_VERSION, ICD_VERSION_QUALIFIER, PAYER_LOGIC_IND, PROC_CD, PROC_SERVICE_DT, REORDER, SCHEDULE_TYPE, SEX, SUPPRESS_HAC_CATEGORIES, TOTAL_CHARGES, USER_KEY_1, USER_KEY_2, LENGTH_OF_STAY, CONTENT_VERSION, FINANCIAL_PAYER, MEMBER_BENEFIT_PLAN, NON_COVERED_CHARGES, PATIENT_RESPONSIBILITY_AMT, CLAIM_EDITS, DX_HAC_CATEGORY, DX_RELATED_GROUP, DRG_FOL_HAC_ADRG_PROCESSING, SOI_FOL_HAC_ADRG_PROCESSING, MEDICAL_SURGICAL_DRG_FLG, SOI_AT_DISCHARGE, SRC_SYS_CLM_UPDATE_DTTM, INSERT_DTTM, INSERT_USER_ID, INSERT_CYCLE_ID, SOURCE_SYSTEM_CD) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53,:54,:55,:56)", rec)
    except TypeError as err:
        print(err)
    except cx_Oracle.IntegrityError as err:
        print(err)
    con.commit()
    cur.close()
    con.close()
    


def GetdbData(tgtConn):
    Field_names = ', '.join(ConfigValues.Tbl_Fields)
    con = cx_Oracle.connect(tgtConn)
    cur = con.cursor()
    sql ='select ' + Field_names + ' from in_grouper.in_grpr_apr_call_3m'
    cur.execute(sql)
    row = cur.fetchall()
    cur.close()
    con.close()
    return row