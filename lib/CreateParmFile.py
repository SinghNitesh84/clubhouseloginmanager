def PrarmDetl(url):
	set1 = """[GLOBAL]
MPLT_APR_3M_CALL_GROUPER.$$USER_KEY_2=APR
MPLT_APR_3M_CALL_GROUPER.$$CALL_TYPE=WS
$$DBConnection=User_Achaud_MVPRODLG
$ParamMyURL="""
	in_url = url
	set2 = """
[VENDOR_3M.WF:W_MTV_EDW_MX_APR_GRP_INPUT]
/* All below SQLs are actually one SQL statement*/
$$SQL1=SELECT DISTINCT claim_id, service_number, sequence_number, admission_dt, admit_diagn_code, (CASE WHEN trunc(months_between(SYSDATE,birth_date) / 12) > 0 THEN NULL ELSE admission_dt - birth_date END) age_in_days, (CASE WHEN trunc(months_between(SYSDATE,birth_date) / 12) > 0 THEN floor(months_between(greatest(admission_dt,discharge_date),birth_date) / 12) ELSE NULL END) age_in_years, birth_date, birth_weight, 1 birth_weight_option_selected, diag_code, diag_poa, discharge_date, disch_status_code, icd_cd_ind, surg_procd_code_id, surg_procd_date, sex_code, total_charges_amt, billing_prov_id, ntwk, covered_days, 1 cycle_id, claim_sts_timestamp status_timestamp FROM ( SELECT TRIM(c.claim_id) claim_id, ce.fk_service_num AS service_number, ce.fk_svc_seq_num AS sequence_number, TRIM(c.admit_diagn_code) admit_diagn_code, c.birth_date birth_date, (CASE WHEN c.admission_date = TO_DATE('01/01/0001','MM/DD/YYYY') THEN covered_from_date ELSE admission_date END) admission_dt, ic.discharge_date discharge_date, (CASE WHEN to_number(TRIM(hcic.value_amount) ) > 10000 THEN '9999' ELSE TRIM(hcic.value_amount) END) birth_weight, TRIM(ic.disch_status_code) disch_status_code, TRIM(ic.covered_days) covered_days, TRIM(cda1.diag_code_id) principal_diag_code, TRIM(cda1.present_on_adm_cd) principal_diag_poa, csp.surg_procd_code_id, cda2_dc.diag_code, cda2_dc.present_on_adm_cd AS diag_poa, TRIM(c.sex_code) sex_code, status_timestamp, c.total_charges_amt, c.billing_prov_id, nvl(TRIM(ic.svc_prv_network_id),'NONPLAN') ntwk, surg_procd_date, (CASE WHEN nvl(TRIM(c.icd_cd_scheme_proc),TRIM(c.admission_diag_code_set_ind) ) = '9' THEN '9' ELSE '0' END) icd_cd_ind, c.status_timestamp claim_sts_timestamp FROM claim c, institutional_clm ic, claim_diag_assn cda1, hlth_care_info_cd hcic, claim_explanation ce, service_line sl, 
$$SQL2=(SELECT fk_claim_id, rtrim(XMLAGG( XMLELEMENT( e, diag_code_id || ',' ) .extract('//text()') ORDER BY sequence_number) ) AS diag_code, rtrim(XMLAGG( XMLELEMENT( e, present_on_adm_cd || ',' ) .extract('//text()') ORDER BY sequence_number) ) AS present_on_adm_cd FROM ( SELECT * FROM ( SELECT DISTINCT fk_claim_id, sequence_number, upper(TRIM(diag_code_id) ) AS diag_code_id, upper(TRIM(present_on_adm_cd) ) AS present_on_adm_cd FROM claim_diag_assn ) a, claim c WHERE c.claim_id = a.fk_claim_id AND c.status_timestamp >= SYSDATE - 30 AND a.diag_code_id IS NOT NULL ORDER BY a.fk_claim_id,sequence_number ) GROUP BY fk_claim_id ) cda2_dc, (SELECT a.fk_claim_id, rtrim(XMLAGG( XMLELEMENT( e, a.surg_procd_code_id || ',' ) .extract('//text()') ORDER BY sequence_number) ) AS surg_procd_code_id, rtrim(XMLAGG( XMLELEMENT( e, TO_CHAR(a.surg_procd_date,'yyyy-mm-dd') || ',' ) .extract('//text()') ORDER BY sequence_number) ) surg_procd_date FROM ( SELECT DISTINCT fk_claim_id, sequence_number, upper(TRIM(surg_procd_code_id) ) AS surg_procd_code_id, surg_procd_date FROM clm_surg_procd ) a, claim c WHERE c.claim_id = a.fk_claim_id AND c.status_timestamp >= SYSDATE - 30 AND a.surg_procd_code_id IS NOT NULL GROUP BY a.fk_claim_id ) csp WHERE status_timestamp >= SYSDATE - 30 
$$SQL3=AND c.claim_type = 'HO' AND C.BUS_LEVEL_7_ID = 'MEDICAID' AND HCIC.HEALTH_CODE_VALUE(+) = '54' AND CDA1.SEQUENCE_NUMBER(+) = 1 AND SL.FK_CLAIM_ID(+) = c.CLAIM_ID AND C.CLAIM_ID = IC.FK_CLAIM_ID AND C.CLAIM_ID = CDA1.FK_CLAIM_ID(+) AND C.CLAIM_ID = CDA2_DC.FK_CLAIM_ID(+) AND IC.FK_CLAIM_ID = CSP.FK_CLAIM_ID(+) AND IC.FK_CLAIM_ID = HCIC.FK_CLAIM_ID(+) and (CE.EXPLN_CODE = '3GP' or (SL.MANUAL_PEND_EX_CD = '3GP' and sl.service_number = ce.FK_SERVICE_NUM)) AND CE.FK_CLAIM_ID = C.CLAIM_ID )

[VENDOR_3M.WF:W_MTV_APR_3M_GRPR_WS_CALL]
/* All below SQLs are actually one SQL statement.*/
$$SQL1=SELECT DISTINCT claim_id, service_number, sequence_number, admission_dt, admit_diagn_code, (CASE WHEN trunc(months_between(SYSDATE,birth_date) / 12) > 0 THEN NULL ELSE admission_dt - birth_date END) age_in_days, (CASE WHEN trunc(months_between(SYSDATE,birth_date) / 12) > 0 THEN floor(months_between(greatest(admission_dt,discharge_date),birth_date) / 12) ELSE NULL END) age_in_years, birth_date, birth_weight, 1 birth_weight_option_selected, diag_code, diag_poa, discharge_date, disch_status_code, icd_cd_ind, surg_procd_code_id, surg_procd_date, sex_code, total_charges_amt, billing_prov_id, ntwk, covered_days, 1 cycle_id, claim_sts_timestamp status_timestamp FROM ( SELECT TRIM(c.claim_id) claim_id, ce.fk_service_num AS service_number, ce.fk_svc_seq_num AS sequence_number, TRIM(c.admit_diagn_code) admit_diagn_code, c.birth_date birth_date, (CASE WHEN c.admission_date = TO_DATE('01/01/0001','MM/DD/YYYY') THEN covered_from_date ELSE admission_date END) admission_dt, ic.discharge_date discharge_date, (CASE WHEN to_number(TRIM(hcic.value_amount) ) > 10000 THEN '9999' ELSE TRIM(hcic.value_amount) END) birth_weight, TRIM(ic.disch_status_code) disch_status_code, TRIM(ic.covered_days) covered_days, TRIM(cda1.diag_code_id) principal_diag_code, TRIM(cda1.present_on_adm_cd) principal_diag_poa, csp.surg_procd_code_id, cda2_dc.diag_code, cda2_dc.present_on_adm_cd AS diag_poa, TRIM(c.sex_code) sex_code, status_timestamp, c.total_charges_amt, c.billing_prov_id, nvl(TRIM(ic.svc_prv_network_id),'NONPLAN') ntwk, surg_procd_date, (CASE WHEN nvl(TRIM(c.icd_cd_scheme_proc),TRIM(c.admission_diag_code_set_ind) ) = '9' THEN '9' ELSE '0' END) icd_cd_ind, c.status_timestamp claim_sts_timestamp FROM claim c, institutional_clm ic, claim_diag_assn cda1, hlth_care_info_cd hcic, claim_explanation ce, service_line sl, 
$$SQL2=(SELECT fk_claim_id, rtrim(XMLAGG( XMLELEMENT( e, diag_code_id || ',' ) .extract('//text()') ORDER BY sequence_number) ) AS diag_code, rtrim(XMLAGG( XMLELEMENT( e, present_on_adm_cd || ',' ) .extract('//text()') ORDER BY sequence_number) ) AS present_on_adm_cd FROM ( SELECT * FROM ( SELECT DISTINCT fk_claim_id, sequence_number, upper(TRIM(diag_code_id) ) AS diag_code_id, upper(TRIM(present_on_adm_cd) ) AS present_on_adm_cd FROM claim_diag_assn ) a, claim c WHERE c.claim_id = a.fk_claim_id AND c.status_timestamp >= SYSDATE - 30 AND a.diag_code_id IS NOT NULL ORDER BY a.fk_claim_id,sequence_number ) GROUP BY fk_claim_id ) cda2_dc, (SELECT a.fk_claim_id, rtrim(XMLAGG( XMLELEMENT( e, a.surg_procd_code_id || ',' ) .extract('//text()') ORDER BY sequence_number) ) AS surg_procd_code_id, rtrim(XMLAGG( XMLELEMENT( e, TO_CHAR(a.surg_procd_date,'yyyy-mm-dd') || ',' ) .extract('//text()') ORDER BY sequence_number) ) surg_procd_date FROM ( SELECT DISTINCT fk_claim_id, sequence_number, upper(TRIM(surg_procd_code_id) ) AS surg_procd_code_id, surg_procd_date FROM clm_surg_procd ) a, claim c WHERE c.claim_id = a.fk_claim_id AND c.status_timestamp >= SYSDATE - 30 AND a.surg_procd_code_id IS NOT NULL GROUP BY a.fk_claim_id ) csp WHERE status_timestamp >= SYSDATE - 30 
$$SQL3=AND c.claim_type = 'HO' AND C.BUS_LEVEL_7_ID = 'MEDICAID' AND HCIC.HEALTH_CODE_VALUE(+) = '54' AND CDA1.SEQUENCE_NUMBER(+) = 1 AND SL.FK_CLAIM_ID(+) = c.CLAIM_ID AND C.CLAIM_ID = IC.FK_CLAIM_ID AND C.CLAIM_ID = CDA1.FK_CLAIM_ID(+) AND C.CLAIM_ID = CDA2_DC.FK_CLAIM_ID(+) AND IC.FK_CLAIM_ID = CSP.FK_CLAIM_ID(+) AND IC.FK_CLAIM_ID = HCIC.FK_CLAIM_ID(+) and (CE.EXPLN_CODE = '3GP' or (SL.MANUAL_PEND_EX_CD = '3GP' and sl.service_number = ce.FK_SERVICE_NUM)) AND CE.FK_CLAIM_ID = C.CLAIM_ID )"""
	ParmValue = set1 + in_url + set2
	ParmFile = open("W_MPG_MTV_OUT_GROUPER.PAR",'w')
	ParmFile.write(ParmValue)
	ParmFile.close

