# -*- coding:utf-8 -*-
import requests
from flask import Flask,render_template,request
from controllers import caseController
from commonMethod import getHost

app = Flask(__name__)


@app.route('/')
def test():
    """
    首页
    :return:
    """
    # 返回所有项目名称
    handler = caseController.CaseControllers()
    proName_results = handler.queryProName()
    # 放到render_template返回的参数,在指定页可直接{{}}使用
    # return的需要用axios接收
    return render_template('home.html', proName_results=proName_results, host=host_front)


@app.route('/queryCase', methods=['POST'])
def queryCase():
    """
    id查询
    :return:
    """
    # data = request.json.get("data")
    proName = request.get_json()['proName']
    isChange = request.get_json()['isChange']
    casePath = request.get_json()['casePath']
    caseSeq = request.get_json()['caseSeq']
    handler = caseController.CaseControllers()
    case_results = handler.queryCase(proName,isChange,casePath,caseSeq)
    return case_results


if __name__ == '__main__':
    # 获取project在运行的本机ipv4地址
    host = getHost.GetHost.host()
    # 测试环境开启Debug 生产关闭
    if str(host) == '10.10.9.4':
        app.debug = True
        host_front = "{}:5000".format(host)
    else:
        app.debug = False
        # 生产域名
        host_front = "testautomated.lianouyiyuan.com"
    app.run(port=5000,host=host)

