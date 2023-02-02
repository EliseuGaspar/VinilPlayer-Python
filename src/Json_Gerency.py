import json


class GerenciadorJson():
    
    def __init__(self ,):
        pass

    def UltimaLista(self ,):
        with open('database/init.json') as file:
            conteudo = file.read()
            conteudo_json = json.loads(conteudo)
        
        return conteudo_json["Ultima_Lista"]
    
    def AdicionarLista(self , dir : str):
        try:
            LIST_ = []
            with open('database/init.json') as file:
                conteudo = file.read()
                conteudo_json = json.loads(conteudo)
            if dir != []:
                list_ = conteudo_json["Ultima_Lista"]
                for item in list_:
                    LIST_.append(item)
                LIST_.append(dir)
                conteudo_json["Ultima_Lista"] = LIST_
            else:
                conteudo_json["Ultima_Lista"] = []

            with open('database/init.json','w',encoding='utf-8') as file:
                json.dump(conteudo_json,file,indent=4,sort_keys=True)
            return True
        except:
            return False

    def CurrentColor(self):
        with open('database/apparence.json',encoding='utf-8') as file:
            content_text = file.read()
            content_json = json.loads(content_text)
        
        return content_json["current_color"]

    def ChangeCurrentColor(self, color : str):
        with open('database/apparence.json',encoding='utf-8') as file:
            content_text = file.read()
            content_json = json.loads(content_text)
        
        content_json["current_color"] = color
        
        with open('database/apparence.json','w',encoding='utf-8') as file:
            json.dump(content_json,file,indent=4,sort_keys=True)

    def CurrentIcone(self):
        with open('database/apparence.json',encoding='utf-8') as file:
            content_text = file.read()
            content_json = json.loads(content_text)
        
        return content_json["current_icone"]

    def ChangeCurrentIcone(self, index : int):
        with open('database/apparence.json',encoding='utf-8') as file:
            content_text = file.read()
            content_json = json.loads(content_text)
        
        content_json["current_icone"] = index
        
        with open('database/apparence.json','w',encoding='utf-8') as file:
            json.dump(content_json,file,indent=4,sort_keys=True)
    
    def Window(self,type : str):
        with open('database/window.json',encoding='utf-8') as file:
            content_text = file.read()
            content_json = json.loads(content_text)
        if type == 'vol':
            return content_json["volume"]
        elif type == 're':
            return content_json["repeat"]
        elif type == 'pl':
            return content_json["playlist"]
        elif type == 'la':
            return content_json["label_abrir"]
        else:
            return content_json["label_info"]

    def SetWindow(self, type : str , value : None):
        with open('database/window.json',encoding='utf-8') as file:
            content_text = file.read()
            content_json = json.loads(content_text)
        
        if type == 'vol':
            content_json["volume"] = value
        elif type == 're':
            content_json["repeat"] = value
        elif type == 'pl':
            content_json["playlist"] = value
        elif type == 'la':
            content_json["label_abrir"] = value
        else:
            content_json["label_info"] = value
        
        with open('database/window.json','w',encoding='utf-8') as file:
            json.dump(content_json,file,indent=4,sort_keys=True)
    
