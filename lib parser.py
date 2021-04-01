import re
from datetime import datetime
taim=datetime.now()
import alltable
import os#для файлов
from lxml import etree#для парсинга xml
from sqlalchemy import *#для работы с БД
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)#
meta = MetaData()#мета данные
Session = sessionmaker(bind = engine) #создания класа сесии
s=Session()#образец класса сесия
parser=etree.XMLParser(remove_comments=True,recover=True)#настройки парсера 
#alltable.creat_table_all()
def pars_e_p_doc_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEPDocType"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['object_name']=i.find("{*}objectName").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_purchase_document_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseDocumentTypes"):
        dic={}
        taim=[]
        dic['placing_way_code']=i.find("{*}placingWayCode").text
        dic['placing_way_type']=i.find("{*}placingWayType").text
        dic['placing_way_name']=i.find("{*}placingWayName").text
        dic['actual']=i.find("{*}actual").text
        for k in i.getiterator("{*}documentType"):
            taim.append(k.find("{*}code").text)
        dic['document_types']=taim
        lis.append(dic)
    return lis
def pars_abandoned_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiAbandonedReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['code']=i.find("{*}code").text
        dic['type']=i.find("{*}type").text
        dic['placing_way_id']=i.find("{*}placingWay/{*}code").text
        dic['doc_type_id']=i.find("{*}docType/{*}code").text
        dic['actual']=i.find("{*}actual").text
        if i.find('{*}objectName')!=None:
            dic['object_name']=i.find("{*}objectName").text
        lis.append(dic)  
    return lis
