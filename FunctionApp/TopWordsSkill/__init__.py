
import azure.functions as func
import json
import logging
import string  

from collections import Counter

# TODO - enhance this list of stopwords
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    #logging.info('Python HTTP trigger function processed a request.')

    try:
        body = json.dumps(req.get_json())
    except ValueError:
        return func.HttpResponse(
             "Invalid body",
             status_code=400
        )
    
    if body:
        result = compose_response(body)
        return func.HttpResponse(result, mimetype="application/json")
    else:
        return func.HttpResponse(
             "Invalid body",
             status_code=400
        )


def compose_response(json_data):
    results = {}
    results["values"] = []
    input_values = json.loads(json_data)['values']

    for input_value in input_values:
        output_value = transform_value(input_value)
        if output_value != None:
            results['values'].append(output_value)
    return json.dumps(results, ensure_ascii=False)

## Perform an operation on a record
def transform_value(value):
    try:
        recordId = value['recordId']
    except AssertionError  as error:
        return None

    # Validate the inputs
    try:         
        assert ('data' in value), "'data' field is required."
        data = value['data']        
        assert ('text' in data), "'text' field is required in 'data' object."
        #assert ('text2' in data), "'text2' field is required in 'data' object."
        # TODO - what are the required fields???  text, text1, text2, etc?
    except AssertionError  as error:
        return (
            {
            "recordId": recordId,
            "errors": [ { "message": "Error:" + error.args[0] }   ]       
            })

    try:  
        text = value['data']['text'] 
        #logging.info('text: ' + text) 
        topWordsString = getTopWords(text)
        logging.info('topWordsString: ' + topWordsString) 
    except:
        return (
            {
            "recordId": recordId,
            "errors": [ { "message": "Could not complete operation for record." }   ]       
            })

    return ({
            "recordId": recordId,
            "data": {
                "text": topWordsString
                    }
            })

def getTopWords(input_text):
    words_list, top_words_list = list(), list()
    for input_word in input_text.split(' '):
        words_list.append(translate_word(input_word))

    c = Counter(words_list)  # [('web', 5), ('', 1), ('flask', 1), ('development', 1), ...]
    for tw_tup in c.most_common(10):
        if len(tw_tup[0]) > 1:
            word = tw_tup[0]
            if word in stopwords:
                pass
            else:
                top_words_list.append(word)
    #logging.info(top_words_list)
    return json.dumps(top_words_list)

def translate_word(w):
    return w.replace('.','').replace(',','').replace('!','').replace('?','').lower().strip()
