# -*- coding:utf-8 -*-
from models import caseModel


class CaseControllers:
    """
    caseSeq,apiId,appName,apiType,requestType,apiName,apiHost,apiPath,parameter,response,isChange,isRead,authType,actualValue,infoRelate,remark,caseTitle
        self.caseSeq = caseSeq
        self.apiId = apiId
        self.appName = appName
        self.apiType = apiType
        self.requestType = requestType
        self.apiName = apiName
        self.apiHost = apiHost
        self.apiPath = apiPath
        self.parameter = parameter
        self.response = response
        self.isChange = isChange
        self.isRead = isRead
        self.authType = authType
        self.actualValue = actualValue
        self.infoRelate = infoRelate
        self.remark = remark
        self.caseTitle = caseTitle
    """

    def __init__(self):
        pass

    def queryCase(self,proName,isChange,casePath,caseSeq):
        param_dict = {}
        if proName != '0':
            param = {'app_name':proName}
            param_dict.update(param)
        if isChange != '0':
            param = {'isChange':isChange}
            param_dict.update(param)
        if casePath is not None and casePath != '':
            param = {'api_path':casePath}
            param_dict.update(param)
        if caseSeq is not None and caseSeq != '':
            param = {'case_seq':caseSeq}
            param_dict.update(param)
        case = caseModel.Case()
        data = case.query(param_dict)
        return {"code":"1","msg":"操作成功","data":data}

    def queryProName(self):
        case = caseModel.Case()
        proName_tup = case.queryProName()
        proName_ls = []
        # 遍历元组元素,放到列表返回
        for i in proName_tup:
            proName_ls.append(i[0])
        data = proName_ls
        return {"code": "1", "msg": "操作成功", "data": data}



if __name__ == '__main__':
    caseController = CaseControllers()
    print(caseController.queryCaseBySeq('daup','1',None,None))
