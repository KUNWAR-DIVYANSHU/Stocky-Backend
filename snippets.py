# @app.route('/graph/<string:graphtype>', methods=['POST'])
# def sendGraphData(graphtype):

#     receievedData = request.json
#     df = pd.read_json(receievedData,orient = 'split')
#     graphObj = fg.Data(df , graphtype)

#     return jsonify(graphObj.send_data().to_json())

# @app.route('/indicator/<string:indicator_name>',
#  methods=['POST'])
# def sendIndData(indicator_name):
#     try:
#         period = request.args.get('period')
#         columns = request.args.get('columns')
#         print(indicator_name , period , columns)
#     except:
#         print("error")
#     receievedData = request.json
#     df = pd.read_json(receievedData,orient = 'split')
#     data_r = calcIndData(df,indicator_name,period,columns)
#     return jsonify(data_r.to_json())
# def calcIndData(df,indicator_name='atr',period=14,columns="close"):
#     if(indicator_name == "atr"):
#         return ind.atr(df,period=int(period))


# @app.route('/news')
# def sendNews():
#     return "aaj ki taaza khabar"