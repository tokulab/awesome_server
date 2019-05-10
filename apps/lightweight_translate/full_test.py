import api as translate_api

translater = translate_api.TrainslateApi()
result = translater.get_text("これはテストです。")
print(result)