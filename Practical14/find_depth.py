import datetime
def dom():
    start_time=datetime.datetime.now()
    import xml.dom.minidom
    doc=xml.dom.minidom.parse("go_obo.xml")
    max_terms={
        "molecular_function":{"count":0},
        "biological_process":{"count":0},
        "cellular_component":{"count":0},
    }
    terms=doc.getElementsByTagName("term")
    for term in terms:
        namespace=term.getElementsByTagName("namespace")[0].firstChild.nodeValue
        term_id=term.getElementsByTagName("id")[0].firstChild.nodeValue
        term_name=term.getElementsByTagName("name")[0].firstChild.nodeValue
        is_a=term.getElementsByTagName("is_a")
        term_count=len(is_a)
        if term_count>max_terms[namespace]['count']:
            max_terms[namespace]["id"]=term_id
            max_terms[namespace]["name"]=term_name
            max_terms[namespace]["count"]=term_count
    print('DOM API:')
    for namespa in ['molecular_function','biological_process','cellular_component']:
        print(f'{namespa}: id:{max_terms[namespa]['id']}, name:{max_terms[namespa]['name']}, count:{max_terms[namespa]['count']}')
    stop_time=datetime.datetime.now()
    duration=(stop_time-start_time).total_seconds()
    print('Duration:',duration)
    return

def sax():
    start_time=datetime.datetime.now()
    import xml.sax
    class TermHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.current_element=''
            self.name=''
            self.id=''
            self.namespace=''
            self.is_a_count=0
            self.max_terms={
                "molecular_function": {"id": "", "name": "", "count": 0},
                "biological_process": {"id": "", "name": "", "count": 0},
                "cellular_component": {"id": "", "name": "", "count": 0},
            }
        def startElement(self,tag,attrs):
            self.current_element=tag
            if tag=='term':
                self.namespace=''
                self.is_a_count=0
                self.name=''
                self.id=''
        def endElement(self,tag):
            if tag=='term':
                #print(self.namespace)
                if self.namespace in self.max_terms:
                    if self.is_a_count>self.max_terms[self.namespace]["count"]:
                        self.max_terms[self.namespace]["id"] = self.id
                        self.max_terms[self.namespace]["name"] = self.name
                        self.max_terms[self.namespace]["count"] = self.is_a_count
            self.current_element=''
        def characters(self,content):
            if self.current_element=='namespace':
                self.namespace=content
            elif self.current_element=='name':
                self.name+=content
            elif self.current_element=='id':
                self.id=content
            elif self.current_element=='is_a':
                self.is_a_count+=1
    parser=xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    handler=TermHandler()
    parser.setContentHandler(handler)
    parser.parse('go_obo.xml')
    print('SAX API:')
    for namespa in ['molecular_function','biological_process','cellular_component']:
        print(f'{namespa}: id:{handler.max_terms[namespa]['id']}, name:{handler.max_terms[namespa]['name']}, count:{handler.max_terms[namespa]['count']}')
    stop_time=datetime.datetime.now()
    duration=(stop_time-start_time).total_seconds()
    print('Duration:',duration)
    return

dom()
sax()
#DOM takes 22.3 seconds.
#SAX takes 4.5 seconds.
#SAX is quicker than DOM.