def pars_andit_action_subject(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiAuditActionSubject"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_bank_guarantee_refusal615_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBankGuaranteeRefusal615Reason"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_bank_guarantee_refusal_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBankGuaranteeRefusalReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_budget(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBudget"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_change_price_foundation(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiChangePriceFoundation"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_closed_e_p_cases(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiClosedEPCases"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_closed_methods_of_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiClosedMethodOfReason"):
        dic={}
        dic['reason_code']=i.find("{*}reasonCode").text
        dic['reason_name']=i.find("{*}reasonName").text
        dic['reason_law']=i.find("{*}reasonLaw").text
        dic['last_update_date']=i.find("{*}lastUpdateDate").text
        dic['actual']=i.find("{*}actual").text
        dic['is_hide_info_required']=i.find("{*}isHideInfoRequired").text
        lis.append(dic)
    return lis
def pars_commission_role(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiCommissionRole"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['order']=i.find("{*}order").text
        dic['right_vote']=i.find("{*}rightVote").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_world_time_zone(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiWorldTimeZone"):
        dic={}
        dic['name']=i.find("{*}name").text
        dic['difference_time']=i.find("{*}differenceTime").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_drugs_o_k_e_i(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiDrugOKEI"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['full_name']=i.find("{*}fullName").text
        dic['local_name']=i.find("{*}localName").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_k_v_r(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiKVR"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_currency(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiCurrency"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['digital_code']=i.find("{*}digitalCode").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_o_k_e_i(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKEI"):
        dic={}
        if i.find("{*}internationalSymbol")!=None:
            dic['international_symbol']=i.find("{*}internationalSymbol").text
        dic['code']=i.find("{*}code").text
        dic['full_name']=i.find("{*}fullName").text
        dic['section_id']=i.find("{*}section/{*}code").text
        dic['group']=i.find("{*}group/{*}id").text
        dic['local_name']=i.find("{*}localName").text
        dic['international_name']=i.find("{*}internationalName").text
        dic['local_symbol']=i.find("{*}localSymbol").text
        dic['actual']=i.find("{*}actual").text
        dic['is_temporary_for_k_t_r_u']=i.find("{*}isTemporaryForKTRU").text    
        lis.append(dic)
    return lis
def pars_placing_way(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPlacingWay"):
        dic={}
        dic['placing_way_id']=i.find("{*}placingWayId").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['type']=i.find("{*}type").text
        dic['subsystem_type']=i.find("{*}subsystemType").text
        dic['actual']=i.find("{*}actual").text
        dic['is_procedure']=i.find("{*}isProcedure").text
        dic['is_exclude']=i.find("{*}isExclude").text
        lis.append(dic)
    return lis
def pars_k_t_r_u_not_using_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiKTRUNotUsingReason"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_o_k_s_m(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKSM"):
        dic={}
        dic['country_code']=i.find("{*}countryCode").text
        dic['country_full_name']=i.find("{*}countryFullName").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_evas_dev_fact_foundation(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEvasDevFactFoundation"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['placing_way_id']=i.find("{*}placingWay/{*}code").text
        dic['placing_way_doc_type_id']=i.find("{*}placingWayDocType/{*}code").text
        dic['integration_object_name']=i.find("{*}integrationObjectName").text
        dic['is_exclude']=i.find("{*}isExclude").text
        dic['is_actual']=i.find("{*}isActual").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['order_num']=i.find("{*}orderNum").text
        lis.append(dic)
    return lis
def pars_contract_currency_c_b_r_f(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractCurrencyCBRF"):
        if flag:
            dic={}
            dic['currency']=i.find("{*}currency/{*}code").text
            dic['actual']=i.find("{*}actual").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_contract_penalty_reason(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractPenaltyReason"):
        if flag:
            dic={}
            dic['code']=i.find("{*}code").text
            dic['name']=i.find("{*}name").text
            dic['penalty_type']=i.find("{*}penaltyType").text
            dic['actual']=i.find("{*}actual").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_e_a_e_s_country(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiEAESCountry"):
        if flag:
            dic={}
            dic['name']=i.find("{*}name").text
            dic['o_k_s_m_code']=i.find("{*}OKSMCode").text
            dic['code2']=i.find("{*}code2").text
            dic['code3']=i.find("{*}code3").text
            dic['order_number']=i.find("{*}orderNumber").text
            dic['update_date']=i.find("{*}updateDate").text
            dic['is_actual']=i.find("{*}isActual").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_purchase_plan_position_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchasePlanPositionChangeReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['description']=i.find("{*}description").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}shortName")!=None:    
            dic['short_name']=i.find("{*}shortName").text
        lis.append(dic)
    return lis
def pars_e_a_doc_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEADocType"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['order_number']=i.find("{*}orderNumber").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        if i.find("{*}fileTypeCode")!=None:
            dic['fileTypeCode']=i.find("{*}fileTypeCode").text
        lis.append(dic)
    return lis
def pars_t_r_u_admission_n_p_a(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTRUAdmissionNPA"):
        dic={}
        dic['n_p_a_code']=i.find("{*}NPACode").text
        dic['short_name']=i.find("{*}shortName").text
        dic['name']=i.find("{*}name").text
        dic['is_n_p_a155']=i.find("{*}isNPA155").text
        dic['start_date']=i.find("{*}startDate").text
        dic['actual']=i.find("{*}actual").text
        dic['order_num']=i.find("{*}orderNum").text
        dic['update_date']=i.find("{*}updateDate").text
        if i.find("{*}typeCodes")!=None:
            dic['type_codes_id']=i.find("{*}typeCodes/{*}typeCode").text
        if i.find("{*}endDate")!=None:
            dic['end_date']=i.find("{*}endDate").text
        lis.append(dic)
    return lis
def pars_tender_plan_purchase_group(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlanPurchaseGroup"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['short_name553']=i.find("{*}shortName553").text
        dic['short_name554']=i.find("{*}shortName554").text
        dic['is_comment']=i.find("{*}isComment").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}fullName553")!=None:
            dic['full_name553']=i.find("{*}fullName553").text
        if i.find("{*}fullName554")!=None:
            dic['full_name554']=i.find("{*}fullName554").text
        lis.append(dic)
    return lis
def pars_contract_execution_doc(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractExecutionDoc"):
        if flag:
            dic={}
            dic['code']=i.find("{*}code").text
            dic['name']=i.find("{*}name").text
            dic['is_accept_doc']=i.find("{*}isAcceptDoc").text
            dic['actual']=i.find("{*}actual").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_contract_o_k_o_p_f_extra_budget(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractOKOPFExtraBudget"):
        if flag:
            dic={}
            dic['extrabudget_id']=i.find("{*}extrabudget/{*}code").text
            dic['legal_form_new_id']=i.find("{*}legalFormNew/{*}code").text
            dic['actual']=i.find("{*}actual").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_contract_refusal_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiContractRefusalReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_contract_reparation_doc(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractReparationDoc"):
        if flag:
            dic={}
            dic['code']=i.find("{*}code").text
            dic['name']=i.find("{*}name").text
            dic['actual']=i.find("{*}actual").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_doc_reject_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiDocRejectReason"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['reason']=i.find("{*}reason").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_single_customer_reason_o_z(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiSingleCustomerReasonOZ"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_contract_modification_reason(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractModificationReason"):
        if flag:
            taim=[]
            dic={}
            dic['code']=i.find("{*}code").text
            dic['name']=i.find("{*}name").text
            dic['actual']=i.find("{*}actual").text
            for k in i.getiterator("{*}document"):
                taim.append(k.find("{*}code").text)
            dic['document']=taim
            dic['is_build_able']=i.find("{*}isBuildAble").text
            dic['is_deletable']=i.find("{*}isDeletable").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_drug_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiDrugChangeReason"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['must_specify_comment_or_request_number']=i.find("{*}mustSpecifyCommentOrRequestNumber").text
        dic['must_specify_drug_ref']=i.find("{*}mustSpecifyDrugRef").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_common_units_measurement(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiCommonUnitsMeasurement"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['o_k_e_i_info_id']=i.find("{*}OKEIInfo/{*}code").text
        dic['updateDate']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_modify_reason_o_z(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiModifyReasonOZ"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_k_o_s_g_u(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiKOSGU"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}parent_code")!=None:
            dic['parent_code']=i.find("{*}parentCode").text    
        lis.append(dic)
    return lis
def pars_national_project(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiNationalProject"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['project_level']=i.find("{*}projectLevel").text
        dic['project_full_name']=i.find("{*}projectFullName").text
        dic['start_date']=i.find("{*}startDate").text
        dic['start_date_active']=i.find("{*}startDateActive").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_o_k_f_s(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKFS"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_contract_price_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiContractPriceChangeReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['subsystem_type']=i.find("{*}subsystemType").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_contract_single_customer_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiContractSingleCustomerReason"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        
        dic['subsystem_type']=i.find("{*}subsystemType").text
        if i.find("{*}documents")!=None:
            for k in i.getiterator("{*}document"):
                taim.append(k.find("{*}code").text)
            dic['documents_id']=taim
            taim=[]
        if i.find("{*}placingWays")!=None:
            for k in i.getiterator("{*}placingWay"):
                taim.append(k.find("{*}code").text) 
            dic['placingWays_id']=taim
            taim=[]
        if i.find("{*}pointLaw")!=None:
            dic['point_law']=i.find("{*}pointLaw").text
        lis.append(dic)
    return lis
def pars_contract_termination_reason(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractTerminationReason"):
        if flag:
            dic={}
            taim=[]
            dic['id']=i.find("{*}id").text
            dic['name']=i.find("{*}name").text
            dic['actual']=i.find("{*}actual").text
            dic['subsystem_type']=i.find("{*}subsystemType").text
            if i.find("{*}documents")!=None:
                for k in i.getiterator("{*}documents/{*}document"):
                    taim.append(k.find("{*}code").text)
                dic['documents_id']=taim
                taim=[]
            if i.find("{*}reparationsDocuments")!=None:
                for k in i.getiterator("{*}reparationsDocuments/{*}document"):
                    taim.append(k.find("{*}code").text) 
                dic['placingWays_id']=taim
                taim=[]
            if i.find("{*}code")!=None:
                dic['code']=i.find("{*}code").text
            lis.append(dic)
        else:
            flag=True
    return lis
def pars_control99_subject(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiControl99Subject"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['control_authority_info_id']=i.find("{*}controlAuthorityInfo/{*}regNum").text
        dic['customer_info']=i.find("{*}customerInfo/{*}regNum").text
        dic['subject_type']=i.find("{*}subjectType").text
        dic['status']=i.find("{*}status").text
        lis.append(dic)
    return lis
def pars_deviation_fact_foundation(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiDeviationFactFoundation"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_e_p_doc_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEPDocType"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['object_name']=i.find("{*}objectName").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_e_t_p(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiETP"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}description")!=None:
                dic['description']=i.find("{*}description").text
        dic['phone']=i.find("{*}phone").text
        dic['address']=i.find("{*}address").text
        dic['email']=i.find("{*}email").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_eval_criterion(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEvalCriterion"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}code")!=None:
            dic['code']=i.find("{*}code").text
        if i.find("{*}criterionCode")!=None:
            dic['criterion_code']=i.find("{*}criterionCode").text
        if i.find("{*}description")!=None:
            dic['description']=i.find("{*}description").text
        if i.find("{*}order")!=None:
            dic['order']=i.find("{*}order").text
        if i.find("{*}numericalCode")!=None:
            dic['numerical_code']=i.find("{*}numericalCode").text
        if i.find("{*}criterionGroups")!=None:
            for k in i.getiterator("{*}criterionGroup"):
                taim.append(k.find("{*}code").text)
            dic['criterionGroups']=taim
        dic['actual']=i.find("{*}actual").text
        dic['need_expert_eval']=i.find("{*}needExpertEval").text
        lis.append(dic)
    return lis
def pars_k_b_k_budget(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiKBKBudget"):
        dic={}
        dic['kbk']=i.find("{*}kbk").text
        dic['budget']=i.find("{*}budget").text
        dic['actual']=i.find("{*}actual").text
        dic['start_date']=i.find("{*}start_date").text
        if i.find("{*}end_date")!=None:
            dic['end_date']=i.find("{*}end_date").text
        lis.append(dic)
    return lis
def pars_off_budget(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOffBudget"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['subsystem_type']=i.find("{*}subsystemType").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_o_k_o_p_f(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKOPF"):
        dic={}
        dic['code']=i.find("{*}code").text
        if i.find("{*}parentCode")!=None:
            dic['parent_code']=i.find("{*}parentCode").text
        dic['full_name']=i.find("{*}fullName").text
        dic['singular_name']=i.find("{*}singularName").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_o_k_v_e_d(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKVED"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['section']=i.find("{*}section").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_o_k_v_e_d2(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKVED2"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['section']=i.find("{*}section").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}comment")!=None:
            dic['comment']=i.find("{*}comment").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_organization_rights(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOrganizationRights"):
        dic={}
        taim=[]
        dic['regNumber']=i.find("{*}regNumber").text
        for k in i.getiterator("{*}organizationLink"):
                taim.append(k.find("{*}id").text)
        dic['organization_link_id']=taim
        lis.append(dic)
    return lis
def pars_organization_types(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOrganizationType"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['description']=i.find("{*}description").text        
        lis.append(dic)
    return lis
def pars_plan_position_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPlanPositionChangeReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['description']=i.find("{*}description").text
        dic['actual']=i.find("{*}actual").text          
        lis.append(dic)
    return lis
def pars_pref_rate(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPrefRate"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['pref_value']=i.find("{*}prefValue").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text          
        lis.append(dic)
    return lis
def pars_public_discussion_decision(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPublicDiscussionDecision"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['type']=i.find("{*}type").text
        dic['phase']=i.find("{*}phase").text   
        dic['actual']=i.find("{*}actual").text  
        if i.find("{*}foundations")!=None:
            for k in i.getiterator("{*}foundation"):
                taim.append(k.find("{*}id").text)
            dic['foundations_id']=taim       
        lis.append(dic)
    return lis
def pars_purchase_document_types(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseDocumentTypes"):
        dic={}
        taim=[]
        dic['placing_way_code']=i.find("{*}placingWayCode").text
        dic['placing_way_type']=i.find("{*}placingWayType").text
        dic['placing_way_name']=i.find("{*}placingWayName").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}phase")!=None:
            dic['phase']=i.find("{*}phase").text   
        dic['actual']=i.find("{*}actual").text  
        for k in i.getiterator("{*}documentType"):
            taim.append(k.find("{*}code").text)
        dic['document_type_id']=taim       
        lis.append(dic)
    return lis
def pars_public_discussion_questionnarie(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPublicDiscussionQuestionnarie"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['facetName']=i.find("{*}facetName").text
        dic['type']=i.find("{*}type").text
        dic['actual']=i.find("{*}actual").text 
        if i.find("{*}questions")!=None:
            for k in i.getiterator("{*}question"):
                taim.append(k.find("{*}id").text)
            dic['question_id']=taim       
        lis.append(dic)
    return lis
def pars_pref_rate(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPrefRate"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['pref_value']=i.find("{*}prefValue").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text          
        lis.append(dic)
    return lis
def pars_o_k_p_d(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKPD"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text          
        lis.append(dic)
    return lis
def pars_o_k_p_d2(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKPD2"):
        dic={}
        dic['id']=i.find("{*}id").text
        if i.find("{*}parentId")!=None:
            dic['parent_id']=i.find("{*}parentId").text
        dic['code']=i.find("{*}code").text
        if i.find("{*}parentCode")!=None:
            dic['parent_code']=i.find("{*}parentCode").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text          
        lis.append(dic)
    return lis
def pars_purchase_reject_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseRejectReason"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['reason']=i.find("{*}reason").text
        dic['actual']=i.find("{*}actual").text  
        dic['subsystem_type']=i.find("{*}subsystemType").text     
        for k in i.getiterator("{*}placingWay"):
            taim.append(k.find("{*}code").text)
        dic['placing_way_id']=taim
        lis.append(dic)
    return lis
def pars_special_purchase(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiSpecialPurchase"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['purchase_plan_short_name']=i.find("{*}purchasePlanShortName").text
        dic['purchase_plan_full_name']=i.find("{*}purchasePlanFullName").text  
        if i.find("{*}tenderPlan2017ShortName")!=None:
            dic['tender_plan2017_short_name']=i.find("{*}tenderPlan2017ShortName").text
        if i.find("{*}tenderPlan2017FullName")!=None:
            dic['tender_plan2017_full_name']=i.find("{*}tenderPlan2017FullName").text 
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
def pars_purchase_preference(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchasePreference"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}shortName")!=None:
            dic['short_name']=i.find("{*}shortName").text
        dic['type']=i.find("{*}type").text
        dic['pref_estimate_app']=i.find("{*}prefEstimateApp").text
        if i.find("{*}placingWays")!=None:
            for k in i.getiterator("{*}placingWay"):
                taim.append(k.find("{*}code").text)
            dic['placing_way_id']=taim
        dic['actual']=i.find("{*}actual").text  
        dic['use_tender_plans']=i.find("{*}useTenderPlans").text      
        lis.append(dic)
    return lis
def pars_tender_plan2017_contract_life_cycle_case(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlan2017ContractLifeCycleCase"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['code']=i.find("{*}code").text
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
def pars_tender_plan2017_position_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlan2017PositionChangeReason"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['full_name']=i.find("{*}fullName").text
        dic['code']=i.find("{*}code").text
        dic['short_name']=i.find("{*}shortName").text
        dic['cancel_chance']=i.find("{*}cancelChance").text
        dic['legal_act_details']=i.find("{*}legalActDetails").text
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
def pars_special_purchases2020(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiSpecialPurchase2020"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['full_name']=i.find("{*}fullName").text
        dic['code']=i.find("{*}code").text
        dic['short_name']=i.find("{*}shortName").text
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
def pars_tender_plan2020_position_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlan2020PositionChangeReason"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['short_name']=i.find("{*}shortName").text
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
def pars_o_k_t_m_o(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKTMO"):
        dic={}
        taim=[]
        dic['code']=i.find("{*}code").text
        if i.find("{*}parent_code")!=None:
            dic['parent_code']=i.find("{*}parent_code").text
        dic['full_name']=i.find("{*}fullName").text
        dic['last_update_date']=i.find("{*}lastUpdateDate").text
        dic['actual']=i.find("{*}actual").text       
        lis.append(dic)
    return lis
def pars_o_k_t_m_o_p_p_o(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKTMOPPO"):
        dic={}
        taim=[]
        dic['code']=i.find("{*}code").text
        if i.find("{*}parent_code")!=None:
            dic['parent_code']=i.find("{*}parent_code").text
        if i.find("{*}OKTMOCode")!=None:
            dic['o_k_t_m_o_Code']=i.find("{*}OKTMOCode").text
        if i.find("{*}settlementType")!=None:
            dic['settlement_type']=i.find("{*}settlementType").text
        if i.find("{*}registerName")!=None:
            dic['register_name']=i.find("{*}registerName").text
        dic['actual']=i.find("{*}actual").text       
        lis.append(dic)
    return lis
#------------------------------------------------------------
def pars_organization(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOrganization"):
        dic={}
        taim=[]
        dic['reg_number']=i.find("{*}regNumber").text
        dic['cons_registry_num']=i.find("{*}consRegistryNum").text
        dic['short_name']=i.find("{*}shortName").text 
        dic['full_name']=i.find("{*}fullName").text 
        dic['factual_address']={"building":i.find("{*}factualAddress/{*}building").text, 
                                "country":i.find("{*}factualAddress/{*}country/{*}countryCode").text,
                                "filled_manually":i.find("{*}factualAddress/{*}filledManually").text,
                                "region":i.find("{*}factualAddress/{*}region/{*}kladrCode").text,
                                "city":i.find("{*}factualAddress/{*}city/{*}kladrCode").text,
                                "shortStreet":i.find("{*}factualAddress/{*}shortStreet").text,
                                "zip":i.find("{*}factualAddress/{*}zip").text}  
        lis.append(dic)
    return lis
#---------------------------------------------------------
def pars (fail):
    pars=etree.parse(fail,parser)
    s=fail.name[fail.name.find("nsi")+3:fail.name.find("_")]
    if s[-1]=='s':
        s=s[0:-1]
    elif s.find("List")!=-1:
        s=s[:s.find("List")]
    s=re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    f=globals()["pars_"+s]
    return f(pars)
#def parse_abondoned_reason(xml_file):
#    res = []
#    for tag in xml_file.find_all('nsiAuditActionSubject'):
#        res.append({
#            'id': tag.find('id').text,
#            'name': tag.find('name').text,
#            'actual': {'true': True, 'false': False}[tag.find('actual').text]
#        })
#    return res

#def import_objects(lib, model):
#    for data in lib:
#        obj = model(**data)
#        session.add(obj)
#    session.commit()

#import_objects(parsed_data, nsiAuditActionSubject)
fails=[]#
fails=os.listdir("libreal")#получение списка всех файлов в библеотеке
with open ("wraiter","w") as wraiter:
    for i in fails:#обработка всех файлов
        with open("libreal/"+i) as fobj:#открытие файла
             t=pars(fobj)#парсинк из документа 
        wraiter.writelines(str(t))
       # if i[4]=='A':
       #     concrete_bazz_1(t)
       # else:
       #     concrete_bazz_2(t)
       # #t=dazz(t)-универсальный парсер. да да зачем он нам он всевото уменьшит работу и решит проблемы
#    for row in s.query(alltable.nsiDeviationFactFoundation).all():
#        wraiter.writelines(str(row.code)+" "+str(row.name)+" "+str(row.actual)+"\n")
#    for row in s.query(alltable.nsiAuditActionSubject).all():
#        wraiter.writelines(str(row.code)+" "+str(row.name)+" "+str(row.actual)+"\n")
print(datetime.now()-taim)
