import re
from datetime import datetime
taim=datetime.now()
import alltable
import os
from lxml import etree
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)
meta = MetaData()
Session = sessionmaker(bind = engine) 
s=Session()
parser=etree.XMLParser(remove_comments=True,recover=True)
#alltable.creat_table_all()
def pars_e_p_doc_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEPDocType"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['object_name']=i.find("{*}objectName").text
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_purchase_document_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseDocumentTypes"):
        dic={}
        taim=[]
        dic['placing_way_type']=i.find("{*}placingWayType").text
        dic['placing_way_name']=i.find("{*}placingWayName").text
        if i.find("{*}placingWayCode")!=None:
            dic['placing_way_code']=i.find("{*}placingWayCode").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}documentTypes")!=None:
            for k in i.getiterator("{*}documentType"):
                taim.append({'code':k.find("{*}code").text,'name':k.find("{*}name").text,'actual':k.find("{*}actual").text,'structured':k.find("{*}structured").text})
            dic['document_type_id']=taim
        lis.append(dic)
    return lis
def pars_abandoned_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiAbandonedReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        if i.find('{*}objectName')!=None:
            dic['object_name']=i.find("{*}objectName").text
        dic['type']=i.find("{*}type").text
        dic['doc_type_id']={'code':i.find("{*}docType/{*}code").text,'name':i.find("{*}docType/{*}name").text}
        dic['placing_way_id']={"code":i.find("{*}placingWay/{*}code").text,"name":i.find("{*}placingWay/{*}name").text}
        dic['actual']=i.find("{*}actual").text
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
        dic['id']=i.find("{*}id").text#id
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_budget(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBudget"):
        dic={}
        dic['code']=i.find("{*}code").text#id
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_change_price_foundation(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiChangePriceFoundation"):
        dic={}
        dic['code']=i.find("{*}code").text#id
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_closed_e_p_cases(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiClosedEPCases"):
        dic={}
        dic['code']=i.find("{*}code").text#id
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
        dic['id']=i.find("{*}id").text#id
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}order")!=None:
            dic['order']=i.find("{*}order").text
        dic['right_vote']=i.find("{*}rightVote").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_world_time_zone(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiWorldTimeZone"):
        dic={}
        dic['name']=i.find("{*}name").text#вроде как id но не уверен пока
        dic['difference_time']=i.find("{*}differenceTime").text#имеет шаблон [+\-]?\d{1,3}
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_drugs_o_k_e_i(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiDrugOKEI"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['full_name']=i.find("{*}fullName").text
        if i.find("{*}localName")!=None:
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
        if i.find("{*}actual")!=None:
            dic['parent_code']=i.find("{*}parentCode").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_currency(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiCurrency"):
        dic={}
        dic['code']=i.find("{*}code").text
        if i.find("{*}digitalCode")!=None:
            dic['digital_code']=i.find("{*}digitalCode").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_o_k_e_i(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKEI"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['full_name']=i.find("{*}fullName").text
        if i.find("{*}section/{*}code")!=None:
            dic['section_id']=i.find("{*}section/{*}code").text
        if i.find("{*}group_id/{*}id")!=None:
            dic['group_id']=i.find("{*}group/{*}id").text
        if i.find("{*}group_id/{*}id")!=None:
            dic['group_id']=i.find("{*}group/{*}id").text
        if i.find("{*}localName")!=None:
            dic['local_name']=i.find("{*}localName").text
        if i.find("{*}internationalName")!=None:
            dic['international_name']=i.find("{*}internationalName").text
        if i.find("{*}localSymbol")!=None:
            dic['local_symbol']=i.find("{*}localSymbol").text
        if i.find("{*}internationalSymbol")!=None:
            dic['international_symbol']=i.find("{*}internationalSymbol").text
        if i.find("{*}trueNationalCode")!=None:
            dic['true_national_code']=i.find("{*}trueNationalCode").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}isTemporaryForKTRU")!=None:
            dic['is_temporary_for_k_t_r_u']=i.find("{*}isTemporaryForKTRU").text    
        lis.append(dic)
    return lis
def pars_placing_way(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPlacingWay"):
        dic={}
        taim=[]
        dic['placing_way_id']=i.find("{*}placingWayId").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['type']=i.find("{*}type").text
        dic['subsystem_type']=i.find("{*}subsystemType").text#может быть либо FZ44 либо FZ94
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}documents")!=None:
            for k in i.getiterator("{*}document"):
                taim.append({"code":k.find("{*}code").text,"name":k.find("{*}name").text,"actual":k.find("{*}actual").text})
            dic['document_id']=taim
            taim=[]
        if i.find("{*}compDocuments")!=None:
            for k in i.getiterator("{*}compDocument"):
                taim.append({"code":k.find("{*}code").text,"name":k.find("{*}name").text,"actual":k.find("{*}actual").text})
            dic['comp_document_id']=taim
            taim=[]
        if i.find("{*}usedInRPGInfo")!=None:
            dic['used_in_r_p_g_info']={}
            if i.find("{*}usedInRPGInfo/{*}usedInRPG")!=None:
                dic['used_in_r_p_g_info'].update({"used_in_r_p_g":i.find("{*}usedInRPGInfo/{*}usedInRPG").text})
            if i.find("{*}usedInRPGInfo/{*}RPGJoint")!=None:
                dic['used_in_r_p_g_info'].update({"r_p_g_joint":i.find("{*}usedInRPGInfo/{*}RPGJoint").text})
            if i.find("{*}usedInRPGInfo/{*}usedInRPG")!=None:
                dic['used_in_r_p_g_info'].update({"r_p_g_not111":i.find("{*}usedInRPGInfo/{*}RPGNot111").text})
        if i.find("{*}isProcedure")!=None:
            dic['is_procedure']=i.find("{*}isProcedure").text
        if i.find("{*}isExclude")!=None:
            dic['is_exclude']=i.find("{*}isExclude").text       
        lis.append(dic)
    return lis
def pars_k_t_r_u_not_using_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiKTRUNotUsingReason"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_o_k_s_m(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKSM"):
        dic={}
        dic['country_code']=i.find("{*}countryCode").text
        if i.find("{*}countryFullName")!=None:
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
        dic['placing_way']=[i.find("{*}placingWay/{*}code").text,i.find("{*}placingWay/{*}name").text]
        dic['placing_way_doc_type']=[i.find("{*}placingWayDocType/{*}code").text,i.find("{*}placingWayDocType/{*}name").text]
        dic['integration_object_name']=i.find("{*}integrationObjectName").text
        dic['is_exclude']=i.find("{*}isExclude").text#При isExclude=true запись становится недоступна для формирования новых протоколов, но отображается в уже созданных протоколах. В случае заполнения значением true обязательно заполняется поле excludeDate текущей или будущей датой
        if i.find("{*}excludeDate")!=None:
            dic['exclude_date']=i.find("{*}excludeDate").text#Может быть планируемой, в будущем. Заполнение будущей датой означает плановое исключение основания из бизнес-процесса
        dic['is_actual']=i.find("{*}isActual").text#При isActual=true запись становится недоступна для формирования новых протоколов и отображения в старых протоколах
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        if i.find("{*}orderNum")!=None:
            dic['order_num']=i.find("{*}orderNum").text
        lis.append(dic)
    return lis
def pars_contract_currency_c_b_r_f(fail):
    lis=[]
    flag=False
    for i in fail.getiterator("{*}nsiContractCurrencyCBRF"):
        if flag:
            dic={}
            dic['currency']=[i.find("{*}currency/{*}code").text,i.find("{*}currency/{*}digitalCode").text,i.find("{*}currency/{*}name").text]
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
            dic['penalty_type']=i.find("{*}penaltyType").text#P - Неустойка; F - Штраф; I - Пени.
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
            if i.find("{*}orderNumber")!=None:
                dic['order_number']=i.find("{*}orderNumber").text
            if i.find("{*}updateDate")!=None:
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
        if i.find("{*}shortName")!=None:    
            dic['short_name']=i.find("{*}shortName").text
        if i.find("{*}description")!=None:
            dic['description']=i.find("{*}description").text
        if i.find("{*}legalActDetails")!=None:
            dic['legal_act_details']=i.find("{*}legalActDetails").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_e_a_doc_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEADocType"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}fileTypeCode")!=None:
            dic['fileTypeCode']=i.find("{*}fileTypeCode").text#Допустимые значения: A - Документ о приемке поставленного товара, выполненной работы, оказанной услуги О - Информация о стране происхождения или информация о производителе товара ЕR - Документ о результатах проведенной экспертизы   поставленного товара, выполненной работы, оказанной услуги E - Документы, подтверждающие исполнение контракта, оплату контракта и документы о начислении неустоек (штрафов, пеней)
        if i.find("{*}noInclude")!=None:
            dic['no_include']=i.find("{*}noInclude").text#Фиксированное значение: 1
        if i.find("{*}orderNumber")!=None:
            dic['order_number']=i.find("{*}orderNumber").text
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_t_r_u_admission_n_p_a(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTRUAdmissionNPA"):
        dic={}
        dic['n_p_a_code']=i.find("{*}NPACode").text
        if i.find("{*}typeCodes")!=None:
            dic['type_codes_id']=i.find("{*}typeCodes/{*}typeCode").text
        if i.find("{*}shortName")!=None: 
            dic['short_name']=i.find("{*}shortName").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}isNPA155")!=None: 
            dic['is_n_p_a155']=i.find("{*}isNPA155").text
        if i.find("{*}startDate")!=None:    
            dic['start_date']=i.find("{*}startDate").text
        if i.find("{*}endDate")!=None:    
            dic['end_date']=i.find("{*}endDate").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}orderNum")!=None: 
            dic['order_num']=i.find("{*}orderNum").text
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        lis.append(dic)
    return lis
def pars_tender_plan_purchase_group(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlanPurchaseGroup"):
        dic={}
        dic['id']=i.find("{*}id").text
        if i.find("{*}code")!=None:
            dic['code']=i.find("{*}code").text
        dic['short_name553']=i.find("{*}shortName553").text
        if i.find("{*}fullName553")!=None:
            dic['full_name553']=i.find("{*}fullName553").text
        dic['short_name554']=i.find("{*}shortName554").text
        if i.find("{*}fullName554")!=None:
            dic['full_name554']=i.find("{*}fullName554").text
        if i.find("{*}isComment")!=None:
            dic['is_comment']=i.find("{*}isComment").text
        dic['actual']=i.find("{*}actual").text
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
            if i.find("{*}isAcceptDoc")!=None:
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
            dic['extrabudget_id']=[i.find("{*}extrabudget/{*}code").text,i.find("{*}extrabudget/{*}name").text]
            if i.find("{*}legalFormOld")!=None:
                dic['legal_form_old']=[i.find("{*}legalFormOld/{*}code").text,i.find("{*}legalFormOld/{*}singularName").text]
            if i.find("{*}legalFormNew")!=None:
                dic['legal_form_new_id']=[i.find("{*}legalFormNew/{*}code").text,i.find("{*}legalFormNew/{*}singularName").text]
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
        if i.find("{*}code")!=None:
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
        if i.find("{*}placingWays")!=None:
            dic['placing_ways']={"code":i.find("{*}placingWays/{*}code").text,"name":i.find("{*}placingWays/{*}name").text}
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
            if i.find("{*}document")!=None:
                for k in i.getiterator("{*}document"):
                    taim.append({"code":k.find("{*}code").text,"name":k.find("{*}name").text,"actual":k.find("{*}actual").text})
                dic['document']=taim
            if i.find("{*}isBuildAble")!=None:
                dic['is_build_able']=i.find("{*}isBuildAble").text
            if i.find("{*}isBuildAble")!=None:
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
        if i.find("{*}OKEIInfo")!=None:
            dic['o_k_e_i_info_id']=i.find("{*}OKEIInfo/{*}code").text
        if i.find("{*}updateDate")!=None:
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
        if i.find("{*}parent_code")!=None:
            dic['parent_code']=i.find("{*}parentCode").text 
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
#не проверил
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
def pars_contract_price_change_reason(fail):#написоно что устарел и не применяется
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
        dic['name']=i.find("{*}name").text
        if i.find("{*}pointLaw")!=None:
            dic['point_law']=i.find("{*}pointLaw").text
        dic['subsystem_type']=i.find("{*}subsystemType").text
        
        if i.find("{*}placingWays")!=None:
            for k in i.getiterator("{*}placingWay"):
                taim.append(k.find("{*}code").text) 
            dic['placingWays_id']=taim
            taim=[]
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}documents")!=None:
            for k in i.getiterator("{*}document"):
                taim.append(k.find("{*}code").text)
            dic['documents_id']=taim
            taim=[]
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
            dic['subsystem_type']=i.find("{*}subsystemType").text
            dic['actual']=i.find("{*}actual").text
        else:
            flag=True
    return lis
#не проверил
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
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_e_t_p(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiETP"):
        dic={}
        dic['code']=i.find("{*}code").text
        if i.find("{*}name")!=None:
            dic['name']=i.find("{*}name").text
        if i.find("{*}description")!=None:
            dic['description']=i.find("{*}description").text
        if i.find("{*}phone")!=None:
            dic['phone']=i.find("{*}phone").text
        if i.find("{*}address")!=None:
            dic['address']=i.find("{*}address").text
        if i.find("{*}email")!=None:
            dic['email']=i.find("{*}email").text
        if i.find("{*}fullName")!=None:
            dic['full_name']=i.find("{*}fullName").text
        if i.find("{*}INN")!=None:
            dic['i_n_n']=i.find("{*}INN").text
        if i.find("{*}KPP")!=None:
            dic['k_p_p']=i.find("{*}KPP").text
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
        if i.find("{*}criterionGroups")!=None:
            for k in i.getiterator("{*}criterionGroup"):
                taim.append(k.find("{*}code").text)
            dic['criterionGroups']=taim
        if i.find("{*}code")!=None:
            dic['code']=i.find("{*}code").text
        if i.find("{*}criterionCode")!=None:
            dic['criterion_code']=i.find("{*}criterionCode").text
        if i.find("{*}description")!=None:
            dic['description']=i.find("{*}description").text
        if i.find("{*}numericalCode")!=None:
            dic['numerical_code']=i.find("{*}numericalCode").text
        if i.find("{*}order")!=None:
            dic['order']=i.find("{*}order").text
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
        if i.find("{*}start_date")!=None:
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
        if i.find("{*}id")!=None:
            dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text#id
        if i.find("{*}section")!=None:
            dic['section']=i.find("{*}section").text
        if i.find("{*}subsection")!=None:
            dic['subsection']=i.find("{*}subsection").text
        if i.find("{*}parentId")!=None:
            dic['parent_id']=i.find("{*}parentId").text
        if i.find("{*}name")!=None:
            dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_o_k_v_e_d2(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKVED2"):
        dic={}
        if i.find("{*}id")!=None:
            dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        if i.find("{*}section")!=None:
            dic['section']=i.find("{*}section").text
        if i.find("{*}parentCode")!=None:
            dic['parent_code']=i.find("{*}parentCode").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}comment")!=None:
            dic['comment']=i.find("{*}comment").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
#не проверил
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
        if i.find("{*}description")!=None:
            dic['description']=i.find("{*}description").text        
        lis.append(dic)
    return lis
def pars_plan_position_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPlanPositionChangeReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}description")!=None:
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
        if i.find("{*}updateDate")!=None:
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
                taim.append({"id":k.find("{*}id").text,"code":k.find("{*}code").text,"name":k.find("{*}name").text,"actual":k.find("{*}actual").text})
            dic['foundations_id']=taim       
        lis.append(dic)
    return lis
def pars_purchase_document_types(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseDocumentTypes"):
        dic={}
        taim=[]
        dic['placing_way_type']=i.find("{*}placingWayType").text
        dic['placing_way_name']=i.find("{*}placingWayName").text
        if i.find("{*}placingWayCode")!=None:
            dic['placing_way_code']=i.find("{*}placingWayCode").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}phase")!=None:
            dic['phase']=i.find("{*}phase").text   
        dic['actual']=i.find("{*}actual").text  
        if i.find("{*}documentTypes")!=None:
            for k in i.getiterator("{*}documentType"):
                taim.append({"code":k.find("{*}code").text,"name":k.find("{*}name").text,"actual":k.find("{*}actual").text,"structured":k.find("{*}structured").text,})
            dic['document_type_id']=taim       
        lis.append(dic)
    return lis
#не праверил 
def pars_public_discussion_questionnarie(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPublicDiscussionQuestionnarie"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['facetName']=i.find("{*}facetName").text
        if i.find("{*}questions")!=None:
            for k in i.getiterator("{*}question"):
                taim.append({"id":k.find("{*}id").text,"code":k.find("{*}code").text,"name":k.find("{*}name").text,"anwsers":k.find("{*}anwsers").text,"actual":k.find("{*}actual").text})
            dic['question_id']=taim
        dic['type']=i.find("{*}type").text #Возможные значения: LP OT
        dic['actual']=i.find("{*}actual").text 
               
        lis.append(dic)
    return lis
def pars_pref_rate(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPrefRate"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['pref_value']=i.find("{*}prefValue").text
        if i.find("{*}updateDate")!=None:
            dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text          
        lis.append(dic)
    return lis
def pars_o_k_p_d(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKPD"):
        dic={}
        if i.find("{*}id")!=None:
            dic['id']=i.find("{*}id").text
        if i.find("{*}parentId")!=None:
            dic['parent_id']=i.find("{*}parentId").text
        dic['code']=i.find("{*}code").text
        if i.find("{*}parentCode")!=None:
            dic['parent_code']=i.find("{*}parentCode").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}comment")!=None:
            dic['comment']=i.find("{*}comment").text 
        dic['actual']=i.find("{*}actual").text          
        lis.append(dic)
    return lis
def pars_o_k_p_d2(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOKPD2"):
        dic={}
        if i.find("{*}id")!=None:
            dic['id']=i.find("{*}id").text
        if i.find("{*}parentId")!=None:
            dic['parent_id']=i.find("{*}parentId").text
        dic['code']=i.find("{*}code").text
        if i.find("{*}parentCode")!=None:
            dic['parent_code']=i.find("{*}parentCode").text
        dic['name']=i.find("{*}name").text
        if i.find("{*}comment")!=None:
            dic['comment']=i.find("{*}comment").text 
        dic['actual']=i.find("{*}actual").text          
        lis.append(dic)
    return lis
def pars_purchase_reject_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseRejectReason"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        if i.find("{*}code")!=None:
            dic['code']=i.find("{*}code").text
        dic['reason']=i.find("{*}reason").text
        dic['actual']=i.find("{*}actual").text  
        dic['subsystem_type']=i.find("{*}subsystemType").text     
        if i.find("{*}placingWays")!=None:
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
        if i.find("{*}purchasePlanShortName")!=None:
            dic['purchase_plan_short_name']=i.find("{*}purchasePlanShortName").text
        if i.find("{*}purchasePlanFullName")!=None:
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
        if i.find("{*}parentShortName")!=None:
            dic['parent_short_name']=i.find("{*}parentShortName").text
        dic['type']=i.find("{*}type").text
        if i.find("{*}prefEstimateApp")!=None:
            dic['pref_estimate_app']=i.find("{*}prefEstimateApp").text
        if i.find("{*}prefValue")!=None:
            dic['pref_value']=i.find("{*}prefValue").text
        if i.find("{*}placingWays")!=None:
            for k in i.getiterator("{*}placingWay"):
                taim.append(k.find("{*}code").text)
            dic['placing_way_id']=taim
        dic['actual']=i.find("{*}actual").text  
        if i.find("{*}useTenderPlans")!=None:
            dic['use_tender_plans']=i.find("{*}useTenderPlans").text  
        if i.find("{*}tenderPlanPurchaseGroups")!=None:
            dic['tender_plan_purchase_groups']=i.find("{*}tenderPlanPurchaseGroups").text
        if i.find("{*}endDate")!=None:
            dic['end_date']=i.find("{*}endDate").text 
        if i.find("{*}countryFrom")!=None:
            dic['country_from']=i.find("{*}countryFrom").text    
        lis.append(dic)
    return lis
def pars_tender_plan2017_contract_life_cycle_case(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlan2017ContractLifeCycleCase"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
def pars_tender_plan2017_position_change_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiTenderPlan2017PositionChangeReason"):
        dic={}
        taim=[]
        dic['id']=i.find("{*}id").text
        dic['code']=i.find("{*}code").text
        dic['full_name']=i.find("{*}fullName").text
        if i.find("{*}shortName")!=None:
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
        if i.find("{*}fullName")!=None:
            dic['full_name']=i.find("{*}fullName").text
        dic['code']=i.find("{*}code").text
        if i.find("{*}shortName")!=None:
            dic['short_name']=i.find("{*}shortName").text
        dic['actual']=i.find("{*}actual").text      
        lis.append(dic)
    return lis
 #не проверил
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
        if i.find("{*}section")!=None:
            dic['section']=i.find("{*}section").text 
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
        dic['name']=i.find("{*}name").text
        if i.find("{*}OKTMOCode")!=None:
            dic['o_k_t_m_o_Code']=i.find("{*}OKTMOCode").text
        if i.find("{*}settlementType")!=None:
            dic['settlement_type']=i.find("{*}settlementType").text
        if i.find("{*}registerName")!=None:
            dic['register_name']=i.find("{*}registerName").text
        dic['actual']=i.find("{*}actual").text       
        lis.append(dic)
    return lis
def pars_organization(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiOrganization"):
        dic={}
        taim=[]
        dic['reg_number']=i.find("{*}regNumber").text
        if i.find("{*}consRegistryNum")!=None:
            dic['cons_registry_num']=i.find("{*}consRegistryNum").text
        if i.find("{*}shortName")!=None:
            dic['short_name']=i.find("{*}shortName").text 
        dic['full_name']=i.find("{*}fullName").text 
        if i.find("{*}GRBSCode")!=None:
            dic['g_r_b_s_code']=i.find("{*}GRBSCode").text
        if i.find("{*}BIK")!=None:
            dic['b_i_k']=i.find("{*}BIK").text
        if i.find("{*}nomBank")!=None:
            dic['nom_bank']=i.find("{*}nomBank").text
        if i.find("{*}factualAddress")!=None:
            address={}
            if i.find("{*}factualAddress/{*}OKATO")!=None:
                address["OKATO"]=i.find("{*}factualAddress/{*}OKATO").text
            if i.find("{*}factualAddress/{*}addressLine")!=None:    
                address["addressLine"]=i.find("{*}factualAddress/{*}addressLine").text
            if i.find("{*}factualAddress/{*}area")!=None:
                areals={}
                areals["kladrType"]=i.find("{*}factualAddress/{*}area/{*}kladrType").text
                areals["kladrCode"]=i.find("{*}factualAddress/{*}area/{*}kladrCode").text
                if i.find("{*}factualAddress/{*}area/{*}fullName")!=None:
                    areals["fullName"]=i.find("{*}factualAddress/{*}area/{*}fullName").text
                address["area"]=areals
            if i.find("{*}factualAddress/{*}building")!=None:    
                address["building"]=i.find("{*}factualAddress/{*}building").text
            if i.find("{*}factualAddress/{*}country")!=None:
                country={}
                country["countryCode"]=i.find("{*}factualAddress/{*}country/{*}countryCode").text
                if i.find("{*}factualAddress/{*}country/{*}countryFullName")!=None:
                    country["countryFullName"]=i.find("{*}factualAddress/{*}country/{*}countryFullName").text
                address["country"]=country
            if i.find("{*}factualAddress/{*}filledManually")!=None:    
                address["filledManually"]=i.find("{*}factualAddress/{*}filledManually").text
            if i.find("{*}factualAddress/{*}office")!=None:    
                address["office"]=i.find("{*}factualAddress/{*}office").text
            if i.find("{*}factualAddress/{*}region")!=None:
                region={}
                region["kladrType"]=i.find("{*}factualAddress/{*}region/{*}kladrType").text
                region["kladrCode"]=i.find("{*}factualAddress/{*}region/{*}kladrCode").text
                if i.find("{*}factualAddress/{*}region/{*}fullName")!=None:
                    region["fullName"]=i.find("{*}factualAddress/{*}region/{*}fullName").text
                address["region"]=region
            if i.find("{*}factualAddress/{*}settlement")!=None:
                settlement={}
                settlement["kladrType"]=i.find("{*}factualAddress/{*}settlement/{*}kladrType").text
                settlement["kladrCode"]=i.find("{*}factualAddress/{*}settlement/{*}kladrCode").text
                if i.find("{*}factualAddress/{*}settlement/{*}fullName")!=None:
                    settlement["fullName"]=i.find("{*}factualAddress/{*}settlement/{*}fullName").text
                address["settlement"]=settlement
            if i.find("{*}factualAddress/{*}city")!=None:
                city={}
                city["kladrType"]=i.find("{*}factualAddress/{*}city/{*}kladrType").text
                city["kladrCode"]=i.find("{*}factualAddress/{*}city/{*}kladrCode").text
                if i.find("{*}factualAddress/{*}city/{*}fullName")!=None:
                    city["fullName"]=i.find("{*}factualAddress/{*}city/{*}fullName").text
                address["city"]=city
            if i.find("{*}factualAddress/{*}shortStreet")!=None:    
                address["shortStreet"]=i.find("{*}factualAddress/{*}shortStreet").text
            if i.find("{*}factualAddress/{*}street")!=None:
                street={}
                street["kladrType"]=i.find("{*}factualAddress/{*}street/{*}kladrType").text
                street["kladrCode"]=i.find("{*}factualAddress/{*}street/{*}kladrCode").text
                if i.find("{*}factualAddress/{*}street/{*}fullName")!=None:
                    street["fullName"]=i.find("{*}factualAddress/{*}street/{*}fullName").text
                address["street"]=street
            if i.find("{*}factualAddress/{*}zip")!=None:    
                address["zip"]=i.find("{*}factualAddress/{*}zip").text
            dic['factualAddress']=address
        if i.find("{*}postalAddress")!=None:
            dic['postal_address']=i.find("{*}postalAddress").text
        if i.find("{*}email")!=None:
            dic['email']=i.find("{*}email").text
        if i.find("{*}phone")!=None:
            dic['phone']=i.find("{*}phone").text
        if i.find("{*}fax")!=None:
            dic['fax']=i.find("{*}fax").text
        if i.find("{*}contactPerson"):
            person={}
            person["lastName"]=i.find("{*}contactPerson/{*}lastName").text
            person["firstName"]=i.find("{*}contactPerson/{*}firstName").text
            if i.find("{*}contactPerson/{*}middleName")!=None:
                person["middleName"]=i.find("{*}contactPerson/{*}middleName").text
            dic['contactPerson']=person
        if i.find("{*}accounts")!=None:
            accounts=[]
            for acc in i.getiterator("{*}account"):
                account={}
                if acc.find("{*}bankAddress")!=None:
                    account["bankAddress"]=acc.find("{*}bankAddress").text
                account["bankName"]=acc.find("{*}bankName").text
                account["bik"]=acc.find("{*}bik").text
                if acc.find("{*}corrAccount")!=None:
                    account["corrAccount"]=acc.find("{*}corrAccount").text
                if acc.find("{*}paymentAccount")!=None:
                    account["paymentAccount"]=acc.find("{*}paymentAccount").text
                if acc.find("{*}personalAccount")!=None:
                    account["personalAccount"]=acc.find("{*}personalAccount").text
                accounts.append(account)
            dic['accounts']=accounts         
        if i.find("{*}budgets")!=None:
            budgets=[]
            for k in i.getiterator("{*}budget"):
                budgets.append({"code":k.find("{*}code").text,"name":k.find("{*}name").text})
            dic['budgets']=budgets 
        if i.find("{*}headAgency")!=None:
            headAgency={}
            headAgency["regNum"]=i.find("{*}headAgency/{*}regNum").text
            if i.find("{*}headAgency/{*}consRegistryNum")!=None:
                headAgency["consRegistryNum"]=i.find("{*}headAgency/{*}consRegistryNum").text
            if i.find("{*}headAgency/{*}fullName").text:
                headAgency["fullName"]=i.find("{*}headAgency/{*}fullName").text
            dic['headAgency']=headAgency 
        if i.find("{*}orderingAgency")!=None:
            orderingAgency={}
            orderingAgency["regNum"]=i.find("{*}orderingAgency/{*}regNum").text
            if i.find("{*}orderingAgency/{*}consRegistryNum")!=None:
                orderingAgency["consRegistryNum"]=i.find("{*}orderingAgency/{*}consRegistryNum").text
            if i.find("{*}orderingAgency/{*}fullName").text:
                orderingAgency["fullName"]=i.find("{*}orderingAgency/{*}fullName").text
            dic['orderingAgency']=orderingAgency
        if i.find("{*}INN")!=None:
            dic['i_n_n']=i.find("{*}INN").text
        if i.find("{*}KPP")!=None:
            dic['k_p_p']=i.find("{*}KPP").text
        if i.find("{*}registrationDate")!=None:
            dic['registration_date']=i.find("{*}registrationDate").text
        if i.find("{*}UBPCode")!=None:
            dic['u_b_p_code']=i.find("{*}UBPCode").text
        if i.find("{*}IKUInfo")!=None:
            IKUInfo=[]
            for k in i.getiterator("{*}IKUInfo"):
                IKU={}
                IKU['IKU']=k.find("{*}IKU").text
                if k.find("{*}dateStIKU")!=None:
                    IKU['dateStIKU']=k.find("{*}dateStIKU").text
                if k.find("{*}dateEndIKU")!=None:
                    IKU['dateEndIKU']=k.find("{*}dateEndIKU").text
                IKUInfo.append(IKU)
            dic['IKUInfo']=IKUInfo
        if i.find("{*}OGRN")!=None:
            dic['OGRN']=i.find("{*}OGRN").text
        if i.find("{*}OKFS/{*}code")!=None:
            dic['OKFS_id']=i.find("{*}OKFS/{*}code").text
        if i.find("{*}OKOPF")!=None:
            dic['OKOPF']={"code":i.find("{*}OKOPF/{*}code").text,"fullName":i.find("{*}OKOPF/{*}fullName").text}
        if i.find("{*}OKPO")!=None:
            dic['OKPO']=i.find("{*}OKPO").text
        if i.find("{*}OKVED")!=None:
            dic['OKVED']=i.find("{*}OKVED").text
        if i.find("{*}OKOGU")!=None:
            dic['OKOGU']={"code":i.find("{*}OKOGU/{*}code").text,"name":i.find("{*}OKOGU/{*}name").text}
        if i.find("{*}organizationRole")!=None:
            dic['organizationRole']=i.find("{*}organizationRole").text
        if i.find("{*}organizationRoles")!=None:
            organizationRoles=[]
            for role in i.getiterator("{*}organizationRoleItem"):
                organizationRoleItem={}
                if role.find("{*}organizationRole")!=None:
                    organizationRoleItem["organizationRole"]=role.find("{*}organizationRole").text
                if role.find("{*}startDate")!=None:
                    organizationRoleItem["startDate"]=role.find("{*}startDate").text
                if role.find("{*}endDate")!=None:
                    organizationRoleItem["endDate"]=role.find("{*}endDate").text
                organizationRoles.append(organizationRoleItem)
            dic['organizationRoles']=organizationRoles
        if i.find("{*}authorityRegion")!=None:
            authorityRegion={}
            authorityRegion["kladrType"]=i.find("{*}authorityRegion/{*}kladrType")
            if i.find("{*}authorityRegion/{*}kladrCode")!=None:
                authorityRegion["kladrCode"]=i.find("{*}authorityRegion/{*}kladrCode")
            if i.find("{*}authorityRegion/{*}fullName")!=None:
                authorityRegion["fullName"]=i.find("{*}authorityRegion/{*}fullName")
            dic["authorityRegion"]=authorityRegion
        if i.find("{*}organizationType")!=None:
            dic['organizationType']={"code":i.find("{*}organizationType/{*}code").text,"name":i.find("{*}organizationType/{*}name").text}
        if i.find("{*}subordinationType")!=None:
            dic['subordinationType']=i.find("{*}subordinationType").text
        if i.find("{*}url")!=None:
            dic['url']=i.find("{*}url").text
        if i.find("{*}timeZone")!=None:
            dic['timeZone']=i.find("{*}timeZone").text
        if i.find("{*}timeZoneUtcOffset")!=None:
            dic['timeZoneUtcOffset']=i.find("{*}timeZoneUtcOffset").text
        if i.find("{*}timeZoneOlson")!=None:
            dic['timeZoneOlson']=i.find("{*}timeZoneOlson").text
        if i.find("{*}actual")!=None:
            dic['actual']=i.find("{*}actual").text
        if i.find("{*}register")!=None:
            dic['register']=i.find("{*}register").text
        lis.append(dic)
    return lis
def pars_commission(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiCommission"):
        dic={}
        taim=[]
        role=[]
        dic['reg_number']=i.find("{*}regNumber").text
        dic['commission_name']=i.find("{*}commissionName").text
        if i.find("{*}commissionMembers")!=None:
            for k in i.getiterator("{*}commissionMember"):
                for rol in k.getiterator("{*}role"):
                    role.append(rol.find("{*}id").text)    
                if k.find("{*}middleName")!=None:
                    taim.append({"id":k.find("{*}id").text,"role":role,"last_name":k.find("{*}lastName").text,"first_name":k.find("{*}firstName").text,"middle_name":k.find("{*}middleName").text})
                else:
                    taim.append({"id":k.find("{*}id").text,"role":role,"last_name":k.find("{*}lastName").text,"first_name":k.find("{*}firstName").text})
            dic['placing_way_id']=taim
        if i.find("{*}owner")!=None:
            dic['owner_id']=i.find("{*}owner/{*}regNum").text
        dic['actual']=i.find("{*}actual").text  
        lis.append(dic)
    return lis
def pars_k_t_r_u(fail):
    lis=[]
    for i in fail.getiterator("{*}data"):
        dic={}
        taim=[]
        dic['code']=i.find("{*}code").text
        if i.find("{*}version")!=None:
            dic['version']=i.find("{*}version").text
        if i.find("{*}inclusionDate")!=None:
            dic['inclusion_date']=i.find("{*}inclusionDate").text
        if i.find("{*}publishDate")!=None:
            dic['publish_date']=i.find("{*}publishDate").text
        if i.find("{*}name")!=None:
            dic['name']=i.find("{*}name").text
        for k in i.getiterator("{*}OKPD2"):
            taim.append(k.find("{*}code").text)
        dic["o_k_p_d2_id"]=taim
        taim=[]
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}applicationDateStart")!=None:
            dic['application_date_start']=i.find("{*}applicationDateStart").text
        if i.find("{*}applicationDateEnd")!=None:
            dic['application_date_end']=i.find("{*}applicationDateEnd").text
        if i.find("{*}OKEIs")!=None:
            for k in i.getiterator("{*}OKEIs"):
                for code in k.getiterator("{*}OKEI"):
                    taim.append(code.find("{*}code").text)
            dic["o_k_e_i_id"]=taim
            taim=[]
        if i.find("{*}NSI")!=None:
            nsi={}
            if i.find("{*}NSI/{*}standarts")!=None:
                for k in i.getiterator("{*}standart"):
                    taim.append(k.find("{*}docName").text)
                nsi["standart"]=taim
                taim=[]
            if i.find("{*}NSI/{*}classifiers")!=None:
                for k in i.getiterator("{*}classifier"):
                    val={}
                    for valie in k.getiterator("{*}value"):
                        val["code"]=valie.find("{*}code").text
                        val["name"]=valie.find("{*}name").text
                        if valie.find("{*}descriptionValue")!=None:
                            val["description_value"]=valie.find("{*}descriptionValue").text
                        if valie.find("{*}price")!=None:
                            val["price"]=valie.find("{*}price").text
                    taim.append({"name":i.find("{*}name").text,"values":val})
                nsi["classifiers"]=taim
                taim=[]
            if i.find("{*}NSI/{*}standardContracts")!=None:
                contract={}
                for k in i.getiterator("{*}standardContract"):
                    if k.find("{*}standardContractNumber")!=None:
                        contract['standard_contract_number']=k.find("{*}standardContractNumber").text
                    if k.find("{*}type")!=None:
                        contract['type']=k.find("{*}type").text
                    if k.find("{*}document")!=None:
                        doc={}
                        if k.find("{*}document/{*}number")!=None:
                            doc["number"]=k.find("{*}document/{*}number").text
                        if k.find("{*}document/{*}name")!=None:
                            doc["name"]=k.find("{*}document/{*}name").text
                        if k.find("{*}document/{*}date")!=None:
                            doc["date"]=k.find("{*}document/{*}date").text
                        contract['document']=doc
                nsi["standardContracts"]=contract
                taim=[]
            dic["n_s_i"]=nsi
        if i.find("{*}characteristics")!=None:
            characts=[]
            for k in i.getiterator("{*}characteristic"):
                charact={}
                charact["code"]=k.find("{*}code").text
                charact["name"]=k.find("{*}name").text
                charact["type"]=k.find("{*}type").text
                if k.find("{*}kind")!=None:
                    charact["kind"]=k.find("{*}kind").text
                if k.find("{*}actual")!=None:
                    charact["actual"]=k.find("{*}actual").text
                if k.find("{*}isRequired")!=None:
                    charact["isRequired"]=k.find("{*}isRequired").text
                if k.find("{*}choiceType")!=None:
                    charact["choiceType"]=k.find("{*}choiceType").text
                valus=[]
                for val in k.getiterator("{*}value"):
                    valu={}
                    if val.find("{*}qualityDescription")!=None:
                        valu['qualityDescription']=val.find("{*}qualityDescription").text
                    else:
                        if val.find("{*}OKEI")!=None:
                            valu['o_k_e_i_id']=val.find("{*}OKEI/{*}code").text
                        if val.find("{*}valueFormat")!=None:
                            valu['value_format']=val.find("{*}valueFormat").text
                        if val.find("{*}rangeSet")!=None:
                            rang={}
                            if val.find("{*}rangeSet/{*}valueRange/{*}minMathNotation")!=None:
                                rang["minMathNotation"]=val.find("{*}rangeSet/{*}valueRange/{*}minMathNotation").text#обозначение мат знака либо больше либо больше равно
                                rang["min"]=val.find("{*}rangeSet/{*}valueRange/{*}min").text
                            if val.find("{*}rangeSet/{*}valueRange/{*}maxMathNotation")!=None:
                                rang["maxMathNotation"]=val.find("{*}rangeSet/{*}valueRange/{*}maxMathNotation").text#обозначение мат знака либо меньше либо меньше равно
                                rang["max"]=val.find("{*}rangeSet/{*}valueRange/{*}max").text
                            valu['range_set']=rang
                        if val.find("{*}valueSet")!=None:
                            valu['valueSet']=val.find("{*}valueSet/{*}concreteValue").text
                    valus.append(valu)
                charact["value"]=valu
                characts.append(charact)
            dic["characteristics"]=characts
        if i.find("{*}products")!=None:
            product={}
            for k in i.getiterator("{*}product"):
                if k.find("{*}tradeName")!=None:
                    product["trade_name"]=k.find("{*}tradeName").text
                if k.find("{*}manufacturer")!=None:
                    product["manufacturer"]=k.find("{*}manufacturer").text
                if k.find("{*}placeOfOrigin")!=None:
                    product["placeOfOrigin"]=k.find("{*}placeOfOrigin/{*}countryCode").text
                if k.find("{*}price")!=None:
                    product["price"]=k.find("{*}price").text
                if k.find("{*}characteristics")!=None:
                    product["price"]=k.find("{*}characteristics/{*}code").text              
        if i.find("{*}rubricators")!=None:
            for k in i.getiterator("{*}rubricatorInfo"):
                taim.append(k.find("{*}name").text)
            dic['rubricators']=taim
            taim=[]
        if i.find("{*}industryClassifier")!=None:
            dic["industryClassifier"]=i.find("{*}industryClassifier/code").text
        if i.find("{*}attachments")!=None:
            colekt=[]
            for k in i.getiterator("{*}attachment"):
                doc={}
                taim=[]
                if k.find("{*}publishedContentId")!=None:
                    doc["published_content_id"]=k.find("{*}publishedContentId").text
                doc["file_name"]=k.find("{*}fileName").text
                if k.find("{*}fileSize")!=None:
                    doc["file_size"]=k.find("{*}fileSize").text
                if k.find("{*}docDescription")!=None:
                    doc["doc_description"]=k.find("{*}docDescription").text
                if k.find("{*}docDate")!=None:
                    doc["doc_date"]=k.find("{*}docDate").text
                if k.find("{*}url")!=None:
                    doc["url"]=k.find("{*}url").text
                if k.find("{*}contentId")!=None:
                    doc["content_id"]=k.find("{*}contentId").text
                if k.find("{*}content")!=None:
                    doc["content"]=k.find("{*}content").text
                if k.find("{*}cryptoSigns")!=None:
                    for typ in k.getiterator("{*}signature"):
                        taim.append({"type":typ.attrib['type'],"signature":typ.text})
                    doc['crypto_signs']=taim
                if k.find("{*}attachmentBusinessType")!=None:
                    doc["attachmentBusinessType"]=k.find("{*}attachmentBusinessType").text
                colekt.append(doc)
            dic["attachments"]=colekt
        if i.find("{*}cancelInfo")!=None:
            dic['cancelInfo']=[i.find("{*}cancelInfo/{*}cancelDate").text,i.find("{*}cancelInfo/{*}cancelReason").text]
        if i.find("{*}nsiDescription")!=None:
            dic['nsi_description']=i.find("{*}nsiDescription").text
        if i.find("{*}isTemplate")!=None:
            dic['is_template']=i.find("{*}isTemplate").text
        if i.find("{*}parentPositionInfo")!=None:
            dic['parent_position_info_id']=i.find("{*}parentPositionInfo/{*}code").text
        if i.find("{*}externalCode")!=None:
            dic['external_code']=i.find("{*}externalCode").text
        if i.find("{*}noNewFeatures")!=None:
            dic['no_new_features']=i.find("{*}noNewFeatures").text
        if i.find("{*}noNewFeaturesReason")!=None:
            dic['no_new_features_reason']=i.find("{*}noNewFeaturesReason").text
        lis.append(dic)
    return lis
def pars_farm_drug_interchange_group(fail):
    lis=[]
    for i in fail.getiterator("{*}interchangeGroup"):
        dic={}
        taim=[]
        inf={}
        inf['interchange_group_i_d']=i.find("{*}groupInfo/{*}interchangeGroupID").text
        inf['code']=i.find("{*}groupInfo/{*}code").text
        inf['name']=i.find("{*}groupInfo/{*}name").text
        inf['level']=i.find("{*}groupInfo/{*}level").text
        inf['is_actual']=i.find("{*}groupInfo/{*}isActual").text
        inf['date_create']=i.find("{*}groupInfo/{*}dateCreate").text
        inf['date_change']=i.find("{*}groupInfo/{*}dateChange").text
        inf['hash']=i.find("{*}groupInfo/{*}hash").text
        if i.find("{*}groupInfo/{*}version")!=None:
            inf['version']=i.find("{*}groupInfo/{*}version").text
        if i.find("{*}groupInfo/{*}ancestorID")!=None:
            inf['ancestor_i_d']=i.find("{*}groupInfo/{*}ancestorID").text
        dic["group_info"]=inf
        inf={}
        dic["group_o_k_e_i"]={"name":i.find("{*}groupOKEI/{*}name").text,"o_k_e_i_id":i.find("{*}groupOKEI/{*}OKEI/{*}code").text}
        for k in i.getiterator("{*}groupPrice"):
            pric={}
            if k.find("{*}value")!=None:
                pric['value']=k.find("{*}value").text
            if k.find("{*}usageMin")!=None:
                pric['usage_min']=k.find("{*}usageMin").text
            if k.find("{*}usageMax")!=None:
                pric['usage_max']=k.find("{*}usageMax").text
            if k.find("{*}type")!=None:
                pric['type']=k.find("{*}type").text
            pric['date_create']=k.find("{*}dateCreate").text
            pric['date_start']=k.find("{*}dateStart").text
            pric['date_end']=k.find("{*}dateEnd").text
            pric['is_actual']=k.find("{*}isActual").text
        for k in i.getiterator("{*}childGroup"):
            inf['interchange_group_i_d']=i.find("{*}groupInfo/{*}interchangeGroupID").text
            inf['code']=k.find("{*}groupInfo/{*}code").text
            inf['name']=k.find("{*}groupInfo/{*}name").text
            inf['level']=k.find("{*}groupInfo/{*}level").text
            inf['isActual']=k.find("{*}groupInfo/{*}isActual").text
            inf['dateCreate']=k.find("{*}groupInfo/{*}dateCreate").text
            inf['dateChange']=k.find("{*}groupInfo/{*}dateChange").text
            inf['hash']=k.find("{*}groupInfo/{*}hash").text
            if k.find("{*}groupInfo/{*}version")!=None:
                inf['version']=k.find("{*}groupInfo/{*}version").text
            if k.find("{*}groupInfo/{*}ancestorID")!=None:
                inf['ancestor_i_d']=k.find("{*}groupInfo/{*}ancestorID").text
            for elem in k.getiterator("{*}element"):
                elements=[]
                element={}
                if elem.find("{*}MNNExternalCode")!=None:
                    element["m_n_n_external_code"]=elem.find("{*}MNNExternalCode").text
                element["date_create"]=elem.find("{*}dateCreate").text
                if elem.find("{*}dateChange")!=None:
                    element["date_change"]=elem.find("{*}dateChange").text
                if elem.find("{*}dateStart")!=None:
                    element["date_start"]=elem.find("{*}dateStart").text
                if elem.find("{*}dateEnd")!=None:
                    element["date_end"]=elem.find("{*}dateEnd").text
                if elem.find("{*}lastUpdateDate")!=None:
                    element["last_update_date"]=elem.find("{*}lastUpdateDate").text
                element["is_actual"]=elem.find("{*}isActual").text
                element["rate_value"]=elem.find("{*}rateValue").text
                if elem.find("{*}packRequirement")!=None:
                    element["pack_requirement"]=elem.find("{*}packRequirement").text
                elements.append(element)
            inf["elements"]=elements
        dic["child_group"]=inf
        lis.append(dic)
    return lis
def pars_farm_drugs_dictionary(fail):
    lis=[]
    for i in fail.getiterator("{*}MNNInfo"):
        dic={}
        taim=[]
        dosa={}
        dic['groupInfo']={"group_code":i.find("{*}groupInfo/{*}groupCode").text,"parent_group_code":i.find("{*}groupInfo/{*}parentGroupCode").text,"group_name":i.find("{*}groupInfo/{*}groupName").text,"actual":i.find("{*}groupInfo/{*}actual").text}
        dic['m_n_n_code']=i.find("{*}MNNCode").text
        dic['m_n_n_drug_code']=i.find("{*}MNNDrugCode").text
        dic['m_n_n_external_code']=i.find("{*}MNNExternalCode").text
        dic['m_n_n_hash']=i.find("{*}MNNHash").text
        dic['m_n_n_name']=i.find("{*}MNNName").text
        dic['ftg_info']={"code":i.find("{*}ftgInfo/{*}ftgCode").text,"name":i.find("{*}ftgInfo/{*}ftgName").text}
        dic['medicamental_form_info']={"code":i.find("{*}medicamentalFormInfo/{*}medicamentalFormCode").text,"name":i.find("{*}medicamentalFormInfo/{*}medicamentalFormName").text}
        dosa["dosage_code"]=i.find("{*}dosagesInfo/{*}dosageInfo/{*}dosageCode").text
        dosa["dosage_name"]=i.find("{*}dosagesInfo/{*}dosageInfo/{*}dosageName").text
        dosa["dosage_g_r_l_s_value"]=i.find("{*}dosagesInfo/{*}dosageInfo/{*}dosageGRLSValue").text
        dosa["dosage_o_k_e_i_id"]=i.find("{*}dosagesInfo/{*}dosageInfo/{*}dosageOKEI/{*}code").text
        dosa["dosage_value"]=i.find("{*}dosagesInfo/{*}dosageInfo/{*}dosageValue").text
        dosa["dosage_user_id"]=i.find("{*}dosagesInfo/{*}dosageInfo/{*}dosageUser/{*}dosageUserOKEI").text
        dic["dosage"]=dosa
        for k in i.getiterator("{*}athInfo"):
            taim.append({"ath_code":k.find("{*}athCode").text,"ath_external_code":k.find("{*}athExternalCode").text,"ath_name":k.find("{*}athName").text})
        dic["ath_info"]=taim
        taim=[]
        dic['is_z_n_v_l_p']=i.find("{*}isZNVLP").text
        dic['is_narcotiс']=i.find("{*}isNarcotic").text
        dic['o_k_p_d2_id']=i.find("{*}OKPD2/{*}code").text
        dic['create_date']=i.find("{*}createDate").text
        dic['start_date']=i.find("{*}startDate").text
        if i.find("{*}endDate")!=None:
            dic['end_date']=i.find("{*}endDate").text
        if i.find("{*}pricesInfo")!=None:
            for k in i.getiterator("{*}priceInfo"):
                price={}
                price["price_code"]=k.find("{*}priceCode").text
                price["price_value"]=k.find("{*}priceValue").text
                price["price_type"]=k.find("{*}priceType").text
                price["price_sigma_value"]=k.find("{*}priceSigmaValue").text
                if k.find("{*}priceSigmaValue")!=None:
                    price["usage_min"]=k.find("{*}usageMin").text
                if k.find("{*}usageMax")!=None:
                    price["usage_max"]=k.find("{*}usageMax").text
                price["author"]=k.find("{*}author").text
                price["create_date"]=k.find("{*}createDate").text
                price["start_date"]=k.find("{*}startDate").text
                if k.find("{*}endDate")!=None:
                    price["end_date"]=k.find("{*}endDate").text
                taim.append(price)
            dic["prices_info"]=taim
            taim=[]
        for k in i.getiterator("{*}positionTradeName"):
            trade={}
            trade['positionTradeNameCode']=k.find("{*}positionTradeNameCode").text
            trade['positionTradeNameExternalCode']=k.find("{*}positionTradeNameExternalCode").text
            trade['positionTradeNameHash']=k.find("{*}positionTradeNameHash").text
            trade['drugCode']=k.find("{*}drugCode").text
            if k.find("{*}MNNNormName")!=None:
                trade['MNNNormName']=k.find("{*}MNNNormName").text
            if k.find("{*}dosageNormName")!=None:
                trade['dosageNormName']=k.find("{*}dosageNormName").text
            if k.find("{*}medicamentalFormNormName")!=None:
                trade['medicamentalFormNormName']=k.find("{*}medicamentalFormNormName").text
            if k.find("{*}isDosed")!=None:
                trade['isDosed']=k.find("{*}isDosed").text
            if k.find("{*}conv")!=None:
                trade['conv']=k.find("{*}conv").text
            trade['tradeInfo']={"tradeCode":k.find("{*}tradeInfo/{*}tradeCode").text,"tradeName":k.find("{*}tradeInfo/{*}tradeName").text}
            for packaging in k.getiterator("{*}packagingInfo"):
                packs=[]
                pack={}
                pack["primary_packaging_info"]={"primaryPackagingCode":packaging.find("{*}primaryPackagingInfo/{*}primaryPackagingCode").text,"primaryPackagingName":packaging.find("{*}primaryPackagingInfo/{*}primaryPackagingName").text}
                pack["packaging1_quantity"]=packaging.find("{*}packaging1Quantity").text
                pack["packaging2_quantity"]=packaging.find("{*}packaging2Quantity").text
                pack["consumer_packaging_info"]={"consumerPackagingCode":packaging.find("{*}consumerPackagingInfo/{*}consumerPackagingCode").text,"consumerPackagingName":packaging.find("{*}consumerPackagingInfo/{*}consumerPackagingName").text}
                packs.append(pack)
            trade['packagings_info']=packs
            trade['completeness']=k.find("{*}completeness").text
            trade['owner']={"certificateKeeperName":k.find("{*}owner/{*}certificateKeeperName").text,"certificateKeeperCountry":k.find("{*}owner/{*}certificateKeeperCountry/{*}countryCode").text}
            trade['certificateNumber']=k.find("{*}certificateNumber").text
            trade['certificateDate']=k.find("{*}certificateDate").text
            if k.find("{*}certificateUpdateDate")!=None:
                trade['certificateUpdateDate']=k.find("{*}certificateUpdateDate").text
            if k.find("{*}barcode")!=None:
                trade['barcode']=k.find("{*}barcode").text
            trade['manufacturerInfo']={"manufacturerOKSM":k.find("{*}manufacturerInfo/{*}manufacturerOKSM/{*}countryCode").text,"manufacturerAdress":k.find("{*}manufacturerInfo/{*}manufacturerAdress").text,"manufacturerName":k.find("{*}manufacturerInfo/{*}manufacturerName").text}
            prices=[]
            for pric in k.getiterator("{*}priceInfo"):
                price={}
                price["priceCode"]=pric.find("{*}priceCode").text
                price["priceValue"]=pric.find("{*}priceValue").text
                price["priceType"]=pric.find("{*}priceType").text
                price["priceSigmaValue"]=pric.find("{*}priceSigmaValue").text
                price["createDate"]=pric.find("{*}createDate").text
                price["startDate"]=pric.find("{*}startDate").text
                if pric.find("{*}endDate")!=None:
                    price["endDate"]=pric.find("{*}endDate").text
                prices.append(price)
            trade['priceInfo']=prices
            lim_prices=[]
            for lim_pric in k.getiterator("{*}limPriceInfo"):
                lim_price={}
                lim_price["priceCode"]=lim_pric.find("{*}priceCode").text
                lim_price["priceValue"]=lim_pric.find("{*}priceValue").text
                lim_price["reqDate"]=lim_pric.find("{*}reqDate").text
                lim_price["reqNumber"]=lim_pric.find("{*}reqNumber").text
                if lim_pric.find("{*}endDate")!=None:
                    lim_price["endDate"]=lim_pric.find("{*}endDate").text
                if lim_pric.find("{*}reasonEnd")!=None:
                    lim_price["reasonEnd"]=lim_pric.find("{*}reasonEnd").text
                if lim_pric.find("{*}deactivateDate")!=None:
                    lim_price["deactivateDate"]=lim_pric.find("{*}deactivateDate").text                
                lim_prices.append(lim_price)
            trade['lim_price_info']=lim_prices
            trade['createDate']=k.find("{*}createDate").text
            trade['startDate']=k.find("{*}startDate").text
            if k.find("{*}endDate")!=None:
                trade['endDate']=k.find("{*}endDate").text
            if k.find("{*}reasonEnd")!=None:
                trade['reasonEnd']=k.find("{*}reasonEnd").text
            trade['changeDate']=k.find("{*}changeDate").text
            trade['actual']=k.find("{*}actual").text
            if k.find("{*}lastChangeDate")!=None:
                trade['lastChangeDate']=k.find("{*}lastChangeDate").text
            descends=[]
            for descendant in k.getiterator("{*}positionTradeNameExternalCode"):
                descends.append(descendant.text)
            trade['descendantInfo']=descends
            ancestors=[]
            for ancestor in k.getiterator("{*}ancestorListInfo"):
                ancestors.append(ancestor.find("{*}positionTradeNameExternalCode").text)
            trade['ancestorListInfo']=ancestors
            if k.find("{*}invalidationDataListInfo")!=None:
                inval_lic=[]
                for inval in k.getiterator("{*}invalidationData"):
                    inval_lic.append({"code":inval.find("{*}code").text,"date":inval.find("{*}date").text,"description":inval.find("{*}description").text})
                trade["invalidation_data_list_info"]=inval_lic
            taim.append(trade)
        dic["position_trade_name"]=taim
        taim=[]    
        dic['change_date']=i.find("{*}changeDate").text
        dic['actual']=i.find("{*}actual").text
        if i.find("{*}lastChangeDate")!=None:
            dic['last_change_date']=i.find("{*}lastChangeDate").text
        if i.find("{*}descendantInfo")!=None:
            for k in i.getiterator("{*}positionTradeNameExternalCode"):
                taim.append(k.text)
            dic["ancestors_list_info"]=taim
            taim=[]
        if i.find("{*}ancestorsListInfo")!=None:
            for ancestor in k.getiterator("{*}ancestorListInfo"):
                taim.append(ancestor.find("{*}positionTradeNameExternalCode").text)
            dic["ancestors_list_info"]=taim
            taim=[]
        if i.find("{*}nonNormMNNsListInfo")!=None:
            for k in i.getiterator("{*}nonNormMNNInfo"):
                taim.append(k.find("{*}MNNName").text)
            dic["non_norm_m_n_ns_list_info"]=taim
            taim=[]   
        if i.find("{*}nonNormMedFormsDosagesListInfo")!=None:
            for k in i.getiterator("{*}nonNormMedFormDosage"):
                taim.append({"medicamental_form_name":k.find("{*}medicamentalFormName").text,"dosage_name":k.find("{*}dosageName").text})
            dic["invalidation_data_list_info"]=taim
            taim=[]
        if i.find("{*}invalidationDataListInfo")!=None:
            for k in i.getiterator("{*}invalidationData"):
                taim.append({"code":k.find("{*}code").text,"date":k.find("{*}date").text,"description":k.find("{*}description").text})
            dic["invalidation_data_list_info"]=taim
            taim=[]
        lis.append(dic)
    return lis
def pars_calendar_day (fail):
    lis=[]
    for i in fail.getiterator("{*}day"):
        dic={}
        dic['dayDate']=i.find("{*}dayDate").text
        if i.find("{*}regions")!=None:
            regions=[]
            for k in i.getiterator("{*}region"):
                region={}
                region["kladrType"]=k.find("{*}kladrType").text
                region["kladrCode"]=k.find("{*}kladrCode").text
                region["fullName"]=k.find("{*}fullName").text
                regions.append(region)
            dic["regions"]=regions
        dic['isWorkDay']=i.find("{*}isWorkDay").text
        lis.append(dic)
    return lis
def record(recor):
    for colum in recor.key():
        if recor[colum].type==list :
            lis_recor(record[colum])
        elif recor[colum].type==dict:
            recor[colum]=record(recor[colum])
    

def lis_record(lis):
    for recor in lis:
        record(recor)
def pars (fail):
    pars=etree.parse(fail,parser)
    s=fail.name[fail.name.find("nsi")+3:fail.name.find("_")]
    if s[-1]=='s':
        s=s[0:-1]
    elif s.find("List")!=-1:
        s=s[:s.find("List")]
    s=re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    f=globals()["pars_"+s]
    s=f(pars)

    return s
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
